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
from appy.model.fields import Field

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Switch(Field):
    '''Complex field made of several sub-sets of fields among which only one is
       chosen. This field allows to have a part of a form being variable.
       The selected sub-set depends on a master/slave relationship that must be
       established between a Switch field and some other master field.
    '''
    view = edit = cell = buttons = Px('''
     <x var="fieldset,fields=field.getChosenFields(o)" if="fields">
      <!-- Remember the chosen fieldset in this hidden input field -->
      <input if="layout == 'edit'" type="hidden" name=":field.name"
             value=":fieldset"/>
      <x var="fieldName=None;
              page,grouped,css,js,phases=o.getGroupedFields(field.pageName, \
                                         layout, fields=fields)">:o.pxFields</x>
     </x>''')

    search = ''

    def __init__(self, fields, validator=None, show=True, renderable=None,
      page='main', group=None, layouts=None, move=0, readPermission='read',
      writePermission='write', width=None, height=None, maxChars=None,
      colspan=1, master=None, masterValue=None, focus=False, mapping=None,
      generateLabel=None, label=None, scolspan=1, swidth=None, sheight=None,
      inlineEdit=False, view=None, cell=None, buttons=None, edit=None,
      custom=None, xml=None, translations=None):
        # p_fields must be a tuple of fieldsets of the form
        #                        ~((s_name, fields),)~
        # Within this tuple, every "fields" entry is a dict of the form
        #                         ~{s_name: Field}~
        self.fields = fields
        # Call the base Field constructor
        super().__init__(validator, (0,1), None, None, show, renderable, page,
          group, layouts, move, False, True, None, None, False, None,
          readPermission, writePermission, width, height, None, colspan, master,
          masterValue, focus, False, mapping, generateLabel, label, False,
          scolspan, swidth, sheight, True, inlineEdit, view, cell, buttons,
          edit, custom, xml, translations)

    def init(self, class_, name):
        '''Switch-specific lazy initialisation'''
        Field.init(self, class_, name)
        for case, fields in self.fields:
            for sub, field in fields.items():
                field.init(class_, sub)

    def getChosenFields(self, o, layout='view', fieldset=None):
        '''Returns, among self.fields, the chosen sub-set, as a "flat" list of
           Field instances.'''
        # More precisely, r_ is a tuple (name, fields), "name" being the name of
        # the chosen fieldset and "fields" being the flat list of corresponding
        # fields.
        req = o.req
        # Determine the name of the chosen fieldset. Get it from p_fieldset or
        # from the request.
        master = self.master
        if not fieldset:
            # Determine the fieldset... 
            if master and master.valueIsInRequest(o, req):
                # ... via the master value if present in the request
                reqValue = master.getRequestValue(o)
                masterValue = master.getStorableValue(o, reqValue, single=True)
                fieldset = self.masterValue(o, masterValue)
            else:
                # ... via the stored value
                fieldset = self.getValue(o)
                if not fieldset and not master:
                    # ... or via the first fieldset, considered as the default
                    # one if the switch has not master.
                    fieldset = self.fields[0][0]
        # Return an empty list of fields if we haven't a fieldset
        if not fieldset: return fieldset, {}
        # Get the list of fields corresponding to the chosen fieldset
        for name, fields in self.fields:
            if name == fieldset:
                return fieldset, fields
        return fieldset, {}

    def injectFields(self, meta, class_, r):
        '''Adds, in dict p_r, any switch sub-field'''
        # p_r is a dict of fields that will be stored on p_self's p_meta-class,
        # as attribute "switchFields".
        for case, fields in self.fields:
            for name, field in fields.items():
                # Ensure this name can be used
                meta.checkFieldName(class_, name)
                r[name] = field
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
