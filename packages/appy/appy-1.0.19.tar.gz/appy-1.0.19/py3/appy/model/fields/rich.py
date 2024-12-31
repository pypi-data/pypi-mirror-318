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
UPLOADED = 'file "%s" uploaded in Ref "%d.%s" via rich "%s".'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import sys, re
from xml.sax._exceptions import SAXParseException

from appy.px import Px
from appy.ui.layout import Layouts
from appy.xml.escape import Escape
from appy.model.fields import Field
from appy.utils.diff import HtmlDiff
from appy.utils.inject import Injector
from appy.model.fields.text import Text
from appy.utils import string as sutils
from appy.ui.layout import Layouts, Layout
from appy.xml.cleaner import Cleaner, StringCleaner
from appy.model.fields.multilingual import Multilingual

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
bn = '\n'
XML_ERROR   = 'Error while reading content of field %s on %s. %s.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Rich(Multilingual, Field):
    '''Field allowing to encode a "rich" text, based on XHTML and external
       editor "ckeditor".'''

    # Some elements are traversable
    traverse = Field.traverse.copy()

    # Required Javascript files
    cdnUrl = 'https://cdn.ckeditor.com/%s/%s/ckeditor.js'

    # Use this constant to say that there is no maximum size for a string field
    NO_MAX = sys.maxsize

    class Layouts(Layouts):
        '''Rich-specific layouts'''
        baseEdit = Layout('lrv-d-f', css='bottomSpaceS')
        b = Layouts(edit=baseEdit, view='l-f')
        c = Layouts(edit=baseEdit, view='lc-f') # Idem but with history
        f = Layouts(edit=baseEdit, view='f') # Field only (no label) on view
        ft = Layouts(edit=baseEdit, view=Layout('f', css='topSpace'))
        g = Layouts(edit=Layout('d2-f;rv=', width='99%'),
                    view=Layout('fl', width='99%'))
        gc = Layouts(edit=Layout('drv-f', width='99%'),
                     view=Layout('cl-f', width='99%')) # Idem but with history

        @classmethod
        def getDefault(class_, field):
            '''Default layouts for this Rich p_field'''
            # Is this field in a grid-style group ?
            inGrid = field.inGrid()
            if field.historized:
                # p_field.historized can be a method or a boolean. If it is a
                # method, it means that under some condition, historization will
                # be enabled. So we come here also in this case.
                r = 'gc' if inGrid else 'c'
            else:
                r = 'g' if inGrid else 'b'
            return getattr(class_, r)

    # Default ways to render multilingual fields
    defaultLanguagesLayouts = {
      'edit': 'horizontal', 'view': 'horizontal', 'cell': 'vertical'}

    verticalLanguagesLayouts = {
      'edit': 'vertical', 'view': 'vertical', 'cell': 'vertical'}

    # Override this dict, defined at the Multilingual level
    lgTop = {'view': 1, 'edit': 1}

    # Default styles to use
    defaultStyles = ('p', 'h1', 'h2', 'h3', 'h4')

    # Default custom styles
    customStyles = [
      # When this style is applied, at the XHTML level, it has no effet, but
      # when dumped in a POD, a page break is inserted just after the paragraph
      # having this style.
      {'id': 'div', 'element': 'div',
       'attributes': {'style': 'page-break-after:always'}},
      # Style for a block of text rendered in a monospace font
      {'id': 'pre', 'element': 'pre'}
    ]

    # The name of the index class storing values of this field in the catalog
    indexType = 'RichIndex'

    # Unilingual view and cell
    viewUni = cellUni = Px('''
     <x var="inlineEdit=field.getAttribute(o, 'inlineEdit');
             css=field.getAttribute(o, 'viewCss');
             mayAjaxEdit=inlineEdit and layout != 'cell' and not showChanges \
                         and guard.mayEdit(o, field.writePermission);
             value=field.injectContent(o, value) if field.inject else value">
      <div if="not mayAjaxEdit"
           class=":css">::value or field.getValueIfEmpty(o)</div>
      <x if="mayAjaxEdit" var2="name=f'{name}_{lg}' if lg else name">
       <div class=":css" contenteditable="true"
            id=":f'{o.iid}_{name}_ck'">::value or field.getValueIfEmpty(o)</div>
       <script if="mayAjaxEdit">::field.getJsInlineInit(o, name, lg)</script>
      </x>
     </x>''')

    # Unilingual edit
    editUni = Px('''
     <textarea var="inputId=name if not lg else f'{name}_{lg}'"
       id=":inputId" name=":inputId" cols=":field.getTextareaCols()"
       style=":field.getTextareaStyle()"
       rows=":field.height">:field.getInputValue(inRequest, requestValue, value)
     </textarea>
     <script>::field.getJsInit(o, lg)</script>''')

    search = Px('''
     <input type="text" maxlength=":field.maxChars" size=":field.swidth"
            value=":field.sdefault" name=":widgetName"/>''')

    def __init__(self, validator=None, multiplicity=(0,1), default=None,
      defaultOnEdit=None, show=True, renderable=None, page='main', group=None,
      layouts=None, move=0, indexed=False, mustIndex=True, indexValue=None,
      searchable=False, filterField=None, readPermission='read',
      writePermission='write', width=None, height=None, maxChars=None,
      colspan=1, master=None, masterValue=None, focus=False, historized=False,
      mapping=None, generateLabel=None, label=None, sdefault='', scolspan=1,
      swidth=None, fwidth=10, sheight=None, persist=True, styles=defaultStyles,
      customStyles=None, documents=False, spellcheck=False, languages=('en',),
      languagesLayouts=None, viewSingle=False, inlineEdit=False,
      toolbar='Standard', view=None, cell=None, buttons=None, edit=None,
      custom=None, xml=None, translations=None, inject=False, valueIfEmpty='-',
      viewCss='xhtml', invalidTexts=None, transformText=None, toItalicize=None):
        # The list of styles that the user will be able to select in the styles
        # dropdown (within CKEditor) is defined hereafter.
        self.styles = styles
        # If you want to add custom, non-standard styles in the above-mentioned
        # dropdown, do not touch attribute "styles", but specify such entries in
        # the following attribute "customStyles". It must be a list or dict of
        # entries; every entry represents a custom style and must be a dict
        # having the following keys and values. Every key and value must be a
        # string.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #    "id"    | An identifier for your style, that must be different from
        #            | any standard CKEditor style like h1, h2, p, div, etc;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #   "name"   | A translated name for your style, that will appear in the
        #            | dropdown. Do not use any special (ie, accentuated) char
        #            | in the value: prefer the use of an HTML entity for
        #            | defining such char.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  "element" | The HTML tag that will surround the text onto which the
        #            | style will be applied. Do not use "blockquote", it does
        #            | not work. Non-standard tag "address" works well, or any
        #            | standard tag like h1, h2, etc. Note that if you use a
        #            | standard tag, it will work, but if you have also
        #            | activated it in attribute "style" hereabove, you won't be
        #            | able to make the difference in the result between both
        #            | styles because they will produce a similar result.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.customStyles = customStyles or Rich.customStyles
        # By mentioning, in attribute "documents", the name of a Ref field
        # pointing to Document instances (see appy/model/document.py), images
        # upload is actived in this rich field. An illustration can be found in
        # standard rich field appy/model/page.py::content, that uses, on the
        # same class, the Ref field named "documents".
        self.documents = documents
        # Automatically enable the CK spellchecker ?
        self.spellcheck = spellcheck
        # What toolbar is used ? Possible values are "Standard", "Simple",
        # "Full" or "FullAll".
        # * The "Full" toolbar requires config.ui.ckDistribution being "full" or
        #   "full-all".
        # * The "FullAll" toolbar requires config.ui.ckDistribution being
        #   "full-all".
        self.toolbar = toolbar
        # If p_inject is True, the XHTML chunk contained in a rich field is
        # allowed to contain "a" tags of the form:
        #
        #      (a)      <a href="<url>">py: <part_specifier></a>
        #      (b)     <a href="<anything>">px: <object>*<px></a>
        #
        # These links will not be rendered as-is: they will represent as many
        # placeholders for injecting other content.
        #
        #                            - - - - - - -
        #                            |  Case (a) |
        #                            - - - - - - -
        #
        # Each URL must point to a pure textual resource containing Python code.
        # When rendering this link, Appy will download the code file and extract
        # from it the part corresponding to <part_specifier>. Possible code
        # specifiers are the following.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  c_<name>    | This will extract the definition of *c*lass named
        #              | <name>, including its subsequent docstring and comment
        #              | lines, until the first line of not-commented code is
        #              | reached, or a comment starting with "# ~" is
        #              | encountered.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  s_<cn>.<mn> | This will extract the *s*ignature of method named <mn>
        #              | in class named <cn>, its subsequent docstring and
        #              | comment lines, until the first not-commented line of
        #              | code is reached, or a comment starting with "# ~" is
        #              | encountered.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  m_<cn>.<mn> | This will extract the complete method named <mn> (as
        #              | defined in class named <cn>), including its body.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #
        #                            - - - - - - -
        #                            |  Case (b) |
        #                            - - - - - - -
        # 
        # This case is used to inject the content of a PX. The content of the
        # "a" tag must start with "px:", followed by a specifier made of 2
        # parts, separated by an asterisk (*):
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "object"  | must be the name of an object, class or module being
        #           | available in the current PX context ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #   "px"    | is the name of the PX to use. It must correspond to an
        #           | attribute, available on "object", and be an instance of
        #           | class appy.px.Px.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #
        # Note that, when using POD to dump content of Rich fields via the xhtml
        # function, special "a" tags as described hereabove (cases (a) and (b))
        # will not be included by default in the result. In order to enable
        # that, use parameter inject=True, ie:
        #
        #     do ...
        #     from xhtml(o.someRichField, inject=True)
        #
        self.inject = inject
        # The value to show on non-edit layouts if the field is empty. Can be a
        # string or a method producing it.
        self.valueIfEmpty = valueIfEmpty
        # When rendering rich content on view or cell layout, standard Appy CSS
        # class named "xhtml" is applied. If you want to specify another class,
        # use the following attribute. A method can also be passed.
        self.viewCss = viewCss
        # If passed, p_invalidTexts must be a tuple or list of regular
        # expressions. If the user tries to encode content, in this field, that
        # matches at least one of these regexes, field validation will fail.
        # Note that we are talking about non-exact matches here (ie, method
        # regex.search will be used, and not regex.match).
        self.invalidTexts = invalidTexts
        # If passed, p_transformText must be a function, that will be called
        # during the process of storing, on disk, p_self's content on some
        # object. Within the chunk of XHTML string to store, everytime raw text
        # is encountered, the function will be called. It must accept a string
        # as unique arg and must return a string, being the parameter or a
        # variant, transformed in some way. Transform functions are available in
        # appy/xml/typo.py (use classmethod named "apply" on the chosen
        # sub-class, but not "run*" methods).
        self.transformText = transformText
        # If passed, p_toItalicize must be a set of terms (or a method producing
        # it) that, if found in field content, will be italicized = surrounded
        # by <i></i> tags. p_toItalicize can also hold a regular expression
        # (regex) (or a method producing it) combining all words, of the form:
        #
        #                         "word1|word2|..."
        #
        # Actually, if you pass a set in p_toItalicize, Appy will convert it to
        # such a regex. The possibility to pass yourself a regex is for
        # performance reasons. Suppose p_self is an inner field within a List or
        # Dict field (this is not possible for a Rich field, but for a Poor
        # field, being a Rich sub-class, it is). If you define, in
        # p_toItalicize, a method producting and caching a regex in the Appy
        # request cache, available on any object (o.cache), the regex will be
        # computed once per request. Else, it will be recomputed for every row
        # of data in your List/Dict field. In order to produce your regex from a
        # set of words, you can use the Appy method, available here:
        #
        #              appy/xml/cleaner.py::Cleaner.getItalicizeRex
        #
        self.toItalicize = toItalicize
        # Call base constructors
        Multilingual.__init__(self, languages, languagesLayouts, viewSingle)
        Field.__init__(self, validator, multiplicity, default, defaultOnEdit,
          show, renderable, page, group, layouts, move, indexed, mustIndex,
          indexValue, None, searchable, filterField, readPermission,
          writePermission, width, height, maxChars, colspan, master,
          masterValue, focus, historized, mapping, generateLabel, label,
          sdefault, scolspan, swidth, sheight, persist, inlineEdit, view, cell,
          buttons, edit, custom, xml, translations)
        # The *f*ilter width
        self.fwidth = fwidth
        # No max chars by default
        if maxChars is None:
            self.maxChars = Rich.NO_MAX

    def getDiffValue(self, o, i=None, language=None):
        '''If p_i is None, the method returns the content of this field on p_o,
           rendered with the cumulative diffs between successive versions, from
           the very first stored version in p_o's history to the currently
           stored value.

           If p_i is not None, it is the index of a Change event in p_o's
           history, and the method returns a diff between the value before this
           change was applied, and its subsequent version, either to be found
           in a more recent change in p_o's history or, failing that, the
           currently stored value on p_o.'''
        # Get the value as currently stored on p_o
        current = self.getStoredValue(o) or ''
        if language and current: current = current.get(language) or ''
        # Initialise data structures
        if i is None:
            start = last = r = None
        else:
            last = o.history[i]
            start = i-1 # The event chronologically after the current one
            r = last.getValue(self.name, language)
        for event in o.history.iter(eventType='Change', chronological=True, \
                                    i=start):
            # Ignore irrelevant events
            if not event.hasField(self.name, language=language): continue
            # We have a matching event
            if i is not None:
                # Return the diff between p_value and the newer version stored
                # in this event.
                newer = event.getValue(self.name, language)
                itext, dtext = last.getDiffTexts(o)
                return HtmlDiff(r, newer, itext, dtext).get()
            # If we are here, a cumulative diff must be produced
            if r is None:
                # This is the first encountered version
                r = event.getValue(self.name, language)
            else:
                # We need to produce the difference between current result
                # and this version.
                newer = event.getValue(self.name, language)
                itext, dtext = last.getDiffTexts(o)
                r = HtmlDiff(r, newer, itext, dtext).get()
            # Remember the last walked event
            last = event
        # If no event was walked, there is no diff to show. Return the currently
        # stored value
        if not last: return current
        # The result must be compared with the v_current value
        itext, dtext = last.getDiffTexts(o)
        return HtmlDiff(r, current, itext, dtext).get()

    def getUniFormattedValue(self, o, value, layout='view', showChanges=False,
                             language=None, contentLanguage=None):
        '''Returns the formatted variant of p_value. If p_contentLanguage is
           specified, p_value is the p_contentLanguage part of a multilingual
           value.'''
        if Field.isEmptyValue(self, o, value) and not showChanges: return ''
        if showChanges:
            # Compute the successive changes that occurred on p_value
            r = self.getDiffValue(o, language=contentLanguage)
        else:
            r = value
        return r

    def getItalicized(self, o):
        '''Returns the set of words to italicize, if relevant'''
        it = self.toItalicize
        return it(o) if callable(it) else it

    def getXhtmlCleaner(self, o, forValidation=False):
        '''Returns a Cleaner instance tailored to p_self'''
        if forValidation:
            invalid = self.invalidTexts
            transform = None
            italicize = None
        else:
            invalid = None
            transform = self.transformText
            italicize = self.getItalicized(o)
        return Cleaner(invalidTexts=invalid, transformText=transform,
                       toItalicize=italicize, logger=o)

    def validateUniValue(self, o, value):
        '''Ensure p_value as will be stored (=cleaned) is valid XHTML'''
        try:
            self.getXhtmlCleaner(o, forValidation=True).clean(value)
        except SAXParseException as err:
            # Try after removing problematic chars
            value = StringCleaner.clean(value)
            if not StringCleaner.isParsable(value):
                return o.translate('bad_xml', mapping={'error': str(err)})
        except Cleaner.InvalidText as err:
            return o.translate('invalid_text', mapping={'text': str(err)})

    def getSearchValue(self, req, value=None):
        '''The input widget for a Rich field is of type "text". So behave like a
           Text field in that case.'''
        return Text.computeSearchValue(self, req, value=value)

    def getHistoryValue(self, o, value, i, language=None, empty='-'):
        '''For a Rich field, instead of showing the previous p_value in p_o's
           history, show a XHTML diff between p_value and a newer version of it
           in p_o's history before p_i, or, if not found, the value as currently
           stored on p_o.'''
        r = Field.getHistoryValue(self, o, value, i, language, empty=None)
        return empty if not r else self.getDiffValue(o, i, language)

    def getUniStorableValue(self, o, value, wrap=True):
        '''Gets the p_value as can be stored in the database within p_o'''
        if not value: return value
        # Clean the value. When image upload is enabled, ckeditor inserts some
        # "style" attrs (ie for image size when images are resized). So in this
        # case we can't remove style-related information.
        cleaner = self.getXhtmlCleaner(o)
        try:
            value = cleaner.clean(value, wrap=wrap)
        except SAXParseException as err:
            # Try to remove chars known for producing SAX errors ...
            value = StringCleaner.clean(value)
            # ... then, re-try
            try:
                value = self.getXhtmlCleaner(o).clean(value, wrap=wrap)
            except SAXParseException as err:
                # Errors while parsing p_value can't prevent the user from
                # storing it.
                o.log(XML_ERROR % (self.name, o.id, str(err)), type='warning')
        # Manage maxChars. Truncating p_value will produce a corrupted chunk of
        # XHTML: the objective here, in allowing size restrictions, is to avoid
        # people or robots to inject large, insidious, content.
        max = self.maxChars
        if max and len(value) > max: value = value[:max]
        return value

    def injectContent(self, o, value):
        '''When p_self.inject is True, this method replaces every "injection
           link" found in p_value with the appropriate content.'''
        if not self.inject: return value
        return Injector.run(value, o)

    def getTextareaStyle(self):
        '''On "edit", get the content of textarea's "style" attribute'''
        # If the width is expressed as a string, the field width must be
        # expressed in attribute "style" (so returned by this method) and not
        # via attribute "cols" (returned by m_getTextareaCols below).
        return f'width:{self.width}' if isinstance(self.width, str) else ''

    def getTextareaCols(self):
        '''When this widget must be rendered as an HTML field of type
           "textarea", get the content of its "cols" attribute.'''
        # Use this attribute only if width is expressed as an integer value
        return self.width if isinstance(self.width, int) else ''

    ckLanguages = {'en': 'en_US', 'pt': 'pt_BR', 'da': 'da_DK', 'nl': 'nl_NL',
                   'fi': 'fi_FI', 'fr': 'fr_FR', 'de': 'de_DE', 'el': 'el_GR',
                   'it': 'it_IT', 'nb': 'nb_NO', 'pt': 'pt_PT', 'es': 'es_ES',
                   'sv': 'sv_SE'}

    def getCkLanguage(self, o, language):
        '''Gets the language for CK editor SCAYT. p_language is one of
           self.languages if the field is multilingual, None else. If p_language
           is not supported by CK, we use english.'''
        if not language:
            language = self.getAttribute(o, 'languages')[0]
        if language in self.ckLanguages: return self.ckLanguages[language]
        return 'en_US'

    def getCkParams(self, o, language):
        '''Gets the base params to set on a rich text field'''
        base = f'{o.buildUrl()}/ckeditor'
        ckAttrs = {'customConfig': f'{base}/config.js?9',
                   'contentsCss': f'{base}/contents.css',
                   'stylesSet': f'{base}/styles.js',
                   'toolbar': self.toolbar, 'format_tags':';'.join(self.styles),
                   'scayt_sLang': self.getCkLanguage(o, language)}
        if self.width: ckAttrs['width'] = self.width
        if self.height: ckAttrs['height'] = self.height
        if self.spellcheck: ckAttrs['scayt_autoStartup'] = True
        if self.toolbar == 'FullAll': ckAttrs['extraPlugins'] = 'emoji'
        # Add custom styles
        if self.customStyles:
            for style in self.customStyles:
                id = style['id']
                ckAttrs[f'format_{id}'] = style
                ckAttrs['format_tags'] += f';{id}'
        if self.documents and not o.isTemp():
            base = o.url
            # Parameter "type=any" is only useful in order to have a parameter.
            # Indeed, when a file is cut & pasted or dragged & dropped to
            # ckeditor, ckeditor calls the URL with suffix "&responseType=json".
            # If there is no existing parameter, the syntax is incorrect
            # (absence of '?' between the URL and its parameters) and the
            # request ends up with a 404 error.
            uploadUrl = f'{base}/{self.name}/upload?type=any'
            ckAttrs['filebrowserUploadUrl'] = uploadUrl
            browseUrl = f'{base}/pxField?name={self.documents}&popup=True&' \
                        f'selector={o.iid},{self.name},repl'
            ckAttrs['filebrowserBrowseUrl'] = browseUrl
        if not o.user.hasRole('Manager'):
            ckAttrs['removeButtons'] = 'Source'
        ck = []
        for k, v in ckAttrs.items():
            if isinstance(v, int): sv = str(v)
            elif isinstance(v, bool): sv = str(v).lower()
            elif isinstance(v, dict): sv = str(v)
            else: sv = f'"{v}"'
            ck.append(f'{k}: {sv}')
        return ', '.join(ck)

    def getJs(self, o, layout, r, config):
        '''A rich field depend on CKeditor'''
        if layout not in ('edit', 'view') or \
           ((layout == 'view') and not self.inlineEdit): return
        # Compute the URL to ckeditor CDN
        ckUrl = Rich.cdnUrl % (config.ui.ckVersion, config.ui.ckDistribution)
        if ckUrl not in r: r.append(ckUrl)

    def getJsInit(self, o, language):
        '''Gets the Javascript init code for displaying a rich editor for this
           field (rich field only). If the field is multilingual, we must init
           the rich text editor for a given p_language (among self.languages).
           Else, p_languages is None.'''
        name = f'{self.name}_{language}' if language else self.name
        return f'CKEDITOR.replace("{name}", {{{self.getCkParams(o,language)}}})'

    def getJsInlineInit(self, o, name, language):
        '''Gets the Javascript init code for enabling inline edition of this
           field (rich text only). If the field is multilingual, the current
           p_language is given and p_name includes it. Else, p_language is
           None.'''
        id = o.iid
        lg = language or ''
        params = self.getCkParams(o,language)
        fieldName = language and name.rsplit('_',1)[0] or name
        return f"CKEDITOR.disableAutoInline = true;{bn}" \
               f"CKEDITOR.inline('{id}_{name}_ck', {{{params}, on: {{blur: " \
               f"function(event) {{ let content = event.editor.getData(); " \
               f"doInlineSave('{id}','{fieldName}','{o.url}','view',true," \
               f"content,'{lg}')}}}}}})"

    def isInnerable(self):
        '''Rich fields cannot be used as inner fields'''
        # Try using the Poor field instead: it is innerable
        return

    traverse['upload'] = 'perm:write'
    def upload(self, o):
        '''Uploads a document to the Ref mentioned in attribute "documents"'''
        # Get the file from the request
        ofile = o.req.upload
        # Create a Document instance and link it to p_o via the Ref mentioned in
        # self.documents.
        doc = o.create(self.documents, title=ofile.name, file=ofile)
        o.H().commit = True
        o.resp.setContentType('json')
        r = {'uploaded': 1, 'fileName': doc.title,
             'url': f'{doc.url}/file/download'}
        o.log(UPLOADED % (ofile.name, o.iid, self.documents, self.name))
        return sutils.getStringFrom(r, c='"')
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
