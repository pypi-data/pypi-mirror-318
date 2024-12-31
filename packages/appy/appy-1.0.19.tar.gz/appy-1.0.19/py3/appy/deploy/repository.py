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
import os
from pathlib import Path

from appy.model.utils import Object as O

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
M_OVERR   = 'This method must be overridden'
RUN_CMD   = 'Run command :: %s'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Repository:
    '''Represents a distant code repository and access credentials'''

    # This abstract class represents a distant code repository (or specific
    # folder within such a repository). 2 concrete classes exist. Each one
    # manages a particular technology:
    #
    #                          appy.deploy.git.Git
    #                   appy.deploy.subversion.Subversion
    #

    # Packages containing concrete Repository classes
    concrete = {'git': O(package='git',        class_='Git'),
                'svn': O(package='subversion', class_='Subversion')}

    def __init__(self, url, name=None):
        # The complete URL to the distant code repository. It must store the
        # distant repo's complete URL and may already contain other elements,
        # like a username, as in example (a) below:
        # (a) ssh://git-hubber@www.geezteem.com:1427/~/Hubber
        # (b) https://svn.appy.be/trunk
        self.url = url
        # p_name is used to name the folder into which the distant code will be
        # imported. Indeed, the name of the module to import may not be found
        # within the URL (as in example (b) hereabove). If it is the case, it
        # must be explicitly defined here. In example (a), it is not required,
        # because, when cloning this Git repo, the local clone will be named
        # "Hubber", which is the desired result. That being said, note that,
        # even for a git repo, a name can be provided, and will be used to name
        # the folder hosting the local repo.
        self.name = name

    # 2 commands can be issued on a distant repository: "download" and "update".
    # Names for those commands are purposedly chosen to be technology neutral.
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # "download" | refers to the initial import of data from the distant
    #            | repository. For git, it is implemented by the "git clone"
    #            | command; for Subversion, it is implemented by "svn checkout".
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # "udate"    | refers to an update to an already imported codebase. It is
    #            | implemented by commands "git pull" or "svn up".
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Consequently, every concrete Repository class must implement the 2
    # following methods, allowing to produce the complete specific commands for
    # performing these 2 operations on the distant repository.

    def getDownloadCommand(self, folder):
        '''Return a tuple (v_command, v_localFolder). v_command is the complete
           command allowing to download the distant code into this local
           p_folder (p_folder being generally a site's "lib" folder);
           v_localFolder is the folder created within p_folder.'''
        # p_folder is a pathlib.Path instance; the returned local folder must
        # also be a Path instance.
        raise Exception(M_OVERR)

    def getUpdateCommand(self, folder):
        '''Return a tuple (v_command, v_localFolder). v_command is the complete
           command allowing to update the distant code that was previously
           imported in p_folder (p_folder being generally a site's "lib"
           folder); v_localFolder is the inner folder, within p_folder,
           containing the code.'''
        # p_folder is a pathlib.Path instance
        raise Exception(M_OVERR)

    def getBranch(self):
        '''A sub-class may define a branch within its repo'''

    @classmethod
    def getEnvironment(class_, asString=True):
        '''Define environment variable GIT_SSH_COMMAND before launching a
           repository-related command. If p_asString is True, the method returns
           the definition a a string. Else, it updates os.environ with it.'''
        # The objective is to ensure we are not blocked by Host key verification
        ssh = 'ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'
        if asString:
            return 'GIT_SSH_COMMAND=\\"%s\\"' % ssh
        else:
            os.environ['GIT_SSH_COMMAND'] = ssh

    def getLocalFolder(self, folder):
        '''Return, within p_folder, the sub-folder where the copy of the distant
           code resides.'''
        name = self.name or Path(self.url).name
        return folder / name

    def download(self, folder):
        '''Download, in this p_folder, a copy of the code retrieved via
           p_self.url and return the created sub-folder.'''
        # Remember the current working directory: we will chdir into p_folder
        curdir = os.getcwd()
        os.chdir(folder)
        # Build the command
        command, local = self.getDownloadCommand(folder)
        # Execute the command
        self.getEnvironment(asString=False)
        print(RUN_CMD % command)
        os.system(command)
        # chdir to the initial working directory
        os.chdir(curdir)
        # Return the path to the local copy
        return local

    @classmethod
    def getConcrete(class_, type):
        '''Returns the concrete Repository class corresponding to this p_type'''
        info = class_.concrete[type]
        module = __import__(f'appy.deploy.{info.package}').deploy
        return getattr(getattr(module, info.package), info.class_)

    @classmethod
    def parse(class_, specifier):
        '''Parses this p_specifier, being the command-line version of a
           repository, and return one of the concrete Repository instances.
           If the p_specifier is wrong, this method returns None.'''
        # Manage the presence of a password
        i = specifier.find('password=')
        if i != -1:
            # A password is there
            password = specifier[i+9:]
            specifier = specifier[:i-1]
        else:
            password = None
        # Parse all other p_specifier attributes
        params = O()
        for part in specifier.split(','):
            name, value = part.split('=', 1)
            params[name] = value
        # Get the concrete Repository class to instantiate
        type = params.type or 'git'
        if type not in class_.concrete or not params.url: return
        concrete = class_.getConcrete(type)
        # Instantiate it
        r = concrete(params.url, params.name)
        if type == 'git':
            if params.branch:
                r.branch = params.branch
        if type == 'svn' and params.login and password:
            r.login = params.login
            r.password = password
        return r

    def asSpecifier(self):
        '''Returns p_self's specifier version'''
        r = f'url={self.url}'
        if self.name:
            r = f'{r},name={self.name}'
        branch = self.getBranch()
        if branch:
            r = f'{r},branch={branch}'
        return r

    def collectIn(self, commands, base):
        '''If the folder where this repo will be downloaded on the distant
           server must be configured, this method will add, in p_commands, the
           command allowing to perform this configiration.'''
        # p_base is the site's base folder

    @classmethod
    def getConfigureFoldersCommand(class_, folders):
        '''Returns the command'''
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
