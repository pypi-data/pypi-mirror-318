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
from appy.model.utils import Object as O
from appy.model.fields.calendar import Cell
from appy.model.fields.calendar.timeslot import Timeslot

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Other:
    '''Represents a Calendar field that must be shown within another, multiple,
       Calendar'''

    # See parameter "others" in class appy.model.fields.calendar.Calendar

    def __init__(self, o, name, color='grey', excludedEvents=(),
                 highlight=False):
        # The object on which this calendar is defined
        self.o = o
        # The other Calendar object
        self.field = o.getField(name)
        self.timeslots = Timeslot.getAll(o, self.field)
        # The color into which events from this calendar must be shown (in the
        # month rendering) in the calendar integrating this one.
        self.color = color
        # The list of event types, in the other calendar, that the integrating
        # calendar does not want to show. Every type in p_excludedEvents may be
        # a mask, starting and/or ending with a *.
        self.excludedEvents = excludedEvents
        # Must this calendar be highlighted ?
        self.highlight = highlight

    def exclude(self, eventType):
        '''Must this p_eventType be excluded according to
           p_self.excludedEvents ?'''
        toExclude = self.excludedEvents
        if not toExclude: return
        for mask in toExclude:
            # v_mask may be a complete event type or a mask
            starEnds = mask.endswith('*')
            if mask.startswith('*') and starEnds:
                condition = mask[1:-1] in eventType
            elif starEnds:
                condition = eventType.startswith(mask[:-1])
            else:
                condition = eventType == mask
            if condition:
                return True

    def getEventsInfoAt(self, r, calendar, date, eventNames, inTimeline,
                        preComputed, gradients):
        '''Gets the events defined at p_date in this calendar and append them in
           p_r.'''
        events = self.field.getEventsAt(self.o, date)
        if not events: return
        for event in events:
            eventType = event.eventType
            # Ignore it if among self.excludedEvents
            if self.exclude(eventType): continue
            # Info will be collected in a Calendar.Cell object
            if inTimeline:
                # Get info about this cell if it has been defined, or
                # (a) nothing if p_self.field.showNoCellInfo is False,
                # (b) a tooltipped dot else.
                info = calendar.getCellInfo(self.o, eventType, preComputed)
                if info:
                    # If the event does not span the whole day, a gradient can
                    # be used to color the cell instead of just a plain
                    # background.
                    if event.timeslot in gradients:
                        dayPart = event.getDayPart(self.o, self.field,
                                                   self.timeslots)
                        info.gradient = gradients[event.timeslot] \
                                        if dayPart < 1.0 else None
                else:
                    info = Cell()
                    if calendar.showNoCellInfo:
                        nameE = eventNames[eventType]
                        info.text = f'<abbr title="{nameE}">▪</abbr>'
            else:
                # Get the event name
                info = Cell(color=self.color, title=eventNames[eventType])
            if info:
                info.event = event
                r.append(info)

    def getEventTypes(self):
        '''Gets the event types from this Other calendar, ignoring
           self.excludedEvents if any.'''
        r = []
        for eventType in self.field.getEventTypes(self.o):
            if not self.exclude(eventType):
                r.append(eventType)
        return r

    def getCss(self):
        '''When this calendar is shown in a timeline, get the CSS class for the
           row into which it is rendered.'''
        return 'highlightRow' if self.highlight else ''

    def mayValidate(self):
        '''Is validation enabled for this other calendar?'''
        return self.field.mayValidate(self.o)

    @classmethod
    def getAll(class_, o, field, preComputed):
        '''Returns the list of other calendars whose events must also be shown
           on this calendar p_field.'''
        r = None
        others = field.others
        if others:
            r = others(o, preComputed)
            if r:
                # Ensure we have a list of lists
                if isinstance(r, Other): r = [r]
                if isinstance(r[0], Other): r = [r]
        return r if r is not None else [[]]

    @classmethod
    def getSep(class_, colspan):
        '''Produces the separator between groups of other calendars'''
        return f'<tr style="height:8px"><th colspan="{colspan}" ' \
               f'style="background-color:grey"></th></tr>'

    @classmethod
    def getEventsAt(class_, field, date, others, eventNames, view, preComputed,
                    gradients=None):
        '''Gets events that are defined in p_others at some p_date'''
        r = []
        isTimeline = field.multiple and view.periodType == 'month'
        if isinstance(others, Other):
            others.getEventsInfoAt(r, field, date, eventNames, isTimeline,
                                   preComputed, gradients)
        else:
            for other in utils.IterSub(others):
                other.getEventsInfoAt(r, field, date, eventNames, isTimeline,
                                      preComputed, gradients)
        return r
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
