'''Loads and returns a Model instance'''

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
import sys, inspect, pathlib, importlib

from appy.tr import po
from appy.utils import exeC
from appy.model.root import Model
from appy.model.fields import Field
from appy.model.fields.ref import Ref
from appy.model.fields.phase import Page
from appy.model.workflow import standard
from appy.model.meta.class_ import Class
from appy.model.fields.string import String
from appy.model.workflow.state import State
from appy.model.meta.workflow import Workflow

# Errors - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
NO_SEARCH = "Note that Appy classes and workflows are not searched within " \
            "your app's __init__.py file, nor within sub-modules."
NO_CLASS  = 'Warning: no Appy class was found in your app @%%s. %s' % NO_SEARCH
DUP_NAME  = '2 or more Appy classes and/or workflows named "%s" have been ' \
            'found in your model. This is not allowed, even if they are in ' \
            'separate Python modules.'
LOADED_RT = 'Model loaded (base+app) - %d classes - %d workflows - %s labels.'
LOADED_MT = 'Model loaded (app) - %d class(es) - %d workflow(s).'
NOT_WF    = '"%s", defined as workflow for class "%s", is not a workflow class.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Loader:
    '''Reads the application model, completes it with the base Appy model, and
       returns a appy.model.Model object.'''

    # Standard folders that are present in every Appy app or ext
    standardFolders = ('tr', 'static')

    def __init__(self, config, appConfig, logger, appOnly):
        # The model config (a appy.model.Config instance)
        self.config = config
        # The root app config
        self.appConfig = appConfig
        # A logger. If None, output will go to stdout.
        self.logger = logger
        # If p_appOnly is True, we will not load the Appy base model: only the
        # classes and workflows defined in the app will be loaded. This
        # minimalist model loading is performed by the appy.tr.updater.Updater
        # (called by <appFolder>/bin/make), for creating or updating the app's
        # i18n files.
        self.appOnly = appOnly

    def log(self, message):
        '''Logs p_message to p_self.logger if it exists, to stdout else'''
        if self.logger:
            self.logger.info(message)
        else:
            print(message)

    def determineMetaClass(self, class_):
        '''If p_class_ is:
           * a Appy class, this method returns meta-class Class;
           * a Appy workflow, this method returns meta-class Wokflow;
           * none of it, this method returns None.
        '''
        # If p_class_ has a static attribute appy=True or at least one static
        # attribute being an instance of appy.fields.Field, it will be
        # considered a Appy class. If it declares at least one static attribute
        # being an instance of appy.fields.workflow.State, it will be considered
        # a Appy workflow.
        if getattr(class_, 'appy', None) is True:
            # Declaring appy=True on a class may be useful, ie, if you want to
            # create a class that inherits from a Appy base class without
            # defining any additional field.
            return Class
        for attr in class_.__dict__.values():
            if isinstance(attr, Field): return Class
            elif isinstance(attr, State): return Workflow

    def complete(self, model):
        '''After the model loader has loaded the app's model (m_run), Appy base
           classes (see Model.baseClasses) may have been redefined or not at the
           app level. In order to have a complete model in self.classes, we must
           add all base classes not being redefined at the app level.

           We must also load standard workflows into self.workflows.
        '''
        # Complete self.classes
        for name in Model.baseClasses:
            if name not in model.classes:
                # Import the corresponding base class
                statement = f'from appy.model.{name.lower()} import {name}'
                pythonClass = exeC(statement, name)
                model.classes[name] = Class(pythonClass, isBase=True)
        # Complete self.workflows
        for name in Model.baseWorkflows:
            model.workflows[name] = Workflow(getattr(standard, name),
                                             isBase=True)

    def updateRefs(self, model):
        '''For "base" and "over" classes, Refs may still point to "base"
           classes. For example, Tool.users may point to appy.model.user.User
           instead of "over" class someApp.user.User. This method updates Refs
           accordingly.'''
        for class_ in model.classes.values():
            # Ignore non-base classes
            if class_.type == 'app': continue
            # Browse forward Ref fields
            for field in class_.fields.values():
                if field.type != 'Ref' or field.isBack: continue
                # Get the target class
                refClass = model.classes[field.class_.__name__]
                # If this class has been overridden, we must update it with the
                # overridden class.
                if refClass.type == 'over':
                    field.class_ = refClass.python
                    # Update the back ref, too
                    if field.back:
                        field.back.class_ = class_.python

    def linkWorkflows(self, model):
        '''Associate classes and workflows at the model level, based on static
           attributes "workflows" defined on classes, and check that such
           classes are really workflows.'''
        for class_ in model.classes.values():
            workflow = getattr(class_.python, 'workflow', standard.Anonymous)
            name = workflow.__name__
            # Get the corresponding Workflow instance
            workflowClass = model.workflows.get(name)
            if not workflowClass:
                raise Model.Error(NOT_WF % (name, class_.name))
            # Make the link
            class_.workflow = workflowClass

    def updateTranslations(self, model):
        '''Injects, on class Translation, a field for every defined i18n
           label. Returns the total number of i18n labels.'''
        # i18n labels are collected from 3 sources:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # Name       | Location   | Description
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # Appy.pot   | appy/tr/po | The labels used in the base Appy classes.
        # <app>.pot  | <app>/tr   | The labels automatically generated by Appy
        #            |            | from the app model.
        # Custom.pot | <app>/tr   | The custom labels managed "by hand" by the
        #            |            | app's developer.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # Translations for Appy.pot labels are not modifiable as-is by the app's
        # user. If the app's developer wants to make some Appy.pot label
        # modifiable, he must define its homonym in Custom.pot.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # As a preamble, load translations from po(t) files
        trPath = self.config.appPath / 'tr'
        self.translationFiles = po.load(path=trPath, pot=False)
        r = 0
        # Get the Translation class
        translationClass = model.classes['Translation']
        # Read the 3 "pot" files
        appyPot = pathlib.Path(inspect.getfile(po)).parent / 'Appy.pot'
        appPot = trPath / f'{self.config.appPath.stem}.pot'
        customPot = trPath / 'Custom.pot'
        for pot in (appyPot, appPot, customPot):
            # Get messages from the current pot file
            potFile = po.Parser(pot).parse()
            messages = potFile.messages
            r += len(messages)
            # Manage messages from Appy.pot
            if pot.stem == 'Appy':
                for message in messages.values():
                    # For every message, create a hidden String field. Indeed,
                    # the user will not be allowed to update them (but will be
                    # allowed to modify translations from the app's pot file,
                    # see below).
                    field = String(show=False, layouts='f')
                    field.init(translationClass, message.id)
                    # Add it to class Translation
                    translationClass.fields[message.id] = field
            # Manage messages from app's pot files
            else:
                # Get all available .po files corresponding to this p_potFile:
                # they will be used for computing the type and length for the
                # fields storing the translations.
                potBase = pot.stem
                poFiles = []
                for fileName, poF in self.translationFiles.items():
                    # Ignore po files not corresponding to p_pot
                    if not fileName.startswith(f'{potBase}-'): continue
                    poFiles.append(poF)
                if pot.stem == 'Custom':
                    phase = 'custom'
                    pageName = 'a'
                else:
                    phase = 'main'
                    pageName = '1'
                pyClass = translationClass.python
                pyClass.getAllFieldsFrom(model.config, translationClass,
                  potFile, page=pageName, phase=phase, poOthers=poFiles)
        return r

    def getAppFolders(self):
        '''Returns the list of folders and sub-folders, within the app folder,
           where to look for Appy classes and workflows.'''
        appPath = self.config.appPath
        r = [appPath]
        for sub in appPath.iterdir():
            name = sub.name
            if not sub.is_dir() or name.startswith('.') or \
               name.startswith('_') or name in self.standardFolders: continue
            r.append(sub)
        return r

    def getAppModules(self, folders):
        '''Returns the imported Python modules corresponding to these
           p_folders.'''
        # Preamble: the app folder's parent must be in sys.path
        appPath = self.config.appPath
        basePath = str(appPath)
        if basePath not in sys.path:
            sys.path.insert(0, basePath)
        # Walk v_folders
        r = []
        i = -1
        for folder in folders:
            i += 1
            # Get all Python modules in v_folder
            for pyModule in folder.glob('*.py'):
                # __init__.py files are not searched
                if pyModule.name == '__init__.py':
                    continue
                if i == 0:
                    # v_pyModule is a file within the main app folder
                    #
                    # We don't use function appy.model.utils.importModule for
                    # loading app modules here. Indeed, "importModule" loads a
                    # fresh copy of a module, instead of returning the module as
                    # already loaded via an "import" statement. But we
                    # specifically need to retrieve the already loaded modules,
                    # because their classes were already patched with back
                    # references.
                    name = f'{folder.name}.{pyModule.stem}'
                    module = importlib.import_module(name)
                else:
                    # v_pyModule is in a sub-package
                    name = pyModule.stem
                    packageName = f'{appPath.stem}.{pyModule.parent.stem}'
                    module = exeC(f'from {packageName} import {name}', name)
                r.append(module)
        return r

    def run(self):
        '''Loads the model'''
        config = self.config
        # Search Appy classes and workflows, in Python files at the root of the
        # App module, __init__.py excepted, and in every direct sub-package.
        folders = self.getAppFolders()
        # The app may contain no Python file and only use the base Appy model.
        # Import, in every folder from v_folders, every found Python file,
        # searching for Appy classes/workflows.
        classType = type(Model)
        classes = {} # ~{s_name: Class}~
        workflows = {} # ~{s_name: Workflow}~
        # Import every Python module found in every folder from v_folders. Do
        # this before reading classes in it. That way, cross-module back
        # references are correctly initialized.
        modules = self.getAppModules(folders)
        # Browse now the loaded modules
        for module in modules:
            # Find classes within this module
            for element in module.__dict__.values():
                # Ignore non-classes or classes imported from other modules
                if type(element) != classType or \
                   element.__module__ != module.__name__: continue
                # Ignore non-Appy classes
                metaClass = self.determineMetaClass(element)
                if not metaClass: continue
                # Add the classes to "classes" or "workflows"
                name = element.__name__
                if name in classes or name in workflows:
                    raise Model.Error(DUP_NAME % name)
                d = classes if metaClass == Class else workflows
                d[name] = metaClass(element, appOnly=self.appOnly)
        # Display a warning if no class was found
        if not classes:
            self.log(NO_CLASS % str(config.appPath))
        # Create the Model instance
        model = Model(self.appConfig, classes, workflows)
        if not self.appOnly:
            # Complete the model with base classes from appy.model
            self.complete(model)
            # Update Refs with "over" classes if defined in the app
            self.updateRefs(model)
            # Link classes with their workflows
            self.linkWorkflows(model)
            # Load translation files and inject every message ID as a field on
            # the Translation class.
            labelsCount = self.updateTranslations(model)
            # Store grantable roles
            model.grantableRoles = model.getRoles(local=False, grantable=True)
            # Inject virtual attributes for every field in every class, in the
            # form of properties.
            for class_ in classes.values(): class_.injectProperties()
            self.log(LOADED_RT % (len(model.classes), len(model.workflows),
                                  labelsCount))
        else:
            self.log(LOADED_MT % (len(model.classes), len(model.workflows)))
        # On server init, also return the translation files, that were already
        # requested while loading the model, in order to determine the length of
        # fields storing translations.
        return model if self.appOnly else (model, self.translationFiles)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
