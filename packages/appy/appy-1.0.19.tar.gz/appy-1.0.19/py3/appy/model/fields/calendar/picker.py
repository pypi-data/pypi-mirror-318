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
from DateTime import DateTime

from appy.model.fields import Field
from appy.model.utils import Object as O
from appy.model.fields.calendar import Calendar

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
n = None

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Picker(Calendar):
    '''Calendar-like widget allowing to pick days in a month calendar'''

    # Unlike the Calendar field, the picker has an edit PX
    edit = Calendar.view

    # PX to use when rendering a calendar cell, in render mode "month"
    monthCell = 'pxCellPick'

    # The format allowing to produce a key representing a day
    dayKey = '%Y%m%d'

    def __init__(self, calendarInfo, validator=None, multiplicity=(0, None),
      default=None, defaultOnEdit=None, show=True, renderable=None, page='main',
      group=None, layouts=None, move=0, readPermission='read',
      writePermission='write', width='100%', height=100, colspan=1, master=None,
      masterValue=None, focus=False, mapping=None, generateLabel=None,
      label=None, view=None, cell=None, buttons=None, edit=None, custom=None,
      xml=None, translations=None, startDate=None, endDate=None,
      defaultDate=None, preCompute=None, exclude=None):

        '''Picker constructor'''

        # p_calendarInfo is a tuple (Calendar, eventType, timeslotId), or a
        # method producing it, allowing to define where and how to store picked
        # days. Indeed, a Picker is a non-persistent field allowing to select
        # days and set corresponding events in a tied Calendar field.
        # Consequently, every picked day will be stored in the tied Calendar
        # field (1st tuple element), as an event of some type (2nd tuple
        # element) in some timeslot (3rd tuple element).
        self.calendarInfo = calendarInfo

        # If some days cannot be picked, place a method in p_exclude. It will be
        # called with, as args, the current day (as a DateTime object) and the
        # result of p_preCompute. If the method returns:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # False    | (or None) the day will be selectable ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # True     | it will be impossible to select that day ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # a string | it will be impossible to select that day; the string is
        #          | supposed to be a message explaining why and it will be
        #          | shown via a tooltipped symbol.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # If p_exclude is None, any day being in the calendar range will be
        # selectable.
        self.exclude = exclude

        # Call the base constructor
        super().__init__(n, n, n, validator, multiplicity, default,
          defaultOnEdit, show, renderable, page, group, layouts, move,
          readPermission, writePermission, width, height, colspan, master,
          masterValue, focus, mapping, generateLabel, label,
          startDate=startDate, endDate=endDate, defaultDate=defaultDate,
          preCompute=preCompute, view=view, cell=cell, buttons=buttons,
          edit=edit, custom=custom, xml=xml, translations=translations)

        # A picker is never persistent in itself: it is an intermediary widget
        # allowing to inject/view data from a Calendar, persistent object, as
        # defined by p_self.calendarInfo.
        self.persist = False

    def isEmptyValue(self, o, value):
        '''p_value is empty if no "on" value is found'''
        if not value: return True
        if isinstance(value, list):
            # This is a value coming from the request
            for val in value:
                if val.endswith('_on'): return False
            return True
        else:
            return bool(value)

    def getRequestValue(self, o, requestName=None):
        '''Standardizes the way p_self's value on p_o is represented in the
           request.'''
        r = o.req[requestName or self.name]
        # When edited via an Ajax request, the request value may be a unique
        # string containing comma-separated values.
        if isinstance(r, str):
            r = r.split(',')
        return r

    def getStorableValue(self, o, value, single=False):
        '''If the value represents a list of not-empty unchecked checkboxes, the
           corresponding events must all be deleted from the tied calendar.'''
        if isinstance(value, list) and value:
            r = value
        else:
            r = None if self.isEmptyValue(o, value) else value
        return r

    def validate(self, o, value):
        '''Bypass the custom Calendar validation logic and use the standard
           Field one.'''
        # When edited via an ajax request, always consider the value as valid
        if o.H().isAjax(): return
        # When coming from the request, p_value may be encoded as a list of
        # strings, or as a unique string containing comma-separated values.
        return Field.validate(self, o, value)

    def hasEventAt(self, o, date, info):
        '''Is there an event of interest at this p_date in p_self's companion
           calendar field ?'''
        return info[0].getEventAt(o, date, timeslot=info[2])

    def getPreComputedInfo(self, o, view):
        '''Returns the result of calling p_self.preComputed, or None if no such
           method exists.'''
        r = super().getPreComputedInfo(o, view) or O()
        # Add a special entry named _ci_ containing the result of calling
        # p_self.calendarInfo.
        r._ci_ = self.getAttribute(o, 'calendarInfo')
        return r

    def completeAjaxParams(self, hook, o, view, params):
        '''In edit mode, when performing an Ajax request for going to another
           month, picked days on the currently shown month must be saved.'''
        # Call the base method
        super().completeAjaxParams(hook, o, view, params)
        if o.H().getLayout() == 'edit':
            # Add an action to trigger a "store" action on p_self
            params['action'] = 'storeFromAjax'

    def store(self, o, value):
        '''Stores this complete p_value on p_o'''
        if value is None: return
        # Use p_self.calendarInfo to update the corresponding events in the
        # companion calendar.
        calendar, eventType, slotId = self.getAttribute(o, 'calendarInfo')
        # Browse values from p_value
        for val in value:
            dateS, suffix = val.rsplit('_', 1)
            # Get, in this v_calendar on this p_o(bject), the potentially
            # existing event of this v_eventType, at this v_dateS, in this
            # v_slotId.
            event = calendar.getEventAt(o, dateS, timeslot=slotId)
            if suffix == 'on':
                # An event must be set
                if not event:
                    # Add one
                    date = DateTime(dateS)
                    calendar.Event.create(o, calendar, date, eventType, slotId,
                                          log=False)
            else:
                # No event of this v_eventType must be defined at this date and
                # v_slotId.
                if event:
                    # Delete it
                    date = DateTime(dateS)
                    calendar.deleteEvent(o, date, slotId, handleEventSpan=False,
                                         say=False)

    def mustExclude(self, o, date, cache):
        '''Must we prevent this p_date from being picked ?'''
        exclude = self.exclude
        return False if exclude is None else exclude(o, date, cache)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
