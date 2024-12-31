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
import os.path, threading

import appy.pod
from appy import utils
from appy.pod import PodError
from appy.pod.converter import Converter
from appy.utils.path import getOsTempFolder

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
LO_PORT_KO = 'Wrong LibreOffice port "%s". Make sure it is an integer.'
CONV_ERR   = 'An error occurred during the conversion. %s'
NO_PY_PATH = 'Extension of result file is "%s". In order to perform ' \
             'conversion from ODT to this format we need to call ' \
             'LibreOffice. But the Python interpreter which runs the current ' \
             'script does not know UNO, the library that allows to connect ' \
             'to LibreOffice in server mode. If you can\'t install UNO in ' \
             'this Python interpreter, you can specify, in parameter ' \
             '"pythonWithUnoPath", the path to a UNO-enabled Python ' \
             'interpreter. One such interpreter may be found in ' \
             '<open_office_path>/program.'
PY_PATH_KO = '"%s" is not a file. You must here specify the absolute path of ' \
             'a Python interpreter (.../python, .../python.sh, .../python.exe' \
             ', .../python.bat...).'
INCOMP_OD  = 'Warning: your OpenDocument file may not be complete (ie, ' \
             'imported documents may not be present). This is because we ' \
             'could not connect to LibreOffice in server mode: %s'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class LO:
    '''Represents a LibreOffice (LO) server with which Appy communicates via its
       UNO API.'''

    def __init__(self, pool, port):
        # A link to the pool
        self.pool = pool
        # The port on which the LO server listens
        self.port = port

    def getCsvOptions(self, renderer, format):
        '''Get CSV options if the output p_format is CSV'''
        if format == 'csv':
            r = (renderer.csvOptions or renderer.CsvOptions.default).asString()
        else:
            r = None
        return r

    def __call__(self, renderer, resultName, result, format):
        '''Call LO by using the Appy converter object'''
        r = None
        # Get CSV options if a CSV file must be produced
        csvOptions = self.getCsvOptions(renderer, format)
        # Call LO
        ren = renderer
        server = self.pool.server
        try:
            # Try first to directly instantiate a Converter
            try:
                try:
                    Converter(resultName, result, server, self.port,
                      ren.stylesTemplate, ren.optimalColumnWidths,
                      ren.distributeColumns, ren.script, ren.resolveFields,
                      ren.pdfOptions, csvOptions, ren.ppp, ren.stream,
                      ren.pageStart).run()
                except Converter.Error as ce:
                    raise PodError(CONV_ERR % str(ce))
            except ImportError:
                # I do not have UNO. So try to launch a UNO-enabled Python
                # interpreter which should be in self.pool.python.
                pyPath = self.pool.python
                if not pyPath:
                    raise PodError(NO_PY_PATH % format)
                if not os.path.isfile(pyPath):
                    raise PodError(PY_PATH_KO % pyPath)
                convScript = '%s/converter.py' % \
                             os.path.dirname(appy.pod.__file__)
                cmd = [pyPath, convScript, resultName, result,
                       '-e', server, '-p', str(self.port)]
                add = cmd.append
                if ren.stylesTemplate:
                    add('-t'); add(ren.stylesTemplate)
                if ren.optimalColumnWidths:
                    add('-o'); add(str(ren.optimalColumnWidths))
                if ren.distributeColumns:
                    add('-d'); add(str(ren.distributeColumns))
                if ren.script:
                    add('-s'); add(ren.script)
                if ren.resolveFields:
                    add('-r'); add(ren.resolveFields)
                if ren.pdfOptions:
                    add('-f'); add(ren.pdfOptions)
                if csvOptions:
                    add('-i'); add(csvOptions)
                if ren.ppp: add('-c')
                if ren.stream != 'auto':
                    add('-a'); add(str(ren.stream))
                if ren.pageStart > 1:
                    add('-g'); add(str(ren.pageStart))
                out, r = utils.executeCommand(cmd)
        except PodError as pe:
            # When trying to call LO in server mode for producing ODT or ODS
            # (=forceOoCall=True), if an error occurs we have nevertheless
            # an ODT or ODS to return to the user. So we produce a warning
            # instead of raising an error.
            if format in ren.templateTypes and ren.forceOoCall:
                print(INCOMP_OD % str(pe))
            else:
                raise pe
        return r

    def getLockFileName(self):
        '''Get the absolute path to the lock file, in the pool folder,
           corresponding to the current thread using this LO instance.'''
        name = '%s.%d' % (threading.get_ident(), self.port)
        return os.path.join(self.pool.folder, name)

    def lock(self):
        '''When multiple LOs are in use, write a file in the pool folder,
           indicating that this LO instance is used by the currently running
           thread.'''
        try:
            f = open(self.getLockFileName(), 'w')
            f.close()
        except (IOError, OSError):
            pass

    def unlock(self):
        '''When multiple LOs are in use, remove, from the pool folder, the file
           indicating that this LO instance was used by the currently running
           thread.'''
        try:
            os.remove(self.getLockFileName())
        except (IOError, OSError):
            pass

    def __repr__(self):
        '''p_self's short string representation'''
        return f'‹LO port={self.port}›'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class LoPool:
    '''Via this class, Appy can manage communication with several LibreOffice
       (LO) servers.'''

    # Even if a single LO server is used, a LoPool instance is created,
    # containing a single LO instance.

    @classmethod
    def get(class_, python, server, port):
        '''Create and return a LoPool instance, based on passed attributes'''
        # Do not create the pool if no port is specified
        if port is None: return
        # Ensure p_port is correct
        if isinstance(port, tuple) or isinstance(port, list):
            for p in port:
                if not isinstance(p, int):
                    raise Exception(LO_PORT_KO % str(p))
        elif not isinstance(port, int):
            raise Exception(LO_PORT_KO % str(port))
        return LoPool(python, server, port)

    def __init__(self, python, server, port):
        # The path to the Python interpreter being UNO-compliant (only required
        # if the Python interpreter running Appy is not UNO-compliant). For
        # performance, using this alternate interpreter should be avoided.
        self.python = python
        # The machine onto which LO servers, being part of this pool, run. Can
        # be "localhost" or a distant server. All LO servers of the pool run on
        # the same machine.
        self.server = server
        # Create as many LO instances as there are ports defined in p_port
        if isinstance(port, int):
            self.los = LO(self, port)
        else:
            los = self.los = {}
            for p in port:
                los[p] = LO(self, p)
            # Define the pool folder
            self.folder = self.getFolder()

    def getFolder(self):
        '''Return the pool folder on this machine. Create it if it does not
           exist yet.'''
        # If several LO servers are in use, a temp folder must be created, named
        #
        #                     <OS temp folder>/appy/lo
        #
        # Every time any thread from any process running on this machine uses
        # appy.pod to communicate with a LO instance, it will create a file
        # named
        #
        #         <OS temp folder>/appy/lo/<thread_id>.<lo_port>
        #
        # The file contains the port of the LO instance being contacted.
        #
        # Everytime a thread needs to communicate with LO, it will search for a
        # LO instance not being busy, by reading these thread-specific files. If
        # it finds one, it will choose it. Else, it will choose the oldest
        # contacted LO.
        r = os.path.join(getOsTempFolder(), 'appy', 'lo')
        if not os.path.isdir(r):
            # Create it
            os.makedirs(r)
        return r

    def readBusy(self):
        '''Return info about the currently running LO servers'''
        # Returns a tuple (busy, oldest), where:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # busy   | is a dict ~{i_port: s_threadId}~, indicating which thread is
        #        | currently communicating with which LO ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # oldest | is the LO instance corresponding to the oldest contacted LO.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # Read files from the pool folder
        folder = self.folder
        names = os.listdir(folder)
        if not names: return None, None
        r = {}
        oldest = oldestDate = None
        los = self.los
        for name in names:
            # Ignore irrelevant files
            parts = name.split('.')
            if len(parts) != 2: continue
            # Unwrap the thread ID and LO port
            id, port = parts
            try:
                port = int(port)
            except Exception:
                continue
            # Ignore this LO instance if not among "our" LO instances
            if port not in los: continue
            # Add an entry in "r"
            r[port] = id
            # Update "oldest"
            mtime = os.stat(os.path.join(folder, name)).st_mtime
            if oldest is None or mtime < oldestDate:
                oldest = los[port]
                oldestDate = mtime
        return r, oldest

    def chooseLO(self):
        '''Choose and return the LO instance that will manage the current
           request.'''
        # The result is a tuple (LO, b_multiple). The boolean value indicates if
        # there are at least 2 LO instances defined in p_self.los.

        # Return the unique LO instance
        if isinstance(self.los, LO): return self.los, False
        # Choose among several LO instances. Read info about busy LO instances.
        busy, oldest = self.readBusy()
        for port, lo in self.los.items():
            if not busy or port not in busy:
                # I have a free LO instance
                return lo, True
        # All the LOs are busy. Return the oldest contacted one.
        return oldest, True

    def __call__(self, renderer, resultName, format=None, outputName=None):
        '''Call one of our LO servers to convert or update, in this p_format,
           the ODF pod result whose path is in p_resultName. Return LO's output
           on stderr, which contains an error message if an error occurred and
           is empty else.'''

        # If p_outputName is:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # None     | The result will be a file whose name is p_resultName, whose
        #          | file extension has been replaced with the one specified in
        #          | p_format.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # not None | The result will be a file named p_outputName. p_format will
        #          | be ignored: the output format will depend on p_outputName's
        #          | file extension.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        r = ''
        # Determine the "result" to ask to LibreOffice
        if outputName:
            result = outputName
            format = os.path.splitext(result)[-1][1:]
        else:
            result = format
        # Get the LO instance that will do the job
        lo, multiple = self.chooseLO()
        # Lock this instance when appropriate
        if multiple: lo.lock()
        # Call LO and return its output on stderr
        try:
            r = lo(renderer, resultName, result, format)
        finally:
            # Unlock it when appropriate
            if multiple: lo.unlock()
        return r
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
