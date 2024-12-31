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

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Legend:
    '''Represents a legend on a timeline calendar'''

    px = Px('''
     <table class=":field.legend.getCss()"
            var="entries=field.legend.getEntries(field, o, allEventTypes, \
                    allEventNames, url, _, activeLayers, preComputed)">
      <tr for="row in field.splitList(entries, field.legend.cols)" valign="top">
       <x for="entry in row">
        <td align="center">
         <table width="13px">
          <tr><td style=":entry.style"
                  align="center">::entry.content or '&nbsp;'</td></tr>
         </table>
        </td>
        <td style=":field.legend.getCssText()">::entry.name</td>
       </x>
      </tr>
     </table>''')

    def __init__(self, position='bottom', cols=4, width='115px', entryName=None,
                 concatenate=', ', update=None, showEntrySeveral=True):
        # The legend can be positioned at the "bottom" or to the "right" of the
        # timeline
        self.position = position
        # It spans a given number of columns
        self.cols = cols
        # A width for the column(s) displaying the text for a legend entry
        self.width = width
        # By default, when an entry, corresponding to an event type, must be
        # added to the legend, the event name, as defined by the tied Calendar
        # field, is used as name for the legend entry. If you prefer to define
        # another name, specify a method in attribute p_entryName. This method
        # will receive these args:
        # 1) an event type (eventType)
        # 2) the dict of all encountered event names (eventNames), keyed by
        # event type.
        # The method must return the name of the corresponding entry.
        self.entryName = entryName
        # If several event types share the same color, a single entry must be
        # produced in the legend. Attribute p_concatenate defines the separator
        # to use between all the event names related to the same legend entry.
        # If p_concatenate is None, once a first event type has been found for a
        # given color, any other event type corresponding to the same color will
        # simply be ignored.
        self.concatenate = concatenate
        # A method that will, once the legend is build, receive it as single arg
        # and possibly update it if necessary.
        self.update = update
        # When multiple events are present in a single cell, this latter is
        # rendered in a specific way, in order to indicate that several events
        # are "hidden" in it. By default, the legend entry for this specific
        # case is present in the legend. If you are sure this case will never
        # happen in your calendar, you can remove the default entry from the
        # legend by setting attribute p_showEntrySeveral to False.
        self.showEntrySeveral = showEntrySeveral

    def getCss(self):
        '''Gets the CSS class(es) for the legend table'''
        r = 'legend'
        if self.position == 'right': r += ' legendRight'
        return r

    def getCssText(self):
        '''Gets CSS attributes for a text entry'''
        return f'padding-left:5px; width:{self.width}'

    def getEntryNameFor(self, o, eventType, allEventNames):
        '''Get the name of the legend entry corresponding to this p_eventType'''
        method = self.entryName
        if method:
            r = method(o, eventType, allEventNames)
        else:
            r = allEventNames[eventType]
        return r

    def getEntries(self, field, o, allEventTypes, allEventNames, url, _,
                   activeLayers, preComputed):
        '''Gets information needed to produce the legend for a timeline'''
        # Produce one legend entry by event type, provided it is shown and
        # colored.
        r = []
        byStyle = {}
        concat = self.concatenate
        for eventType in allEventTypes:
            # Create a new entry for every not-yet-encountered color
            info = field.getCellInfo(o, eventType, preComputed)
            if not info or not info.bgColor: continue
            style = f'background-color:{info.bgColor}'
            if style not in byStyle:
                entryName = self.getEntryNameFor(o, eventType, allEventNames)
                if entryName:
                    entry = O(name=entryName, content='', style=style)
                    r.append(entry)
                    byStyle[style] = entry
            elif concat is not None:
                # Update the existing entry with this style
                entry = byStyle[style]
                entryName = self.getEntryNameFor(o, eventType, allEventNames)
                if entryName:
                    entry.name = f'{entry.name}{concat}{entryName}'
        # Add, if appropriate, the background indicating that several events are
        # hidden behind a timeline cell.
        if self.showEntrySeveral:
            r.append(O(name=_('several_events'), content='',
                       style=url('angled', bg=True)))
        # Add layer-specific items
        for layer in field.layers:
            if layer.name not in activeLayers: continue
            entries = layer.getLegendEntries(o)
            if entries:
                # Take care of entry duplicates
                for entry in entries:
                    style = f'{entry.content or ""}{entry.style}'
                    if style not in byStyle:
                        r.append(entry)
                        byStyle[style] = entry
                    elif concat is not None:
                        # Update the existing entry with this style
                        existingEntry = byStyle[style]
                        existingEntry.name = f'{existingEntry.name}{concat}' \
                                             f'{entry.name}'
        # Update the legend with a custom method if needed
        if self.update: self.update(o, r)
        return r
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
