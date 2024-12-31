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
# This module manages the totals that can be computed from lists of objects
# (List/Dict fields, Search results, etc)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from appy.px import Px
from appy.model.utils import Object as O

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Total:
    '''Represents the computation of a specific total that will be aggregated
       from a series of cells within a list of objects.'''

    def __init__(self, name, field, initValue):
        # A name for the total. If the total represents a computation on a given
        # field, p_name is the name of the field and p_field is this field.
        # Else, p_field is ignored.
        self.name = name
        # In the case of an inner field, p_field.name is prefixed with the main
        # field name.
        self.field = field
        # The value to compute requires an initial value, that will also
        # indicate its type: 0, 0.0, '', [], ...
        self.value = initValue
        # Cell-specific style, expressed as a string containing a a semi-colon-
        # separated list of CSS properties. It can be defined via the developer
        # method laid in Totals.onCell, when parameter "last" is True (to avoid
        # defining it several times).
        self.style = None

    def __repr__(self):
        return f'‹Total {self.name}={str(self.value)}›'

    def getStyled(self, tag=None):
        '''If p_tag is passed ("th" or "td"), return the complete table cell
           containing p_self.value, with a potential p_self.style applied. If
           p_tag is None, it only returns the style attribute corresponding to
           p_self.style.'''
        style = f' style="{self.style}"' if self.style else ''
        if tag is None: return style
        val = self.value
        val = '-' if val is None else str(val)
        return f'<{tag}{style}>{val}</{tag}>'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Totals:
    '''If you want to add column or rows representing totals computed from lists
       of objects (List/Dict rows, Search results), specify it via Totals
       objects (see doc on the using class).'''

    # For Search results, only totals as rows below the other rows are allowed.
    # For List/Dict fields, totals as additional rows and/or columns can be
    # added.

    # Possible names for iterator variables representing Running* objects
    iterVars = ('totals', 'totalsC')

    def __init__(self, id, label, fields, labelPlace, onCell, initValue=0.0,
                 css='total'):
        # p_id must hold a short name or acronym and must be unique within all
        # Totals objects defined on the same container.
        self.id = id
        # p_label is a i18n label that will be used to produce a longer name
        # that will be shown at the start of the total row or as header for a
        # column.
        self.label = label
        # p_fields is a list or tuple of field names for which totals must be
        # computed. When computing totals from an outer field, these fields
        # must be a sub-set from this fields' inner fields. The name of every
        # inner field must be of the form
        #
        #             <outer field name>*<inner field name>
        #
        # , as in this example:
        #
        #                        "expenses*amount"
        #
        # When used for total rows, there will be one column being filled per
        # specified field. For shown fields that do not belong to p_self.fields,
        # cells in the total row will be left empty.
        #
        # When used for total columns, the computation corresponding to a column
        # total will be based on field values from the current row, provided
        # the corresponding fields are mentioned p_self.fields. For any field
        # shown in the row that would not be mentioned in p_self.fields, its
        # value will be ignored while computing the total.
        self.fields = fields
        # [rows only] Within the row that will display totals for these
        # p_fields, choose one unused column, where to put p_label. This
        # p_labelPlace must be the name of such a field for which no total will
        # be produced. For a dict field, the first column can be referred by
        # special place named "key". When p_self represents a column,
        # p_labelPlace is ignored.
        self.labelPlace = labelPlace
        # p_onCell stores a method that will be called every time a cell
        # corresponding to a field listed in p_self.fields is walked in the
        # list of objects. When used by a List/Dict field, this method must be
        # defined on the object where the List/Dict field is defined; when used
        # by a Search, this method must be defined on the class whose objects
        # are the search results.
        #
        # p_onCell will be called with these args:
        # [* row  ]  [List/Dict only] The current "row", as an Object instance.
        #            For a Search, it is useless: the Appy object is already
        #            available via your method's p_self's attribute.
        # * value    The value of the current field on this object or row/col.
        #            WARNING: when displaying a diff value in the object's
        #            history, it is possible that this value be a diff (as a
        #            chunk of XHML code in a string) and not a value that
        #            conforms to your field. Take this into account if you
        #            enable history changes.
        # * total    The Total instance (see above) corresponding to the current
        #            total.
        # * last     A boolean that is True if we are walking the last row or
        #            column.
        self.onCell = onCell
        # "initValue" is the initial value given to created Total instances
        self.initValue = initValue
        # [rows only] The name of the CSS class that will bbe applied to the
        # "tr" tag corresponding to this Totals instance.
        self.css = css

    @classmethod
    def init(class_, container, iterator, columns, containerTotals, rows=True):
        '''Create a Running* object containing Total objects'''
        concrete = RunningRows if rows else RunningCols
        return concrete(container, iterator, columns, containerTotals)

    @classmethod
    def updateAll(class_, field, c):
        '''Called before rendering a field value, this method updates all totals
           being currently computed.'''
        for name in class_.iterVars:
            # Get a Running* object
            running = c[name]
            if running is None or not isinstance(running, RunningRows):
                continue
            # Get the currently looped object
            looped = c[running.iterator]
            running.update(c.o, looped, field.name, c.rawValue, c.loop)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class RunningRows(dict):
    '''Represents a bunch of Total objects being currently computed, for totals
       shown in rows situated below the other table rows.'''

    # Every key is the ID of a Totals instance. Every value is an object storing
    # one attribute per field whose total must be computed (Totals.fields). So,
    # for each such field, this object stores O.<fieldName> = <Total instance>.

    def __init__(self, container, iterator, columns, containerTotals):
        # The container element from which totals can be computed: a List field,
        # a Search instance,...
        self.container = container
        # The name of the iterator variable used to loop over objects for which
        # totals are being computed.
        self.iterator = iterator
        # Names of all shown columns in the list of objects. This will be used
        # at the end of the process, for rendering total rows.
        self.columns = columns
        # The Totals objects defined on the p_container
        self.containerTotals = containerTotals
        # Initialise the dict
        self.init()

    def init(self):
        '''Initialises the dict'''
        for totals in self.containerTotals:
            subTotals = O()
            for name in totals.fields:
                tot = Total(name, self.container.getField(name),
                            totals.initValue)
                setattr(subTotals, name, tot)
            self[totals.id] = subTotals

    def getTotalFor(self, totalsO, name):
        '''Returns, within p_self, the Total object corresponding to the Totals
           object in p_totalsO.'''
        return getattr(self[totalsO.id], name, None)

    def update(self, o, looped, name, value, loop):
        '''Every time a cell is encountered while rendering a given field value
           within a table or list of objects for which totals must be computed,
           this method is called, if required, to update p_self's running
           totals.'''
        # In the case of an outer field, the currently walked object, p_looped,
        # is an inner row within this field on p_o. In any other case,
        # o == looped.
        #
        # Browse Totals objects
        for totalsO in self.containerTotals:
            # Are there totals to update ?
            total = self.getTotalFor(totalsO, name)
            if total:
                last = loop[self.iterator].last
                if o == looped:
                    totalsO.onCell(o, value, total, last)
                else:
                    totalsO.onCell(o, looped, value, total, last)

    def getCellFor(self, tot, totalsO, col, _):
        '''Generates, as a complete "td" tag, the cell corresponding to this
           p_col(umn) within this total p_row (=Totals object).'''
        # This cell may contain :
        # (a) the rows label,
        # (b) a total or
        # (c) an empty string, if the p_col(umn) contains no summable info.
        #
        # Extract the field name from p_col
        if isinstance(col, tuple):
            # The field corresponding to this column may be None if it is not
            # currently showable. In that case, do not dump any cell at all.
            field = col[1]
            if field is None: return ''
            name = field.name
        elif isinstance(col, str):
            name = col
        elif isinstance(col.field, str):
            name = col.field
        else:
            name = col.field.name
        # This field may be the hook for placing the total label
        if name == totalsO.labelPlace:
            # Force this label to be left-aligned
            r = f'<td style="text-align:left">{_(totalsO.label)}</td>'
        else:
            # Try to get a Total object for this field
            total = tot[name]
            r = total.getStyled('td') if total else '<td></td>'
        return r

    # Display total rows at the end of a list of objects
    px = Px('''
     <tr for="totalsO in totals.containerTotals" class=":totalsO.css"
         var2="tot=totals[totalsO.id]">
      <x for="col in totals.columns">::totals.getCellFor(tot,totalsO,col,_)</x>
     </tr>''')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class RunningCols(RunningRows):
    '''Represents a bunch of Total objects being currently computed, for totals
       shown in columns besides the other table columns, for the current row.'''

    # Every key is the ID of a Totals object. Every value is a Total object. We
    # don't care about storing all RunningCols objects corresponding to all
    # table rows. Consequently, we will create a unique RunningCols object
    # allowing to compute column totals for a unique row, and everytime a new
    # row will be encountered, we will reinitialise our unique RunningCols
    # object.

    # The name of a Total object being inside a RunningCols object is not
    # important: define a standard none.
    totalName = 'rowX' # The xth row

    def init(self):
        '''p_self will not be initialised at construction time, but everytime a
           row will be found, via m_reset.'''

    def reset(self):
        '''Resets the dict'''
        name = RunningCols.totalName
        for totals in self.containerTotals:
            id = totals.id
            valI = totals.initValue
            if id in self:
                # Recycle the existing Total object
                self[id].__init__(name, None, valI)
            else:
                # Create a new object
                self[id] = Total(name, None, valI)

    def getTotalFor(self, totalsO, name):
        '''Returns, within p_self, the Total object corresponding to the Totals
           object in p_totalsO.'''
        # Return the total only if the field named p_name is among those to take
        # into account.
        if name in totalsO.fields:
            return self.get(totalsO.id)

    # Display column headers
    pxHeaders= Px('<th for="col in totalsC.containerTotals">:_(col.label)</th>')

    # Display column cells at the end of the current row
    px = Px('''
     <x for="totalsO in totalsC.containerTotals"
        var2="tot=totalsC[totalsO.id]">::tot.getStyled('th')</x>''')
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
