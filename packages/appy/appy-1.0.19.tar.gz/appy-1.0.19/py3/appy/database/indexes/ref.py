'''An index for Ref fields'''

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
from appy.database.indexes import Index

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class RefIndex(Index):
    '''Index for a Ref field'''

    # Types of atomic values this index may store
    atomicTypes = (int, str)

    @classmethod
    def toIndexed(class_, value, field):
        '''Converts p_value, a list of tied objects, into their internal index
           representation = a list of their IIDs, or an alternate attribute as
           defined in p_field.indexAttribute.'''
        # If there is no value at all, nothing must be indexed
        if value is None:
            return
        elif isinstance(value, class_.atomicTypes):
            # Already an object IID (or alternate attribute coming from
            # p_field.indexAttribute) ready to be indexed (probably a default
            # value to index from field.emptyIndexValue).
            return value
        elif not hasattr(value, '__iter__'):
            # An object: get its indexable value
            return getattr(value, field.indexAttribute)
        else:
            # Convert a list of objects into a list of their indexable values
            return [getattr(o, field.indexAttribute) for o in value]

    @classmethod
    def toTerm(class_, value, field):
        '''Ensure p_value is an object's indexable value'''
        if isinstance(value, int):
            r = value
        elif isinstance(value, str):
            # p_value can be from a specific attribute, or be an IID encoded as
            # a string.
            r = int(value) if value.isdigit() else value
        else:
            # p_value is an object
            r = getattr(value, field.indexAttribute)
        return r

    @classmethod
    def toString(class_, o, value):
        '''The string representation for tied objects stored in p_value is the
           concatenation of their titles.'''
        if not value:
            r = None
        elif not hasattr(value, '__iter__'):
            # A single object
            r = value.getShownValue()
        else:
            # Several objects
            r = ' '.join([tied.getShownValue() for tied in value])
        return r

    # The CSS class to use when rendering the "recompute" icon for a Ref index
    boxIconCss = 'boxIconR'
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
