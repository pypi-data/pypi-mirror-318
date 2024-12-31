'''Deployment system for Appy sites and apps'''

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
import os, sys
from pathlib import Path

from appy.utils import termColorize
from appy.model.utils import Object as O
from appy.deploy.repository import Repository

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TG_LOG    = 'Log file for'
TP_UPDATE = 'Updating'
TG_ACT    = '\n☉  %s target %s (%d/%d)... ☉\n'
OPT_APPLY = '\nApplying option %s - %s...\n'
TG_NEXT   = '⚠  Once the site\'s log is shown, type Ctrl-C to go to the ' \
            'next target or retrieve terminal prompt. ⚠\n'
T_EXEC    = 'Executing :: %s'
T_LIST    = 'Available target(s) for app "%s", from reference site "%s":\n%s'
NO_CONFIG = 'The "deploy" config was not found in config.deploy.'
NO_TARGET = 'No target was found on config.deploy.targets.'
TARGET_KO = 'Target "%s" not found.'
TARGET_NO = 'Please specify a target to run this command.'
TARGET_VL = 'No valid target was mentioned.\n\nAvailable target(s):\n%s.'
ALL_RESV  = '\n⚠ Name "ALL" is reserved to update all targets at once. ' \
            'Please rename the target having this name.\n'
SINGLE_TG = 'Command "%s" cannot be run on more than one target.'
APA_NO    = 'Apache option was not applied: no Apache configuration found. ' \
            'Place an instance of appy.deploy.apache.Config in attribute ' \
            'Target.apache.'
SYNC_CMD  = '\n\n   ./deploy list -o sync'
CFG_D_NO  = '\n⚠  Your have defined folder "%%s" to store your target\'s ' \
            'config.py files. This folder does not exist yet. Use the ' \
            'following command to create it and add, into it, one template ' \
            'config.py file per target.%s' % SYNC_CMD
CF_MIS    = '\n⚠  %%d missing file(s) in "%%s": %%s.\n\nUse the following ' \
            'command to create missing files:%s' % SYNC_CMD
CF_SUR    = '\n⚠  %d file(s) in "%s" that do not correspond to any of ' \
            'your currently defined targets:: %s.\n\nPlease remove or ' \
            'rename it yourself.'
SYNC_KO   = 'If you want to automate the management of your target\'s ' \
            'config.py files, define, in attribute config.deploy.configFiles,' \
            ' a local folder where disttant config.py files mwill be ' \
            'synchronized.'
SYNC_NN   = 'Sync is not needed: no file is missing.'
SYNC_NF   = '\n⚠  Config file "%%s" not found. Generate one by executing:' \
            '%s' % SYNC_CMD
SYNC_F_C  = '%s created.'

# Explanations about options
INIT_D    = 'Create and configure an init script for controlling'
INIT_DET  = '(re)start / stop / status + start at boot'
OPT_INF   = {
  'lo'     : '%s LibreOffice (LO) in server mode - %s' % (INIT_D, INIT_DET),
  'init'   : '%s the distant site - %s' % (INIT_D, INIT_DET),
  'apache' : 'Create or update an Apache virtual host for this site, and ' \
             'restart Apache',
  'sync'   : 'Create or update local copies of config.py target files',
  'clean'  : "Recursively delete *.pyc files in the target site's lib folder"
}

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Target:
    '''Represents an app deployed on a site on a distant machine'''

    def __init__(self, sshHost, sshPort=22, sshLogin='root', sshKey=None,
                 sitePath=None, sitePort=8000, siteApp=None, siteExt=None,
                 siteOwner='appy:appy', siteDependencies=None, default=False,
                 apache=None):
        # The name of the distant host, for establishing a SSH connection
        self.sshHost = sshHost
        # The port for the SSH connection
        self.sshPort = sshPort
        # The login used to connect to the host in SSH
        self.sshLogin = sshLogin
        # The private key used to connect to the host in SSH
        self.sshKey = sshKey
        # Information about the Appy site on the target
        #
        # The path to the site. Typically: /home/appy/<siteName>. Extract the
        # distant site name from it.
        self.sitePath = sitePath
        self.siteName = os.path.basename(sitePath)
        # The port on which this site will listen
        self.sitePort = sitePort
        # Instances representing the distant repos where the app and ext reside.
        # Must be instances of classes appy.deploy.git.Git or
        # appy.deploy.subversion.Subversion.
        self.siteApp = siteApp
        self.siteExt = siteExt
        # The owner of the distant site. Typically: appy:appy.
        self.siteOwner = siteOwner
        self.siteUser = siteOwner.split(':')[0]
        # A list of Python dependencies to install on the distant app, in its
        # "lib" folder. Every dependency must be specified via a Repository
        # instance, from one of the concrete classes as mentioned hereabove (see
        # attributes p_self.siteApp and p_self.siteExt).
        self.siteDependencies = siteDependencies or []
        # Is this target the default target ? It is not mandatory to have a
        # default target. It is useful if you want to launch deployer commands
        # without specfying arg "-t <target>": the default target will be
        # automatically chosen.
        self.default = default
        # Info about LibreOffice (LO) running in server mode on the target
        #
        # The port on which LO listens on the target machine
        self.loPort = 2002
        # Info about an Apache virtual host that you may want to define, if you
        # use Apache as a reverse proxy in front of your Appy site. Place here,
        # if applicable, an instance of class appy.deploy.apache::Config.
        self.apache = apache

    def __repr__(self):
        '''p_self's string representation'''
        return f'‹Target {self.sshHost}:{self.sshPort}@{self.sitePath}›'

    def execute(self, command, exe='ssh', forceExit=False):
        '''Executes p_command on this target'''
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # If p_exe is...
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "ssh"  | (the default) p_command is a shell command to execute on the
        #        | distant target via the "ssh" executable ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "scp"  | a file must be copied on the target via the "scp" executable:
        #        | p_command is a 2-tuple containing the source and destination
        #        | paths.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        r = [exe]
        # If p_forceExit is True, add the "-t" ootion to ensure the distant
        # terminal will be shut down.
        if forceExit:
            r.append('-t')
        host = f'{self.sshLogin}@{self.sshHost}'
        if exe == 'ssh':
            r.append(host)
            r.append(f'"{command}"')
            # Option for port is '-p'
            portOption = 'p'
        else:
            # Add the source file
            r.append(command[0])
            # Add the destination file
            r.append(f'{host}:{command[1]}')
            # For scp, option is '-P'
            portOption = 'P'
        # Determine port
        if self.sshPort != 22:
            r.insert(1, f'-{portOption}{self.sshPort}')
        # Determine "-i" option (path to the private key)
        if self.sshKey: r.insert(1, f'-i {self.sshKey}')
        # Build the complete command
        r = ' '.join(r)
        print(T_EXEC % r)
        os.system(r)

    def copy(self, source, dest):
        '''Copy local file whose absolute path is p_source to the distant file,
           on this target, whose absolute path is p_dest.'''
        # If p_dest exists on the target, it will be overwritten
        self.execute((source, dest), exe='scp')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Config:
    '''Deployment configuration'''

    def __init__(self):
        # This dict stores all the known targets for deploying this app. Keys
        # are target names, values are Target instances.
        self.targets = {}
        # Managing target's config.py files
        #
        # If you want to automate the management of targets' config.py files, 
        # specify, in the following attribute, a path, on your local machine,
        # where local copies of config.py files will be created / updated, and
        # pushed to targets. Note that in that mode, any manual change performed
        # in config.py files on targets can potentially be lost.
        #
        # Within this folder, every config.py file is named:
        #
        #                        <key>.config.py
        #
        # <key> is the key at which the Target object can be found within
        # p_self.targets.
        self.configFiles = None

    def warnFiles(self, collectOnly=False):
        '''Issue warnings if config files are in use but not complete, or
           silently collect missing files if p_collectOnly is True.'''
        # No warning at all if config files are not in use
        folder = self.configFiles
        if not folder: return ()
        # Issue a warning if the folder does not exist
        folder = Path(folder)
        if not folder.is_dir():
            if not collectOnly:
                print(CFG_D_NO % folder)
            return
        # Issue a warning if there is not exactly one config.py file per target
        targets = self.targets
        info = O(missing=[], surplus=[])
        for name, target in targets.items():
            fileName = f'{name}.config.py'
            path = folder / fileName
            if not path.is_file():
                info.missing.append(fileName)
        # Also note files being there but that do not corrrespond to any target
        # from p_self.targets.
        for sub in folder.glob('*'):
            name = sub.name
            # Ignore files not being configuration files
            if not name.endswith('.config.py'): continue
            key = name.split('.', 1)[0]
            if key not in targets:
                info.surplus.append(name)
        if info.missing and not collectOnly:
            print(CF_MIS % (len(info.missing), folder, ', '.join(info.missing)))
        if info.surplus and not collectOnly:
            print(CF_SUR % (len(info.surplus), folder, ', '.join(info.surplus)))
        return info

    def syncFiles(self, info):
        '''Create any missing config.py file within p_self.configFiles'''
        if info is None:
            # The files folder is not defined in the config
            print(SYNC_KO)
            return
        # Do nothing if p_info s None: nothing is missing
        if not info.missing:
            print(SYNC_NN)
            return
        # Ensure folder p_self.configFiles exists
        folder = Path(self.configFiles)
        folder.mkdir(parents=True, exist_ok=True)
        # Create any missing file. Lazy-import the local module to avoid loading
        # it in RAM when not needed.
        from appy.deploy import local
        for missing in info.missing:
            # Get the corresponding Target instance
            target = self.targets[missing.split('.',1)[0]]
            # Misuse class local.Target: I want to use one of its methods
            o = local.Target()
            o.folder = target.sitePath
            o.app = target.siteApp.getLocalFolder(Path(f'{o.folder}/lib'))
            o.port = target.sitePort
            o.createFile(folder/missing, local.config)
            print(SYNC_F_C % missing)

    def pushFile(self, targetName, target):
        '''Copies the local config.py file corresponding to this p_target to the
           distant machine.'''
        # Don't do anything if sync is not enabled
        folder = self.configFiles
        if not folder: return
        # Find the local file
        local = Path(folder) / f'{targetName}.config.py'
        if not local.is_file():
            print(SYNC_NF % local)
            return
        # Copy it to the p_target
        target.copy(str(local), f'{target.sitePath}/config.py')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Deployer:
    '''App deployer'''

    # apt command for installing packages non interactively
    apt = 'DEBIAN_FRONTEND=noninteractive apt-get -yq install'

    # OS packages being Appy dependencies
    osDependencies = 'libreoffice git python3-pip apache2 imagemagick'

    # Commands for which a target is not required
    noTargetCommands = ('list',)

    # Commands accepting several targets
    manyTargetsCommands = ('update', 'view')

    def __init__(self, appPath, sitePath, command, targetName=None,
                 options=None, method=None, blind=False):
        # The path to the app
        self.appPath = appPath
        # The path to the reference, local site, containing targets definition
        self.sitePath = sitePath
        # The chosen target(s), as a string (program input). If p_targetName is
        # None and p_command requires a target, the default target(s) will be
        # selected.
        self.targetName = targetName
        # Options
        self.options = options or ()
        # When restarting the distant site after having updated it, must a
        # m_method be run?
        self.method = method
        # Must the "update" command be run blind ?
        self.blind = blind
        # Will hold the list of Target instances corresponding to p_targetName
        self.targets = None
        # Will hold the first (or unique) Target from p_self.target
        self.target = None
        # The command to execute
        self.command = command
        # The app config
        self.config = None

    def quote(self, arg):
        '''Surround p_arg with quotes'''
        r = arg if isinstance(arg, str) else str(arg)
        return f"'{r}'"

    def buildPython(self, statements):
        '''Builds a p_command made of these Python p_statements'''
        statements = ';'.join(statements)
        return f"python3 -c \\\"{statements}\\\""

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                              Commands
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Command for consulting the last lines in a target's app.log file
    tail = 'tail%s -n %d %s/var/app.log'

    def sync(self, info=None):
        '''Create one config.py file for every target for which no such file
           locally exists in folder p_self.config.deploy.configFiles.'''
        return self.config.deploy.syncFiles(info)

    def list(self):
        '''Lists the available targets on the config'''
        infos = []
        default = None
        i = 1
        config = self.config.deploy
        # Make a first round to get the longest target name
        longest = 0
        for name, target in config.targets.items():
            longest = max(len(name), longest)
        # Walk targets
        for name, target in config.targets.items():
            suffix = ' [default]' if target.default else ''
            zi = str(i).zfill(2)
            info = f'{zi}. {name.ljust(longest)} - {target}{suffix}'
            infos.append(info)
            if name == 'ALL':
                # This word is reserved
                print(ALL_RESV)
            i += 1
        infos = '\n'.join(infos)
        print(T_LIST % (self.appPath.name, self.sitePath.name, infos))
        # Add a warning if a "configFiles" folder is defined but does not
        # contain one config.py file per target.
        if config.configFiles:
            files = config.warnFiles(collectOnly='sync' in self.options)
        else:
            files = None
        # Apply options
        self.applyOptions(files)

    def info(self):
        '''Retrieve info about the target OS'''
        self.target.execute('cat /etc/lsb-release')

    def lo(self, target):
        '''Create or update an init script for LibreOffice on this p_target'''
        # Lazy-import module "init" to avoid loading it into RAM when not needed
        from appy.deploy import init
        init.LO(target).deploy()

    def init(self, target):
        '''Create or update an init script for this p_target'''
        from appy.deploy import init
        init.Site(target).deploy()

    def apache(self, target):
        '''Create or update a virtual host on this p_target'''
        # Ensure an Apache configuration has been defined
        if not target.apache:
            print(APA_NO)
            return
        from appy.deploy.apache import Apache
        Apache(target).deploy()

    def clean(self, target):
        '''Recursively clean any .pyc file in the p_target's lib folder'''
        target.execute(f'find {target.sitePath}/lib -name "*.pyc" -delete')

    def applyOptions(self, arg=None):
        '''Apply the options as defined in p_self.options'''
        # Apply options
        for option in self.options:
            descr = OPT_INF[option]
            print(OPT_APPLY % (termColorize(option, color='3'), descr))
            method = getattr(self, option)
            if arg:
                method(arg)
            else:
                method()

    def install(self):
        '''Installs required dependencies on the target via "apt" and "pip3" and
           create special user "appy" on the server.'''
        target = self.target
        commands = [
          # Install required dependencies via Aptitude
          f'{self.apt} {self.osDependencies}',
          # Install Appy and dependencies via pip
          'pip3 install appy -U',
          # Create special user "appy"
          'adduser --disabled-password --gecos appy appy'
        ]
        target.execute(';'.join(commands))
        # Apply options
        self.applyOptions(target)

    def site(self):
        '''Creates an Appy site on the distant server'''
        t = self.target
        # Collect commands to be potentially ran on the distant folders where
        # repos will be downloaded.
        configCommands = set()
        # Build args to appy/bin/make
        q = self.quote
        args = [q(t.sitePath), q('-a'), q(t.siteApp.asSpecifier()), q('-p'),
                q(t.sitePort), q('-o'), q(t.siteOwner)]
        t.siteApp.collectIn(configCommands, t.sitePath)
        if t.siteExt:
            args.append(q('-e'))
            args.append(q(t.siteExt.asSpecifier()))
            t.siteExt.collectIn(configCommands, t.sitePath)
        if t.siteDependencies:
            args.append(q('-d'))
            for dep in t.siteDependencies:
                args.append(q(dep.asSpecifier()))
                dep.collectIn(configCommands, t.sitePath)
        # Build the statements to pass to the distant Python interpreter
        argsS = ','.join(args)
        statements = [
          'import sys', 'from appy.bin.make import Make',
          f"sys.argv=['make.py','site',{argsS}]",
          'Make().run()'
        ]
        command = self.buildPython(statements)
        # Execute it
        t.execute(command)
        # Execute the config commands if any
        if configCommands:
            t.execute(';'.join(configCommands))
        # Copy the local config.py if config files are synchronized
        self.config.deploy.pushFile(self.targetName, t)
        # Apply options
        self.applyOptions(t)

    def update(self):
        '''Performs, on these p_self.targets, an update of all software known to
           the site and coming from external sources (app and dependencies), and
           (re)starts the site.'''
        targets = self.targets
        # After updating a given target, the last lines of its log file will be
        # shown via a command like:
        #
        #                       tail -f -n 100 app.log
        #
        # Then, when you are tired looking at this log file, type <Ctrl>-C to
        # update the next target or retrieve terminal prompt.
        #
        # If there are several targets, the number of shown lines will be
        # reduced:
        #
        #                        tail -n 30 app.log
        #
        total = len(self.targets)
        tailNb = 100 if total == 1 else 30
        i = 0
        # Browse targets
        for targetName, target in self.targets.items():
            i += 1
            print(TG_ACT % (TP_UPDATE, termColorize(targetName), i, total))
            if not self.blind:
                print(TG_NEXT)
            # (1) Build and run the set of commands to update the app, ext and
            #     dependencies.
            commands = []
            siteOwner = target.siteOwner
            lib = Path(target.sitePath) / 'lib'
            for name in ('App', 'Ext'):
                repo = getattr(target, f'site{name}')
                if repo:
                    command, folder = repo.getUpdateCommand(lib)
                    commands.append(command)
                    commands.append(f'chown -R {siteOwner} {folder}')
            # Update dependencies
            for repo in target.siteDependencies:
                command, folder = repo.getUpdateCommand(lib)
                commands.append(command)
                commands.append(f'chown -R {siteOwner} {folder}')
            # Run those commands as the main SSH user: else, agent forwarding
            # will not be allowed and will prevent to update repositories using
            # public key authentication.
            commandS = ';'.join(commands)
            command = f'{Repository.getEnvironment()} {commandS}'
            target.execute(command)
            # (2) Copy the config.py file if applicable
            self.config.deploy.pushFile(targetName, target)
            # (3) Apply potential options
            self.applyOptions(target)
            # (4) Build and run the command to restart the distant site and
            #     possibly display its log file.
            commands = []
            restart = f'{target.sitePath}/bin/site restart'
            if self.method:
                restart = f'{restart} -m {self.method}'
            commands.append(restart)
            # Display the site's app.log (if not blind)
            if not self.blind:
                commands.append(self.tail % (' -f', tailNb, target.sitePath))
            # These commands will be ran with target.siteOwner
            command = ';'.join(commands)
            owner = siteOwner.split(':')[0]
            if owner != target.sshLogin:
                command = f"su - {owner} -c '{command}'"
            target.execute(command, forceExit=self.blind)

    def view(self):
        '''Launch a command "tail -f" on the target's app.log file'''
        total = len(self.targets)
        if total == 1:
            # Display the log file of a single target, with tail "-f"
            lines = 200
            opt = ' -f'
        else:
            # Display several target's log files: do not use the '-f' option and
            # show a smaller number of lines per target.
            lines = 5
            opt = ''
        # Browse targets
        i = 0
        for name, target in self.targets.items():
            i += 1
            print(TG_ACT % (TG_LOG, termColorize(name), i, total))
            target.execute(self.tail % (opt, lines, target.sitePath))

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                             Main method
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def getTargets(self, targets):
        '''Return the targets onto which the command must be applied, among all
           p_targets as defined in the config.'''
        names = self.targetName
        notFound = []
        if not names:
            # Collect the default target(s)
            r = {n:t for n,t in targets.items() if t.default}
        else:
            r = {} # Collect the chosen targets ~{s_name:Target}~
            for name in names.split(','):
                if name == 'ALL':
                    # Add all targets
                    for n, t in targets.items():
                        r[n] = t
                elif name in targets:
                    r[name] = targets[name]
                else:
                    notFound.append(name)
                    print(TARGET_KO % name)
        return r, notFound

    def run(self):
        '''Performs p_self.command on the specified p_self.targetName'''
        # Add the relevant paths to sys.path
        for path in (self.sitePath, self.sitePath / 'lib', self.appPath.parent):
            sys.path.insert(0, str(path))
        # Get the config and ensure it is complete
        self.config = __import__(self.appPath.name).Config
        cfg = self.config.deploy
        if not cfg:
            print(NO_CONFIG)
            sys.exit(1)
        targets = cfg.targets
        if not targets:
            print(NO_TARGET)
            sys.exit(1)
        # Get the specified target(s) when relevant
        if self.command not in Deployer.noTargetCommands:
            self.targets, notFound = self.getTargets(targets)
            if not self.targets:
                if self.targetName is None:
                    message = TARGET_NO
                else:
                    available = tuple(self.config.deploy.targets.keys())
                    message = TARGET_VL % '\n'.join(available)
                print(message)
                sys.exit(1)
            # Abord the whole operation if at least one wrong target was found
            if notFound:
                sys.exit(1)
            if self.command not in Deployer.manyTargetsCommands:
                # Unwrap the first and unique target in p_self.target
                for target in self.targets.values():
                    self.target = target
                    break
                # Abort if there is more than one target
                if len(self.targets) > 1:
                    print(SINGLE_TG % self.command)
                    sys.exit(1)
        getattr(self, self.command)()
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
