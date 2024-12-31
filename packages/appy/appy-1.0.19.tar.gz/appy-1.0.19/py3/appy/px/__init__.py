'''PX stands for *P*ython *X*ML. It is a templating engine that reuses the pod
   engine to produce XML (including XHTML) from templates written as a mix of
   Python and XML.'''

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
import xml.sax

from appy.utils import css
from appy.pod import Evaluator
from appy.model.utils import Object as O
from appy.pod.buffers import MemoryBuffer
from appy.xml import xmlPrologue, xhtmlPrologue
from appy.px.parser import PxParser, PxEnvironment

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
SPEC_KO      = 'wrong specifier. A specifier must be of the form ' \
               '"<objectName>*<pxName>", like in "tool*pxTest".'
SPEC_NAME_KO = 'name "%s" does not correspond to any object in the context.'
PX_NAME_KO   = 'attribute "%s.%s" does not exist or is not a Px instance.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
bn = '\n'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Px:
    '''Represents a (chunk of) PX code'''

    class Error(Exception): pass
    xmlPrologue = xmlPrologue
    xhtmlPrologue = xhtmlPrologue

    # There are various ways to define a PX
    STRING = 0 # PX code directly written down in a string
    FILE   = 1 # PX code read from a file
    METHOD = 2 # As a method that must return PX code

    def __init__(self, content, type=STRING, partial=True, template=None,
                 hook=None, prologue=None, css=None, js=None, cssVars=None,
                 name=None):
        '''Creates a PX object'''

        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # If p_type is... | p_content is...
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #     STRING      | a chunk of PX code as a string 
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #      FILE       | the path to a file on disk, containing PX code
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #     METHOD      | (cheat mode) a method that will accept the PX
        #                 | context as unique arg and must return XML code, just
        #                 | as a PX would do. This allows to "implement" a PX
        #                 | with Python code, which may, in some cases, be
        #                 | appropriate for performance reasons.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        # If the PX code represents a complete XML file, p_partial is False.
        # Else, p_content will be surrounded by a root tag to be able to parse
        # it with a SAX parser.

        # If this PX is based on another PX template, specify the PX template in
        # p_template and the name of the p_hook where to insert this PX into the
        # template PX.

        # If a p_prologue is specified, it will be rendered at the start of the
        # PX result.

        # You can specify, in p_css and p_js, PX-specific CSS styles and
        # Javascript code, as strings. These strings will be surrounded by the
        # appropriate HTML tag ("style" for p_css and "script" for p_js) and
        # dumped just before the PX result. Note that if the PX is executed more
        # than once, its corresponding p_css and p_js will only be dumped before
        # the first PX result.

        # Get the PX content
        if type == Px.FILE:
            with open(content) as f: self.content = f.read()
        else:
            self.content = content
        self.isMethod = callable(content)
        # It this content a complete XML file, or just some part of it ?
        self.partial = partial
        # Is this PX based on a template PX ?
        self.template = template
        self.hook = hook
        # Is there some (XML, XHTML...) prologue to dump ?
        self.prologue = prologue
        # PX-specific CSS and JS code
        self.css = self.compact(css)
        self.js = self.compact(js)
        # Variables can be defined within self.css. When a CSS variables patcher
        # is found in the PX context, at key "_css_", it is executed, to replace
        # these variables by their actual values. The patcher uses a default
        # base object from which it gets variables' values. You can specify an
        # alternate object by setting, in p_cssVariables, an expression that
        # will be evaluated wiith the current PX context and whose result must
        # be this alternate object.
        self.cssVars = cssVars
        # A PX can have a name
        self.name = name or ''
        # A PX can be profiled (see m_profile below)
        self.profiler = None
        # Parse the PX
        if not self.isMethod:
            self.parse()

    def clone(self, keepTemplate=True):
        '''Create a clone from (my)p_self'''
        # p_keepTemplate offers the possibility to produce p_self's variant,
        # being unwrapped from its template.
        if keepTemplate:
            template = self.template
            hook = self.hook
        else:
            template = None
            hook = None
        r = Px(self.content, partial=self.partial, template=template, hook=hook,
               prologue=self.prologue)
        # Avoid re-compacting CSS and JS
        r.css = self.css
        r.js = self.js
        return r

    def parse(self):
        '''Parses self.content and create the structure corresponding to this
           PX.'''
        if self.partial:
            # Surround the partial chunk with a root tag: it must be valid XML
            self.content = f'<x>{self.content}</x>'
        # Create a PX parser
        self.parser = PxParser(PxEnvironment(), self)
        # Parses self.content (a PX code in a string) with self.parser, to
        # produce a tree of memory buffers.
        try:
            self.parser.parse(self.content)
        except xml.sax.SAXParseException as spe:
            self.completeErrorMessage(spe)
            raise spe

    def compact(self, s):
        '''Removes single-line comments and unnecessary spaces in p_s,
           representing CSS or JS code.'''
        return css.File.compact(s)

    def addCssJs(self, code, type):
        '''Adds this p_code, being CSS or JS, depending on p_type'''
        code = self.compact(code)
        existing = getattr(self, type)
        if existing:
            code = f'{existing}{bn}{code}'
        setattr(self, type, code)

    def addCss(self, css): self.addCssJs(css, 'css')
    def addJs(self, js): self.addCssJs(js, 'js')

    def getCss(self, context):
        '''Returns the CSS code possibly defined on this PX. Perform variables
           replacement when relevant.'''
        css = self.css
        if not css: return
        # Return v_css as is if no patcher is found
        if '_css_' not in context: return css
        # Perform variables' replacements within v_css. But based on which
        # object ?
        cssVars = self.cssVars
        if cssVars:
            ctx = context if isinstance(context, dict) else context.d()
            base = eval(cssVars, ctx)
        else:
            base = None # will be the Appy UI configuration (config.ui)
        return context['_css_'](css, base=base, o=context.get('o'))

    def completeErrorMessage(self, parsingError):
        '''A p_parsingError occurred. Complete the error message with the
           erroneous line from self.content.'''
        # Split lines from self.content
        splitted = self.content.split('\n')
        i = parsingError.getLineNumber() - 1
        # Get the erroneous line, and add a subsequent line for indicating
        # the erroneous column.
        column = ' ' * (parsingError.getColumnNumber()-1) + '^'
        lines = [splitted[i], column]
        # Get the previous and next lines when present
        if i > 0: lines.insert(0, splitted[i-1])
        if i < len(splitted)-1: lines.append(splitted[i+1])
        parsingError._msg += f'{bn}{bn.join(lines)}'

    def __call__(self, context, applyTemplate=True, isTemplate=False):
        '''Renders the PX'''
        # If the PX is based on a template PX, we have 2 possibilities.
        # 1. p_applyTemplate is True. This case corresponds to the initial call
        #    to the current PX. In this case we call the template with a context
        #    containing, in the hook variable, the current PX.
        # 2. p_applyTemplate is False. In this case, we are currently executing
        #    the PX template, and, at the hook, we must include the current PX,
        #    as is, without re-applying the template (else, an infinite
        #    recursion would occur).
        #
        # Ensure PX-specific keys are in the context
        context['_ctx_'] = context
        context['_eval_'] = Evaluator
        # Include, in the context, variable names for "reserved" PX chars
        context['PIPE'] = '|'
        context['SEMICOLON'] = ';'

        # The first PX to be called will be stored as key "_px_", while the
        # *c*urrently called (sub-)PX will be stored at key "_cpx_".
        px = context.get('_px_')
        if not isTemplate:
            if px is None: # This is the first PX to be called
                context['_px_'] = self
            context['_cpx_'] = self

        # This PX call is probably one among a series of such calls, sharing the
        # same p_context. Within this context, we add a sub-dict at key "rt"
        # (*r*un-*t*ime) for counting the number of times every PX is called.
        # It allows us to include PX-specific CSS and JS code only once.
        if '_rt_' not in context: context['_rt_'] = {}

        if self.hook and applyTemplate:
            # Call the template PX, filling the hook with the current PX
            context[self.hook] = self
            r = self.template(context, isTemplate=True)
        else:
            # Start profiling when relevant
            profiler = self.profiler
            if profiler: profiler.enter(self.name)
            # Run the PX
            if self.isMethod:
                r = self.content(context)
            else:
                # Create a Memory buffer for storing the result
                env = self.parser.env
                result = MemoryBuffer(env, None)
                # Execute the PX
                env.ast.evaluate(result, context)
                # Get the PX result
                r = result.content
            # Count this call and include CSS and JS code when relevant
            pxId = id(self)
            rt = context['_rt_']
            if pxId in rt:
                rt[pxId] += 1
            else:
                rt[pxId] = 1
                # This is the first time we execute it: include CSS and JS code
                # if present, excepted if the are executing the first PX in the
                # context of an Ajax request: in that case, JS and CSS, if any,
                # are already present, just above the ajax-refreshed zone.
                if px is None and context.get('ajax'):
                    pass
                else:
                    if self.js: r = f'<script>{self.js}</script>{bn}{r}'
                    css = self.getCss(context)
                    if css: r = f'<style>{css}</style>{bn}{r}'
            # Include the prologue
            if self.prologue:
                r = self.prologue + r
            # Stop profiling when relevant
            if profiler: profiler.leave()
        # Restore the previous PX in the context
        if px: context['_cpx_'] = px
        # Return the result
        return r

    def override(self, content, partial=True):
        '''Overrides the content of this PX with a new p_content (as a
           string).'''
        self.partial = partial
        self.content = content
        # Parse again, with new content
        self.parse()

    def profile(self, name, profiler):
        '''Enables profiling of this PX, that will be named p_name in the
           p_profiler's output.'''
        self.name = name
        self.profiler = profiler

    # Literals to convert via method p_convertValue below. Although not being
    # purely Pythonic, literals 'true' and 'false' are converted to Python
    # booleans.
    literals = {'True': True, 'False': False, 'None': None,
                'true': True, 'false': False}

    @classmethod
    def convertValue(class_, value, tool):
        '''Converts p_value as found in the request to a value as can be added
           to a PX context.'''
        if isinstance(value, list):
            r = [class_.convertValue(v, tool) for v in value]
        elif not isinstance(value, str):
            r = value # Do not touch already "typed" values
        elif value.startswith(':'):
            # The value contains an object ID: convert it to a real object
            r = value[1:]
            if ':' not in r:
                r = tool.getObject(r)
            else:
                # A field name lies besides the object ID: create an initiator
                # object representing them.
                id, fname = r.split(':', 1)
                o = tool.getObject(id)
                r = tool.Initiator(tool, o.req, (o, o.getField(fname)))
        elif value in class_.literals:
            r = class_.literals[value]
        elif value.isdigit():
            r = int(value)
        else:
            r = value
        return r

    @classmethod
    def injectRequest(class_, context, req, tool, specialOnly=False):
        '''Inject all p_req(uest) values into the PX p_context (or only
           search-related entries if p_searchOnly is True).'''
        if not specialOnly:
            # Inject every (key, value) pair found in the request into the
            # context, with automatic type conversion for values.
            for name, value in req.items():
                setattr(context, name, class_.convertValue(value, tool))
        # When some special keys are found in the request, create related,
        # additional entries in the PX context. These keys correspond to base
        # Appy concepts that are regularly transmitted between the browser and
        # the server.
        if 'className' in req:
            # Add entry "class_"
            context.class_ = tool.model.classes.get(req.className)
        if 'search' in req:
            tool.Search.initContext(req.search, tool, context)

    @classmethod
    def createContext(class_, traversal, layout, Quote):
        '''Creates a context containing all base variables required to execute
           the PX named p_name.'''
        # Unwrap base objects from the p_traversal
        handler = traversal.handler
        guard = handler.guard
        tool = handler.tool
        req = handler.req
        o = traversal.o or tool
        # The logged user and the home object
        try:
            user = guard.user
            lang = guard.userLanguage # The user language (2-letters ISO code)
        except AttributeError:
            # The guard does not exist
            user = traversal.user
            lang = user.getLanguage()
        # Is this language LTR or RTL ?
        dir, dleft, dright = handler.Languages.getDirection(lang)
        # The main app config
        config = handler.server.config
        # Define and return the context
        r = O(
          traversal=traversal, handler=handler, guard=guard, tool=tool, req=req,
          o=o, layout=layout, ui=tool.ui, _=tool.translate, user=user,
          isAnon=user.isAnon(), Px=Px, config=config, field=traversal.field,
          appName=config.model.appName, q=Quote.js, url=tool.buildUrl,
          svg=tool.buildSvg, lang=lang, dir=dir, dleft=dleft, dright=dright,
          mobile=handler.isMobile(), siteUrl=config.server.getUrl(handler),
          _css_=config.ui.patchCss)
        # Ensure keys "ajax" and "popup" are present
        for name in ('ajax', 'popup'):
            setattr(r, name, getattr(r, name) or False)
        # Compute and add the home object
        r.home = tool.computeHomeObject(user, r.popup)
        # Inject request values in it
        class_.injectRequest(r, req, tool)
        return r

    # Names of the base variables that must be present in the context of any
    # standard Appy PX.
    contextKeys = ('traversal', 'handler', 'guard', 'tool', 'req', 'o', 'home',
      'layout', 'popup', 'ajax', 'ui', '_', 'user', 'isAnon', 'Px', 'config',
      'appName', 'q', 'url', 'svg', 'lang', 'dir', 'dleft', 'dright',
      'mobile', '_css_')

    @classmethod
    def copyContext(class_, context, other, overwrite=False):
        '''Copy base variables whose names are defined in p_class_.contextKeys
           from p_other to p_context.'''
        for key in class_.contextKeys:
            if overwrite or key not in context:
                context[key] = other[key]

    # Names of the PXs being Appy home pages. Key indicates if "public" pages
    # are taken into account or not.
    appyHomePXs = {
      True:  {'home':None, 'homes':None, 'public':None},
      False: {'home':None, 'homes':None}
    }

    @classmethod
    def isHome(class_, ctx, orPublic=True):
        '''Returns True if the currently shown PX has the name of one of the
           Appy home PXs.'''
        return ctx._px_.name in class_.appyHomePXs[orPublic]

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Utility methods
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    @staticmethod
    def truncateValue(value, width=20, suffix='...'):
        '''Truncates string p_value according to p_width'''
        width = width or 20 # p_width could be None
        if len(value) > width:
            value = value[:width] + suffix
        return value

    @staticmethod
    def truncateText(text, width=20, suffix='...', tag='abbr', css=None):
        '''Truncates p_text to max p_width chars. If the text is longer than
           p_width, the truncated part is put in a xhtml p_tag.'''
        # Optional p_css class(es) are applied to the p_tag
        width = width or 20 # p_width could be None
        css = f' class="{css}"' if css else ''
        if len(text) > width:
            text = f'<{tag} title="{text}"{css}>{text[:width]}{suffix}</{tag}>'
        return text

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Call a PX from a "specifier"
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    @classmethod
    def callFromSpec(class_, specifier, o):
        '''Calls the PX mentioned in p_specifier, with the context defined on
           p_o.traversal.context.'''

        # A specifier is of the form <name>*<px>.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # <name> | is a name that must be present in the PX context, pointing
        #        | to an object, module, class...
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  <px>  | is the name of the PX instance that must exist as attribute
        #        | on the object denoted by <name>.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        # Check if the p_specifier is valid
        parts = specifier.split('*', 1)
        if len(parts) != 2: raise class_.Error(SPEC_KO)
        # Does the named object exist in the context ?
        name, px = parts
        ctx = o.traversal.context
        if name not in ctx: raise class_.Error(SPEC_NAME_KO % name)
        # Does the named PX exist on the object ?
        obj = ctx[name]
        px = getattr(obj, px, None)
        if (px is None) or not isinstance(px, Px):
            raise class_.Error(PX_NAME_KO % (name, parts[1]))
        return px(ctx)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
