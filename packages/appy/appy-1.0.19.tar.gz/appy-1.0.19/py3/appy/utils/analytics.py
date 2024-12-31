'''Management of Google Analytics'''

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

# The code to inject into any page to enable Analytics - - - - - - - - - - - - -
code = '''
<script async src="https://www.googletagmanager.com/gtag/js?id=%s"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', '%s');
</script>
'''

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Analytics:
    '''Manage the use of Google Analytics within your Appy site'''

    def  __init__(self, id):
        # The ID received from Google
        self.id = id

    def get(self, tool):
        '''Return the chunk of code to inject in every page to enable
           Analytics.'''
        # Disable it when the site is in debug mode
        if tool.H().server.mode == 'fg': return
        # Get the code, configured with the ID
        return code % (self.id, self.id)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
