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
from pathlib import Path

from appy.xml import Environment, Parser, xmlPrologue

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PROPS_KO  = 'Variable "%s" does not contain a GraphicProperties object but is' \
            ' mentioned as is in a pod graphic.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Types of ranges that can be defined. In the following examples, "sh" stands
# for "sheet".

FOUR_PARTS = 0 # 2 column headers and 2 single-column ranges
               # Example: Sh.B2:Sh.B2 Sh.B3:Sh.B7 Sh.C2:Sh.C2 Sh.C3:Sh.C7

COMPLETE   = 1 # The complete range, encompassing header + values, both columns
               # Example: Sh.B2:Sh.C7

COL_ONE    = 2 # The first column, values only (no header)
               # Example: Sh.B3:Sh.B7

COL_TWO    = 3 # The second column, values only (no header)
               # Example: Sh.C3:Sh.C7

HEAD_TWO   = 4 # The second column header
               # Example: Sh.C2:Sh.C2

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class GraphicProperties:
    '''Defines properties to apply to an ODS graphic'''

    def __init__(self, stroke='none', strokeColor='#b3b3b3', fill='solid',
                 fillColor='#004586', fontSize='10pt'):
        self.stroke = stroke # Possible values: 'none', 'solid', ...
        self.strokeColor = strokeColor
        self.fill = fill # Possible values: 'none', 'solid', ...
        self.fillColor = fillColor
        self.fontSize = fontSize

    def getGraphicProperties(self):
        '''Returns ODS graphic properties'''
        return f'<style:graphic-properties draw:stroke="{self.stroke}" ' \
               f'draw:stroke-color="{self.strokeColor}" ' \
               f'draw:fill="{self.fill}" draw:fill-color="{self.fillColor}" />'

    def getChartProperties(self):
        '''Returns ODS graphic properties'''
        return '<style:chart-properties chart:link-data-style-to-source=' \
               '"true"/>'

    def getTextProperties(self):
        '''Returns ODS text properties'''
        size = self.fontSize
        return f'<style:text-properties fo:font-size="{size}" ' \
               f'style:font-size-asian="{size}" ' \
               f'style:font-size-complex="{size}"/>'

    def getStyle(self, name='ch1', numberName='N0'):
        '''Generates the ODS style that corresponds to there graphic
           properties.'''
        # p_name is the name of the ODS style to dump. p_numberName is the name
        # of the number style to refer.
        if numberName:
            numS = f' style:data-style-name="{numberName}"'
        else:
            numS = ''
        return f'<style:style style:name="{name}" style:family="chart"{numS}>' \
               f'{self.getChartProperties()}{self.getGraphicProperties()}' \
               f'{self.getTextProperties()}</style:style>'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Graphic:
    '''Represents a Pod-controlled graphic within an ODS pod template'''

    # Make class GraphicProperties available here
    Properties = GraphicProperties

    @classmethod
    def get(class_, tag, attrs, env):
        '''Returns a Graphic object, if this p_tag, encountered in the currently
           parsed content.xml, represents a POD graphic, ie, a graphic whose
           range of cells is dynamic and depends on the result of a pod "for"
           statement.'''
        if tag != 'draw:frame' or 'draw:name' not in attrs: return
        name = attrs['draw:name']
        # A POD-compliant graphic has a name of the form:
        #
        #            <rangeStart>-<rangeEnd>-<podVar>[-<propsVar>]
        #
        # Part "propsVar" is optional
        return Graphic(name, env) if 2 <= name.count('-') <= 3 else None

    def __init__(self, spec, env):
        '''Create a Graphic object based on this p_spec (see m_get)'''
        # p_spec (see m_get hereabove) is made of the following elements:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # start | The cell corresponding to the abstract range start (ie, "B2")
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # end   | The cell corresponding to the abstract range end (ie, "C3")
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # var   | The name of the pod variable that will be used to expand the
        #       | abstract range into a concrete range of values, as produced by
        #       | a pod "for" statement.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # props | [optional] The name of the pod variable storing a
        #       | GraphicProperties object.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # Values in "start" and "end" may be prefixed by the sheet name (ie,
        # "Sheet1.B2", "Sheet1.C3").
        #
        # This range is an abstract, Pod-based range definition representing
        # graphic's data, that will be converted to a LO-compliant range by the
        # renderer's "finalize" method.        
        #
        parts = spec.strip().split('-')
        if len(parts) == 3:
            start, end, self.var = parts
            self.props = None
        else:
            start, end, self.var, self.props = parts
        #
        # Prefix p_self.start and p_self.end with the current sheet name, if not
        # already done.
        tableName = None
        if '.' not in start:
            # Implicitly, the range is to be found in the current sheet
            # (=the current table)
            sheet = env.getTable().name
            start = f'{sheet}.{start}'
        if '.' not in end:
            end = f'{sheet or env.getTable().name}.{end}'
        self.start = start
        self.end = end
        # Get p_self.start and p_self.end components
        self.sheet, self.startCol, self.startRow = self.getCellParts(self.start)
        self.sheet, self.endCol, self.endRow = self.getCellParts(self.end)
        # The following attribute will store the actual values corresponding to
        # this v_graphic.
        self.values = None

    def getCellParts(self, name):
        '''Returns a 3-tuple containing the (s_sheet, s_col, i_row) parts for
           the cell having this p_name.'''
        # p_name may contain the sheet name
        if '.' in name:
            sheet, name = name.split('.')
            sheet = f'{sheet}.'
        else:
            sheet = ''
        # Extract, in v_col, the column letter(s) and, in v_row, the row number
        col = ''
        row = ''
        for char in name:
            if char.isdigit():
                row = f'{row}{char}'
            else:
                col = f'{col}{char}'
        return sheet, col, int(row)

    def getPodRange(self, prefix='appyRange.'):
        '''Gets p_self's range, as a short string, with this p_prefix'''
        r = f'{self.start}:{self.end}:{self.var}'
        return f'{prefix}{r}' if prefix else r

    def getLoRange(self, rangeType):
        '''Returns the LO range for p_self, based on these expanded
           p_self.values.'''
        # Prerequisite: p_self.value must have been computed
        #
        # Build the various required range elements
        sheet = self.sheet
        startCol = f'{sheet}{self.startCol}'
        endCol = f'{sheet}{self.endCol}'
        startRow = self.startRow
        endRow = self.endRow + len(self.values) - 1 # = the actual end row,
                                                    # based on the number of
                                                    # actual p_self.values
        if rangeType == FOUR_PARTS:
            # 4 values are expected: 2 headers and 2 single-column ranges
            head1 = f'{self.start}:{self.start}'
            vals1 = f'{startCol}{startRow+1}:{startCol}{endRow}'
            head2 = f'{endCol}{startRow}:{endCol}{startRow}'
            vals2 = f'{endCol}{startRow+1}:{endCol}{endRow}'
            r = f'{head1} {vals1} {head2} {vals2}'
        elif rangeType == COMPLETE:
            # 2 values are expected: the start and end of the complete range,
            # encompassing all columns and all rows.
            end = f'{endCol}{endRow}'
            r = f'{self.start}:{end}'
        elif rangeType == COL_ONE:
            # Values of the first column only
            r = f'{startCol}{startRow+1}:{startCol}{endRow}'
        elif rangeType == COL_TWO:
            # Values of the second column only
            r = f'{endCol}{startRow+1}:{endCol}{endRow}'
        elif rangeType == HEAD_TWO:
            # The second column header
            r = f'{endCol}{startRow}:{endCol}{startRow}'
        return r

    def resolveProps(self, context):
        '''Converts p_self.props, being the name of a pod variable potentially
           containing a GraphicProperties object, into this object.'''
        props = self.props
        if props is None:
            # Use a defaut GraphicProperties object
            self.props = GraphicProperties()
        else:
            self.props = context.get(props)
            if self.props is None:
                # Take a default one
                self.props = GraphicProperties()
            elif not isinstance(self.props, GraphicProperties):
                raise Exception(PROPS_KO % props)

    def __repr__(self):
        '''p_self as a short string'''
        return f'‹Graphic · Pod range {self.getPodRange(None)}›'

    def register(self, env, attrs):
        '''Registers a new pod-controlled graphic that was encountered in a
           draw:frame tag.'''
        # A draw:frame > draw:object sub-tag has just been encountered, having
        # these p_attrs: it corresponds to the Appy-controlled graphic already
        # stored in p_env.currentOdsGraphic.
        #
        # Add the graphic's abstract range in the appropriate tag attribute: it
        # will then be "resolved", by the renderer's "finalize" method, to a
        # concrete LO range.
        attrs._attrs['draw:notify-on-update-of-ranges'] = self.getPodRange()
        # Add an entry in p_self.odsGraphics
        graphics = env.odsGraphics
        if graphics is None:
            graphics = env.odsGraphics = {}
        graphics[attrs['xlink:href']] = self

    def patchContent(self, contentXml):
        '''Patches p_contentXml with a range based on the actual
           p_self.values.'''
        # Get the LO range from p_self.values
        loRange = self.getLoRange(FOUR_PARTS)
        # Replace the POD range with the LO range in p_contextXml
        podRange = self.getPodRange()
        return contentXml.replace(podRange, loRange)

    @classmethod
    def patch(class_, renderer, contentXml):
        '''Called by the renderer's "finalize" method, this method patches
           p_contentXml and graphics-specific sub-files, with info about the
           resolved data ranges.'''
        env = renderer.contentParser.env
        graphics = env.odsGraphics
        if not graphics: return contentXml
        # Browse every encountered pod-controlled graphic
        context = env.context
        for path, graphic in graphics.items():
            # Get the actual values corresponding to this v_graphic
            graphic.values = context[graphic.var]
            # Get a GraphicProperties object in v_graphic.props
            graphic.resolveProps(context)
            # Patch p_contentXml
            contentXml = graphic.patchContent(contentXml)
            # Patch the graphic-specific sub-content.xml
            fileName = Path(renderer.unzipFolder) / path / 'content.xml'
            with open(fileName) as f:
                gContent = f.read()
            gContent = GraphicParser(graphic, caller=renderer).parse(gContent)
            with open(fileName, 'w') as f:
                f.write(f'{xmlPrologue}{gContent}')
        return contentXml

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class GraphicEnvironment(Environment):
    '''Environment for the Graphic parser'''

    def __init__(self):
        # Call the base constructor
        super().__init__()
        # The chart type
        self.chartClass = None
        # Are we parsing the tag representing the x-axis ?
        self.xAxis = False
        # The last encountered style
        self.lastStyle = None
        # The name of the series style that will be generated
        self.seriesStyle = None

    def getNextStyle(self):
        '''Gets the next style, logically following p_self.lastStyle'''
        last = self.lastStyle
        if last:
            prefix = ''
            number = ''
            for char in last:
                if char.isdigit():
                    number += char
                else:
                    prefix += char
            number = number or '1'
            r = f'{prefix}{int(number)+1}'
        else:
            r = 'ch1'
        return r

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class GraphicParser(Parser):
    '''Parses a graphic-specific content.xml file within an ODS file and patches
       it with Pod-based graphic data.'''

    # The template "series" tag
    series = '<chart:series chart:style-name="%s" chart:values-cell-range-' \
             'address="%s" chart:label-cell-address="%s" chart:class="%s">' \
             '<chart:data-point chart:repeated="%s"/></chart:series>'

    # The string to use as hook for dumping the series style
    styleHook = '_s_t_y_l_e_'

    def __init__(self, graphic, caller=None):
        # Define a default environment if p_env is None
        env = GraphicEnvironment()
        # Call the base constructor
        super().__init__(env, caller)
        # The tied Graphic object
        self.graphic = graphic

    def startDocument(self):
        '''Initialise the result'''
        super().startDocument()
        self.r = []

    def endDocument(self):
        '''Concatenate all elements into a single string'''
        self.r = ''.join(self.r)
        # Dump the series style
        props = self.graphic.props
        style = props.getStyle(name=self.env.seriesStyle)
        self.r = self.r.replace(self.styleHook, style)

    def addPlotAreaAttributes(self, attrs):
        '''Add, in p_attrs, p_self.graphic-specific attributes'''
        d = attrs._attrs
        d['table:cell-range-address'] = self.graphic.getLoRange(COMPLETE)
        d['chart:data-source-has-labels'] = 'both'

    def addXAxisAttributes(self, attrs):
        '''Add, in p_attrs, specific x-axis attributes'''
        attrs._attrs['chartooo:axis-type'] = 'text'

    def startElement(self, name, attrs):
        '''Called when a start tag having this p_name is encountered'''
        env = self.env
        # Remember the name of the last encountered style
        if name == 'style:style':
            styleName = attrs.get('style:name')
            if styleName:
                env.lastStyle = styleName
        # Reify the start tag and its attributes
        r = f'<{name}'
        if attrs:
            if name == 'chart:chart':
                # Remember the type of chart
                env.chartClass = attrs['chart:class']
            elif name == 'chart:plot-area':
                # Add specific attributes
                self.addPlotAreaAttributes(attrs)
            elif name == 'chart:axis' and attrs.get('chart:dimension') == "x":
                # Add specific attributes
                self.addXAxisAttributes(attrs)
                self.env.xAxis = True
            # Dump attributes as a string
            attrs = [f'{name}="{value}"' for name, value in attrs.items()]
            r = f'{r} {" ".join(attrs)}'
        self.r.append(f'{r}>')

    def endElement(self, name):
        '''Called when an end tag having this p_name is encountered'''
        env = self.env
        # Patch the x-axis when relevant
        isAxis = name == 'chart:axis'
        isX = env.xAxis
        if isAxis and isX:
            # Add a sub-tag
            rangeX = self.graphic.getLoRange(COL_ONE)
            sub = f'<chart:categories table:cell-range-address="{rangeX}"/>'
            self.r.append(sub)
            env.xAxis = False
        # Add a hook for dumping, afterwards, the series style
        if name == 'office:automatic-styles':
            self.r.append(self.styleHook)
        # Reify the end tag
        self.r.append(f'</{name}>')
        if isAxis and not isX:
            # After both axis, add a series
            graphic = self.graphic
            rangeTwo = graphic.getLoRange(COL_TWO)
            headTwo = graphic.getLoRange(HEAD_TWO)
            count = len(graphic.values)
            style = env.seriesStyle = env.getNextStyle()
            series = self.series % (style, rangeTwo, headTwo, env.chartClass,
                                    count)
            self.r.append(series)

    def characters(self, content):
        '''Add the encountered p_content to the result'''
        self.r.append(content)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
