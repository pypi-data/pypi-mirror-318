'''This module contains command-line programs'''

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
import sys, argparse

from appy.model.utils import Object as O

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Program:
    '''Abstract base class for all command-line programs'''

    def __init__(self, **kwargs):
        # p_kwargs may be passed, if this program is not called via the
        # command-line, but programmatically.
        if kwargs:
            self.args = O(**kwargs)
        else:
            # Create the argument parser
            self.parser = argparse.ArgumentParser()
            # Define arguments
            self.defineArguments()
            # Parse arguments
            self.args = self.parser.parse_args()
        # Analyse parsed arguments
        self.analyseArguments()

    def defineArguments(self):
        '''Override this method to define arguments to self.parser (using
           method self.parser.add_argument): see documentation for the
           argparse module.'''

    def analyseArguments(self):
        '''Override this method to analyse arguments that were parsed an stored
           in self.args:
           * check their validity;
           * potentially apply some computation on it and store, on p_self, new
             attributes derived from self.args.
           If this method detects an error within self.args, abort program
           execution by calling m_exit (see below).
        '''

    def exit(self, msg, printUsage=True):
        '''Display this p_msg on stderr and exit the program afer an error has
           been encountered.'''
        print(msg, file=sys.stderr)
        if printUsage:
            self.parser.print_usage()
        return sys.exit(1)

    def run(self):
        '''Executes the program after arguments were successfully analysed'''
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
