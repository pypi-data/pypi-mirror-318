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
class ColSet:
    '''Represents a named set of columns to show when displaying Search results
       or tied objects from a Ref.'''

    def __init__(self, identifier, label, columns):
        # A short identifier for the set
        self.identifier = identifier
        # The i18n label to use for giving a human-readable name to the set
        self.label = label
        # The list/tuple of column layouts. To be more precise: if you are a
        # developer and you instantiate a ColSet instance, p_columns must
        # contain column layouts. If Appy instantiates a ColSet instance,
        # p_columns is an instance of class appy.ui.columns.Columns.
        self.columns = columns
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
