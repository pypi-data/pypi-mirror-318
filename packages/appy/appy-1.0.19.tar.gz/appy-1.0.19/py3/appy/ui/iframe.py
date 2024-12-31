'''Global elements to include in HTML pages'''

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
import base64
from appy.ui.js import Quote
from appy.ui.includer import Includer

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Iframe:
    '''Represents the unique Appy iframe popup'''

    view = '''
     <div id="iframeMask"></div>
     <div id="iframePopup" class="popup"
          onmousedown="dragStart(event)" onmouseup="dragStop(event)"
          onmousemove="dragIt(event)"
          onmouseover="dragPropose(event)" onmouseout="dragStop(event)">
      <!-- Icon for closing the popup -->
      <img src="%s" class="clickable iClose iconXS"
           onclick="closePopup('iframePopup',null,true)"/>
      <!-- Header icon -->
      <img class="iconM popupI" src="%s"/>
      <iframe id="appyIFrame" name="appyIFrame" frameborder="0"></iframe>
     </div>'''

    # HTML page to render for closing the popup
    back = '<!DOCTYPE html>\n<html><head>%s%s</head><body>' \
           '<script>backFromPopup(%d)</script></body></html>'

    @classmethod
    def goBack(class_, o, initiator=None):
        '''Returns a HTML page allowing to close the iframe popup and refresh
           the base page.'''
        # A back URL may be forced by a request key or by an initiator
        back = o.req._back
        if not back and initiator:
            back = initiator.backFromPopupUrl
        # Set the cookie containing information required for closing the popup
        if back:
            close = base64.b64encode(back.encode())
        else:
            close = 'yes'
        resp = o.resp
        resp.setCookie('closePopup', close)
        # Include appy.js and call a Javascript function that will do the job
        version = o.config.server.static.versions['appy.js']
        # If the version of appy.js is not mentioned, it will be impossible to
        # debug inside it. Adding statements like: "console.log" or "debugger"
        # will not work, because the browser will consider "appy.js" not being
        # the effective appy.js. In short, for the browser, appy.js is not
        # appy.js?6.
        return class_.back % (Includer.js(o.buildUrl(f'appy.js?{version}')),
                              Includer.vars(o), o.iid)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
