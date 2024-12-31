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
# This module implements "integration" testing. It works by:
# - defining an executable test plan as an ODT file containing tests as tables
#   conforming to conventions as described in appy/utils/tables.py ;
# - executing this plan, or only a sub-part of its tests ;
# - producing a report about success or failure of every test ran.

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from pathlib import Path
import os, os.path, sys, time

from appy.bin import Program
from appy.xml.diff import Diff
from appy.utils import Traceback
from appy.utils import path as putils
from appy.utils.tables import TablesParser

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class TesterError(Exception): pass
class InternalError(Exception): pass

# TesterError-related constants
TEST_PLAN_KO = 'The test plan you specified does not correspond to an ' \
               'existing ODT file.'
_FLAVOUR     = 'A flavour represents a test configuration.'
FLV_NOT_LIST = 'The flavours specified must be a list or tuple of ' \
               'string. ' + _FLAVOUR
FLV_NOT_STR  = 'Each specified flavour must be a string. ' + _FLAVOUR
TEST_FCT_KO  = 'You must give a test factory that inherits from the abstract ' \
               '"appy.test.integration.TestFactory" class.'
CREAT_T_N_O  = 'The appy.test.integration.TestFactory.createTest method must ' \
               'be overridden in your concrete TestFactory.'
M_TABLE_KO   = 'No table "TestSuites" found in test plan "%s".'
M_TABLE_MF   = 'The "TestSuites" table must have at least two columns, named ' \
               '"Name" and "Description".'
T_SUITE_KO   = 'Table "%s.descriptions" and/or "%s.data" were not found.'
T_SUITE_MF   = 'Tables "%s.descriptions" and "%s.data" do not have the same ' \
               'length. For each test in "%s.data", You should have one line ' \
               'in "%s.descriptions" describing the test.'
FILE_KO      = 'File to compare "%s" was not found.'
WRONG_FLV    = 'Wrong flavour "%s". Flavour must be one of %s.'
TEST_A_SUITE = 'Specify a single test or test suite but not both.'

# InternalError-related constants
TR_SING_ERR  = 'You can only use the TestReport constructor once. After that ' \
               'you can access the single TestReport instance via the ' \
               'TestReport.instance static member.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class TestReport:
    '''Collects data about test results for producing a report'''

    # The single TestReport instance to be ever created
    instance = None

    def __init__(self, reportPath, verbose):
        if TestReport.instance is None:
            self.report = open(str(reportPath), 'w')
            self.verbose = verbose
            TestReport.instance = self
        else:
            raise InternalError(TR_SING_ERR)

    def say(self, msg, force=False):
        if self.verbose or force:
            print(msg)
        self.report.write(msg)
        self.report.write('\n')

    def close(self): self.report.close()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Test:
    '''Abstract test class'''
    def __init__(self, testData, testDescription, testFolder,
                 config, flavour, rendererParams):
        self.data = testData
        self.description = testDescription
        self.testFolder = testFolder
        self.tempFolder = None
        self.report = TestReport.instance
        self.errorDump = None
        self.config = config
        self.flavour = flavour
        self.rendererParams = rendererParams

    def compareFiles(self, expected, actual, areXml=False, xmlTagsToIgnore=(),
                     xmlAttrsToIgnore=()):
        '''Compares 2 files. r_ is True if files are different. The differences
        are written in the test report.'''
        for f in expected, actual:
            assert f.is_file(), TesterError(FILE_KO % f)
        # Expected result (may be different according to flavour)
        expected = str(expected)
        actual = str(actual)
        if self.flavour:
            specific = f'{expected}.{self.flavour}'
            if os.path.exists(specific):
                expected = specific
        # Perform the comparison
        differ = Diff(actual,expected,areXml,xmlTagsToIgnore,xmlAttrsToIgnore)
        return not differ.filesAreIdentical(report=self.report)

    def run(self):
        say = self.report.say
        say('-' * 79)
        say(f'- Test {self.data["Name"]}.')
        bn = '\n'
        say(f'- {self.description}{bn}')
        # Prepare test data
        self.tempFolder = self.testFolder / 'temp'
        if self.tempFolder.exists():
            putils.FolderDeleter.delete(self.tempFolder)
        self.tempFolder.mkdir()
        try:
            self.do()
            say('Checking result...')
            testFailed = self.checkResult()
        except:
            testFailed = self.onError()
        self.finalize()
        return testFailed

    def do(self):
        '''Concrete part of the test. Must be overridden.'''

    def checkResult(self):
        '''r_ is False if the test succeeded.'''
        return True

    def onError(self):
        '''What must happen when an exception is raised during test
           execution? Returns True if the test failed.'''
        self.errorDump = Traceback.get()
        self.report.say('Exception occurred:')
        self.report.say(self.errorDump)
        return True

    def finalize(self):
        '''Performs sme cleaning actions after test execution.'''
        pass

    def isExpectedError(self, expectedMessage):
        '''An exception was thrown. So check if the actual error message
           (stored in self.errorDump) corresponds to the p_expectedMessage.'''
        r = True
        for line in expectedMessage:
            if self.errorDump.find(line) == -1:
                r = False
                self.report.say(f'"{line}" not found among error dump.')
                break
        return r

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class TestFactory:
    @staticmethod
    def createTest(testData, testDescription, testFolder, config, flavour,
                   rendererParams):
        '''This method allows you to create tests that are instances of classes
           that you create. Those classes must be children of
           appy.shared.test.Test. m_createTest must return a Test instance and
           is called every time a test definition is encountered in the test
           plan.'''
        raise TesterError(CREAT_T_N_O)

# Program help - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
HELP_V   = 'Dumps the whole test report on stdout'
HELP_KT  = 'Keep the temp folder, in order to be able to copy some results ' \
           'and make them expected results when needed.'
HELP_TST = 'Run only a specified test.'
HELP_TSU = 'Run only a specified test suite.'
HELP_RP  = 'Specific renderer parameters, of the form name1=val1,name2=v2'
HELP_FLV = 'Specify the configuration flavour, which may be one of %s.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Tester(Program):
    def __init__(self, testPlan, flavours, testFactory):
        # Check test plan
        plan = Path(testPlan)
        if not plan.is_file() or not plan.name.endswith('.odt'):
            raise TesterError(TEST_PLAN_KO)
        self.testPlan = plan
        self.testFolder = plan.absolute().parent
        # Check flavours
        if not isinstance(flavours, (list, tuple)):
            raise TesterError(FLV_NOT_LIST)
        for flavour in flavours:
            if not isinstance(flavour, str):
                raise TesterError(FLV_NOT_STR)
        self.flavours = flavours
        self.flavour = None
        # Check test factory
        if not issubclass(testFactory, TestFactory):
            raise TesterError(TEST_FCT_KO)
        self.testFactory = testFactory
        # Call the base constructor: it will read and check args
        Program.__init__(self)
        # Create the report that will collect info from all executed tests
        self.report = TestReport(self.testFolder / 'Tester.report',
                                 self.verbose)

    def getRendererParams(self, params):
        '''Returns a dict with additional Renderer params'''
        r = {}
        if not params: return r
        for param in params.split(','):
            name, value = param.split('=')
            r[name] = value
        return r

    def defineArguments(self):
        '''Define the allowed arguments for this program'''
        parser = self.parser
        add = parser.add_argument
        if self.flavours:
            add('flavour', help=Make.HELP_FLV % self.flavours)
        add('-v', '--verbose', action='store_true', help=HELP_V)
        add('-k', '--keepTemp', action='store_true', help=HELP_KT)
        add('-t', '--test', help=HELP_TST)
        add('-s', '--testSuite', help=HELP_TSU)
        add('-r', '--rendererParams', help=HELP_RP)

    def analyseArguments(self):
        '''Check arguments'''
        if self.flavours:
            sflavours = ', '.join(self.flavours)
            if self.flavour not in self.flavours:
                raise TesterError(WRONG_FLV % (self.flavour, sflavours))
        args = self.args
        self.verbose = args.verbose
        self.keepTemp = args.keepTemp
        self.rendererParams = self.getRendererParams(args.rendererParams)
        # If the user wants to run a single test
        self.singleTest = args.test
        # If the user wants to run a single test suite
        self.singleSuite = args.testSuite
        if self.singleTest and self.singleSuite:
            raise TesterError(TEST_A_SUITE)

    def runSuite(self, suite):
        self.report.say('*' * 79)
        self.report.say(f'* Suite {suite["Name"]}.')
        bn = '\n'
        self.report.say(f'* {suite["Description"]}{bn}')
        i = -1
        for testData in self.tables[f'{suite["Name"]}.data']:
            self.nbOfTests += 1
            i += 1
            testName = testData['Name']
            if testName.startswith('_'):
                self.nbOfIgnoredTests += 1
            elif self.singleTest and (testName != self.singleTest):
                self.nbOfIgnoredTests += 1
            else:
                t = suite['Name']
                description = self.tables[f'{t}.descriptions'][i]['Description']
                test = self.testFactory.createTest(
                    testData, description, self.testFolder, self.config,
                    self.flavour, self.rendererParams)
                testFailed = test.run()
                if not self.verbose:
                    sys.stdout.write('.')
                    sys.stdout.flush()
                if testFailed:
                    self.report.say('Test failed.\n')
                else:
                    self.report.say('Test successful.\n')
                    self.nbOfSuccesses += 1
    def run(self):
        '''Runs the tests'''
        self.startTime = time.time()
        self.report.say('Parsing ODT file... ')
        self.tables = tables = TablesParser(self.testPlan).run()
        self.config = None
        ext = f'.{self.flavour}' if self.flavour else ''
        configTableName = f'Configuration{ext}'
        if configTableName in tables:
            self.config = tables[configTableName].asDict()
        self.tempFolder = os.path.join(self.testFolder, 'temp')
        if os.path.exists(self.tempFolder):
            putils.FolderDeleter.delete(self.tempFolder)
        self.nbOfTests = 0
        self.nbOfSuccesses = 0
        self.nbOfIgnoredTests = 0
        if 'TestSuites' not in tables:
            raise TesterError(M_TABLE_KO % str(self.testPlan))
        # Browse test suites
        for suite in tables['TestSuites']:
            if 'Name' not in suite or 'Description' not in suite:
                raise TesterError(M_TABLE_MF)
            # Must we ignore this test suite ?
            if suite['Name'].startswith('_'):
                name = suite['Name'][1:]
                tsIgnored = True
            else:
                name = suite['Name']
                tsIgnored = self.singleSuite and name != self.singleSuite
            # For every suite, 2 tables must exist: one with test descriptions
            # and the other with test data.
            descrTable = tables.get(f'{name}.descriptions')
            dataTable = tables.get(f'{name}.data')
            if not descrTable or not dataTable:
                raise TesterError(T_SUITE_KO % (name, name))
            if len(descrTable) != len(dataTable):
                raise TesterError(T_SUITE_MF % ((name,)*4))
            # The suite can still be ignored if self.singleTest is not among it
            if self.singleTest:
                inSuite = False
                for test in dataTable:
                    testName = test['Name']
                    if testName.startswith('_'): testName = testName[1:]
                    if testName == self.singleTest:
                        inSuite = True
                        break
                if not inSuite: tsIgnored = True
            if tsIgnored:
                nbOfIgnoredTests = len(dataTable)
                self.nbOfIgnoredTests += nbOfIgnoredTests
                self.nbOfTests += nbOfIgnoredTests
            else:
                self.runSuite(suite)
        self.finalize()

    def finalize(self):
        duration = time.time() - self.startTime
        total = self.nbOfTests-self.nbOfIgnoredTests
        msg = f'{self.nbOfSuccesses}/{total} successful test(s) performed ' \
              f'in {duration:.2f} seconds'
        if self.nbOfIgnoredTests > 0:
            msg += f', but {self.nbOfIgnoredTests} ignored test(s) not counted'
        msg += '.'
        self.report.say(msg, force=True)
        self.report.close()
        if not self.keepTemp:
            if os.path.exists(self.tempFolder):
                putils.FolderDeleter.delete(self.tempFolder)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
