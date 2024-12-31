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
import tempfile
from pathlib import Path

from appy.tr import po
from appy.model.base import Base
from appy.ui.layout import Layouts
from appy.model.fields.text import Text
from appy.model.fields.phase import Page
from appy.model.fields.string import String
from appy.model.fields.action import Action
from appy.model.fields.computed import Computed

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TR_UPDATED = 'Translation file for "%s" loaded - %d messages.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Translation(Base):
    '''Base class representing a group of translations in some language'''

    # Translations are not indexed by default
    indexable = False

    p = {'page': Page('main'), 'label': 'Translation'}

    @staticmethod
    def update(class_):
        '''Make field "title" uneditable'''
        title = class_.fields['title']
        title.show = False
        title.page = class_.python.p['page']
        title.label = class_.python.p['label']
        title.indexed = False

    # The "source language", used as base for translating labels of this
    # translation, is defined in the RAM config (which is the default value),
    # but can be changed for a specific translation.
    sourceLanguage = String(width=4, multiplicity=(1,1), **p)

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                           Update from po files
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def updateFromFiles(self, appyFiles, appFiles, extFiles):
        '''Loads labels on p_self from Appy, app and ext's po files'''
        # Count the number of loaded messages
        count = 0
        appName = self.config.model.appName
        lg = self.id
        # Load messages from: (1) Appy, (2) app's automatic labels, (3) app's
        # custom labels and (4) ext's custom labels.
        for place in (appyFiles.get(f'{lg}.po'), \
                      appFiles.get(f'{appName}-{lg}.po'), \
                      appFiles.get(f'Custom-{lg}.po'), \
                      extFiles.get(f'Custom-{lg}.po')):
            if not place: continue # There may be no "ext" file
            for message in place.messages.values():
                setattr(self, message.id, message.get())
                count += 1
        self.log(TR_UPDATED % (lg, count))

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                          Get a translated text
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def get(self, label, mapping=None):
        '''Gets the translated text stored on p_self for this i18n p_label'''
        # Gets the translated text
        r = getattr(self, label, '') or ''
        if not r or not mapping: return r
        # Apply p_mapping
        if mapping:
            for name, repl in mapping.items():
                repl = repl if isinstance(repl, str) else str(repl)
                r = r.replace(f'${{{name}}}', repl)
        return r

    # Propose 2 buttons to produce and download the "po" files containing,
    # respectively, automatic and custom labels, reflecting any change performed
    # by the user on translation pages.
    p.update({'result': 'file', 'show': 'buttons'})
    poReplacements = ( ('<br/>', '\\n'), ('\r\n', '\\n'), ('\n', '\\n'),
                       ('"', '\\"') )

    @classmethod
    def downloadPo(class_, o, fields, name, phase=None, pot=None):
        '''Generate and download the .po file corresponding to this translation
           p_o(bject). On this object, retrieve values from these p_fields,
           potentially limited to those being in pages from this this p_phase.
           The resulting file will be named p_name.'''
        count = 0
        # Create a po.File object as basis for generating the file on disk
        poFile = po.File(Path(name))
        for field in fields.values():
            # Ignore unpaged, technical fields
            if not field.pageName: continue
            # Ignore fields not being in the passed p_phase
            if phase and field.page.phase != phase: continue
            # Ignore any other irrelevant field
            if field.pageName == 'main' or not isinstance(field, (String,Text)):
                continue
            # Adds the PO message corresponding to this field
            msg = o.values.get(field.name) or ''
            # Perform some replacements in v_msg
            for old, new in class_.poReplacements:
                msg = msg.replace(old, new)
            # Compute the default text
            deF = pot.messages[field.name].default if pot else field.poDefault
            message = po.Message(field.name, msg, deF or '')
            poFile.addMessage(message, needsCopy=False)
            count += 1
        stringIo = poFile.generate(inFile=False)
        stringIo.name = name # To mimic a file
        stringIo.seek(0)
        return True, stringIo

    def downloadPoFile(self, type):
        '''Generates the "po" file corresponding to this translation, updated
           with the potential changes performed by the user on translation
           pages.'''
        tool = self.tool
        baseName = self.config.model.appName if type == 'main' else 'Custom'
        displayName = f'{baseName}-{self.id}.po'
        # Get the corresponding pot file: default texts are stored in it
        pot = self.appPath / 'tr' / f'{baseName}.pot'
        potFile = po.Parser(pot).parse()
        return Translation.downloadPo(self, self.class_.fields, displayName,
                                      phase=type, pot=potFile)

    poAutomatic = Action(action=lambda tr: tr.downloadPoFile('main'),
                         icon='download.svg', **p)

    poCustom = Action(action=lambda tr: tr.downoadPoFile('custom'),
                      icon='download.svg', **p)

    def computeLabel(self, field):
        '''The label for a text to translate displays the text of the
           corresponding message in the source translation.'''
        tool = self.tool
        # It may have been cached on p_field
        text = field.poSource
        # Get the name of the companion field, storing the translated value
        # (p_field is the Computed field used for rendering the source
        # translation).
        labelId = field.name[:-3]
        if not text:
            # Get the source language: either defined on the translation itself,
            # or from the config.
            sourceLg = self.sourceLanguage or self.config.ui.sourceLanguage
            source = self.getObject(sourceLg)
            # If we are showing the source translation, we do not repeat the
            # message in the label.
            text = '' if self.id == sourceLg else getattr(source, labelId)
            # Note here that carriage returns are represented, in v_text, as
            # <br/> tags.
        # Apply some transform to p_text, to make it UI-compliant. For example,
        # we don't want HTML code to be interpreted. This way, the translator
        # sees the HTML tags and can reproduce them in the translation.
        if text:
            if self.H().getLayout() == 'edit':
                text = text.replace('<','&lt;').replace('>','&gt;')
            text = text.replace('\\n', '↲<br/>').replace('\\"', '"')
        # Return the complete result
        helpIcon = self.buildSvg('help')
        return f'<div class="trLabel"><abbr title="{labelId}">' \
               f'<img src="{helpIcon}"/></abbr>{text}</div>'

    def showField(self, field):
        '''Show a field (or its label) only if the corresponding source message
           is not empty.'''
        tool = self.tool
        # Source message emptyness may be cached on p_field
        if field.poSourceEmpty is not None:
            return not field.poSourceEmpty
        name = field.name[:-3] if field.type == 'Computed' else field.name
        # Get the source message
        sourceLang = self.config.ui.sourceLanguage
        source = tool.getObject(sourceLang)
        sourceMsg = getattr(source, name)
        return not field.isEmptyValue(self, sourceMsg)

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                       Get fields from po messages
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    @classmethod
    def getFieldDimensions(class_, content):
        '''Returns a tuple (i_width, i_height, i_crCount) representing the
           dimensions for the field corresponding to this message p_content, and
           the number of *c*arriage *r*eturn chars being present in it.'''
        # We suppose a line is 60 chars long
        width = len(content)
        # Compute height (a "\n" counts for one line)
        crCount = content.count('\\n')
        height = int(len(content)/60) + crCount + 1
        return width, height, crCount

    @classmethod
    def getFieldsFrom(class_, metaClass, poFile, message, page, d=None,
                      poOthers=None):
        '''Computes the Appy fields corresponding this p_message, coming from
           this p_poFile. If p_d is not None, those fields are added into this
           dict. Else, the fields are injected into the translation p_class_.'''
        # When p_d is passed, the p_metaClass can be an alternate class than
        # p_class_'s metaclass.
        inject = d is None
        # In "inject" mode, p_poFile is a .pot file and all the available .po
        # files are in p_poOthers. In non-inject mode, p_poFile is a .po file
        # and p_poFiles contains a unique .po file being the source language .po
        # file.
        #
        # For every m_message, 2 fields will be created, in this p_page:
        # (1) a Computed field allowing to display the text in the source
        #     language ;
        # (2) an editable String field for storing the corresponding i18n
        #     p_message.
        #
        # Create the Computed field displaying the text in the source message
        labelField = Computed(method=class_.computeLabel, page=page,
                              show=class_.showField, layouts=Layouts.f)
        name = f'{message.id}_lB'
        labelField.init(metaClass, name)
        # Store custom attributes on v_labelField: "poDefault" is the default
        # value as written down in the .po file, while "poSource" is the source
        # language value.
        labelField.poDefault = message.default
        if inject:
            metaClass.fields[name] = labelField
            # Here, I do not compute v_labelField.poSource, but it is not a
            # problem because it is easily computable at form rendering time.
            labelField.poSource = labelField.poSourceEmpty = None
        else:
            labelField.poSource = poOthers[0].messages[message.id].msg \
                                  if poOthers else message.default
            sourceVal = (labelField.poSource or '').strip()
            labelField.poSourceEmpty = not sourceVal
            d[name] = labelField
        # Create the String field for storing the translation
        params = {'page': page, 'layouts': Layouts.f, 'show': class_.showField}
        # Scan messages corresponding to p_message from translation files in
        # p_poOthers: the field length will be the longer found message content.
        width = height = 0
        for poFile in poOthers:
            otherMessage = poFile.messages[message.id]
            w, h, crCount = class_.getFieldDimensions(otherMessage.msg)
            # Compute width
            width = max(width, w)
            height = max(height, h)
        if width == 0:
            width, height, crCount = class_.getFieldDimensions(message.default)
        if crCount == 0 and width <= 100:
            # Propose a one-line field
            params['width'] = width
            fieldClass = String
        else:
            # Propose a multi-line field, or a very-long-single-lined field
            fieldClass = Text
            params['height'] = height
        field = fieldClass(**params)
        field.init(metaClass, message.id)
        field.poSourceEmpty = labelField.poSourceEmpty
        # This is convenient to have the message default value both on
        # v_labelField and on p_field.
        field.poDefault = labelField.poDefault
        # Also store, on v_field, the already translated text
        field.poText = message.get(escapeCrTo='<br/>' if inject else '\n')
        if inject:
            metaClass.fields[message.id] = field
        else:
            d[message.id] = field

    @classmethod
    def getAllFieldsFrom(class_, config, metaClass, poFile, page='1',
                         phase='main', d=None, poOthers=None):
        '''Creates, in this p_metaClass, appropriate Appy fields corresponding
           to messages from p_poFile.'''
        # The first fields will start in this p_page and p_phase. Then,
        # additional pages will be created every
        # tool.config.ui.translationsPerPage.
        page = Page(page, phase=phase, sticky=True)
        # If p_d is passed, the created fields are added into it. Else, the
        # fields are injected on this Translation p_class_. Are we in "inject"
        # mode ?
        inject = d is None
        # Walk p_poFile's messages
        i = 0
        perPage = config.ui.translationsPerPage
        for message in poFile.messages.values():
            # [Inject mode] If this message overrides one from Appy.pot, remove
            #               the overridden field added from Appy.pot. This way,
            #               we keep app's fields in the right order.
            if inject and message.id in metaClass.fields:
                del(metaClass.fields[message.id])
            i += 1
            # For every message, create 2 fields:
            # - a Computed used to display the text to translate;
            # - a String holding the translation in itself.
            class_.getFieldsFrom(metaClass, poFile, message, page, d=d,
                                 poOthers=poOthers)
            # Switch to a new page when appropriate
            if (i % perPage) == 0:
                page = Page(page.nextName(), phase=page.nextPhase(),
                            sticky=True)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
