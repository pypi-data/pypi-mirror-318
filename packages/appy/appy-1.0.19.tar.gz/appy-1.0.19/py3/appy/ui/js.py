'''Module implementing Javascript-related functionality'''

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
import re

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Quote:
    '''This class escapes strings to be integrated as Javascript string literals
       in Javascript code, and, once escaped, quotes them.'''

    # The "escaping" part of this class is inspired by class appy/xml/Escape
    rex = re.compile("[\n\t\r']")
    blanks = {'\n':'', '\t':'', '\r':''}

    # There are 2 ways to escape a single quote
    values = {True: {"'": '&apos;'}, False: {"'": "\\'"}}
    for d in values.values(): d.update(blanks)

    # Match functions, used by m_js below. Dict keys represent values for
    # parameter "withEntity".
    matchFunctions = {
      True : lambda match: Quote.values[True][match.group(0)],
      False: lambda match: Quote.values[False][match.group(0)],
    }

    @classmethod
    def js(class_, s, withEntity=True):
        '''Escapes blanks and single quotes in string p_s. Single quotes are
           escaped with a HTML entity if p_withEntity is True or with a quote
           prefixed with a "backslash" char else. Returns p_s, escaped and
           quoted.'''
        s = s if isinstance(s, str) else str(s)
        fun = class_.matchFunctions[withEntity]
        return f"'{class_.rex.sub(fun, s)}'"
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
