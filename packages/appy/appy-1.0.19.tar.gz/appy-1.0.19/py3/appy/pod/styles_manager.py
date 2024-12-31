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
import re, os.path
from collections import UserDict

from appy import utils
from appy.pod import *
from appy.utils import css
from appy.utils.string import randomName
from appy.pod.odf_parser import OdfEnvironment, OdfParser

# Possible states for the styles parser
READING          = 0 # Default state
PARSING_STYLE    = 1 # Parsing a style definition
PARSING_M_STYLES = 2 # Parsing section "master-styles"
PARSING_P_LAYOUT = 3 # Parsing a page layout

# Dict types
dictTypes = (dict, UserDict)
bn = '\n'

# Error-related constants  - - - - - - - - - - - - - - - - - - - - - - - - - - -
MAP_KO     = 'The styles mapping must be a dictionary or a UserDict instance.'
KEY_STR_KO = "The styles mapping dictionary's keys must be strings."
VAL_STR_KO = 'The styles mapping value for key "%s" must be a string.'
VAL_EMPTY  = 'In your styles mapping, you inserted an empty key and/or value.'
VAL_TYP_KO = 'For key "%s", the value must be of type "%s".'
UNSTYL_TAG = 'You can\'t associate a style to element "%s". Unstylable ' \
             'elements are: %s'
STYLE_N_F  = 'OpenDocument style "%s" was not found in your template. Note ' \
             'that the styles names ("Heading 1", "Standard"...) that appear ' \
             'when opening your template with OpenOffice, for example, are a ' \
             'super-set of the styles that are really recorded into your ' \
             'document. Indeed, only styles that are in use within your ' \
             'template are actually recorded into the document. You may ' \
             'consult the list of available styles programmatically by ' \
             'calling your pod renderer\'s "getStyles" method.'
P_ODT_TXT  = 'For XHTML element "%s", you must associate a paragraph-wide ' \
             'OpenDocument style. "%s" is a "text" style (that applies to ' \
             'only a chunk of text within a paragraph).'
TXT_ODT_P  = 'For XHTML element "%s", you must associate an OpenDocument ' \
             '"text" style (that applies to only a chunk of text within a ' \
             'paragraph). "%s" is a paragraph-wide style.'
IMPLIC_PS  = '%s: no explicit page style is defined in it, but attribute ' \
             '"managePageStyles" has been set with an integer value. In that ' \
             'case, you must explicitly define the default page style on the ' \
             'first page of your POD template.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Properties:
    '''Abstract base class for table and list properties'''

    # HTML elements whose styles are defined by Property instances instead of
    # Style instances.
    elems = ('table', 'ol', 'ul')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class TableProperties(Properties):
    '''In a styles mapping, the value @key "table" must be an instance of this
       class.'''

    defaultMargins = (0.3, 0.0, 0.3, 0.0)
    columnModifiersPrefixes = {'optimize': 'OCW', 'distribute': 'DC'}

    # Predefined width of 100%
    width100 = css.Value('width', '100%')

    def __init__(self, pageWidth=None, px2cm=css.px2cm, cellPx2cm=10.0,
              wideAbove=495, minColumnWidth=0.07, columnModifier=None,
              minCellPadding=0.0, cellContentStyle='podCellContent',
              headerContentStyle='podHeaderCellContent', margins=defaultMargins,
              unbreakable=False, unbreakableRows=False, border=None,
              prevails=False):
        # pod computes, in cm, the width of the master page for a pod template.
        # Table widths expressed as percentages will be based on it. But if your
        # XHTML table(s) lie(s) within a section that has a specific page style
        # with another width, specify it here (as a float value, in cm).
        self.pageWidth = pageWidth
        # Table widths expressed as pixels will use a "pixels to cm" ratio as
        # defined in css.px2cm. If this is wrong for you, specify another ratio
        # here. The width in cm will be computed as:
        #
        #                 (table width in pixels) / px2cm
        #
        self.px2cm = px2cm
        # Table cell paddings may use another px / cm ratio. Indeed,
        # cellspacing="1" is converted to 0.02cm with the standard ratio, which
        # is low.
        self.cellPx2cm = cellPx2cm
        # Every table with no specified width will be "wide" (=100% width).
        # If a table width is specified in px and is above the value defined
        # here, it will be forced to 100%.
        self.wideAbove = wideAbove
        # pod ensures that every column will at least get a minimum width
        # (expressed as a percentage: a float value between 0.0 and 1.0). You
        # can change this minimum here.
        self.minColumnWidth = minColumnWidth
        # If a column modifier is specified, any parameter related to table and
        # column widths is ignored: we will let LibreOffice (LO) compute himself
        # the table and column widths via its algorithm
        # "SetOptimalColumnWidths" if p_columnModifier is "optimize" or
        # "DistributeColumns"      if p_columnModifier is "distribute".
        # This requires LO to run in server mode and the
        # appy.pod.renderer.Renderer being launched with parameters
        #                   optimalColumnWidths="OCW_.*"
        # and                distributeColumns="DC_.*"
        self.columnModifier = columnModifier
        # When cell padding is defined (CSS table property "border-spacing" or
        # HTML table attribute "cellspacing"), a minimum value can be defined
        # here, as a float value (cm). If no padding is defined, the default one
        # from pod default style "podCell" is used and is 0.1cm.
        self.minCellPadding = minCellPadding
        # The styles to use for cell and cell header content. The default values
        # correspond to styles defined in styles.xmlt.
        self.cellContentStyle = cellContentStyle
        self.headerContentStyle = headerContentStyle
        # The table margins, as a tuple of 4 float values (cm):
        # top, right, bottom and left margins.
        self.margins = margins
        # May the table be spread on several pages ?
        self.unbreakable = unbreakable
        # May a single table row be spread on several pages ?
        self.unbreakableRows = unbreakableRows
        # Table-wide border properties can be defined, for example:
        #                    '0.018cm solid #000000'
        # If defined, it will override the potential CSS value defined on tables
        self.border = border
        # If CSS attributes and corresponding TableProperties attributes are
        # both encountered, who prevails ? If p_prevails is True,
        # TableProperties attributes prevail.
        self.prevails = prevails

    def getWidth(self, attrs, original=False):
        '''Return the table width as a css.Value object. p_attrs is a css.Styles
           object containing parsed table attributes. If p_original is False,
           p_self.wideAbove is not taken into account.'''
        # Widths being "0" or not being floats are simply ignored
        if not hasattr(attrs, 'width') or attrs.width.value == 0 or \
            isinstance(attrs.width.value, str):
            return self.width100
        r = attrs.width
        if original: return r
        if self.wideAbove is not None and r.unit == 'px' and \
           r.value > self.wideAbove:
            return self.width100
        return r

    def getCellPadding(self, value):
        '''CSS "border-spacing" is defined in p_value. This method gets the
           final value, taking into account self.minCellPadding.'''
        unit = value.unit
        # We must get p_value in cm
        if unit == 'cm':
            val = value.value
        elif unit == 'px':
            val = float(value.value) / self.cellPx2cm
        else:
            # We do not support this
            val = self.minCellPadding
        # Return the max between the p_value and the minimum value
        return max(val, self.minCellPadding)

    def getMargins(self, attrs, getWidth=False):
        '''Returns ODF properties allowing to define margins as specified by
           self.margins or by CSS p_attrs. If no margin is defined, r_ is an
           empty string.'''
        # If p_getWidth is True, the result is a tuple, whose second element is
        # the width (as a float representing cm) taken by potential left and/or
        # right margins.
        r = ''
        i = -1
        width = 0.0
        for direction in css.Styles.directions:
            i += 1
            # Get the value from CSS attributes
            cssValue = getattr(attrs, f'margin{direction}', None)
            if cssValue: cssValue = cssValue.cm(formatted=False)
            # Get the value as defined on p_self
            tbValue = self.margins[i]
            # Choose the prevailing value
            if not self.prevails:
                value = cssValue if cssValue is not None else tbValue
            else:
                value = tbValue if tbValue is not None else cssValue
            if value is None: continue
            # Determine the name of the corresponding ODF property
            name = f'fo:margin-{direction}'
            r = f'{r} {name}="{value:.2f}cm"'
            if direction in css.Styles.directionsW:
                width += value
        return (r, width) if getWidth else r

    @classmethod
    def initStylesMapping(class_, stylesMapping, ocw, dc):
        '''If our special regular expressions are in use in parameters
           p_ocw ("optimalColumnWidths") or p_dc ("distributeColumns"), we
           must provide specific style mapping entries allowing to map CSS
           attribute "table-layout" and its values to column modifiers
           "optimize" or "distribute".'''
        if (ocw == class_.ocwRex) or (dc == class_.dcRex):
            stylesMapping['table[table-layout=auto]'] = class_.ocw
            stylesMapping['table[table-layout=fixed]'] = class_.dc
            stylesMapping['table[table-layout=none]'] = class_.default

    @classmethod
    def init(class_):
        '''Sets, on this p_class_, some static attributes related to column
           width optimization.'''
        # The regular expressions to give to converter.py for it to recognize
        # tables whose column widths must be optimized or evenly distributed.
        class_.ocwRex = 'OCW_.*'
        class_.dcRex = 'DC_.*'
        # The default TableProperties instance
        class_.default = TableProperties()
        # TableProperties instances with OCW/DC enabled
        class_.ocw = TableProperties(columnModifier='optimize')
        class_.dc = TableProperties(columnModifier='distribute')
TableProperties.init()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class ListProperties(Properties):
    '''Base abstract class for defining properties of a XHTML list'''

    def __init__(self, levels, formats, delta, firstDelta, space, paraStyle):
        # The number of indentation levels supported
        self.levels = levels
        # The list of format characters for bullets or numbers
        self.formats = formats
        # The number of inches to increment at each level (as a float)
        self.delta = delta
        # The first delta can be different than any other
        self.firstDelta = firstDelta
        # The space, in inches (as a float), between the bullet/number and the
        # text.
        self.space = space
        # A specific style to apply to the inner paragraphs
        self.paraStyle = paraStyle
        # The number of levels can be > or < to the number of formats. In those
        # cases, formats will be applied partially or cyclically to levels.

    def dumpStyle(self, name):
        '''Returns the OpenDocument style definition corresponding to this
           instance.'''
        r = []
        fmt = utils.formatNumber
        spaceBefore = 0
        space = fmt(self.space, sep='.', removeTrailingZeros=True)
        for i in range(self.levels):
            # Determine if "delta" or "firstDelta" must be used
            if i == 0 and self.firstDelta is not None:
                delta = self.firstDelta
            else:
                delta = self.delta
            spaceBefore += delta
            sb = fmt(spaceBefore, sep='.', removeTrailingZeros=True)
            attr = self.getLevelAttributes(i)
            props = self.getTextProperties(i)
            level = f'  <text:list-level-style-{self.type} text:level=' \
              f'"{i+1}" text:style-name="{self.textStyle}" {attr}>{bn}    ' \
              f'<style:list-level-properties text:space-before="{sb}in" ' \
              f'text:min-label-width="{space}in"/>{props}{bn}  ' \
              f'</text:list-level-style-{self.type}>'
            r.append(level)
        return f'<text:list-style style:name="{name}">{bn}{bn.join(r)}{bn}' \
               f'</text:list-style>'

    def getTextProperties(self, i):
        '''Allows to define text properties at level p_i'''
        return ''

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class BulletedProperties(ListProperties):
    '''In a styles mapping, the value @key "ul" must be an instance of this
       class.'''

    type = 'bullet'
    defaultFormats = ('•', '◦', '▪')
    textStyle = 'podBulletStyle'

    def __init__(self, levels=4, formats=defaultFormats,
                 delta=0.32, firstDelta=0.08, space=0.16, paraStyle=None):
        ListProperties.__init__(self, levels, formats, delta, firstDelta,
                                space, paraStyle)

    def getLevelAttributes(self, i):
        '''Dumps bullet-specific attributes for level p_i'''
        # Get the bullet to render at this level
        bullet = utils.getElementAt(self.formats, i)
        return f'text:bullet-char="{bullet}"'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class NumberedProperties(ListProperties):
    '''In a styles mapping, the value @key "ol" must be an instance of this
       class.'''

    type = 'number'
    defaultFormats = ('1',)
    defaultSuffixes = ('.',)
    textStyle = 'podNumberStyle'

    def __init__(self, levels=4, formats=defaultFormats,
                 suffixes=defaultSuffixes, delta=0.32, firstDelta=0.08,
                 space=0.16, paraStyle=None):
        ListProperties.__init__(self, levels, formats, delta, firstDelta,
                                space, paraStyle)
        # The list of suffixes
        self.suffixes = suffixes

    def getLevelAttributes(self, i):
        '''Dumps number-specific attributes for level p_i'''
        # Get the number type and suffix to render at this level
        suffix = utils.getElementAt(self.suffixes, i)
        fmt =  utils.getElementAt(self.formats, i)
        return f'style:num-suffix="{suffix}" style:num-format="{fmt}"'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Style:
    '''Represents an ODF style. Either parsed from an ODF file or used for
       dumping a style into an ODF file.'''

    numberRex = re.compile(r'(\d+)(.*)')

    def __init__(self, name, family, defaults=None, outlineLevel=None):
        self.name = name
        self.family = family # May be 'paragraph', etc.
        self.displayName = name
        self.styleClass = None # May be 'text', 'list', etc.
        self.fontSize = None
        self.fontSizeUnit = None # May be pt, %, ...
        # Were the styles lies within styles and substyles hierarchy
        self.outlineLevel = outlineLevel
        # A possible delta to apply to the outline level. Do not confuse this
        # notion of delta, that applies when the outline level needs to be
        # dumped as attribute to a "text:h" paragraph whose style is p_self,
        # with the notion of delta being in use for a styles mapping (key "h*"),
        # allowing to fine-tune the mapping between outline levels implicitly
        # expressed on XHTML tags ("h1", "h2", etc) and ODF styles's outline
        # levels.
        self.outlineDelta = 0
        # Namespace for the ODF "style-name" attribute corresponding to this
        # style
        self.styleNameNs = 'table' if family == 'table-cell' else 'text'
        # Default ODF attributes for this style
        self.defaults = defaults
        # For some unknown reason, ODF parent-child links don't work
        self.inheritWorks = family != 'table-cell'

    def setFontSize(self, fontSize):
        rexRes = self.numberRex.search(fontSize)
        self.fontSize = int(rexRes.group(1))
        self.fontSizeUnit = rexRes.group(2)

    def __repr__(self):
        '''p_self's short string representation'''
        r = f'<Style {self.name}|family {self.family}'
        if self.displayName is not None:
            r += f'|displayName "{self.displayName}"'
        if self.styleClass is not None:
            r += f'|class {self.styleClass}'
        if self.fontSize is not None:
            r += f'|fontSize {self.fontSize}{self.fontSizeUnit}'
        if self.outlineLevel is not None: r += f'|level {self.outlineLevel}'
        return f'{r}>'

    def getOdfAttributes(self, attrs=None, withName=True, withDefaults=False,
                         exclude=None):
        '''Gets the ODF attributes corresponding to this style. p_attrs, when
           given, are attributes of an XHTML tag.'''
        # Style name
        r = f' {self.styleNameNs}:style-name="{self.name}"' if withName else ''
        # Outline level when relevant
        if self.outlineLevel is not None:
            level = self.outlineLevel + self.outlineDelta
            r = f'{r} text:outline-level="{level}"'
        # Colspan and rowspan when relevant
        if attrs and 'colspan' in attrs:
            r = f'{r} table:number-columns-spanned="{attrs["colspan"]}"'
        if attrs and 'rowspan' in attrs:
            r = f'{r} table:number-rows-spanned="{attrs["rowspan"]}"'
        # Additional parameters as stored in self.defaults
        if withDefaults and self.defaults:
            for name, value in self.defaults.items():
                if exclude and name in exclude: continue
                r = f'{r} {name}="{value}"'
        return r

    def getOdfParentAttributes(self, childAttrs=None):
        '''If style inheritance works, this method simply returns the attribute
           "style:parent-style-name" allowing to define some style as child from
           this one. If inheritance does not work (like for "table-cell"
           styles), this method returns, in extenso, the parent ODF properties,
           so they will be entirely copied into the child style.'''
        if self.inheritWorks:
            r = f' style:parent-style-name="{self.name}"'
        else:
            r = self.getOdfAttributes(withName=False, withDefaults=True,
                                      exclude=childAttrs)
        return r

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class GraphicalStyle:
    '''Represents an ODF style of type "graphic"'''

    defaultAttributes = 'draw:textarea-horizontal-align="center" ' \
      'draw:textarea-vertical-align="top" fo:margin-left="0.318cm" ' \
      'fo:margin-right="0.318cm" fo:margin-top="0cm" fo:margin-bottom="0cm" ' \
      'style:run-through="background" style:wrap="run-through" ' \
      'style:number-wrapped-paragraphs="no-limit" ' \
      'style:vertical-pos="from-top" style:vertical-rel="paragraph" ' \
      'style:horizontal-pos="from-left" style:horizontal-rel="paragraph" ' \
      'draw:wrap-influence-on-position="once-concurrent" ' \
      'loext:allow-overlap="true" style:flow-with-text="false"'

    def __init__(self, name, stroke='none', strokeWidth='0cm',
                 strokeColor='#666666', fill='solid', fillColor='#666666'):
        self.name = name
        self.stroke = stroke
        self.strokeWidth = strokeWidth
        self.strokeColor = strokeColor
        self.fill = fill
        self.fillColor = fillColor

    def getOdfAttributes(self):
        '''Returns p_self's attributes expressed as ODF'''
        return f'draw:stroke="{self.stroke}" svg:stroke-width="' \
               f'{self.strokeWidth}" svg:stroke-color="{self.strokeColor}" ' \
               f'draw:fill="{self.fill}" draw:fill-color="{self.fillColor}" ' \
               f'{self.defaultAttributes}'

    def asOdf(self):
        '''Returns p_self's representation as ODF code'''
        return f'<style:style style:name="{self.name}" style:family="graphic">'\
               f'<style:graphic-properties {self.getOdfAttributes()}/>' \
               f'</style:style>'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class PageStyle:
    '''Represents a page style'''

    # Attributes storing the style name
    nameAttributes = ('style:name', 'style:display-name')

    # Attributes storing references to other styles
    refAttributes = ('style:next-style-name',)

    # The attribute defining a page start number
    startAttr = 'style:page-number="%s"'

    def __init__(self, name, attrs):
        self.name = name
        self.attrs = dict(attrs)
        self.uniqueName = None # Will be the new name

    def rename(self):
        '''Give to this style a new, unique name'''
        self.uniqueName = getUuid(prefix='PS', removeDots=True)
        # Update attributes
        for name in PageStyle.nameAttributes:
            if name in self.attrs:
                self.attrs[name] = self.uniqueName

    def update(self, styles):
        '''If this style refers to other styles, update these references with
           the new style names.'''
        for attr in PageStyle.refAttributes:
            if attr in self.attrs:
                oldName = self.attrs[attr]
                self.attrs[attr] = styles[oldName].uniqueName

    def reifyStartTag(self):
        '''Re-creates the ODF start tag corresponding to this style'''
        attrs = [f'{n}="{v}"' for n, v in self.attrs.items()]
        return f'<style:master-page {" ".join(attrs)}>'

    def reifyUsingStartTag(self, match, start):
        '''Re-creates the ODF style definition using this page style'''
        # Apply the page start number when relevant
        params = match.group(3)
        if start is not None:
            params = params.replace(self.startAttr % 'auto',
                                    self.startAttr % start)
        return f'<style:style{match.group(1)}style:master-page-name="' \
               f'{self.uniqueName}"{params}</style:style>'

    def __repr__(self):
        '''String representation for this page style'''
        attrs = f', attrs={str(self.attrs)}' if self.attrs else ''
        return f'<PageStyle name={self.name}, uniqueName={self.uniqueName}' \
               f'{attrs}>'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class PageStyles:
    '''Stores all page styles found in a document'''

    # Rex for parsing a page style definition in styles.xml
    STYLES_DEF = re.compile(r'<style:master-page\s+style:name="(.*?)"\s+.*?>')

    # Rex for parsing a tag, in content.xml, that refers to a page style
    CONTENT_USE = re.compile('<style:style([^<]+)style:master-page-name='\
                             '"([^"]+)"(.*?)</style:style>')

    def __init__(self):
        self.styles = {} # ~{s_name, PageStyle}~
        # If page numbering must be restarted at some number within this page
        # style, this number will be stored here.
        self.startNumber = None
        # Has this PageStyles instance already been initialised ? When reusing
        # the same renderer several times (ie, when re-importing the same
        # sub-pod), we must avoid calling m_init more than once.
        self.initialised = False
        # The name of the current pod template, for use in error messages
        self.template = None

    def add(self, style):
        '''Adds a newly parsed page p_style'''
        self.styles[style.name] = style

    def init(self, managePageStyles, template):
        '''Post-initialisation'''
        # Do not perform this if initialisation already occurred
        if self.initialised: return
        self.template = template
        # Take p_managePageStyles into account
        if isinstance(managePageStyles, int):
            self.startNumber = managePageStyles
        # When merging sub-documents into a master document, we need to give
        # unique names to sub-doc's page styles; else, they won't be retrieved
        # correctly in the master document.
        styles = self.styles
        # 1. Give a unique (display) name to every page style
        for style in styles.values(): style.rename()
        # 2. Update links between styles
        for style in styles.values(): style.update(styles)
        self.initialised = True
        return self

    def getNewStyleDefinition(self, match):
        '''Produce the new style definition'''
        style = self.styles[match.group(1)]
        return style.reifyStartTag()

    def getNewStyleUse(self, match):
        '''Produce the new style use'''
        style = self.styles[match.group(2)]
        # Determine the start number for sub-pages
        if self.first:
            start = self.startNumber
        else:
            start = None
        r = style.reifyUsingStartTag(match, start)
        self.first = False
        return r

    def renameIn(self, name, content):
        '''Adapts, in p_content, any mention (definition or usage) to this page
           style according to its new unique name. If p_name is:
           - "styles", p_content is the string content of styles.xml;
           - "content", p_content is the string content of content.xml.
        '''
        r = content
        if name == 'styles':
            # Replace style definitions with their renamed versions
            r = self.STYLES_DEF.sub(self.getNewStyleDefinition, r)
        elif name == 'content':
            # When a start number is defined, we must set it only on the first
            # encountered page style use, so we remember if we are on the first
            # one or not.
            self.first = True
            # Replace style uses with their renamed versions
            r = self.CONTENT_USE.sub(self.getNewStyleUse, r)
            # Raise an exception if no replacement has been made, but a start
            # number was specified.
            if self.startNumber is not None and self.first:
                raise Exception(IMPLIC_PS % self.template)
        return r

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Default ODF styles for XHTML elements. They correspond to styles from
# content.xmlt or styles.xmlt. Default cell and header attributes are repeated
# here because (a) for an unknown reason, they are not inherited from default
# styles defined in styles.xmlt when generating a child sub-style, and (b) they
# slightly differ. For example, default vertical alignment for XHTML is not the
# same as for ODF. "podCell" here will use the XHTML standard, while "podCell"
# in content.xmlt will use the ODF standard.
DEFAULT_CELL_PARAMS = {'fo:padding':'0.1cm',
  'fo:border':'0.018cm solid #000000', 'style:vertical-align': 'middle'}
DEFAULT_HEADER_PARAMS = DEFAULT_CELL_PARAMS.copy()
DEFAULT_HEADER_PARAMS['fo:background-color'] = '#e6e6e6'
DEFAULT_STYLES = {
  'table': TableProperties.default,
  'td': Style('podCell', 'table-cell', DEFAULT_CELL_PARAMS),
  'th': Style('podHeader', 'table-cell', DEFAULT_HEADER_PARAMS),
}
for i in range(1,7):
    DEFAULT_STYLES[f'h{i}'] = Style(f'podH{i}', 'paragraph', outlineLevel=i)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class PageLayout:
    '''Represents a kind of page-level style'''

    def __init__(self, name):
        self.name = name

    def getFloat(self, value):
        '''Extract the float value from the string p_value'''
        r = ''
        for c in value:
            if c.isdigit() or c == '.':
                r += c
        return float(r)

    def setProperties(self, e, attrs):
        '''Sets properties of this page layout based on parsed p_attrs from tag
           "page-layout-properties".'''
        # Compute page dimensions. May be missing for ods files.
        widthAttr = e.tags['page-width']
        if widthAttr not in attrs: return
        self.width = self.getFloat(attrs[widthAttr])
        heightAttr = e.tags['page-height']
        if heightAttr not in attrs: return
        self.height = self.getFloat(attrs[heightAttr])
        # Compute margins
        marginAttr = e.tags['margin']
        if marginAttr not in attrs:
            defaultMargin = '2cm'
        else:
            defaultMargin = attrs[marginAttr]
        for margin in css.Styles.directions:
            key = e.tags[f'margin-{margin}']
            value = (key in attrs) and attrs[key] or defaultMargin
            marginAttr = f'margin{margin.capitalize()}'
            setattr(self, marginAttr, self.getFloat(value))

    def getWidth(self, substractMargins=True):
        '''Return, as a float, the page width in cm'''
        r = getattr(self, 'width', None)
        if not r: return
        if substractMargins: r -= self.marginLeft + self.marginRight
        return r

    def getHeight(self, substractMargins=True):
        '''Return, as a float, the page height in cm'''
        r = getattr(self, 'height', None)
        if not r: return
        if substractMargins: r -= self.marginTop + self.marginBottom
        return r

    def __repr__(self): return f'<Page layout {self.name}>'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Styles(UserDict):
    '''A dict of styles'''

    def getParagraphStyleAtLevel(self, level):
        '''Tries to find a style which has level p_level. Returns None if no
           such style exists.'''
        for style in self.values():
            if style.family == 'paragraph' and style.outlineLevel == level:
                return style

    def getStyle(self, displayName):
        '''Gets the style that has this p_displayName. Returns None if not
           found.'''
        r = None
        for style in self.values():
            if style.displayName == displayName:
                r = style
                break
        return r

    def getStyles(self, stylesType='all'):
        '''Returns a list of all the styles of the given p_stylesType'''
        r = []
        if stylesType == 'all':
            r = self.values()
        else:
            for style in self.values():
                if style.family == stylesType and style.displayName:
                    r.append(style)
        return r

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class FontsInjector:
    '''Allows to inject a font within all styles in a ODF document'''

    # Regular expressions allowing to identify, in styles.xml, fonts and
    # font-family definitions.
    any = '.*?'
    fontAttr = 'style:font-name="%s"'
    fontRex = re.compile(fontAttr % any)
    familyAttr = 'fo:font-family="%s"'
    familyRex = re.compile(familyAttr % any)

    def __init__(self, font):
        # The font name may also include the font family
        parts = font.split(',', 1)
        if len(parts) == 1:
            self.font = self.family = parts[0]
        else:
            # In that case, the "family" must also be used for the font name
            self.font = self.family = parts[1]

    def injectIn(self, stylesXml):
        '''Injects, within every style found in a "styles.xml" file whose string
           content is in p_stylesXml, the font as defined in p_self.font.'''
        # Set the correct font name
        r = self.fontRex.sub(lambda match: self.fontAttr % self.font, stylesXml)
        # Set the correct family name
        return self.familyRex.sub(
                 lambda m: self.familyAttr % f"'{self.family}'", r)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class StylesEnvironment(OdfEnvironment):
    '''Environment for the styles parser'''

    def __init__(self):
        OdfEnvironment.__init__(self)
        # Namespace definitions are not already encountered
        self.gotNamespaces = False
        # Names of some tags, that we will compute after namespace propagation
        self.tags = None
        # All styles, page styles excepted
        self.styles = Styles()
        # Page styles
        self.pageStyles = PageStyles()
        # The currently parsed style definition
        self.currentStyle = None
        # The found page layouts, keyed by their name
        self.pageLayouts = {}
        self.currentPageLayout = None # The currently parsed page layout
        # The name of the page layout defined for the whole document
        self.masterLayoutName = None
        self.state = READING

    def onStartElement(self):
        ns = self.namespaces
        if not self.gotNamespaces:
            # We suppose that all the interesting (from the POD point of view)
            # XML namespace definitions are defined at the root XML element.
            # Here we propagate them in XML element definitions that we use
            # throughout POD.
            self.gotNamespaces = True
            self.propagateNamespaces()
        return ns

    def propagateNamespaces(self):
        '''Propagates the namespaces in all XML element definitions that are
           used throughout POD.'''
        ns = self.namespaces
        # Create a table of names of used tags and attributes (precomputed,
        # including namespace, for performance).
        s = ns[self.NS_STYLE]
        fo = ns[self.NS_FO]
        office = ns[self.NS_OFFICE]
        tags = {
          'style': f'{s}:style',
          'name': f'{s}:name',
          'family': f'{s}:family',
          'class': f'{s}:class',
          'display-name': f'{s}:display-name',
          'default-outline-level': f'{s}:default-outline-level',
          'text-properties': f'{s}:text-properties',
          'font-size': f'{fo}:font-size',
          'master-styles': f'{office}:master-styles',
          'master-page': f'{s}:master-page',
          'page-layout-name': f'{s}:page-layout-name',
          'page-layout': f'{s}:page-layout',
          'page-layout-properties': f'{s}:page-layout-properties',
          'page-width': f'{fo}:page-width',
          'page-height': f'{fo}:page-height',
          'margin': f'{fo}:margin',
          'margin-top': f'{fo}:margin-top',
          'margin-right': f'{fo}:margin-right',
          'margin-bottom': f'{fo}:margin-bottom',
          'margin-left': f'{fo}:margin-left',
        }
        self.tags = tags

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class StylesParser(OdfParser):
    '''The styles parser'''

    def __init__(self, env, caller):
        OdfParser.__init__(self, env, caller)

    def endDocument(self):
        e = OdfParser.endDocument(self)
        # Repatriate interesting outputs on the parser itself
        caller = self.caller
        caller.styles = e.styles
        caller.pageStyles = e.pageStyles
        caller.pageLayout = e.pageLayouts[e.masterLayoutName]

    def startElement(self, elem, attrs):
        e = OdfParser.startElement(self, elem, attrs)
        ns = e.onStartElement()
        if elem == e.tags['style']:
            e.state = PARSING_STYLE
            # Create the style
            style = Style(name=attrs[e.tags['name']],
                          family=attrs[e.tags['family']])
            classAttr = e.tags['class']
            if classAttr in attrs: style.styleClass = attrs[classAttr]
            dnAttr = e.tags['display-name']
            if dnAttr in attrs: style.displayName = attrs[dnAttr]
            dolAttr = e.tags['default-outline-level']
            if dolAttr in attrs and attrs[dolAttr].strip():
                style.outlineLevel = int(attrs[dolAttr])
            # Record this style in the environment
            e.styles[style.name] = style
            e.currentStyle = style

        elif elem == e.tags['page-layout']:
            e.state = PARSING_P_LAYOUT
            pageLayout = PageLayout(attrs[e.tags['name']])
            # Record this page layout in the environment
            e.pageLayouts[pageLayout.name] = pageLayout
            e.currentPageLayout = pageLayout

        elif elem == e.tags['master-styles']:
            e.state = PARSING_M_STYLES

        elif e.state == PARSING_STYLE:
            # Find properties within this style definition
            if elem == e.tags['text-properties']:
                fontSizeAttr = e.tags['font-size']
                if fontSizeAttr in attrs:
                    e.currentStyle.setFontSize(attrs[fontSizeAttr])

        elif e.state == PARSING_P_LAYOUT:
            # Find properties within this page layout definition
            if elem == e.tags['page-layout-properties']:
                e.currentPageLayout.setProperties(e, attrs)

        elif e.state == PARSING_M_STYLES:
            # I am parsing section "master-styles"
            if elem == e.tags['master-page']:
                plnAttr = e.tags['page-layout-name']
                # In case there are several master styles, keep the first one
                if not e.masterLayoutName and plnAttr in attrs:
                    e.masterLayoutName = attrs[plnAttr]
                # Add this page style
                name = attrs['style:name']
                e.pageStyles.add(PageStyle(name, attrs))

    def endElement(self, elem):
        e = OdfParser.endElement(self, elem)
        if elem == e.tags['style']:
            e.state = READING
            e.currentStyle = None
        elif elem == e.tags['page-layout']:
            e.state = READING
            e.currentPageLayout = None
        elif elem == e.tags['master-styles']:
            e.state = READING

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Css2odf:
    '''Allows to get a OpenDocument attribute from a CSS attribute'''

    # Map CSS attribute names to ODF attribute names. CSS attributes names
    # have lost their inner dashes (margin-left => marginleft) because they are
    # used as Python attributes on css.Styles instances.
    namesMap = {
      'marginleft': 'fo:margin-left', 'marginright': 'fo:margin-right',
      'margintop': 'fo:margin-top', 'marginbottom': 'fo:margin-bottom',
      'textalign': 'fo:text-align', 'textindent': 'fo:text-indent',
      'backgroundcolor': 'fo:background-color', 'color': 'fo:color',
      'fontsize': 'fo:font-size', 'fontvariant': 'fo:font-variant',
      'fontweight': 'fo:font-weight', 'fontstyle': 'fo:font-style',
      'border': 'fo:border', 'borderspacing': 'fo:padding',
      'lineheight': 'style:line-spacing',

      # Vertical-align map to different ODF attributes depending on its use:
      # aligning table cell content or text (sub or sup).
      'verticalalign': {
        'top': ('style:vertical-align', 'top'),
        'middle': ('style:vertical-align', 'middle'),
        'bottom': ('style:vertical-align', 'bottom'),
        'super': ('style:text-position', 'super 58%'),
        'sub': ('style:text-position', 'sub 58%'),
      },

      # CSS text-decoration corresponds to a different ODF attribute, depending
      # on its value.
      'textdecoration': {
        'underline': ('style:text-underline-style', 'solid'),
        'line-through': ('style:text-line-through-style', 'solid'),
        'overline': ('style:text-overline-style', 'solid')},

      # Idem for the following attributes
      'pagebreakafter': {'always': ('fo:break-after', 'page')},
      'pagebreakbefore': {'always': ('fo:break-before', 'page')},
    }

    # Map XHTML CSS values to values of their corresponding ODF attributes when
    # they are different.
    valuesMap = {
      'textalign': {'left': 'start', 'start': 'start', 'center': 'center',
                    'right': 'end', 'end': 'end', 'justify': 'justify',
                    'match-parent': 'start'},
      'border': {'0': 'none', 'undefined': 'none', '*':'*'},
      'fontsize': {'medium': '100%', 'xx-small': '55%', 'x-small': '70%',
                   'small': '85%', 'large': '115%', 'x-large': '130%',
                   'xx-large': '145%', 'smaller': '85%', 'larger': '115%',
                   'initial': '100%', 'inherit': '100%'},
      'lineheight': {'normal': 'normal', 'initial': 'normal',
                     'inherit': 'normal'}
    }

    # CSS properties representing combinations of CSS properties
    combined = ('background', 'border')

    # For the following attributes, an alternative px2cm ratio can be defined
    px2cmRatios = {'lineheight': css.px2cm * 2 }

    # The following attributes will not be converted to ODF if their related
    # condition evaluates to True.
    notNegInTable = 'self.inTable() and (val < 0)'
    ignore = {
      # Ignore negative text-indent and margin-left attributes within tables
      'textindent': notNegInTable, 'marginleft': notNegInTable,
    }

    def __init__(self):
        '''The p_xhtmlParser from the current conversion from XHTML to ODT may
           be required to fine-tune the conversion.'''
        self.xhtmlParser = None # Will be set later

    def getOdf(self, attributes, name, value, sub=None):
        '''Compute, when possible, the ODF attribute, as a tuple (name, value)
           corresponding to CSS attribute p_name having some p_value (and the
           specific p_sub-value if p_value is multiple). If such an ODF
           attribute is found, it is appended in this list of p_attributes.'''
        # Is there an ODF attribute corresponding to this CSS attribute ?
        odfName = self.namesMap.get(name)
        if not odfName: return
        val = sub or value.value
        # Must we ignore this attribute ?
        if (name in self.ignore) and eval(self.ignore[name]): return
        # Is the ODF attribute different according to CSS value ?
        if isinstance(odfName, dict):
            # "val" can be absent from the list of values that must be mapped to
            # an ODF style (ie, "none").
            r = odfName.get(val)
            if r: attributes.append(r)
            return
        # Standardize the attribute for use within an ODF document
        unit = value.unit or ''
        if unit and (unit != '%'):
            ratio = self.px2cmRatios.get(name, css.px2cm)
            try:
                val = value.cm(value=val, ratio=ratio)
                unit = 'cm'
            except TypeError: # Prevent crash when the value is invalid
                return
        # Convert the value to the ODF equivalent when needed
        if not unit and (name in self.valuesMap):
            # The value in valuesMap can add a unit
            values = self.valuesMap[name]
            if val in values:
                val = values[val]
            elif '*' in values:
                # Keep the value, and map it to the value at "*" or keep it
                # as-is if the mapping is "*":"*".
                rVal = values['*']
                if rVal != '*':
                    val = rVal
            else:
                # Ignore the value if not among supported values
                return
        attributes.append((odfName, f'{val}{unit}'))

    def isCombined(self, name, value):
        '''Returns True if the CSS property p_name is a combined CSS property,
           ie, a property representing a set of CSS properties.'''
        return name in self.combined and ' ' in value.value

    def inTable(self):
        '''In the XHTML > ODT conversion, are we currently parsing a table ?'''
        parser = self.xhtmlParser
        return parser and parser.env.currentTables

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class DynamicStyles:
    '''Styles generated on-the-fly by POD'''

    # While working, POD may identify and create on-the-fly "dynamic styles", to
    # insert either in the "automatic-styles" section of content.xml (ie, the
    # column styles of tables generated from XHTML tables via xhtml2odt.py), in
    # the "automatic-styles" section of styles.xml (ie, styles used in the
    # header and the footer) or in its "styles" section (ie, bullet styles).

    # The styles must be injected just before these "hooks"
    hooks = {'content':     '</office:automatic-styles>',
             'styles_base': '</office:styles>',
             'styles':      '</office:automatic-styles>'}

    def __init__(self):
        # Styles to be injected in the "automatic-styles" tag within content.xml
        self.content = []
        # Styles to be injected in the "automatic-styles" tag within styles.xml
        self.styles = []
        # Styles to be injected in the "styles" tag within styles.xml
        self.styles_base = []

    def addListStyles(self):
        '''Add bullet-related styles in attr "styles_base"'''
        styles = self.styles_base
        styles.append(NumberedProperties().dumpStyle('podNumberedList'))
        styles.append(BulletedProperties().dumpStyle('podBulletedList'))

    def add(self, attr, style):
        '''Adds this p_style definition p_self's attribute named p_attr'''
        getattr(self, attr).append(style)

    def injectIn(self, attr, content):
        '''Inject the styles generated and collected in p_self's attribute named
           p_attr and inject them in p_content.'''
        # For "styles_base", add list-related styles now
        if attr == 'styles_base': self.addListStyles()
        # p_content is the string content of either content.xml or styles.xml
        styles = getattr(self, attr)
        if not styles: return content
        # Perform the injection
        hook = self.hooks[attr]
        styles = f'{"".join(styles)}{hook}'
        return content.replace(hook, styles)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class StylesGenerator:
    '''Analyse, for a given XHTML tag, its attributes (including CSS attributes
       within the "style" attribute) and possibly generate a custom style.'''

    suffix = 'pod'

    # Map HTML tags to ODF style families. Any tag not present in this list is
    # supposed to have family "text".
    styleFamilies = {'p': 'paragraph', 'div': 'paragraph', 'td': 'table-cell',
                     'th': 'table-cell'}

    # For paragraph styles, there are 2 kinds of properties: paragraph and text
    # properties. Any property not being listed as a text property below will be
    # considered as a paragraph property.
    textProperties = {
      'fo:color': True, 'fo:font-size': True, 'fo:font-variant': True,
      'fo:font-weight': True, 'fo:font-style': True,
      'style:text-underline-style': True,
      # For this one, this is more subtle: the property will be considered a
      # text property only if the HTML tag is not of type "para" nor "list".
      'fo:background-color': {'para': False, 'list': False, 0: True},
      'style:text-line-through-style': True, 'style:text-overline-style': True,
      'style:text-position': True}

    # Properties applying to table cells and that are not transferred to inner
    # paragraphs.    
    cellProperties = ('fo:padding', 'fo:border', 'fo:background-color',
                      'style:vertical-align')
    # Default parent styles to apply for generated styles. Those styles are not
    # listed among DEFAULT_STYLES because, when there is no custom style to
    # generate, they must not be specified, it is implicit.
    standardStyle = Style('Standard', 'paragraph')
    defaultParents = {'p': standardStyle, 'div': standardStyle}

    def __init__(self, stylesManager):
        # From one renderer execution to another, we need to produce styles
        # having unique names. Indeed, when LO incorporates sub-pods into a
        # master pod, homonym syles are considered to be exactly the same.
        self.prefix = randomName()
        # The number attributed to the last generated style
        self.last = 0
        # The names of the styles that were already generated, keyed by some
        # hash value.
        self.generated = {}
        self.stylesManager = stylesManager
        # Allows to convert CSS to ODF attributes
        self.css2odf = Css2odf()
        # Are we generating an ODT or ODS file ?
        self.isOds = stylesManager.renderer.templateType == 'ods'

    def addStyle(self, style, store):
        '''Adds this p_style definition into this p_store (content.xml or
           styles.xml).'''
        self.stylesManager.dynamicStyles.add(store, style)

    def addStyleInstance(self, name):
        '''Add the style named p_name to the style manager's defined styles, as
           a Style instance.'''
        styles = self.stylesManager.styles
        if name not in styles:
            styles[name] = Style(name, 'paragraph')

    def addGraphicalStyle(self, target, **kwargs):
        '''Creates and add a style of type "graphic" within the dynamically
           generated styles.'''
        # Generate a name for this new style
        name = self.generateStyleName()
        # Create a instance of GraphicalStyle
        style = GraphicalStyle(name, **kwargs)
        # Add it among dynamically created styles
        self.addStyle(style.asOdf(), target)
        return style

    def getStyleHash(self, xhtmlElem, odfAttrs, baseStyle, store):
        '''Returns a string uniquely representing the given set of ODF
           attributes p_odfAttrs that will be used to create/retrieve a style to
           be applied to the ODF element corresponding to p_xhtmlElem.'''
        odfAttrs.sort()
        attrs = self.flattenOdfAttributes(odfAttrs, forHash=True)
        r = f'{xhtmlElem.elem}{store[0]}{"".join(attrs)}'
        if baseStyle:
            # The base style must be part of the hash; else, the same set of
            # attributes on the same tag, but with 2 different base styles,
            # would be considered equal.
            r = f'{r}*{baseStyle.name}'
        return r

    def getStyleFamily(self, xhtmlElem):
        '''Returns the ODF family style corresponding to p_xhtmlElem'''
        return self.styleFamilies.get(xhtmlElem.elem, 'text')

    def generateStyleName(self):
        '''Generates a new style name'''
        self.last += 1
        return f'{self.prefix}{self.last}{self.suffix}'

    def getStyleName(self, xhtmlElem, odfAttrs, baseStyle, store):
        '''Return the ODF style name for the style that will be applied to ODF
           element corresponding to the given XHTML element (p_xhtmlElem). We
           have already computed attributes for the ODF style in p_odfAttrs. If
           a style has already been generated by this styles generator, for this
           tag and with this combination of attributes, we simply return its
           name. Else, we note that we must generate a new style; we compute a
           new (incremental) name for it and we return this name.'''

        # More precisely, this method returns a tuple (createNew, styleName):
        # - "createNew" is a boolean indicating if a new style must be
        #               generated;
        # - "styleName" is the style name.

        # If the style hash corresponds to an existing style, simply return
        # its name.
        hash = self.getStyleHash(xhtmlElem, odfAttrs, baseStyle, store)
        if hash in self.generated:
            return False, self.generated[hash]
        # A new style must be generated
        r = self.generateStyleName()
        self.generated[hash] = r
        return True, r

    def flattenOdfAttributes(self, odfAttrs, forHash=False):
        '''Produce a string from the list of (name, value) pairs in
           p_odfAttrs.'''
        fmt = '%s%s' if forHash else '%s="%s"'
        return [fmt % (name, value) for name, value in odfAttrs]

    def isTextProperty(self, xhtmlElem, name):
        '''Is property p_name a text property ?'''
        if name in self.textProperties:
            r = self.textProperties[name]
            if isinstance(r, dict):
                # It depends on p_xhtmlElem
                if xhtmlElem.elemType in r:
                    r = r[xhtmlElem.elemType]
                else:
                    r = r[0]
        else:
            r = False
        return r

    # This method generates most of the tags. If no specific method is found for
    # some tag, this method is used.

    def getStylesStore(self, tag, stylesStore):
        '''Where must a style related to this p_tag be generated ? In
           content.xml or in styles.xml ?'''
        # Use custom dict p_styleStore if passed
        r = stylesStore.get(tag) if stylesStore else None
        if r: return r
        # Within an ODT file, injecting styles in content.xml does not work
        # properly in some cases. For example, a percentage value for attribute
        # "fo-font-size" will be ignored if the style is dumped in content.xml.
        # Inversely, in an ODS file, it is preferable to dump everything in
        # content.xml.
        return 'content' if self.isOds else 'styles_base'

    def get_any(self, xhtmlElem, odfAttrs, baseStyle, add=False,
                stylesStore=None):
        '''Generates a (or returns an existing) paragraph style'''
        # Must the style be created in styles.xml or in content.xml ?
        store = self.getStylesStore(xhtmlElem.elem, stylesStore)
        createNew, styleName = self.getStyleName(xhtmlElem, odfAttrs,
                                                 baseStyle, store)
        if not createNew:
            # Manage p_add being True (see comment below)
            if add: self.addStyleInstance(styleName)
            return styleName
        # Generate a new style. Is there a parent style ?
        baseStyle = baseStyle or self.defaultParents.get(xhtmlElem.elem)
        names = [name for name, value in odfAttrs]
        parent = baseStyle.getOdfParentAttributes(names) if baseStyle else ''
        # Among p_odfAttrs, distinguish "paragraph" and "text" properties
        paraAttrs = []
        textAttrs = []
        for name, value in odfAttrs:
            if self.isTextProperty(xhtmlElem, name):
                textAttrs.append((name, value))
            else:
                paraAttrs.append((name, value))
        paraProps = textProps = ''
        if paraAttrs:
            paraProps = f'<style:paragraph-properties ' \
                        f'{" ".join(self.flattenOdfAttributes(paraAttrs))}/>'
        if textAttrs:
            textProps = f'<style:text-properties ' \
                        f'{" ".join(self.flattenOdfAttributes(textAttrs))}/>'
        family = self.getStyleFamily(xhtmlElem)
        style = f'<style:style style:name="{styleName}" ' \
                f'style:family="{family}"{parent}>{textProps}{paraProps}' \
                f'</style:style>'
        # Within an ODT file, injecting styles in content.xml does not work
        # properly in some cases. For example, a percentage value for attribute
        # "fo-font-size" will be ignored if the style is dumped in content.xml.
        # Inversely, in an ODS file, it is preferable to dump everything in
        # content.xml.
        self.addStyle(style, store)
        # If p_add is True, also add the style to styleManager's defined styles
        # (as a Style instance). Else, it won't be found when it will need to be
        # applied on an inner paragraph.
        if add: self.addStyleInstance(styleName)
        return styleName

    def get_td(self, xhtmlElem, odfAttrs, baseStyle, stylesStore=None):
        '''Generates a table cell style'''
        # If there is a "text-related" property among p_odfAttrs, we must
        # generate a style for the inner-paragraph within this cell. Indeed, in
        # XHTML, this kind of information can be defined at the "td" tag level,
        # while, in ODF, it must be defined at the inner-paragraph level. A cell
        # style will only be generated if there is a "cell-related" property
        # among p_odfAttrs.
        paraAttrs = []
        cellAttrs = []
        store = 'content'
        for name, value in odfAttrs:
            if name == 'fo:text-align': paraAttrs.append((name, value))
            elif name in self.cellProperties: cellAttrs.append((name, value))
            elif name in self.textProperties: paraAttrs.append((name, value))
        # Generate a paragraph style to be applied on this td's inner paragraph
        if paraAttrs:
            xhtmlElem.innerStyle = self.get_any(xhtmlElem.protos['p'],paraAttrs,
                             Style(xhtmlElem.innerStyle, 'paragraph'), add=True)
        # Generate a cell style
        if cellAttrs:
            # Generate (or retrieve) a table-cell style, based on the standard
            # Appy cell style.
            createNew, styleName = self.getStyleName(xhtmlElem, cellAttrs,
                                                     baseStyle, store)
            if not createNew: return styleName
            # Generate a new style. For table cells there is always a baseStyle.
            names = [name for name, value in cellAttrs]
            parentAttrs = baseStyle.getOdfParentAttributes(names)
            flattened = " ".join(self.flattenOdfAttributes(cellAttrs))
            style = f'<style:style style:name="{styleName}" ' \
              f'style:family="{self.getStyleFamily(xhtmlElem)}">' \
              f'<style:table-cell-properties{parentAttrs} {flattened}/>' \
              f'</style:style>'
            self.addStyle(style, store)
            return styleName
    get_th = get_td

    def get(self, xhtmlElem, baseStyle, stylesStore=None):
        '''Generates a custom style when relevant. p_baseStyle is a Style object
           that could have been found from a style mapping. In this case, the
           generated style will get it as parent style.'''
        # If no CSS styles are defined, no custom style can be defined
        cssStyles = xhtmlElem.cssStyles
        if not cssStyles: return baseStyle
        # If the elem is a table or list, return the base style (None or a
        # Properties object). The caller will generate the style himself.
        if xhtmlElem.elem in Properties.elems: return baseStyle
        # Analyse CSS styles
        elem = xhtmlElem.elem
        # Collect ODF attributes corresponding to CSS attributes
        odfAttrs = []
        for name, value in cssStyles.get().items():
            if name == 'classes': continue
            if self.css2odf.isCombined(name, value):
                # Combined values are currently ignored, "border" excepted
                if name == 'border':
                    self.css2odf.getOdf(odfAttrs, name, value)
            elif value.isMultiple():
                for v in value.value.split(' '):
                    self.css2odf.getOdf(odfAttrs, name, value, v)
            else:
                self.css2odf.getOdf(odfAttrs, name, value)
        if not odfAttrs: return baseStyle
        # I have attributes to apply. Call the corresponding "get_[tag]" method
        # for generating a custom style, or "get_any" if here is no specific
        # method for this tag.
        methodName = f'get_{elem}'
        if not hasattr(self, methodName): methodName = 'get_any'
        method = getattr(self, methodName)
        styleName = method(xhtmlElem, odfAttrs, baseStyle,
                           stylesStore=stylesStore)
        # "styleName" may be empty. For example, it may not be necessary to
        # generate a custom style for a "td", although we must generate, from
        # its attrs, a custom style for its inner-paragraph.
        if not styleName: return baseStyle
        return Style(styleName, self.getStyleFamily(xhtmlElem))

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class StylesManager:
    '''Reads the paragraph styles from styles.xml within an ODT file, and
       updates styles.xml with some predefined POD styles.'''

    podSpecificStyles = {
      'ParaKWN': Style('ParaKWN', 'paragraph'),
      # This style is common to bullet and number items. Behind the scenes,
      # there are 2 concrete ODT styles: podBulletItemKeepWithNext and
      # podNumberItemKeepWithNext. pod chooses the right one.
      'podItemKeepWithNext': Style('podItemKeepWithNext', 'paragraph'),
      # Default style for paragraphs within cells and lists
      'podCellContent': Style('podCellContent', 'paragraph'),
      'podHeaderCellContent': Style('podHeaderCellContent', 'paragraph'),
      'podBulletItem': Style('podBulletItem', 'paragraph'),
      'podNumberItem': Style('podNumberItem', 'paragraph'),
    }

    # Valid value types for some keys within style mappings
    mappingValueTypes = {'h*': int, 'table': TableProperties,
                         'ol': NumberedProperties, 'ul': BulletedProperties}

    def __init__(self, renderer):
        self.renderer = renderer
        self.stylesString = renderer.stylesXml
        # The collected styles, as a list of Style instances
        self.styles = None
        # The main page layout, as a PageLayout instance
        self.pageLayout = None
        # Global styles mapping
        self.stylesMapping = None
        self.stylesParser = StylesParser(StylesEnvironment(), self)
        self.stylesParser.parse(self.stylesString)
        # Now self.styles contains the styles.
        # Text styles from self.styles
        self.textStyles = self.styles.getStyles('text')
        # Paragraph styles from self.styles
        self.paragraphStyles = self.styles.getStyles('paragraph')
        # The custom styles generator
        self.stylesGenerator = StylesGenerator(self)
        # Dynamically-generated styles
        self.dynamicStyles = DynamicStyles()
        # Apply outline deltas, if specified
        if renderer.stylesOutlineDeltas:
            styles = self.styles
            for name, delta in renderer.stylesOutlineDeltas.items():
                if name in styles:
                    styles[name].outlineDelta = delta

    def checkStylesAdequation(self, htmlStyle, odtStyle):
        '''Checks that p_odtStyle may be used for style p_htmlStyle'''
        if htmlStyle in XHTML_PARA_TAGS and odtStyle in self.textStyles:
            raise PodError(P_ODT_TXT % (htmlStyle, odtStyle.displayName))
        if htmlStyle in XHTML_INNER_TAGS and odtStyle in self.paragraphStyles:
            raise PodError(TXT_ODT_P % (htmlStyle, odtStyle.displayName))

    def addStyleEntry(self, stylesMapping, key, value, cssAttrs):
        '''Adds, in dict p_stylesMapping (the output of m_checkStylesMapping
           below), a p_key:p_value entry.'''
        alreadyIn = key in stylesMapping
        if cssAttrs or alreadyIn:
            # I must create a complex structure for this mapping
            if not alreadyIn:
                stylesMapping[key] = [(cssAttrs, value)]
            else:
                val = stylesMapping[key]
                if not isinstance(val, list):
                    stylesMapping[key] = [(cssAttrs, value), (None, val)]
                else:
                    val.insert(0, (cssAttrs, value))
        else:
            stylesMapping[key] = value

    def checkStylesMapping(self, stylesMapping):
        '''Checks that the given p_stylesMapping is correct, and returns the
           internal representation of it.'''

        # p_stylesMapping is a dict.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # Every key can be:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # (1) | the name of a XHTML 'paragraph-like' tag (p, h1, h2...) or the
        #     | meta-name "para", representing "p", "div", "blockquote" or
        #     | "address";
        # (2) | the name of a XHTML 'text-like' tag (span, b, i, em...);
        # (3) | the name of a CSS class;
        # (4) | string 'h*';
        # (5) | 'table';
        # (6) | 'ol' or 'ul'.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # Every value must be:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # (a) | if the key is (1), (2) or (3), value must be the display name of
        #     | an ODT style;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # (b) | if the key is (4), value must be an integer indicating how to
        #     | map the outline level of outlined styles (ie, for mapping XHTML
        #     | tag "h1" to the OD style with outline-level=2, value must be
        #     | integer "1". In that case, h2 will be mapped to the ODT style
        #     | with outline-level=3, etc.). Note that this value can also be
        #     | negative;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # (c) | if key is "table", the value must be an instance of
        #     | appy.pod.styles_manager.c_TableProperties;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # (d) | if key is "ol", the value must be an instance of
        #     | appy.pod.styles_manager.c_NumberedProperties;
        #     | if key is "ul", the value must be an instance of
        #     | appy.pod.styles_manager.c_BulletedProperties.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # Some precisions now about about keys. If key is (1) or (2), parameters
        # can be given between square brackets. Every such parameter represents
        # a CSS attribute and its value, with 2 possible operators: = and !=.
        # For example, a key can be:
        #
        #                     p[text-align=center,color=blue]
        #
        # This feature allows to map XHTML tags having different CSS attributes
        # to different ODT styles. Note that special attribute "parent" can be
        # used and does not represent a CSS attribute but the parent tag. For
        # example, if you want to apply a specific style to a "p" tag, excepted
        # those within "td" tags, specify this key:
        #
        #                           p[parent!=td]
        #
        # For a parent, you can use meta-name "cell" that denotes any tag being
        # "th", "td" or "li". For example: p[parent=cell]
        # 
        # Special attribute "class" can also be used to check whether some CSS
        # class is defined in attribute "class", ie:
        #
        #                         div[class=MyClass]
        #
        # For this "class" attribute, you can use value "None", representing no
        # class at all. For example, the following key matches any "p" tag
        # having any defined CSS class:
        #
        #                           p[class!=None]
        #
        # The method returns a dict which is the internal representation of the
        # styles mapping.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # Every key can be:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # (I)   | the name of a XHTML tag, corresponding to (1), (2), (5) or (6)
        #       | whose potential parameters have been removed;
        # (II)  | the name of a CSS class (=(3));
        # (III) | string 'h*' (=(4)).
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # Every value can be:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # (i)   | a Style instance that was found from the specified ODT style
        #       | display name in p_stylesMapping, if key is (I) and if only one
        #       | non-parameterized XHTML tag was defined in p_stylesMapping;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # (ii)  | a list of the form [ (params, Style), (params, Style),...] if
        #       | key is (I) and if one or more parameterized (or not) XHTML
        #       | tags representing the same tag were found in p_stylesMapping.
        #       | "params", which can be None, is a dict whose pairs are of the
        #       | form (cssAttribute, cssValue);
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # (iii) | an integer value (=(b));
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # (iv)  | [x]Properties instance if cases (5) or (6).
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # ! Cheat ! Mapping a td class to its inner p
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # ODF requires a paragraph to be present within a table cell, which is
        # not the case in XHTML: a "td" tag can directly contain text, without
        # adding an intermediate "p" or "div" tag. Consequently, when Appy must
        # convert an XHTML code like "<td>Text</td>", it adds an inner
        # paragraph, in order to produce valid ODF code, just as if the input
        # code was <td><p>Text</p></td>. Imagine now the input code defines a
        # CSS class on the "td" tag:
        #
        #                 <td class="smallText">Text</td>
        #
        # Because named, cell-level styles can't be defined from the LibreOffice
        # UI, this class is useless for Appy. This is why Appy, in that case,
        # copies the class to the added inner paragraph, as if it was initially
        # coded as:
        #
        #       <td class="smallText"><p class="smallText">Text</p></td>
        #
        # Note that this cheat occurs only if no paragraph is defined within the
        # "td" tag in the input code. For example,
        #
        #                <td class="smalltext"><p>Text</p></td>
        #
        # will be converted as if it was
        #
        #                          <td><p>Text</p></td>
        #
        # Another example:
        #
        #         <td class="smalltext"><p class="para">Text</p></td>
        #
        # will be converted as if it was
        #
        #                     <td><p class="para">Text</p></td>
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        r = {}
        if not isinstance(stylesMapping, dictTypes):
            raise PodError(MAP_KO)
        for xhtmlStyleName, odtStyleName in stylesMapping.items():
            if not isinstance(xhtmlStyleName, str):
                raise PodError(KEY_STR_KO)
            # Separate CSS attributes if any
            cssAttrs = None
            if '[' in xhtmlStyleName:
                xhtmlStyleName, attrs = xhtmlStyleName.split('[')
                xhtmlStyleName = xhtmlStyleName.strip()
                attrs = attrs.strip()[:-1].split(',')
                cssAttrs = {}
                for attr in attrs:
                    name, value = attr.split('=')
                    # Operators = and != can be used
                    name = name.strip()
                    value = value.strip()
                    if name.endswith('!'):
                        name = name[:-1].strip()
                        value = '!' + value
                    cssAttrs[name] = value
            # Using CSS attrs is only allowed in the open source version
            if cssAttrs and utils.commercial: raise utils.CommercialError()
            # Continue checks
            if xhtmlStyleName in StylesManager.mappingValueTypes:
                # Using these keys is only granted to open source users
                if utils.commercial: raise utils.CommercialError()
                vType = StylesManager.mappingValueTypes[xhtmlStyleName]
                if not isinstance(odtStyleName, vType):
                    raise PodError(VAL_TYP_KO % (xhtmlStyleName,vType.__name__))
            else:
                if not isinstance(odtStyleName, str):
                    raise PodError(VAL_STR_KO % xhtmlStyleName)
                if not xhtmlStyleName or not odtStyleName:
                    raise PodError(VAL_EMPTY)
            if xhtmlStyleName in XHTML_UNSTYLABLE_TAGS:
                raise PodError(UNSTYL_TAG % (xhtmlStyleName,
                                             XHTML_UNSTYLABLE_TAGS))
            # Add the entry in the result
            if xhtmlStyleName not in StylesManager.mappingValueTypes:
                odtStyle = self.styles.getStyle(odtStyleName)
                if not odtStyle:
                    if odtStyleName in self.podSpecificStyles:
                        odtStyle = self.podSpecificStyles[odtStyleName]
                    else:
                        raise PodError(STYLE_N_F % odtStyleName)
                self.checkStylesAdequation(xhtmlStyleName, odtStyle)
                odtTarget = odtStyle
            else:
                # In this case (iii, iv), it is the outline level or a
                # [x]Properties instance.
                odtTarget = odtStyleName
            self.addStyleEntry(r, xhtmlStyleName, odtTarget, cssAttrs)
        return r

    def styleMatch(self, xhtmlElem, matchingAttrs):
        '''p_matchingAttrs is a dict of attributes corresponding to some style
           (or can be None). This method returns True if p_xhtmlElem has the
           the winning (name, value) pairs that match those in p_matchingAttrs.
           Note that ALL attrs in p_matchingAttrs must be present on
           p_xhtmlElem.'''
        # No p_matchingAttrs means: any p_xhtmlElem matches
        if not matchingAttrs: return True
        cssStyles = xhtmlElem.cssStyles
        for name, value in matchingAttrs.items():
            # Manage the potential "not" operator stored in the value
            if value.startswith('!'):
                negate = True
                value = value[1:]
            else:
                negate = False
            if name == 'parent':
                # Check if p_xhtmlElem has this parent element
                parent = xhtmlElem.parent
                if not parent:
                    match = False
                else:
                    # Manage special meta-name "cell"
                    if value == 'cell':
                        match = parent.elem in XHTML_CELL_TAGS
                    else:
                        match = parent.elem == value
            elif name == 'class':
                # Manage special value "None" representing "no class at all"
                if value == 'None':
                    match = xhtmlElem.noClass()
                else:
                    # Check if p_xhtmlElem has this CSS class
                    match = xhtmlElem.hasClass(value)
            else:
                # Check if p_xhtmlElem has this CSS attribute
                if not cssStyles:
                    match = False
                else:
                    cssValue = cssStyles.get(name)
                    match = cssValue and value == cssValue.value
            # Negate the match when appropriate
            if negate: match = not match
            # Return None if there is no match
            if not match: return
        # If we are here, all attributes match
        return True

    def getMatchingStyle(self, xhtmlElem, styles):
        '''p_styles is a value from a styles mapping as transformed by
           m_checkStylesMapping above. If it represents a list of styles
           (see case (ii) in m_checkStylesMapping), this method must return the
           relevant Style instance from this list, depending on CSS attributes
           found on p_xhtmlElem.'''
        if not isinstance(styles, list): return styles
        # Is there a style from p_styles matching p_xhtmlElem's characteristics?
        for matchingAttrs, style in styles:
            if self.styleMatch(xhtmlElem, matchingAttrs):
                return style

    def getStyleFromMapping(self, stylesMapping, xhtmlElem, elem=None,
                            checkMetaElems=True):
        '''If p_stylesMapping contains a style corresponding to p_xhtmlElem, it
           returns it. This method takes care of meta-elems like "para"
           representing several elements. This method is recursive: when called
           to get a style from a meta-element, it is done via p_elem.'''
        # The first time m_getStyleFromMapping is called, p_elem is None. It
        # means that the element itself has priority over its meta-element.
        elem = elem or xhtmlElem.elem
        styles = stylesMapping.get(elem)
        if styles:
            # Is there a matching style among "styles" ?
            r = self.getMatchingStyle(xhtmlElem, styles)
            if r or not checkMetaElems:
                return r
        # Check if a style exists for p_elem's meta-tag
        meta = XHTML_META_TAGS.get(elem)
        if meta:
            return self.getStyleFromMapping(stylesMapping, xhtmlElem,
                                            elem=meta, checkMetaElems=False)

    def getLoStyle(self, name):
        '''Gets the LibreOffice style (from self.styles) corresponding to some
           style p_name, if it exists.'''
        # Within LO styles, the underscore is replaced by its URL-encoded value
        name = name.replace('_', '_5f_')
        return self.styles.get(name)

    def findStyle(self, xhtmlElem, localStylesMapping, stylesStore=None):
        '''Finds the ODT style that must be applied to this p_xhtmlElem (as a
           xhtml2odt:HtmlElement object).'''

        # The global styles mapping is in p_self.stylesMapping; the local styles
        # mapping is in p_localStylesMapping.

        # Here are the places where we will search, ordered by priority (highest
        # first):
        # (1) local styles mapping (CSS style in "class" attr)
        # (2)         "            (HTML elem)
        # (3) global styles mapping (CSS style in "class" attr)
        # (4)          "            (HTML elem)
        # (5) ODT style that has the same name as CSS style in "class" attr
        # (6) Predefined pod-specific ODT style that has the same name as
        #     CSS style in "class" attr
        # (7) ODT style that has the same outline level as HTML elem
        # (8) a default Appy ODT style

        # After this step, we have (or not) a base ODT style. In a final step we
        # will analyse XHTML attributes (including CSS attributes within the
        # "style" attribute) to get more elements and possibly generate, via the
        # styles generator define hereabove, a custom style based on the base
        # ODT style.

        r = None
        elem = xhtmlElem.elem
        css = xhtmlElem.getClass(last=True)
        # (1)
        if css in localStylesMapping:
            r = localStylesMapping[css]
        # (2)
        if not r:
            r = self.getStyleFromMapping(localStylesMapping, xhtmlElem)
        # (3)
        if not r and css in self.stylesMapping:
            r = self.stylesMapping[css]
        # (4)
        if not r:
            r = self.getStyleFromMapping(self.stylesMapping, xhtmlElem)
        # (5)
        if not r and css:
            r = self.getLoStyle(css)
        # (6)
        if not r and css in self.podSpecificStyles:
            r = self.podSpecificStyles[css]
        # (7)
        if not r and elem in XHTML_HEADINGS:
            # Try to find a style with the correct outline level. Is there a
            # delta that must be taken into account ?
            outlineDelta = 0
            if 'h*' in localStylesMapping:
                outlineDelta += localStylesMapping['h*']
            elif 'h*' in self.stylesMapping:
                outlineDelta += self.stylesMapping['h*']
            outlineLevel = int(elem[1]) + outlineDelta
            # Normalize the outline level
            if outlineLevel < 1: outlineLevel = 1
            r = self.styles.getParagraphStyleAtLevel(outlineLevel)
        # (8)
        if r and elem in Properties.elems and not isinstance(r, Properties):
            r = None
        if not r and elem in DEFAULT_STYLES: r = DEFAULT_STYLES[elem]
        # Check styles adequation
        if r: self.checkStylesAdequation(elem, r)
        # Get or generate a custom style if there are specific CSS attributes
        return self.stylesGenerator.get(xhtmlElem, r, stylesStore)

    def setXhtmlParser(self, xhtmlParser):
        '''Store the p_xhtmlParser if a XHTML > ODT conversion is ongoing'''
        self.stylesGenerator.css2odf.xhtmlParser = xhtmlParser
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
