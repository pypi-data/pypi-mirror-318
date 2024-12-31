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
from appy import utils
from appy.px import Px
from appy.xml.escape import Escape

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TOT_KO = 'Totals can only be specified when "render" is "monthMulti".'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Total:
    '''Represents a computation that will be executed on a series of cells
       within a timeline calendar.'''

    def __init__(self, name, initValue, color=None, title=None, bgColor=None,
                 style=None):
        '''Total constructor'''
        # The name associated to this total (see class Totals)
        self.name = name
        # If p_initValue is mutable, get a copy of it
        if isinstance(initValue, dict):
            initValue = initValue.copy()
        elif isinstance(initValue, list):
            initValue = initValue[:]
        self.value = initValue
        # The following attributes allow to style the cell into which the total
        # will be dumped.
        self.color = color # The font coloe
        self.title = title # The cell's tooltip
        self.bgColor = bgColor # The cell's backgroud color
        self.style = style # Any additional CSS property can be expressed here,
                           # as a classic semi-colon-separated list of CSS
                           # properties.

    def __repr__(self):
        '''p_self's short string representation'''
        return f'‹Total::{self.name}={str(self.value)}›'

    def getStyles(self):
        '''Returns potential CSS attributes to apply to the HTML cell as
           produced by m_asCell.'''
        r = None
        # Font color
        if self.color:
            color = f'color:{self.color}'
            if r is None: r = []
            r.append(color)
        # Background color
        if self.bgColor:
            bgColor = f'background-color:{self.bgColor}'
            if r is None: r = []
            r.append(bgColor)
        # Other CSS attributes
        if self.style:
            if r is None: r = []
            r.append(self.style)
        if r is None: return ''
        r = ';'.join(r)
        return f' style="{r}"'

    def asCell(self):
        '''Renders the "td" tag containing p_self's value'''
        val = self.value
        if val is None:
            val = ''
        else:
            if not isinstance(val, str):
                val = str(val)
        # Integrate CSS and other elements
        title = f' title={Escape.xhtml(self.title)}' if self.title else ''
        return f'<td{title}{self.getStyles()}>{val}</td>'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Totals:
    '''For a timeline calendar, if you want to add rows or columns representing
       totals computed from other rows/columns (representing agendas), specify
       it via Totals objects (see Agenda attributes named "totalRows" and
       "totalCols".'''

    def __init__(self, name, label, onCell, initValue=0, translated=False):
        # "name" must hold a short name or acronym and will directly appear
        # at the beginning of the row. It must be unique within all Totals
        # instances defined for a given Calendar field.
        self.name = name
        # "label" is a i18n label that will be used to produce a longer name
        # that will be shown as an "abbr" tag around the name.
        self.label = label
        # If p_translated is True, p_label is not a i18n label, but an already
        # translated term.
        self.translated = translated
        # A method that will be called every time a cell is walked in the
        # agenda. It will get these args:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #    date     | The date representing the current day (a DateTime
        #             | instance) ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #    other    | The Other instance representing the currently walked
        #             | calendar ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #    events   | The list of events (as Event instances) defined at that
        #             | day in this calendar. Be careful: this can be None ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #    total    | The Total object (see above) corresponding to the
        #             | current column ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #    last     | A boolean that is True if we are walking the last shown
        #             | calendar ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #   checked   | A value "checked" indicating the status of the possible
        #             | validation checkbox corresponding to this cell. If there
        #             | is a checkbox in this cell, the value will be True or
        #             | False; else, the value will be None.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # preComputed | The result of Calendar.preCompute (see below).
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.onCell = onCell
        # "initValue" is the initial value given to created Total objects
        self.initValue = initValue

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                             Class methods
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    @classmethod
    def getAjaxData(class_, field, o, type, hook):
        '''Initializes an AjaxData object on the DOM node corresponding to
           the zone containing the total rows/cols (depending on p_type) in a
           timeline calendar.'''
        suffix = 'trs' if type == 'rows' else 'tcs'
        return f"new AjaxData('{o.url}/{field.name}/Totals/pxFromAjax','GET'," \
               f"{{'multiple':'1'}},'{hook}_{suffix}','{hook}')"

    @classmethod
    def get(class_, o, field, type):
        '''Returns the Totals objects by getting or computing them from
           p_field.totalRows or p_field.totalCols (depending on p_type).'''
        r = getattr(field, f'total{type.capitalize()}')
        return r(o) if callable(r) else r

    # Status for checkboxes used to (in)validate calendar events
    checkboxStatuses = {'validated': True, 'discarded': False}

    @classmethod
    def getValidationCBStatus(class_, req):
        '''Gets the status of the validation checkboxes from the request'''
        r = {}
        for status, value in class_.checkboxStatuses.items():
            ids = req[status]
            if ids:
                for id in ids.split(','): r[id] = value
        return r

    @classmethod
    def compute(class_, field, allTotals, totalType, o, grid, others,
                preComputed):
        '''Compute the totals for every column (p_totalType == 'row') or row
           (p_totalType == "col").'''
        if not allTotals: return
        # Count other calendars and dates in the grid
        othersCount = 0
        for group in others: othersCount += len(group)
        datesCount = len(grid)
        isRow = totalType == 'row'
        # Initialise, for every (row or col) totals, Total instances
        totalCount = datesCount if isRow else othersCount
        lastCount = othersCount if isRow else datesCount
        r = {}
        for totals in allTotals:
            name = totals.name
            r[name] = [Total(name, totals.initValue) for i in range(totalCount)]
        # Get the status of validation checkboxes
        status = class_.getValidationCBStatus(o.req)
        # Walk every date within every calendar
        indexes = {'i': -1, 'j': -1}
        ii = 'i' if isRow else 'j'
        jj = 'j' if isRow else 'i'
        for other in utils.IterSub(others):
            indexes['i'] += 1
            indexes['j'] = -1
            for date in grid:
                indexes['j'] += 1
                # Get the events in this other calendar at this date
                events = other.field.getEventsAt(other.o, date)
                # From info @this date, update the total for every totals
                last = indexes[ii] == lastCount - 1
                # Get the status of the validation checkbox that is possibly
                # present at this date for this calendar
                checked = None
                dateS = date.strftime('%Y%m%d')
                cbId = f'{other.o.iid}_{other.field.name}_{dateS}'
                if cbId in status: checked = status[cbId]
                # Update the Total instance for every totals at this date
                for totals in allTotals:
                    total = r[totals.name][indexes[jj]]
                    totals.onCell(o, date, other, events, total, last,
                                  checked, preComputed)
        return r

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                                  PX
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Total rows shown at the bottom of a timeline calendar
    pxRows = Px('''
     <tbody id=":f'{hook}_trs'"
            var="grid=view.grid;
                 rows=field.Totals.get(o, field, 'rows');
                 totals=field.Totals.compute(field, rows, 'row', o, grid,
                                             others, preComputed)">
      <script>:field.Totals.getAjaxData(field, o, 'rows', hook)</script>
      <tr for="row in rows"
          var2="rowTitle=row.label if row.translated else _(row.label)">
       <td class="tlLeft">
        <abbr title=":rowTitle"><b>:row.name</b></abbr></td>
       <x for="date in grid">::totals[row.name][loop.date.nb].asCell()</x>
       <td class="tlRight">
        <abbr title=":rowTitle"><b>:row.name</b></abbr></td>
      </tr>
     </tbody>''')

    # Total columns besides the calendar, as a separate table
    pxCols = Px('''
     <table cellpadding="0" cellspacing="0" class="list timeline"
            style="float:right" id=":f'{hook}_tcs'"
            var="grid=view.grid;
                 cols=field.Totals.get(o, field, 'cols');
                 rows=field.Totals.get(o, field, 'rows');
                 totals=field.Totals.compute(field, cols, 'col', o , grid,
                                             others, preComputed)">
      <script>:field.Totals.getAjaxData(field, o, 'cols', hook)</script>

      <!-- 2 empty rows -->
      <tr><th for="col in cols" class="hidden">-</th></tr>
      <tr><td for="col in cols" class="hidden">-</td></tr>

      <!-- The column headers -->
      <tr>
       <td for="col in cols"><abbr title=":_(col.label)">:col.name</abbr></td>
      </tr>

      <!-- Re-create one row for every other calendar -->
      <x var="i=-1" for="groupO in others">
       <tr for="other in groupO" var2="@i=i+1">
        <x for="col in cols">::totals[col.name][i].asCell()</x>
       </tr>

       <!-- The separator between groups of other calendars -->
       <x if="not loop.groupO.last">::field.Other.getSep(len(cols))</x>
      </x>

      <!-- Add empty rows for every total row -->
      <tr for="row in rows"><td for="col in cols">&nbsp;</td></tr>

      <!-- Repeat the column headers -->
      <tr>
       <td for="col in cols"><abbr title=":_(col.label)">:col.name</abbr></td>
      </tr>

      <!-- 2 empty rows -->
      <tr><td for="col in cols" class="hidden">-</td></tr>
      <tr><th for="col in cols" class="hidden">-</th></tr>
     </table>''')

    # Ajax-call pxRows or pxCols
    pxFromAjax = Px('''
     <x var="view=field.View.get(o, field);
             totalType=req.totalType.capitalize();
             hook=f'{o.iid}{field.name}';
             preComputed=field.getPreComputedInfo(o, view);
             others=field.Other.getAll(o, field,
               preComputed)">:getattr(field.Totals, f'px{totalType}')</x>''')
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
