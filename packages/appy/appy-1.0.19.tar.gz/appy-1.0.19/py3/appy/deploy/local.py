'''Elements used for "local deployment" by program appy/bin/make.py'''

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

# Elements from this package are used by program appy/bin/make to generate local
# sites, apps and exts. This activity can be considered as "local deployment":
# this is why they are located in this appy.deploy.local sub-package. Moreover,
# some of them are also required for "truly distant" deployments.

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import os
from pathlib import Path

from appy.tr.po import File
from appy.utils.path import chown
from appy.utils.loc import Counter
from appy.tr.updater import Updater

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
UPDATING_F  = 'Updating %s...'
ACT_DONE    = 'Done.'

# File templates - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# <site>/bin/site
site = """
#!{self.python}

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import sys
from pathlib import Path

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
site = Path('{self.folder}')
app  = Path('{self.app}')
ext  = '{self.ext}'
ext  = Path(ext) if ext else None

paths = [site, site/'lib', app.parent]
if ext: paths.append(ext.parent)

for path in paths:
    path = str(path)
    if path not in sys.path:
        sys.path.insert(0, path)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Import Appy after sys.path has been updated
from appy.bin.run import Run

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == '__main__':
    Run().run(site, app, ext)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""

# <site>/bin/deploy
deploy = """
#!{self.python}

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import sys

lib = '{self.folder}/lib'
if lib not in sys.path:
    sys.path.insert(0, lib)

from appy.bin.deploy import Deploy

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == '__main__':
    sys.argv.insert(1, '{self.folder}')
    sys.argv.insert(1, '{self.app}')
    Deploy().run()
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""

# <site>/config.py
config = """
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
app = '{self.app}'
site = '{self.folder}'

# Complete the config  - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def complete(c, minimal=False):
    '''Completes the global p_c(onfig)'''
    # Amon, the Appy monitoring tool, if used, will call this function with
    # p_minimal being True. If you use Amon, please take the habit to put any
    # non-standard stuff requiring specific "import" statements in conditional
    # expressions, like in this example:
    #
    # if not minimal:
    #     from MyApp import MySpecificConfig
    #     c.myConfig = MySpecificConfig()
    #     ...
    #
    # In doing so, Amon will be able to import your config.py file without
    # rurning into trouble, trying to import a whole network of Python packages.
    #
    c.model.set(app)
    c.server.set(app, site)
    c.server.port = {self.port}
    c.database.set(site + '/var')
    c.log.set(site + '/var/site.log', site + '/var/app.log')
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""

# <app>/__init__.py
appInit = '''
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import appy
from appy.database import log
from appy.server import guard, scheduler, backup
from appy import database, model, ui, server, deploy, peer

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Config(appy.Config):
    server = server.Config()
    security = guard.Config()
    backup = backup.Config()
    jobs = scheduler.Config()
    database = database.Config()
    log = log.Config()
    model = model.Config()
    ui = ui.Config()
    deploy = deploy.Config()
    peers = peer.Config()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Try to import the site-specific configuration, being absent at maketime
from importlib.util import find_spec
if find_spec('config'):
    import config
    config.complete(Config)

# WARNING - The Config class is built according to that sequence:
# 1) A sub-class of appy.Config is created in the present file
# 2) This sub-class is completed by the site's config.py::complete function
# 3) [If an ext is defined] The ext imports and completes the Config class
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
'''

# <app>/make
appMake = '''
#!{self.python}
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from pathlib import Path
from appy.bin.make import App

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
App(Path('.')).update()
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
'''

# <ext>/__init__.py
extInit = '''
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Import the app's main Config instance
from %s import Config as c

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Declare this extension
from pathlib import Path
c.declareExt(Path(__path__[0]))

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Apply ext's changes to this instance
# c.<attribute> = ...

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
'''

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Target:
    '''Abstract class representing the artefact to create or update'''

    def createFile(self, path, content, permissions=None):
        '''Create a file on disk @ p_path, with some p_content and
           p_permissions.'''
        folder = path.parent
        # Create the parent folder if it does not exist
        if not folder.exists(): folder.mkdir(parents=True)
        # Patch content with variables
        content = content.format(self=self)[1:]
        # Create the file
        path = str(path)
        f = open(path, 'w')
        f.write(content)
        f.close()
        # Set specific permissions on the created file when required
        if permissions: os.chmod(path, permissions)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Site(Target):
    '''A site listens to some port and runs an app'''

    # A site is made of 3 sub-folders:
    folders = ('bin', 'lib', 'var')
    # "bin" stores the scripts for controlling the app (start/stop), backuping
    #       or restoring its data, etc;
    # "lib" stores or links the Python modules available to the site. It
    #       contains at least the app;
    # "var" stores the data produced or managed by the site: database files and
    #       folders and log files.

    def __init__(self, folder, app, port, owner, dependencies, ext):
        # The base folder for the site
        self.folder = folder
        # The folder or distant specifier for the app and its ext
        self.app = app
        self.ext = ext
        # The Python interpreter to use. Using the absolute path to the
        # currently running interpreter (sys.executable) does not work if you
        # are within a Python virtual env.
        self.python = '/usr/bin/env python3'
        # The port on which the site will listen
        self.port = port
        # The owner of the site tree (if None, the user executing the script
        # will become owner of the tree).
        if owner:
            if ':' in owner:
                self.owner, self.ownerGroup = owner.split(':')
            else:
                self.owner = owner
                self.ownerGroup = None
        else:
            self.owner = self.ownerGroup = None
        # Site dependencies
        self.dependencies = dependencies

    def create(self):
        '''Creates a fresh site'''
        # Create the root folder (and parents if they do not exist)
        self.folder.mkdir(parents=True)
        # Create the sub-folders
        for name in Site.folders: (self.folder/name).mkdir()
        # If the app or ext are distant, download, in lib/<appOrExtName>, a copy
        # from the code.
        lib = self.folder / 'lib'
        if not isinstance(self.app, Path):
            self.app = self.app.download(lib)
        ext = self.ext
        if ext:
            self.ext = ext if isinstance(ext, Path) else ext.download(lib)
        else:
            self.ext = ''
        # Integrate dependencies into the site
        dependencies = self.dependencies
        if dependencies:
            for dep in dependencies:
                if isinstance(dep, Path):
                    # A dependency to a local package. Symlink it in <site>/lib.
                    os.symlink(dep, lib / dep.name)
                else:
                    # A remote repo: download a copy <site>/lib
                    dep.download(lib)
        # Create <site>/bin/site and <site>/bin/deploy
        self.createFile(self.folder/'bin'/'site', site, 0o770)
        self.createFile(self.folder/'bin'/'deploy', deploy, 0o770)
        # Create <site>/config.py
        self.createFile(self.folder/'config.py', config)
        # Chown the tree to p_self.owner if it has been specified
        owner = self.owner
        if owner:
            chown(self.folder, owner, group=self.ownerGroup, recursive=True)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class App(Target):
    '''An app is a piece of software being Appy-compliant'''

    # Mandatory app sub-folders
    subFolders = (
      'tr',    # Stores "po" and "pot" files (for translations)
      'static' # Stores any static content (images, CSS or Javascript files...)
    )

    def __init__(self, folder):
        # The base folder for the app. Ensure it is absolute.
        if not folder.is_absolute():
            folder = folder.resolve()
        self.folder = folder
        # The path to the currently running Python interpreter
        self.python = '/usr/bin/env python3'

    def create(self):
        '''Creates a new app'''
        # Create <app>/__init__.py
        path = self.folder / '__init__.py'
        if not path.exists():
            self.createFile(path, appInit)
        # Create <app>/make
        path = self.folder / 'make'
        if not path.exists():
            self.createFile(path, appMake, 0o770)
        # Create base folders
        for name in App.subFolders:
            folder = self.folder / name
            if not folder.exists():
                folder.mkdir()

    def update(self):
        '''Updates an existing app'''
        print(UPDATING_F % self.folder)
        # Ensure the base folders are created
        self.create()
        # Call the translations updater that will create or update translation
        # files for this app.
        Updater(self.folder / 'tr').run()
        # Count the lines of code in the app
        Counter(self.folder).run()
        print(ACT_DONE)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Ext(App):
    '''An ext is an extension to a given app'''

    def __init__(self, folder, app):
        # Call the base constructor
        App.__init__(self, folder)
        # The app's Path
        self.app = app

    def getAppLanguages(self):
        '''Retrieve the languages supported by the app'''
        # It is done by searching the app's .po files. Doing it by importing the
        # app and reading its Config instance, in order to access attribute
        # Config.languages, has been felt more risky, because importing the app
        # could lead to import errors.
        r = []
        name = self.app.name
        for po in (self.app / 'tr').glob(f'{self.app.name}-*.po'):
            r.append(po.stem.rsplit('-')[1])
        return r

    def create(self):
        '''Creates a new ext'''
        # Create <ext>/__init__.py
        path = self.folder / '__init__.py'
        if not path.exists():
            self.createFile(path, extInit % self.app.name)
        # Create base folders
        for name in App.subFolders:
            folder = self.folder / name
            if not folder.exists(): folder.mkdir()
        # Create a "po" file for every app language, in case the ext needs to
        # override some i18n labels.
        for lang in self.getAppLanguages():
            # Create an empty file named <ext>/tr/Custom-<lang>.po
            name = f'Custom-{lang}.po'
            File(self.folder / 'tr' / name).generate()
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
