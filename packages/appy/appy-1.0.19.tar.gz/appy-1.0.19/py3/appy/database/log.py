'''Appy module managing log files'''

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
import logging, sys, pathlib

from appy.px import Px
from appy.model.utils import Object as O

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
L_CREA  = '%s created.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Config:
    '''Logging-related parameters for your app'''

    # 2 log files exist per Appy site, one for each of the following types.
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # "app"  | The *app*lication log stores entries corresponding to app-related
    #        | actions performed by users (or the system itself). Method "log",
    #        | available on any Appy object, outputs log in this file. Appy
    #        | itself also uses this log file for outputting various infos (user
    #        | logins, logouts...), warnings or errors.
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # "site" | The site log contains every hit on the site = enery HTTP POST or
    #        | GET request.
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    logTypes = ('app', 'site')

    # Available attributes to dump within log entries
    logAttributes = {
      'time': 'asctime', # The current date & time
      'level': 'levelname', # The log level
      'message': 'message' # The message to log, prefixed by the user login
    }

    def __init__(self, siteDateFormat='%Y/%m/%d %H:%M:%S',
                 appDateFormat='%Y/%m/%d %H:%M:%S',
                 siteAttributes=('time', 'message'),
                 appAttributes=('time', 'level', 'message'),
                 # Add "agent" hereafter to get the browser's User-Agent string
                 siteMessageParts=('ip', 'port', 'command', 'protocol',
                                   'path', 'message'),
                 appMessageParts=('user', 'message'),
                 siteSep=' | ', appSep=' | '):
        '''Initializes the logging configuration options'''

        # - p_siteDateFormat and p_appDateFormat define the format of dates
        #   dumped in log messages;
        # - p_siteAttributes and p_appAttributes store the list of attributes
        #   that will be dumped in every log entry;
        # - p_siteMessageParts and p_appMessageParts store the list of
        #   attributes contained within composite attribute "message";
        # - p_siteSep and p_appSep store the separators that will be inserted
        #   between attributes.

        # Create a sub-object for splitting site- and app-related configuration
        # options.
        for type in self.logTypes:
            sub = O(dateFormat=eval(f'{type}DateFormat'),# ~pathlib.Path~
                    attributes=eval(f'{type}Attributes'),
                    messageParts=eval(f'{type}MessageParts'),
                    sep=eval(f'{type}Sep'))
            setattr(self, type, sub)

    def set(self, siteLogFolder, appLogFolder):
        '''Sets site-specific configuration elements'''
        # self.site.path is the path to the site log file, logging all HTTP
        # traffic on the site.
        self.site.path = pathlib.Path(siteLogFolder)
        # self.app.path is the path to the app-specific log, containing messages
        # dumped by the app and some by Appy itself.
        self.app.path = pathlib.Path(appLogFolder)
        # Typically, the site and app log files have standardized names and are
        # stored in <site>/var, with database-related files:
        # * "siteLogPath"    is <site>/var/site.log
        # * "appLogPath"     is <site>/var/app.log

    def getFormatter(self, type):
        '''Gets a logging.Formatter object for log entries of p_type'''
        sub = getattr(self, type)
        # Define the list of attributes to dump in every log entry
        attributes = []
        for name in sub.attributes:
            attributes.append(f'%({Config.logAttributes[name]})s')
        return logging.Formatter(sub.sep.join(attributes),
                                 datefmt=sub.dateFormat)

    def getLogger(self, type, debug=False):
        '''Return the site or app logger instance (depending on p_type), that
           will output log messages to self.siteLogPath or self.appLogPath. If
           p_debug is True, we are in debug mode: an additional handler will be
           defined for producing output on stdout.'''
        logger = logging.getLogger(type)
        # Get the path to the file where to log messages
        sub = getattr(self, type)
        path = sub.path
        # Add a file handler to the logger
        created = not path.is_file()
        path = str(path)
        logger.addHandler(logging.FileHandler(path))
        if debug:
            # Add an additional handler for outputing messages to stdout as well
            logger.addHandler(logging.StreamHandler(sys.stdout))
            level = logging.DEBUG
        else:
            level = logging.INFO
        # Messages under this level will not be dumped
        logger.setLevel(level)
        # Set a formatter for log entries
        formatter = self.getFormatter(type)
        for handler in logger.handlers:
            handler.setFormatter(formatter)
        # Return the created logger
        if created: logger.info(L_CREA % path)
        return logger

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
LOG_T_KO   = 'Unknown log type "%s".'
LOG_M_KO   = 'Unknown log mode "%s".'
LOG_F_KO   = 'File "%s" does not exist.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Viewer:
    '''Log viewer, available from the UI's admin zone'''

    # Possible modes are the following.
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # "tail" | The n last lines of the selected log file are displayed
    # "full" | The complete file content is shown
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    modes = ('tail', 'full')

    # Attributes having sense in "tail" mode
    bounded = O( # Values having min and max bounds
     n           = O(max=500, min=50, default=100), # Number of retrieved lines
     refreshRate = O(max=30 , min=3, default=15) , # Refresh rate (seconds)
    )
    chunkSize   = 1024 # Number of bytes retrieved at a time

    # The main PX
    px = Px('''
     <!-- Controls -->
     <form class="logControls" id="logForm"
           var="logType=req.logType or 'app';
                mode=req.mode or 'tail'">

      <!-- App or site log ? -->
      <div>
       <input type="radio" value="app"  name="logType" id="app"
              checked=":logType == 'app'" onchange="refreshLogZone()"/>
       <label lfor="app">app</label>
       <input type="radio" value="site" name="logType" id="site"
              checked=":logType == 'site'" onchange="refreshLogZone()"/>
       <label lfor="site">site</label>
      </div>

      <!-- Log file selector -->
      <select name="logFile" var="files=viewer.listFiles(logType)"
              onchange="refreshLogZone()">
        <option for="id, name in files" value=":id"
                selected=":req.logFile == id">:name</option>
      </select>

      <!-- Refresh every x seconds -->
      <div class="iflex1">
       <input name="refreshAuto" id="refreshAuto" type="checkbox"
              checked=":req.refreshAuto in (None, '1')"/>
       <label lfor="refreshAuto" class="textual">Refresh every</label>
       <input var="b=viewer.bounded.refreshRate" name="refreshRate"
              type="number" min=":b.min" max=":b.max" step=":b.min"
              class="editNB rateR"
              value=":viewer.getBounded(req, 'refreshRate')"/>
       <label class="textual">seconds</label>
      </div>

      <!-- Mode (tail or full) -->
      <div class="iflex1">

       <!-- Tail mode -->
       <input type="radio" value="tail"  name="mode" id="tail"
              checked=":mode == 'tail'" onchange="refreshLogZone()"/>

       <!-- Get last x lines -->
       <label class="textual" lfor="tail">Get last</label>
       <input var="b=viewer.bounded.n" name="n" type="number" min=":b.min"
              max=":b.max" class="editNB tailN" step=":b.min"
              value=":viewer.getBounded(req, 'n')"/>
       <label class="textual">lines</label>

       <!-- Full mode -->
       <input type="radio" value="full"  name="mode" id="full"
              checked=":mode == 'full'" onchange="showWholeFile(this)"/>
       <label lfor="full" class="textual">Whole file</label>
      </div>

      <!-- Refresh now -->
      <input type="button" onclick="refreshLogZone()" value="Update"/>
     </form>

     <!-- The file content -->
     <pre id="logContent" class="logText">:content</pre>
     <script>:viewer.getAjaxData(_ctx_)</script>
     <script>initViewer()</script>''',

     js='''
      // Ajax-refresh the log zone
      refreshLogZone = function() {
        let f = document.getElementById('logForm'),
            params = {},
            hook = '1_logsViewer';
        // Remove any existing timeout
        clearTimeoutField(hook);
        form2dict(f, params);
        askField(hook, siteUrl+'/tool', 'view', params);
      }

      showWholeFile = function() {
        // Uncheck the "refresh" box before refreshing the zone
        document.getElementById('refreshAuto').checked = false;
        refreshLogZone();
      }

      initViewer = function() {
        // Set, when appropriate, a timeout for automatic refresh
        let f = document.getElementById('logForm'),
            cb = f['refreshAuto'],
            hook = '1_logsViewer';
        if (cb.checked) {
          let delay = parseInt(f['refreshRate'].value) * 1000;
          setTimeoutField(hook, refreshLogZone, delay);
        }
        // Scroll to the content end
        let content=document.getElementById("logContent");
        content.scrollTop = content.scrollHeight;
      }''',

     css='''.logControls { display:flex; align-items:center; gap:0.3em }
            .logControls select { padding:0; margin:0; font-size:90% }
            .textual { display:flex; align-items:center; font-size:90%;
                       color:grey; text-transform:none }
            .logText { overflow:auto;width:65vw;height:55vh;font-size:90% }
            .editNB { margin:0 0.1em 0 0.3em; text-align:center }
            .rateR { width:2.5em; margin-right:0.4em }
            .tailN { width:4em; margin-right:0.4em }
            #logForm input[type=button] {
              color:inherit; padding:0.3em 0.7em; text-transform:none;
              font-size:80%; border:1px solid grey }''')

    def __init__(self, tool):
        self.tool = tool

    def getBounded(self, req, type):
        '''Get the bounded value of this p_type'''
        b = Viewer.bounded[type]
        r = req[type]
        if r is None:
            r = b.default
        else:
            r = int(r)
        r = min(r, b.max)
        return max(b.min, r)

    def tail(self, f):
        '''Mimics the unix-like tool "tail" by returning the n last lines from
           file p_f.'''
        # Get the number of lines to retrieve
        n = self.getBounded(self.tool.req, 'n')
        # Go to the end of the file
        f.seek(0, 2)
        current = f.tell() # The current position in the file
        remaining = n # The number of lines yet to retrieve
        chunkSize = Viewer.chunkSize
        chunks = [] # Chunks of p_f, each being of this p_chunkSize, in reverse
                    # order starting from the end of the file.
        while remaining > 0 and current > 0:
            if (current - chunkSize) > 0:
                # Read the next chunk
                f.seek((-len(chunks)+1) * chunkSize, 2)
                chunks.append(f.read(chunkSize))
            else:
                # We have reached the beginning of the file, or the file was
                # smaller than the chunk size.
                f.seek(0,0)
                # Read what was not been read yet
                chunks.append(f.read(current))
                break
            # Count how much lines were encountered in the current chunk
            remaining -= chunks[-1].count(b'\n')
            current -= chunkSize
        r = b''.join(reversed(chunks))
        return b'\n'.join(r.splitlines()[-n:]).decode()

    def full(self, f):
        '''Returns the full p_f(ile) content'''
        return f.read()

    def getContent(self):
        '''Returns the appropriate part of the content corresponding to the
           currently selected log file.'''
        tool = self.tool
        req = tool.req
        # What is the log file for which content must be shown ?
        logType = req.logType or 'app'
        if logType not in Config.logTypes:
            r = LOG_T_KO % logType
        else:
            # What is the view mode ?
            mode = req.mode or 'tail'
            if mode not in Viewer.modes:
                r = LOG_M_KO % mode
            else:
                # Is that the current log file or a backup log file ?
                fileName = req.logFile or 'app.log'
                config = tool.config
                if fileName.count('.') == 1 or \
                   not fileName.startswith(logType + '.'):
                    # It is the current log file: get its path from the config.
                    # If the fileName does not correspond to the current log
                    # type, this latter has probably been switched from the UI:
                    # in that case, also get the current log file.
                    path = getattr(config.log, logType).path
                else:
                    # A backup file
                    path = config.backup.path / 'logs' / fileName
                if not path.is_file():
                    r = LOG_F_KO % str(path)
                else:
                    # Open the log file. In "tail" mode, if the file is not
                    # opened in binary mode, it is not possible to perfom seeks
                    # with a negative offset being relative to the end of the
                    # file.
                    modeF = 'rb' if mode == 'tail' else 'r'
                    with open(path, modeF) as f:
                        # Call the method corresponding to the mode
                        r = getattr(self, mode)(f)
        # Call the main PX
        context = O(viewer=self, tool=tool, req=req, svg=tool.buildSvg,
                    content=r)
        return self.px(context)

    def getAjaxData(self, c):
        '''Creates the Ajax data allowing to Ajax-refresh the log zone'''
        return f"new AjaxData('{c.tool.url}','GET',null,'1_logsViewer')"

    def listFiles(self, logType):
        '''Lists the existing log files of this p_logType'''
        config = self.tool.config
        # Start with the current log file
        path = getattr(config.log, logType).path
        current = (path.name, str(path))
        r = None
        # Add backup files if any
        bconfig = config.backup
        if bconfig and bconfig.path:
            logFolder = bconfig.path / 'logs'
            if logFolder.is_dir():
                r = []
                for logFile in logFolder.glob(f'{logType}.*.log'):
                    r.append((logFile.name, str(logFile)))
                # Sort them in antichronological order
                r.sort(key=lambda e: e[0], reverse=True)
                # Insert the current log at the start of the list
                r.insert(0, current)
        return [current] if r is None else r

    @classmethod
    def run(class_, tool):
        '''Create a Viewer instance'''
        return Viewer(tool).getContent()
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
