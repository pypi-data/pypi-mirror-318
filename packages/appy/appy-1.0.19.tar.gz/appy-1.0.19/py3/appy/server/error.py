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
from http import HTTPStatus

from appy.px import Px
from appy.ui.js import Quote
from appy.utils import Traceback
from appy.xml.escape import Escape
from appy.ui.template import Template
from appy.utils import MessageException

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Error:
    '''Represents a server error'''

    byCode = {
     # Error 404: page not found
     404: {'label': 'not_found', 'px':
       Px('''<div>::msg</div>
             <div if="not isAnon and not popup">
              <a href=":tool.computeHomePage()">:_('app_home')</a>
             </div>''', template=Template.px, hook='content', name='error')},

     # Error 403: unauthorized
     403: {'label': 'unauthorized', 'px':
       Px('''<div><img src=":svg('password')" class="iconERR"/>
                  <x>::msg</x></div>''',
          template=Template.px, hook='content', name='error')},

     # Error 500: server error
     500: {'label': 'server_error', 'px':
       Px('''<div><img src=":svg('warning')" class="iconERR"/>
                  <x>::msg</x></div>''',
          template=Template.px, hook='content', name='error')},

     # Error 503: service unavailable. This error code is used by Appy when, due
     # to too many conflict errors (heavy load), the server cannot serve the
     # request.
     503: {'label': 'conflict_error',
           'px': Px('''<div>::msg</div>''',
                    template=Template.px, hook='content', name='error')},

     # Return code 200: a logical error rendering a nice translated message to
     # the user, but not considered being an error at the HTTP level.
     200: {'px': Px('''<img src=":svg('warning')" class="iconERR"/>
                       <x>::msg</x>''',
                    template=Template.px, hook='content', name='error')}
    }

    @classmethod
    def getTextFrom(class_, error):
        '''Extracts and returns the text explaining this p_error being an
           Exception instance.'''
        if error and error.args and error.args != (None,):
            r = str(error).strip()
        else:
            r = None
        return r

    @classmethod
    def getContent(class_, asXml, traversal, code, error, text, handler):
        '''Get the textual content to render in the error page'''
        # Return simple p_text if the response type is not HTML
        if asXml: return text or str(error)
        # Managers will get technical details
        isManager = traversal.user.hasRole('Manager')
        if isManager and code == 500:
            # Dump a traceback for a Manager
            r = Traceback.get(html=True)
        else:
            if isinstance(error, MessageException):
                r = error.getText(text, handler)
            elif isinstance(error, traversal.handler.Guard.Error) and \
                 error.translated:
                # Unauthorized with a specific human-readable message: use it
                r = Escape.xhtml(error.translated)
            else:
                # Produce a standard message, completed with an optional
                # additional message (in p_text).
                r = handler.tool.translate(Error.byCode[code]['label'])
                if text and isManager:
                    r = f'{r}<div class="discreet">{Escape.xhtml(text)}</div>'
        return r

    @classmethod
    def get(class_, resp, traversal, error=None):
        '''A server error just occurred. Try to return a nice error page. If it
           fails (ie, the error is produced in the main PX template), dump a
           simple traceback.'''
        # When managing an error, ensure no database commit will occur
        handler = resp.handler
        handler.commit = False
        # Complete the handler when appropriate
        if not traversal: handler.complete()
        traversal = handler.traversal
        # Did the error occurred in the context of an Ajax request ?
        context = traversal.context
        ajax = (context and context.ajax) or handler.req.ajax == 'True'
        # Log the error
        code = resp.code if resp.code in Error.byCode else 500
        # Message exceptions are special errors being 200 at the HTTP level
        is200 = code == 200
        message = f'{code} on {handler.path}'
        text = class_.getTextFrom(error)
        if text:
            message = f'{message} - {text}'
        handler.log('app', 'warning' if is200 else 'error', message=message)
        if code in (500, 503):
            handler.log('app', 'error', Traceback.get().strip())
        # Compute the textual content that will be returned
        asXml = handler.resp.contentType == 'xml'
        content = class_.getContent(asXml, traversal, code, error, text,
                                    handler)
        # Return XML if needed
        if asXml: return f'<error>{Escape.xml(content)}</error>'
        # If we are called by an Ajax request, return only the error message,
        # and set the return code to 200; else, browsers will complain.
        if ajax:
            resp.code = HTTPStatus.OK
            # Add a link to the referer, if any
            suffix = MessageException.getBackText(handler)
            # Thanks to the DOCTYPE preamble, the Ajax subsystem will understand
            # we are in a special context and will take care of rendering the
            # message appropriately.
            return f'<!DOCTYPE html><p>{content}</p>{suffix}'
        # Return the PX corresponding to the error code. For rendering it, get
        # the last PX context, or create a fresh one if there is no context.
        if not context:
            # Remove some variables from the request to minimise the possibility
            # that an additional error occurs while creating the PX context.
            req = handler.req
            if 'search' in req: del(req.search)
            traversal.context = context = traversal.createContext()
        else:
            # Reinitialise PX counts. Indeed, we have interrupted a "normal"
            # page rendering that has probably already executed a series of PXs.
            # Without reinitialising counts, Appy will believe these PXs were
            # already executed and will not include CSS and JS code related to
            # these PXs.
            context['_rt_'] = {}
        context.msg = content
        try:
            return Error.byCode[code]['px'](context)
        except Exception as err:
            return f'<p>{content}</p>'
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
