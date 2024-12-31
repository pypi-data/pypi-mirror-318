#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Copyright (C) 2007-2024 Gaetan Delannay

# This file is part of Appy.

# Appy is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.

# Appy is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with
# Appy. If not, see <http://www.gnu.org/licenses/>.

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from appy.px import Px
from appy.model.utils import Object as O
from appy.model.fields.calendar.views.month import Month

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class MonthMulti(Month):
    '''Represents a calendar, monthly view for several individual calendars'''

    multiple = True

    # Background colors for columns representing special days
    timelineBgColors = {'Fri': '#dedede', 'Sat': '#c0c0c0', 'Sun': '#c0c0c0'}

    def getMonths(self, preComputed):
        '''Given the p_self.grid of dates, returns the list of corresponding
           months.'''
        r = []
        for date in self.grid:
            if not r:
                # Get the month corresponding to the first day in the grid
                m = O(month=date.aMonth(), colspan=1,
                      year=date.year(), first=date)
                r.append(m)
            else:
                # Augment current month' colspan or create a new one
                current = r[-1]
                if date.aMonth() == current.month:
                    current.colspan += 1
                else:
                    m = O(month=date.aMonth(), colspan=1,
                          year=date.year(), first=date)
                    r.append(m)
        # Replace month short names with translated names, whose format may vary
        # according to colspan (a higher colspan allows to produce a longer
        # month name).
        o = self.o
        for m in r:
            monthS = o.translate(f'month_{m.month}')
            text = f'{monthS} {m.year}'
            if m.colspan < 6:
                # Short version: a single letter with an abbr
                m.month = f'<abbr title="{text}">{text[0]}</abbr>'
            else:
                m.month = text
            # Allow to customize the name of the month when required
            method = self.field.timelineMonthName
            if method: method(o, m, preComputed)
        return r

    def getColumnStyle(self, date):
        '''What style(s) must apply to the table column representing p_date
           in the calendar ?'''
        # Cells representing specific days must have a specific background color
        r = ''
        day = date.aDay()
        # Do we have a custom color scheme where to get a color ?
        color = None
        method = self.field.columnColors
        if method:
            color = method(self.o, date)
        if not color and day in self.timelineBgColors:
            color = self.timelineBgColors[day]
        if color: r = f'background-color:{color}'
        return r

    def getCellStyle(self, events):
        '''Gets the cell style to apply to the cell corresponding to p_date'''
        if not events: return
        elif len(events) > 1:
            # Return a special background indicating that several events are
            # hidden behing this cell.
            return f'background-image:url({self.o.siteUrl}/static/appy/' \
                   f'angled.png)'
        else:
            return events[0].getStyles()

    def getCellTitle(self, events):
        '''Returns content for the cell's "title" attribute'''
        if len(events) == 1:
            r = events[0].name
        else:
            r = []
            for event in events:
                if event.name:
                    r.append(f'{event.name} ({event.event.timeslot})')
            r = ', '.join(r)
        return r

    def getCellSelectParams(self, date, content):
        '''Gets the parameters allowing to (de)select a cell, as a tuple
           ("onclick", "class") to be used as HTML attributes for the cell (td
           tag).'''
        if not content and not self.field.selectableEmptyCells: return '', ''
        dateS = date.strftime('%Y%m%d')
        return f' onclick="onCell(this,\'{dateS}\')"', ' class="clickable"'

    def buildCell(self, date, style, title, content, actions,
                  disableSelect=False):
        '''Called by m_getCell to build the final XHTML "td" tag representing
           a timeline cell.'''
        style = f' style="{style}"' if style else ''
        title = f' title="{title}"' if title else ''
        content = content or ''
        if disableSelect or not actions:
            onClick = css = ''
        else:
            onClick, css = self.getCellSelectParams(date, content)
        return f'<td{onClick}{css}{style}{title}>{content}</td>'

    def getCell(self, c, date, actions):
        '''Gets the content of a cell in a timeline calendar'''
        # Unwrap some variables from the PX context
        o = self.o
        date = c.date
        other = c.other
        field = self.field
        cache = c.preComputed
        # Get the events defined at that day, in the current calendar
        events = field.Other.getEventsAt(field, date, other, c.allEventNames,
                                         self, cache, c.gradients)
        # Compute the cell attributes
        style = title = content = None
        # In priority, get info from layers
        if c.activeLayers:
            # Walk layers in reverse order
            layer = field.layers[-1]
            info = layer.getCellInfo(o, c.activeLayers, date, other, events,
                                     cache)
            if info:
                style, title, content = info
                if not layer.merge:
                    # Exclusively display the layer info, ignoring the base info
                    return self.buildCell(date, style, title, content, actions)
        # Define the cell's style and title
        style = style or self.getCellStyle(events)
        title = title or self.getCellTitle(events)
        # Define its content
        disableSelect = False
        if not content:
            if events and c.mayValidate:
                # If at least one event from p_events is in the validation
                # schema, propose a unique checkbox, that will allow to validate
                # or not all validable events at p_date.
                otherV = other.field.validation
                for info in events:
                    if otherV.isWish(other.o, info.event.eventType):
                        dateS = date.strftime('%Y%m%d')
                        cbId = f'{other.o.iid}_{other.field.name}_{dateS}'
                        totalRows = 'true' if field.totalRows else 'false'
                        totalCols = 'true' if field.totalCols else 'false'
                        name = c.allEventNames.get(info.event.eventType) or '?'
                        content = f'<input type="checkbox" checked="checked"' \
                          f' class="smallbox" id="{cbId}" title="{name}" ' \
                          f'onclick="onCheckCbCell(this,\'{c.hook}\',' \
                          f'{totalRows},{totalCols})"/>'
                        # Disable selection if a validation checkbox is there
                        disableSelect = True
                        break
            if not content and len(events) == 1:
                # A single event: if not colored, show a symbol. When there are
                # multiple events, a background image is already shown (see the
                # "style" attribute), so do not show any additional info.
                content = events[0].text
        return self.buildCell(date, style, title, content, actions,
                              disableSelect=disableSelect)

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                                  PXs
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # The row displaying month namess
    pxMonths = Px('''
     <tr>
      <th class="hidden"></th>
      <th for="mInfo in monthsInfos" colspan=":mInfo.colspan">::mInfo.month</th>
      <th class="hidden"></th>
     </tr>''')

    # The row displaying day letters
    pxDayLetters = Px('''
     <tr>
      <td class="hidden"></td>
      <td for="date in view.grid"><b>:namesOfDays[date.aDay()].name[0]</b></td>
      <td class="hidden"></td>
     </tr>''')

    # The row displaying day numbers
    pxDayNumbers = Px('''
     <tr>
      <td class="hidden"></td>
      <td for="date in view.grid"><b>:str(date.day()).zfill(2)</b></td>
      <td class="hidden"></td>
     </tr>''')

    # Main PX
    px = Px('''
     <table cellpadding="0" cellspacing="0" class="list timeline"
            id=":f'{hook}_cal'" style="display: inline-block"
            var="monthsInfos=view.getMonths(preComputed);
                 gradients=field.getGradients(o)">

      <!-- Column specifiers -->
      <colgroup>
       <col/> <!-- 1st col: Names of calendars -->
       <col for="date in view.grid" style=":view.getColumnStyle(date)"/>
       <col/>
      </colgroup>

      <tbody>
       <!-- Header rows (months and days) -->
       <x>:view.pxMonths</x>
       <x>:view.pxDayLetters</x><x>:view.pxDayNumbers</x>

       <!-- Other calendars -->
       <x for="groupO in others">
        <tr for="other in groupO" id=":other.o.iid"
            var2="tlName=view.getNameOnMulti(other);
                  mayValidate=mayValidate and other.mayValidate();
                  css=other.getCss()">
         <td class=":f'tlLeft {css}'.strip()">::tlName</td>
         <!-- A cell in this other calendar -->
         <x for="date in view.grid"
            var2="inRange=field.dateInRange(date, view)">
          <td if="not inRange"></td>
          <x if="inRange">::view.getCell(_ctx_, date, actions)</x>
         </x>
         <td class=":f'tlRight {css}'.strip()">::tlName</td>
        </tr>
        <!-- The separator between groups of other calendars -->
        <x if="not loop.groupO.last">::field.Other.getSep(len(view.grid)+2)</x>
       </x>
      </tbody>

      <!-- Total rows -->
      <x if="field.totalRows">:field.Totals.pxRows</x>
      <tbody> <!-- Footer (repetition of months and days) -->
       <x>:view.pxDayNumbers</x><x>:view.pxDayLetters</x>
       <x>:view.pxMonths</x>
      </tbody>
     </table>

     <!-- Total columns, as a separate table, and legend -->
     <x if="field.legend.position == 'right'">:field.legend.px</x>
     <x if="field.totalCols">:field.Totals.pxCols</x>
     <x if="field.legend.position == 'bottom'">:field.legend.px</x>

     <!-- Popup for validating events -->
     <x if="mayValidate">:field.validation.pxPopup</x>''')
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
