#!/usr/bin/env python3

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

from appy.bin import Program
from appy.deploy import Deployer

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Deploy(Program):
    '''This program allows to deploy apps in sites on distant servers'''

    # Available commands
    COMMANDS = {'list':    'Lists the available targets.',
                'info':    'Retrieve info about the target OS.',
                'install': 'Install required dependencies via the OS ' \
                           'package system (currently: "apt" only).',
                'site':    'Create an Appy site on the target.',
                'update':  'Updates a site and (re)start it.',
                'view':    "View app.log's tail on the target."
    }

    def helpCommands(COMMANDS):
        '''Builds the text describing available commands'''
        r = []
        # Get the longest command first
        longest = 0
        for command in COMMANDS:
            longest = max(longest, len(command))
        # Dump help about every command
        for command, text in COMMANDS.items():
            r.append(f'"{command.ljust(longest)}" - {text}')
        return ' -=- '.join(r)

    # Help messages (and message parts)
    LO_SV        = 'LibreOffice (LO) in server mode'
    SITE_NAME    = '<site name>'
    SITE_SV      = 'the site on the target (start,stop,...)'
    INIT_D       = 'Creates an init script /etc/init.d/%s for controlling %s'
    DEB_O        = 'Debian systems only'

    HELP_APP     = 'The path, on this machine, to the app to deploy ' \
                   '(automatically set if called from <site>/bin/deploy).'
    HELP_SITE    = 'The path, on this machine, to the reference site ' \
                   '(automatically set if called from <site>/bin/deploy).'
    HELP_COMMAND = 'The command to perform. Available commands are:\n%s' % \
                   helpCommands(COMMANDS)
    HELP_TARGET  = 'The target(s) to deploy to. If not specified, the ' \
                   'default will be chosen. ["update" & "view" commands ' \
                   'only] You can specify several targets, using a comma-' \
                   'separated list of targets containing no space, ie, ' \
                   '"dev,acc,prod". You can also specify term "ALL" to ' \
                   'denote all targets.'
    HELP_OPTIONS = 'Some commands accept options. Options must be specified ' \
                   'as a comma-separated list of names. [Options ' \
                   'for command "install"] "lo" (%s) - %s. ' \
                   '[Options for command "site"] "lo" (if not executed via ' \
                   'command "install", this option can still be applied when ' \
                   'launching command "site" on some target), "init" (%s) - ' \
                   '%s, "apache" (create an Apache virtual host). [Options ' \
                   'for command "update"] "init" & "apache" (see above), ' \
                   'still available if not applied via the "site" command, ' \
                   'and "clean" - Remove, on the target site\'s lib folder ' \
                   'and sub-folders, *.pyc files.' % \
                   (DEB_O, INIT_D % ('lo', LO_SV),
                    DEB_O, INIT_D % (SITE_NAME, SITE_SV))
    HELP_METHOD  = '["update" command only] When restarting a target after ' \
                   'having updated it, the specified method will be ' \
                   'executed, just after methog tool::onInstall. This method ' \
                   'must exist on the distant tool.'
    HELP_BLIND   = '["update" command only] If set, when updating several ' \
                   'targets, there is no stop between each one (such stops ' \
                   'allow to consult the target\'s app.log to ensure ' \
                   'everything went well).'

    # Allowed options, for every command. A command not being in this dict
    # accepts no option at all.
    allowedOptions = {
      'list'   : ('sync',),
      'install': ('lo',),
      'site'   : ('lo', 'init', 'apache'),
      'update' : ('init', 'apache', 'clean'),
    }

    # Error messages
    FOLDER_KO    = '%s does not exist or is not a folder.'
    COMMAND_KO   = 'Command "%s" does not exist.'
    OPTIONS_NO   = 'Command "%s" accepts no option at all.'
    OPTIONS_KO  =  'Option "%s" is illegal for command "%s".'

    def defineArguments(self):
        '''Define the allowed arguments for this program'''
        parser = self.parser
        add = parser.add_argument
        # Positional arguments
        add('app', help=Deploy.HELP_APP)
        add('site', help=Deploy.HELP_SITE)
        add('command', help=Deploy.HELP_COMMAND)
        # Optional arguments
        add('-t', '--target' , dest='target' , help=Deploy.HELP_TARGET)
        add('-o', '--options', dest='options', help=Deploy.HELP_OPTIONS)
        add('-m', '--method' , dest='method' , help=Deploy.HELP_METHOD)
        add('-b', '--blind'  , dest='blind'  , help=Deploy.HELP_BLIND,
                               action='store_true')

    def analyseOptions(self):
        '''Ensure options are coherent w.r.t the command'''
        if not self.options: return
        command = self.command
        allowed = Deploy.allowedOptions.get(command)
        # Prevent specifying options for commands for which no option is allowed
        if allowed is None:
            self.exit(self.OPTIONS_NO % command)
        # Ensure every specified option is legal w.r.t p_self.command
        for option in self.options:
            if option not in allowed:
                self.exit(self.OPTIONS_KO % (option, command))

    def analyseArguments(self):
        '''Check and store arguments'''
        args = self.args
        # Check and get the paths to the app and site
        for name in ('app', 'site'):
            path = Path(getattr(args, name))
            if not path.is_dir():
                self.exit(self.FOLDER_KO % path)
            setattr(self, name, path)
        self.command = args.command
        if self.command not in Deploy.COMMANDS:
            self.exit(self.COMMAND_KO % self.command)
        self.target = args.target
        self.blind = args.blind
        # Get and analyse options
        if args.options:
            self.options = args.options.split(',')
        else:
            self.options = None
        self.method = args.method
        self.analyseOptions()

    def run(self):
        return Deployer(self.app, self.site, self.command, self.target,
                        options=self.options, method=self.method,
                        blind=self.blind).run()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == '__main__': Deploy().run()
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
