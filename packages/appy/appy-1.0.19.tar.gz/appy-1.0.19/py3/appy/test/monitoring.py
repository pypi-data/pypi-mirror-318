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
from appy import version
from appy.utils import executeCommand
from appy.model.fields.pod import Config as PodConfig

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Monitoring:
    '''Implements stuff allowing to perform monitoring on a Appy application.
       * URL <yourapp>/tool/check can be called to get monitoring info;
       * Configure monitoring parameters by updating attributes of the
         Monitoring instance defined in the Config class.'''

    def __init__(self, forceComplete=False, checkLo=False):
        # When returning a success status code, what code to return ?
        self.ok = 'OK'
        # When returning a failure status code, what code to return ?
        self.ko = 'KO'
        # Do we check the presence of LibreOffice running in server mode ?
        self.checkLo = checkLo
        # Normally, producing a complete or summary status depends on a request
        # parameter. If p_forceComplete is True, however, we always return the
        # complete status.
        self.forceComplete = forceComplete
        # The app may define here additional version information, as a list of
        # (key, value) tuples, keys and values being strings.
        self.app = []

    def asText(self, r):
        '''Returns monitoring info p_r as pure text'''
        return '\n'.join('%s: %s' % (k, v) for k, v in r)

    def asHtml(self, r):
        '''Returns monitoring info p_r as HTML'''
        rows = ['<tr><th>%s</th><td>%s</td>' % (k, v) for k, v in r]
        return '<table class="small">%s</table>' % '\n'.join(rows)

    def get(self, tool, html=False):
        '''Returns monitoring-related info'''
        # The global monitoring status
        success = True
        # Check if LibreOffice is running
        if self.checkLo:
            loLine = ''
            out, err = executeCommand('ps -ef | grep "soffice"', shell=True)
            for line in out.split('\n'):
                if "accept=socket" in line:
                    loLine = line
                    break
            if not loLine:
                success = False
        # Do we need to return complete information or only a status code ?
        status = self.ok if success else self.ko
        if 'all' not in tool.req and not self.forceComplete: return status
        # Return complete information
        cfg = tool.config.pod or PodConfig()
        r = [('Status', status), ('Appy version', version.verbose)]
        if self.checkLo:
            # Appy parameters for connecting to LibreOffice in server mode
            r.append( ('UNO-enabled Python',
                       cfg.unoEnabledPython or '<the one running this site>'))
            r.append(('LibreOffice port', str(cfg.libreOfficePort)))
            # Info about the running LibreOffice server
            if not loLine:
                r.append(('LibreOffice status', 'Not found'))
            else:
                r.append(('LibreOffice status', 'Running: %s' % loLine))
        # Add app-specific info when available
        if self.app: r += self.app
        # Return pure text of HTML when requested
        html = tool.req.html == '1' or html
        return self.asHtml(r) if html else self.asText(r)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
