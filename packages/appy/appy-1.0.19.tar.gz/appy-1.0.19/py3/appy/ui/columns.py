'''Manage columns in a UI table'''

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
from appy.px import Px
from appy.utils import string as sutils
from appy.ui.layout import ColumnLayout

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
F_MISSING  = 'Field "%s", used in a column specifier, not found.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Col:
    '''Represents an individual column'''

    # Direct Col instances are not special
    special = False

    # Header, in a table containing search results
    pxHeader = Px('''
     <th>
      <div if="col.header" class="ghead">
       <span if="col.headerLabel != False"
             class="htitle" >::col.getHeaderText(_ctx_, field)</span>

       <div class="thead" var="field, filterPx=field.getFilterField()">

        <!-- Filter -->
        <x if="filterPx">:filterPx</x>

        <!-- Toggle descriptions' visibility -->
        <x if="ui.Title.showToggleSub(class_, col.field, tool, \
                  from_=mode.refField)">:ui.Title.pxToggleSub</x>

        <!-- Sort icons -->
        <div if="field.isSortable() and mode.batch.total &gt; 1" class="iflex1">
         <img if="mode.sortKey != field.name or mode.sortOrder == 'desc'"
              onclick=":'askBunchSorted(%s, %s, %s)' % \
                         (q(mode.hook), q(field.name), q('asc'))"
              src=":svg('asc')" class="clickable iconST"/>
         <img if="mode.sortKey != field.name or mode.sortOrder == 'asc'"
              onclick=":'askBunchSorted(%s, %s, %s)' % \
                        (q(mode.hook), q(field.name), q('desc'))"
              src=":svg('asc')" class="clickable iconST"
              style="transform:rotate(180deg)"/>
        </div>
       </div>
      </div>
     </th>''')

    # Header, in a table containing Ref objects
    pxHeaderRef = Px('''
     <th>
      <div if="col.header" class="ghead">
       <span if="col.headerLabel != False"
             class="htitle">::col.getHeaderText(_ctx_, refField)</span>

       <div class="thead">

        <!-- Sort icons -->
        <div if="not selector" class="iflex1">:field.pxSortIcons</div>

        <!-- Toggle descriptions' visibility -->
        <x if="ui.Title.showToggleSub(tiedClass, refField,
                tool, from_=field)">:ui.Title.pxToggleSub</x>
       </div>
      </div>
     </th>''')

    def getHeaderText(self, c, field):
        '''Returns the text to dump in p_self being a header cell'''
        # Get the translated text for the column label, or, if not specified,
        # the field label.
        r = c._(c.col.headerLabel or field.labelId)
        if not r.startswith('<'):
            # v_r is probably a "abbr" or "acronym" tag. That case, do not try
            # to shorten it if too long.
            r = Px.truncateText(r)
        return r

    # A non-specific column renders a field value
    def getCell(c):
        '''Renders p_c.field.pxResult, wrapped in a td with potential styles
           applied.'''
        style = c.col.getCssFor(c.o)
        attr = f' style="{style}"' if style else ''
        return f'<td{attr}>{c.field.pxResult(c)}</td>'

    pxCell = Px(getCell)

    # Cell content, in a table containing Ref objects
    pxCellRef = Px('''<td>:field.pxTied</td>''')

    # Attributes storing CSS properties or rules
    cssAttributes = ('th', 'ths', 'td', 'tds')

    def __init__(self, columnLayout, th=None, td=None, ths=None, tds=None,
                 otd=None, headerLabel=None, phLabel='search_button'):
        '''Initialise p_self from a p_columnLayout. Additional p_th(s) and
           p_td(s)-specific CSS properties may be defined.'''
        layout = ColumnLayout(columnLayout)

        # Base attributes are the following.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # name   | For most columns ("=non-special ones, see below), it stores
        #        | the name of the field whose values are rendered in the
        #        | colummn. Else, it stores a predefined name, prefixed with
        #        | an underscore.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # width  | The column width, in any format being compliant with the
        #        | homonym CSS attribute.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # align  | Text alignment within every column cell, in any format being
        #        | compliant with the homonym CSS attribute.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # header | If True, indicates that no name must appear in the column
        #        | header.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        name, self.width, self.align, self.header = layout.get()
        # If p_self corresponds to a field, the Field instance will be stored
        # here by m_setField. Else, p_self.field will store p_self.name.
        self.field = self.name = name
        # p_th may contain CSS properties, as a string: they will be applied to
        # the header cell of this column. Here is an example:
        #
        #                 "font-size:110%;font-weight:bold"
        #
        self.th = th
        # If you want to apply CSS properties to the th sub-elements, p_ths may
        # specify one (as a string) or several (as a tuple or list) specific
        # *s*elector and sub-rules. For example, the following rule will apply a
        # grey background to any div element being within the th.
        #
        #                "> div { background-color:grey }"
        #
        self.ths = ths
        # Similarly, p_td and p_tds may contain CSS properties that will be
        # applied to any non-header cell in this column.
        self.td = td
        self.tds = tds
        # While p_td and p_tds apply to all content cells of a list of objects,
        # p_otd will apply on an individual cell. p_otd (*o*bject *td*) can
        # hold a method that will be called on the object for which a row is
        # currently being computed. The method must CSS properties, as a string
        # whose format is similar to p_th or p_td, as explained hereabove.
        self.otd = otd
        # For field-related columns, the field's label is used by default for
        # the text to dump in the column header. You may specify an alternate
        # i18n label in p_headerLabel. If you want no label at all, set
        # p_headerLabel to False.
        self.headerLabel = headerLabel
        # If input text fields are present within the header cell, indicate here
        # the i18n to use for producing a placeholder. Set None to hide such
        # placeholders.
        self.phLabel = phLabel

    def init(self, o, oclass):
        '''Lazy initialisation: initialises p_self.field. Return None if a
           problem occurred.'''
        self.field = field = oclass.fields.get(self.name)
        if not field:
            o.log(F_MISSING % self.name, type='warning')
            return
        return True

    def getCss(self):
        '''Returns lists of CSS attributes and/or rules corresponding to
           p_self.'''
        # The method returns a dict. Every entry value is a string containing
        # CSS properties or rules.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # At key:  | we have:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "common" | CSS properties being common to any cell ;
        # "th"     | CSS properties being specific to the header cell ;
        # "ths"    | CSS rules being specific to header cell sub-elements ;
        # "td"     | CSS properties being specific to all content cells ;
        # "tds"    | CSS rules being specific to content cell sub-elements.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        r = {}
        # Common to any cell: alignment
        common = [f'text-align:{self.align}']
        # Common to any cell: width
        if self.width:
            common.append(f'width:{self.width}')
        if common: r['common'] = ';'.join(common)
        # Add any other not-empty key/value
        for name in self.cssAttributes:
            value = getattr(self, name)
            if value:
                r[name] = value
        return r

    def getCssFor(self, o):
        '''Returns specific CSS properties tied to this p_o(bject), if any.'''
        return self.otd(o) or '' if self.otd else ''

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Number(Col):
    '''Specific column containing rows' numbers and related controls'''

    special = True

    def init(self, o, oclass):
        '''Nothing more must be done for this type of column'''
        return True

    # No header for a Number column
    pxHeaderRef = Px('''<th></th>''')

    # Cel content, in a table containing Ref objects
    pxCellRef = Px('''
     <td><x if="objectIndex is not None">:ifield.pxNumber</x></td>''')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Checkbox(Col):
    '''Specific column containing rows' checkboxes'''

    special = True

    # Header, in a table containing search results
    pxHeader = Px('''
     <th class=":mode.cbClass">
      <div if="col.header" class="ghead">
       <img src=":svg('checkAll')" class="iconSEL"
            onclick=":'toggleAllCbs(%s)' % q(mode.checkboxesId)"
            title=":_('check_uncheck')"/>
      </div>
     </th>''')

    # Header, in a table containing Ref objects
    pxHeaderRef = Px('''
     <th class=":selector.cbClass if selector else ''">
      <x if="col.header">
       <img src=":svg('checkAll')" class="iconSEL"
            onclick=":'toggleAllCbs(%s)' % q(hook)"
            title=":_('check_uncheck')"/>
      </x>
     </th>''')

    # Cell content, in a table containing search results
    pxCell = Px('''
     <td class=":mode.cbClass">
      <input type="checkbox" var="checked=mode.cbChecked"
             name=":mode.checkboxesId" id=":cbId" value=":id"
             onclick="toggleCb(this)" checked=":checked"/>
     </td>''')

    # Cel content, in a table containing Ref objects
    pxCellRef = Px('''
     <td class=":selector.cbClass if selector else ''">
      <input if="mayView" type="checkbox" name=":hook" id=":cbId"
             var2="checked=cbChecked|False" checked=":checked"
             value=":id" onclick="toggleCb(this)"/>
     </td>''')

    def init(self, o, oclass):
        '''Nothing more must be done for this type of column'''
        return True

# Make child Col classes available on the base class itself
Col.Number = Number
Col.Checkbox = Checkbox

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Columns(list):
    '''Represents a list of columns in a UI table, and all its related
       characteristics.'''

    # Standard columns
    number   = Number('_number*15px^')
    checkbox = Checkbox('_checkbox*10px|')

    # The CSS selector template representing a given column
    colSelector = '.%s>tbody>tr>%s:nth-child(%d)'

    @classmethod
    def getColClass(class_, layout):
        '''Gets the Col (sub)class corresponding to this column p_name'''
        if layout.startswith('_'):
            i = layouts.find('*')
            name = layouts[1:] if i == -1 else layouts[1:i]
            r = eval(name.capitalize())
        else:
            r = Col
        return r

    @classmethod
    def get(class_, o, oclass, infos, addNB=False, addCB=False):
        '''Creates, from a list of column p_infos, a Columns object, required
           for displaying columns of field values for p_oclass's instances.
        '''
        # p_infos is a list of column layouts or Cell instances: each one
        # specifies how a field value must be shown. Two not-field-related infos
        # can be specified among p_infos, as column layouts, with these names:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "_number"   | if the listed objects must be numbered, this string
        #             | represents the column containing that number ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "_checkbox" | if checkboxes must be shown for the listed objects, this
        #             | string represents the column containing the checkboxes.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # If "_number" and "_checkbox" are not among p_infos but are required
        # (by p_addNB and p_addCB), they are added to the result. Specifying
        # them within p_infos allows to give them a precise position among all
        # columns. When automatically added, they will appear before any other
        # column (which is desirable in most cases).
        r = Columns()
        nbFound = cbFound = False
        for info in infos:
            if isinstance(info, Col):
                # We have already have a Col instance
                col = info
            else:
                # Get a Col instance from a column layout
                col = class_.getColClass(info)(info)
            # Remember when a special column has been already been met
            nbFound = nbFound or isinstance(col, Number)
            cbFound = cbFound or isinstance(col, Checkbox)
            # Lazy-init the Col instance (set the field)
            ok = col.init(o, oclass)
            if not ok: continue
            r.append(col)
        # Add special columns if required and not present
        if addCB and not cbFound:
            r.insert(0, class_.checkbox)
        if addNB and not nbFound:
            r.insert(0, class_.number)
        return r

    def __init__(self):
        '''Columns constructor'''
        super().__init__()
        # The name of the dynamically-created CSS class that will serve as hook
        # for defining all CSS properties corresponding to p_self's columns.
        self.name = sutils.randomName()

    def addSubCss(self, r, type, base, sub):
        '''Add, in p_r, CSS rules of this type ("th" or "td"), built from this
           p_base rule + s_sub-part(s).'''
        # p_sub may contain a single sub-rule or several ones
        sub = (sub,) if isinstance(sub, str) else sub
        for rule in sub:
            r.append(base % (type, f' {rule}'))

    def getCss(self, hasHeader, rowAlign, width='100%'):
        '''Returns a set of CSS rules representing characteristics as defined
           by p_self's columns, plus some table-wide CSS properties.'''
        # The name of the CSS class to apply to the whole list
        name = self.name
        # Start with global CSS rules: table width
        r = [f'.{name} {{ width:{width or "auto"} }}']
        # Rows' vertical alignment. Take care of not specifying row alignment
        # for the table header, when present.
        part = ':not(:first-child)' if hasHeader else ''
        r.append(f'.{name}>tbody>tr{part} {{ vertical-align:{rowAlign} }}')
        # Add column-related CSS rules
        selector = self.colSelector
        for i in range(len(self)):
            cellCss = self[i].getCss()
            if not cellCss: continue
            # The common part of CSS rules to generate
            add = r.append
            rule = f'.{self.name}>tbody>tr>%s:nth-child({i+1})%s'
            if 'common' in cellCss:
                add(rule % ('', f' {{ {cellCss["common"]} }}'))
            if 'th' in cellCss:
                add(rule % ('th', f' {{ {cellCss["th"]} }}'))
            if 'ths' in cellCss:
                self.addSubCss(r, 'th', rule, cellCss['ths'])
            if 'td' in cellCss:
                add(rule % ('td', f' {{ {cellCss["td"]} }}'))
            if 'tds' in cellCss:
                self.addSubCss(r, 'td', rule, cellCss['tds'])
        return '\n'.join(r)

    def getFiltered(self):
        '''Returns info about every column for which a filter must be shown'''
        r = [] # ~[(filterField, px)]~
        for col in self:
            field = col.field
            if isinstance(field, str): continue
            filterField, px = field.getFilterField()
            if px:
                r.append((filterField, px))
        return r
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
