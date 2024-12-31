'''The Appy meta-model contains meta-classes representing classes of Appy
   classes: essentially, Appy classes and workflows.'''

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
from appy.model.base import Base
from appy.model.root import Model

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ATTR       = 'Attribute "%s" in %s "%s"'
UNDERS     = 'contains at least one underscore, which is not allowed'
US_IN_ATTR = '%s %s. Please consider naming your fields, searches, states ' \
             'and transitions in camelCase style, the first letter being a ' \
             'lowercase letter. For example: "myField", instead of ' \
             '"my_field". Furthermore, there is no need to define "private" ' \
             'fields starting with an underscore.' % (ATTR, UNDERS)
US_IN_CLS  = 'Class or workflow "%%s" %s. Please consider naming your ' \
             'classes and workflows in CamelCase style, the first letter ' \
             'being an uppercase letter. For example: "MyClass", instead of ' \
             '"my_class".' % UNDERS
UP_NAME    = '%s must start with a lowercase letter. This rule holds for any ' \
             'field, search, state or transition.' % ATTR
LOW_NAME   = 'Name of %s "%s" must start with an uppercase letter.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
bn = '\n'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Meta:
    '''Abstract base class representing a Appy class or workflow'''

    # Reserved attribute names unallowed for naming a meta-class related
    # attribute, like a field, search, state, transition...

    unallowedNames = {
      'id'        : None, # The object's identifier
      'iid'       : None, # The object's integer identifier
      'values'    : None, # Dict storing all field values
      'container' : None, # Info about the objet's container
      'history'   : None, # The object's history
      'localRoles': None, # The object's local roles
      'locks'     : None, # Locks on object pages
      'default'   : None, # Default page name for object traversal
    }

    @classmethod
    def unallowedName(class_, name):
        '''Return True if p_name can't be used for naming a Field or Search'''
        # A name is unallowed if
        # (a) it corresponds to some standard attribute added at object creation
        #     on any Appy object (but not declared at the class level);
        # (b) it corresponds to an attribute or method defined in class Base.
        return name in class_.unallowedNames or name in Base.__dict__

    def __init__(self, class_, appOnly):
        # p_class_ is the Python class found in the Appy app. Its full name is
        #              <Python file name>.py.<class name>
        self.python = class_
        # Make this link bidirectional
        class_.meta = self
        # Its name. Ensure it is valid.
        self.name = self.checkClassName(class_)
        # If p_appOnly is True, stuff related to the Appy base model must not be
        # defined on this meta-class. This minimalist mode is in use when
        # loading the model for creating or updating translation files.
        self.appOnly = appOnly

    def asString(self):
        r = f'‹class {self.python.__module__}.{self.name}'
        for attribute in self.attributes.keys():
            r = f'{r}{bn} {attribute}:'
            for name, field in getattr(self, attribute).items():
                r = f'{r}{bn} {name} : {str(field)}'
        return f'{r}›'

    def checkClassName(self, class_):
        '''The name of a class or workflow must start with an uppercase letter
           and cannot contain an underscore.'''
        name = class_.__name__
        if '_' in name:
            raise Model.Error(US_IN_CLS % (name))
        if name[0].islower():
            type = self.__class__.__name__.lower()
            raise Model.Error(LOW_NAME % (type, name))
        return name

    def checkAttributeName(self, name):
        '''Checks if p_name is valid for being used as attribute (field, search,
           state or transition) for this class or workflow.'''
        # Underscores are not allowed
        if '_' in name:
            type = self.__class__.__name__.lower()
            raise Model.Error(US_IN_ATTR % (name, type, self.name))
        # The name must start with a lowercase char
        if not name[0].islower():
            type = self.__class__.__name__.lower()
            raise Model.Error(UP_NAME % (name, type, self.name))

    def __repr__(self):
        '''p_self's string representation'''
        prefix = self.__class__.__name__.lower()
        module = self.python.__module__
        return f'‹meta{prefix} {self.name} from module {module}›'
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
