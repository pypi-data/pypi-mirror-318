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
from persistent import Persistent

from appy.ui.layout import Layouts
from appy.model.fields import Field

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Custom(Field):
    '''A custom field has the purpose of storing a data structure that is not
       proposed by other available fields.'''

    class Layouts(Layouts):
        '''Info-specific layouts'''
        b = Layouts(edit='f')

        @classmethod
        def getDefault(class_, field):
            '''Default layouts for this Custom p_field'''
            return class_.b

    # If your objective is to build a complete custom widget, with specific
    # "edit" and "view" PXs and with a custom data structure, please use a field
    # of type Computed(unfreezable=True).

    # Indeed, the purpose of the Custom field is simpler and aims at storing a
    # data structure that is produced by your code independently of any UI
    # concern. Of course, if you wish, you can define a PX in attribute "view"
    # in order to add UI-visibility.

    # Typically, a Custom field is only "viewable" in the XML layout
    view = edit = cell = buttons = search = ''

    def __init__(self, validator=None, multiplicity=(1,1), show='xml',
      renderable=None, page='main', group=None, layouts=None, move=0,
      readPermission='read', writePermission='write', width=None, height=None,
      maxChars=None, colspan=1, master=None, masterValue=None, focus=False,
      historized=False, mapping=None, generateLabel=None, label=None, view=None,
      cell=None, buttons=None, edit=None, custom=None, xml=None,
      translations=None):
        # Parameter "persist" is not available and is automatically set to True
        super().__init__(None, (0,1), None, None, show, renderable, page, group,
          layouts, move, False, True, None, None, False, None, readPermission,
          writePermission, width, height, None, colspan, master, masterValue,
          focus, historized, mapping, generateLabel, label, None, None, None,
          None, True, False, view, cell, buttons, edit, custom, xml,
          translations)

    def isEmptyValue(self, o, value):
        '''An empty persistent value must not be considered as empty'''
        # Indeed, an empty persistent list or dict is an existing data container
        # being significant. Supposed you have initialised an empty persistent
        # dict on your custom field o.myCustom:
        #
        #                 o.myCustom = PersistentMapping()
        #
        # If this empty persistent mapping was considered as an "empty" value,
        # getting:
        #
        #                          o.myCustom
        #
        # would return None, and not the persistent mapping, because, when a
        # value is considered being empty, a default value is searched. If no
        # default value is found, None is returned.
        if isinstance(value, Persistent): return
        return super().isEmptyValue(o, value)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
