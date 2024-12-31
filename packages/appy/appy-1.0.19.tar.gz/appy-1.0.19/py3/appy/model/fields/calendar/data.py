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
from DateTime import DateTime
from persistent import Persistent

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class EventData(Persistent):
    '''Abstract base class used to define objects that will be stored within
       appy.model.field.calendar.Event objects, in attribute "data".'''

    # In order to store custom data in a calendar event (within its "data"
    # attribute), define a class inheriting from this one.

    # Custom data is to be used when it is not possible or desirable to use
    # standard Appy objects in a calendar. Indeed, if you want to "store" Appy
    # objects within calendar fields, a lot easier approach is to create the
    # Appy objects the standard way, and then store an event whose type is or
    # includes the Appy object's IID. Custom data allows you to directly inject
    # and manipulate data in calendar events. Consequently:
    #
    # - the standard Calendar views will not do much for you to graphically
    #   represent the data, or allow to edit it ;
    # - some standard functions, like merging events of the same day, will
    #   potentially imply losing custom data.
    #
    # But it is very likely that you will build custom UI controls to
    # manipulate, visualize or edit such data.

    def __init__(self):
        # The container event
        self.event = None
        # p_self's creation date (will hold a DateTime.DateTime object)
        self.created = None
        # p_self's creator (user login)
        self.creator = None
        # p_self's last modification date (will hold a DateTime.DateTime object)
        self.modified = None
        # p_self's last modifier
        self.modifier = None

    def complete(self, o, event):
        '''Fills p_self's base attributes on p_event creation'''
        self.event = event
        self.created = self.modified = DateTime()
        self.creator = self.modifier = o.user.login

    # This PX renders the base EventData attributes, as defined in the
    # hereabove-defined constructor.
    pxBase = Px('''
     <div class="dropdownMenu menuCal" onmouseover="toggleDropdown(this)"
          onmouseout="toggleDropdown(this,'none')">
      <div>🛈</div>
      <div class="dropdown fadedIn ddCal" style="display:none">
       <div>
        <b>:_('Base_creator')</b> 
        <x>:o.user.getTitleFromLogin(data.creator)</x> 
        <x>:_('date_on')</x> 
        <x>:tool.formatDate(data.created, withHour=True)</x>
       </div> 
       <div if="data.modified and data.modified != data.created"
            class="topSpaceS">
        <b>:_('Base_modified')</b> 
        <x>:o.user.getTitleFromLogin(data.modifier)</x> 
        <x>:_('date_on')</x> 
        <x>:tool.formatDate(data.modified, withHour=True)</x>
       </div>
      </div>
     </div>''',

     css='''.menuCal { float:left;cursor:help;font-weight:normal;
                       font-style:normal }
            .ddCal { margin-left:-3em; width:10em;
                     font-size:85% !important }''')

    # The specific fields your sub-class adds may be rendered in the standard
    # Appy calendar views via the PXs you may override in the following static
    # attributes, on your sub-class.
    pxMonth = pxMonthMulti = pxDay = pxDayMulti = None

    def updateContext(self, c, mode):
        '''Override this to complete the PX p_c(ontext) that will be passed to
           s_px.'''

    def render(self, o, mode='Month'):
        '''Returns a 2-tuple with the 2 parts one may render about p_self: the
           standard attributes as defined in the EventData constructor, and the
           sub-class custom rendering.'''
        context = O(data=self, o=o, _=o.translate, tool=o.tool)
        # Let a sub-class update the context
        self.updateContext(context, mode)
        # Get annd execute the PX
        px = getattr(self, f'px{mode}')
        custom = px(context) if px else None
        return custom, self.pxBase(context)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
