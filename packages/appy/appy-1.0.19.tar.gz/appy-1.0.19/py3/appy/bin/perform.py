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
from appy.model.utils import importModule
from appy.test.performance import Config, Tester

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Performer(Program):
    '''Executes performance tests by sending HTTP requests to a Appy server and
       measuring response times.'''

    HELP_CONFIG = 'The configuration file. It must be a file containing an ' \
      'instance of appy.test.performance.Config, in a variable named "cfg".'
    CONFIG_NOT_FOUND = '%s does not exist or is not a file.'
    CONFIG_KO = '%s does not contain variable "cfg" or this variable does ' \
      'not hold an instance of appy.test.performance.Config.'

    def defineArguments(self):
        '''Define the allowed arguments for this program'''
        parser = self.parser
        # The configuration file
        parser.add_argument('config', help=Performer.HELP_CONFIG)

    def analyseArguments(self):
        '''Check and stores arguments'''
        name = self.args.config
        path = Path(name)
        # Does the config file exist ?
        if not path.is_file():
            self.exit(self.CONFIG_NOT_FOUND % name)
        # Does is contain the right variable ?
        config = importModule('config', name)
        if not hasattr(config, 'cfg') or not isinstance(config.cfg, Config):
            self.exit(self.CONFIG_KO % name)
        # Are configuration parameters correct ?
        self.config = config.cfg
        msg = self.config.check()
        if msg:
            self.exit(msg)

    def run(self):
        Tester(self.config).run()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == '__main__': Performer().run()
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
