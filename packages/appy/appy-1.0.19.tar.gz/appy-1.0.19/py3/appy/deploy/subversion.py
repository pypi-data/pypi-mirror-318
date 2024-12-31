'''Execute commands to a Subversion repository'''

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
from appy.deploy.repository import Repository

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Subversion(Repository):
    '''Represents a distant Subversion server'''

    # svn options for non interactive mode
    nonInteractive = '--non-interactive --no-auth-cache'

    def __init__(self, url, name=None, login=None, password=None):
        '''Defines a distant Subversion repo'''
        super().__init__(url, name)
        # Optional credentials
        self.login = login
        self.password = password

    def build(self, command, folder):
        '''Builds the Subversion p_command based on info from p_self and the
           concerned local p_folder.'''
        # Returns a tuple (v_command, v_folder), v_command being the complete
        # Subversion command (p_command and added args), and v_folder being the
        # p_folder completed with the local folder name in <site>/lib.
        r = ['svn', command]
        # Compute the local folder name in <site>/lib
        local = self.getLocalFolder(folder)
        if command == 'checkout':
            # Add the checkout URL and local
            r.append(self.url)
            # Add the name of the local folder to checkout to, if it is
            # different from the last part of the URL.
            if self.name: r.append(self.name)
        elif command == 'update':
            # Add the local folder that must be updated
            r.append(str(local))
        # Add parameters for running commands in a non interactive mode
        r.append(Subversion.nonInteractive)
        # Add authentication-related parameters if found
        if self.login:
            r.append('--username %s --password %s' % (self.login,self.password))
        return ' '.join(r), local

    def getDownloadCommand(self, folder):
        '''Produce the complete command allowing to "svn co" this repo (p_self)
           in this local p_folder.'''
        return self.build('checkout', folder)

    def getUpdateCommand(self, folder):
        '''Produce the complete command allowing to "svn up" this repo (p_self)
           in this local p_folder.'''
        return self.build('update', folder)

    def asSpecifier(self):
        '''Returns p_self's specifier version'''
        r = '%s,type=svn' % super().asSpecifier()
        if self.login:
            r = '%s,login=%s,password=%s' % (r, self.login, self.password)
        return r
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
