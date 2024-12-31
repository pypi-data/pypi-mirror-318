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
# Some of the imports below are just there to belong to the interpreter context

import io
from DateTime import DateTime
from contextlib import redirect_stdout
from persistent.list import PersistentList
from persistent.mapping import PersistentMapping

from appy.px import Px
from appy.utils import Traceback
from appy.xml.escape import Escape
from appy.model.fields import Field
from appy.model.fields.hour import Hour
from appy.utils import string as sutils
from appy.model.utils import Object as O
from appy.database.operators import or_, and_, in_

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
COMMIT   = 'Committed from %d: %s'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Python(Field):
    '''Through-the-web Python interpreter'''

    # Explain checkbox "Force commit"
    cr = '&#013;'
    FC_TEXT = f'This will force a database commit.{cr}{cr}Note that if you ' \
              f'call a method that sets handler.commit to True,{cr}a commit ' \
              f'will nevertheless be done even if the checkbox is unchecked.'

    # Some elements will be traversable
    traverse = Field.traverse.copy()

    # All layouts produce the same rendering. That being said, in 99% of all
    # situations, only the "view" layout will be used.
    view = cell = buttons = edit = Px('''
     <div class="python"
          var="prefix=f'{o.iid}_{field.name}';
               hook=f'{prefix}_output'">
      <div id=":hook"></div>
      <div class="prompt">&gt;&gt;&gt;</div>
      <input type="text" id=":f'{prefix}_input'" autocomplete="false"
         onkeydown=":'if (event.keyCode==13) onPyCommand(%s, this)' % q(hook)"/>
      <div class="iactions">
        <input type="checkbox" id=":f'{prefix}_commit'"/>
        <label lfor=":f'{prefix}_commit'">
         <abbr title="::field.FC_TEXT">Force commit</abbr>
        </label>
      </div>
      <script>:"document.getElementById('%s_input').focus();%s" %
               (prefix, field.getAjaxData(hook, o))</script>
     </div>''',

     js='''
       onPyCommand = function(hook, input){
         var command = input.value.trim();
         if (!command) return;
         input.value = '';
         // Misuse the 'exit' command to clear the command history
         if (command == 'exit') {
           document.getElementById(hook).innerHTML = '';
           return;
         }
         // Must a database commit occur ?
         var id = hook.substring(0, hook.length-6) + 'commit',
             cb = document.getElementById(id),
             commit = cb.checked.toString();
         cb.checked = false;
         askAjax(hook, null, {'command':command, 'commit':commit});
       }

       onPyOutput = function(rq, injected) {
         // Scroll to ensure the input field is still visible
         injected.nextSibling.nextSibling.scrollIntoView();
       }

       class CommandHistory {
         constructor(){
           this.commands = []; // Commands already typed in the interpreter
           this.i = -1;        // The currently select command
         }
       }''',

     css='''
      .python { background-color:|pythonBgColor|; color:|brightColor|;
         padding:5px; font-family:monospace; height:40vh; overflow-y:auto }
      .prompt { display:inline; padding-right:10px }
      .python input[type=text] { padding:0; margin:0; border:none;
         color:|brightColor|; font-family:monospace; width:80% }
      .iactions { float:right; padding-bottom:10px }
      .iactions label { color:|brightColor|; padding-right:10px }
      .iactions input { background-color:#eee; opacity:0.6 }
      .commitMsg { font-style:italic; color:|altColor| }
     ''')

    # There is no possibility to render this field on layout "search"
    search = ''

    def __init__(self, show='view', renderable=None, page='main', group=None,
      layouts=None, move=0, readPermission='read', writePermission='write',
      width=None, height=None, colspan=1, master=None, masterValue=None,
      focus=False, mapping=None, generateLabel=None, label=None, view=None,
      cell=None, buttons=None, edit=None, custom=None, xml=None,
      translations=None):
        # Call the base constructor
        super().__init__(None, (0,1), None, None, show, renderable, page, group,
          layouts, move, False, True, None, None, False, None, readPermission,
          writePermission, width, height, None, colspan, master, masterValue,
          focus, False, mapping, generateLabel, label, None, None, None, None,
          False, False, view, cell, buttons, edit, custom, xml, translations)

    def getAjaxData(self, hook, o):
        '''Initializes an AjaxData object on the DOM node corresponding to this
           field.'''
        params = {'hook': hook}
        params = sutils.getStringFrom(params)
        # Complete params with default parameters
        return "new AjaxData('%s/%s/onCommand', 'GET', %s, '%s', null, null, " \
               "onPyOutput, true)" % (o.url, self.name, params, hook)

    def formatOutput(self, output, fromExpr):
        '''Formats this Python command p_output. p_fromExpr is True if it was
           the result of evaluating a Python expression. p_fromExpr is False in
           any other case: p_output was collected from the redirected stdout, or
           was a no-result following the execution of a Python statement.'''
        if fromExpr:
            # Surround a string with quotes
            if isinstance(output, str):
                r = "'%s'" % output.replace("'", "\\'")
            else:
                # Convert it to a string
                r = repr(output)
        else:
            r = output
        # XHTML-escape it
        return Escape.xhtml(r)

    def doCommit(self, o, mustCommit, command):
        '''If a database commit is required (p_mustCommit is True), do it, log
           if and return a message to the UI.'''
        if mustCommit:
            o.log(COMMIT % (o.iid, command))
            o.H().commit = True
            r = '<div class="commitMsg">Commit done and logged.</div>'
        else:
            r = ''
        return r

    traverse['onCommand'] = 'Manager'
    def onCommand(self, o):
        '''Evaluates the Python expression entered into the UI'''
        # Security check
        if o.user.login not in o.config.security.consoleUsers:
            o.raiseUnauthorized()
        command = o.req.command
        # Redirect stdout to a StringIO
        with io.StringIO() as buf, redirect_stdout(buf):
            try:
                fromExpr = True
                try:
                    r = eval(command)
                    if r is None:
                        # If the result of evaluating the command is None and
                        # something was dumped on stdout, return this output.
                        output = buf.getvalue()
                        if output:
                            r = output
                            fromExpr = False
                except SyntaxError as se:
                    # Try interpreting the command as a statement
                    exec(command)
                    r = ''
                    fromExpr = False
                # Format the result
                r = self.formatOutput(r, fromExpr)
                # Is commit required ?
                commit = o.req.commit == 'true'
            except Exception as e:
                r = Traceback.get(html=True)
                commit = False
        # Manage commit
        message = self.doCommit(o, commit, command)
        # Return the command echoed + the command output
        return '<div>&gt;&gt;&gt; %s</div>%s%s' % \
               (Escape.xhtml(command), r, message)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
