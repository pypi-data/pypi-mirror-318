#!/usr/bin/env python3

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

import appy
from appy.bin import Program
from appy.deploy import local
from appy.deploy.repository import Repository

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Make some names available here
App = local.App

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
RUN_DONE  = 'Done.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Make(Program):
    '''This program allows to create or update an app or a site'''

    # We can create/update the following artefacts
    allowedTargets = ('app', 'site', 'ext')

    # Help messages
    APP_S   = 'url=<url>,[type=<type>,name=<name>,branch=<branch>,' \
              'login=<login>,password=<password>]'
    HELP_TG = 'can be "app" for creating/updating an app, "site" for ' \
              'creating a site or "ext" for creating an extension to an app.'
    HELP_F  = 'folder is the absolute path to the base folder for the app, ' \
              'site or ext.'
    HELP_A  = 'Mandatory when target is [site] or [ext], specify here the ' \
              'absolute path to the related app (if the app is to be found ' \
              'locally), or a distant app specifier of the form %s. ' \
              'A distant specifier must point to a Git (type=git) or ' \
              'Subversion (type=svn) repository. For a git specifier, ' \
              'attributes "login" and "password" are useless: only ' \
              'public-key authentication is supported. For a git specifier, ' \
              'mentioning "type=git" is useless: it is the default value. ' \
              'In a specifier, attribute "url" must always be the first one; ' \
              'attribute "password", when included, must always be the last ' \
              'one.' % APP_S
    HELP_P  = '[site] the port on which the site will listen. Defaults to 8000.'
    HELP_O  = "[site, unix/linux only] the owner of the site. If specified, " \
              "the whole site tree will be chown'ed to this owner. " \
              "Optionally, you may specify the group by suffixing the owner " \
              "by a colon and the group name, ie: appy:appy."
    HELP_D  = '[site] dependencies, as a series of local paths or ' \
              'specifiers. For every local path, a symlink will be created ' \
              'in <site>/lib. For every specifier, a local copy will be ' \
              'created in <site>/lib.'
    HELP_E  = '[site] The absolute path to the optional extension to the app ' \
              'specified via option "-a" (if the ext is to be found locally) ' \
              'or a distant ext specifier of the form "%s".' % APP_S

    # Error messages
    WRONG_TARGET = 'Wrong target "%s".'
    F_EXISTS     = '%s already exists. An inexistent path must be specified ' \
                   'if you want this script to create and populate a fresh %s.'
    NO_APP       = 'No app was specified.'
    WRONG_APP    = '%s does not exist or is not a folder.'
    WRONG_APP_S  = 'Wrong app specifier: %s'
    APP_S_KO     = 'An app specifier must be of the form "%s".' % APP_S
    SPEC_APP_KO  = "In that context, the app's local path must be given."
    NAME_CLASH   = 'Your Python interpreter already knows about a package or ' \
                   'module named "%s". Please choose another name in order ' \
                   'to avoid a name clash.'

    def defineArguments(self):
        '''Define the allowed arguments for this program'''
        add = self.parser.add_argument
        # Positional arguments, common to all targets (app and site)
        add('target', help=Make.HELP_TG)
        add('folder', help=Make.HELP_F)
        # Optional arguments specific to "site"
        add('-a', '--app',  dest='app',  help=Make.HELP_A)
        add('-p', '--port', dest='port', help=Make.HELP_P)
        add('-o', '--owner', dest='owner', help=Make.HELP_O)
        add('-d', '--dependencies', dest='dependencies', nargs='+',
            help=Make.HELP_D)
        add('-e', '--ext',  dest='ext',  help=Make.HELP_E)

    def analyseApp(self, app, isExt=False, specifierDisallowed=False):
        '''Get the path to a local app (or ext if p_isExt is True) or the
           distant specifier else.'''
        if not app and not isExt: self.exit(self.NO_APP)
        if app.startswith('url='):
            # A specifier
            if specifierDisallowed: self.exit(self.SPEC_APP_KO)
            r = Repository.parse(app)
            if r is None:
                print(self.WRONG_APP_S % app)
                self.exit(self.APP_S_KO % app)
        else:
            # It must be the path to a local folder
            r = Path(app).resolve()
            # This path must exist
            if not r.is_dir():
                self.exit(self.WRONG_APP % r)
        return r

    def analyseDependencies(self, dependencies):
        '''Analyses the specified p_dependencies and converts, in it, paths to
           Path instances and specifiers to Object instances.'''
        if not dependencies: return []
        i = 0
        length = len(dependencies)
        while i < length:
            dep = dependencies[i]
            if dep.startswith('url='):
                # A specifier
                dep = Repository.parse(dep)
                if dep is None:
                    print(self.WRONG_APP_S % dep)
                    self.exit(self.APP_S_KO % dep)
            else:
                dep = Path(dep).resolve()
            dependencies[i] = dep
            i += 1
        return dependencies

    def checkPackageExistence(self):
        '''Exits if the name of the app or ext under creation corresponds to an
           existing package or module known by the currently running Python
           interpreter.'''
        # We are in the process of creating an app or ext. If a module having
        # this name already exists on the currently running Python interpreter
        # (in the Python standard library for instance), a name clash will
        # occur.
        name = self.folder.name
        try:
            __import__(name)
            self.exit(self.NAME_CLASH % name, printUsage=False)
        except ImportError:
            pass

    def analyseArguments(self):
        '''Check and store arguments'''
        # "folder" will be a Path created from the "folder" argument
        self.folder = None
        # Site/ext-specific attributes
        self.app = None # The result of parsing the '-a' option
        # Check arguments
        args = self.args
        # Check target
        target = args.target
        if target not in self.allowedTargets:
            self.exit(self.WRONG_TARGET % target)
        # Get a Path for the "folder" argument
        self.folder = Path(self.args.folder).resolve()
        # Check site-specific arguments and values
        if target == 'site':
            # The path to the site must not exist
            if self.folder.exists():
                self.exit(self.F_EXISTS % (self.folder, 'site'),
                          printUsage=False)
            # Manage the app and its ext
            self.app = self.analyseApp(self.args.app)
            ext = self.args.ext
            self.ext = None if not ext else self.analyseApp(ext, isExt=True)
            # The port must be an integer value
            port = self.args.port
            if port and not port.isdigit():
                self.exit(self.PORT_KO % port, printUsage=False)
            self.port = int(port) if port else 8000
            # An owner may be specified
            self.owner = self.args.owner
            # Manage dependencies
            self.dependencies = self.analyseDependencies(self.args.dependencies)
        elif target == 'app':
            # Do not check folder existence: the folder can exist or not.
            # Prevent name clashes.
            self.checkPackageExistence()
        elif target == 'ext':
            # Prevent name clashes
            self.checkPackageExistence()
            # The path to the ext must not exist (it is not possible to update
            # an ext, only create it).
            if self.folder.exists():
                self.exit(self.F_EXISTS % (self.folder, 'ext'),
                          printUsage=False)
            # The path to the related app must be given
            self.app = self.analyseApp(self.args.app, specifierDisallowed=True)

    def run(self):
        target = self.args.target
        if target == 'site':
            local.Site(self.folder, self.app, self.port, self.owner,
                       self.dependencies, self.ext).create()
        elif target == 'app':
            action = 'update' if self.folder.exists() else 'create'
            eval(f'local.App(self.folder).{action}()')
        elif target == 'ext':
            local.Ext(self.folder, self.app).create()
        print(RUN_DONE)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == '__main__': Make().run()
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
