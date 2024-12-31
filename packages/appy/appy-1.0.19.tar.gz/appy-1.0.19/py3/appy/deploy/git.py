'''Execute commands to a Git repository'''

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
from pathlib import Path

from appy.deploy.repository import Repository

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
GIT_EXE  = 'Executing %s...'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Git(Repository):
    '''Represents a remote Git repository'''

    def __init__(self, url, name=None, login=None, password=None,
                 branch='master'):

        '''Defines a distant Git repo'''
        super().__init__(url, name)

        # The name of the branch to retrieve
        self.branch = branch

        # For a Git repository, it is not possible to define login/password
        # credentials: public-key authentication is used instead. The Git repo
        # must be configured with your public key; the machine running the
        # import must either store the private key, or transmit it from your
        # development machine. This latter option is preferable and is achieved
        # by defining the deployment machine as a SSH forward agent. Here is an
        # example.

        # Suppose you have your development machine D. In your home folder, you
        # have a .ssh folder, containing your private and public keys. Via the
        # Appy deployer, you want to deploy code on some production machine P,
        # named some.machine.net. You have configured the SSH daemon on P to be
        # able to log on P with your public key. If, in your .ssh folder (on D),
        # you add a file named "config" and containing the following content,
        # when the Appy deployer will, from machine P, try to download or update
        # the code from some repository machine M, it will transmit your private
        # key without storing it on P, and the download/update will be done.
        #
        # Host some.machine.net
        #   ForwardAgent yes
        #
        # Note that the SSH daemon on P must be configured as a forward agent.

    def getDownloadCommand(self, folder):
        '''Produce the complete command allowing to "git clone" this repo
           (p_self) in this local p_folder.'''
        local = self.getLocalFolder(folder)
        command = f'git clone {self.url} {str(local)} --single-branch ' \
                  f'--branch {self.branch}'
        return command, local

    def getUpdateCommand(self, folder):
        '''Produce the complete command allowing to "git pull" this repo
           (p_self) in this local p_folder.'''
        local = self.getLocalFolder(folder)
        command = f'git -C {str(local)} pull'
        return command, local

    def getBranch(self):
        '''Return the branch of interest within this repo'''
        return self.branch

    def collectIn(self, commands, base):
        '''Collects, in set p_folders, the git-managed distant folders'''
        # Build the absolute path to the folder
        folder = self.getLocalFolder(Path(base) / 'lib')
        command = f'git config --global --add safe.directory {str(folder)}'
        # Without this command, updating git repositories may pose problems, due
        # to user permissions, if the user running git commands is not the same
        # as the git repository user.
        commands.add(command)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
