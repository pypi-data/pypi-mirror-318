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
class Gridder:
    '''Specification about how to produce search results in grid mode. An
       instance of Gridder can be specified in static attribute
       SomeAppyClass.gridder.'''

    def __init__(self, width='350px', gap='20px', justifyContent='space-evenly',
                 alignContent='space-evenly', cols=None, colsAuto=False,
                 margin=None, showFields=True, flex=False):
        # ~~~
        # If a p_width is specified, there will not be a fixed number of
        # columns: this number will depend on available space and this width.
        # If, for example, p_with is defined as being "350px" and the available
        # width is 800 pixels, the grid will have 2 columns.
        # ~~~
        # If p_cols is specified, p_width is ignored. p_cols defines the maximum
        # number of columns for the grid.
        # ~~~
        # The minimum width of every grid element
        self.width = width
        # The gap between grid elements. Will be passed to CSS property
        # "grid-gap".
        self.gap = gap
        # Specify how to align the whole grid horizontally inside the container.
        # Will be passed to CSS property "justify-content".
        self.justifyContent = justifyContent
        # Specify how to align the whole grid vertically inside the container.
        # Will be passed to CSS property "align-content".
        self.alignContent = alignContent
        # The maximum number of columns
        self.cols = cols
        # If colsAuto is True, the columns will be rendered with default
        # settings. Else, columns will have grid-template-columns with:
        # repeat(X,1fr)
        self.colsAuto = colsAuto
        # The gridder's margins
        self.margin = margin
        # By default, for every object rendered in a grid, the following
        # information is rendered, in that order:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # a) | o.getSupTitle(nav)
        # b) | o.title
        # c) | o.getSubTitle()
        # d) | any other field as defined, either in an initiator Ref field
        #    | (via its attribute "shownInfo"), or via attribute "listColumns"
        #    | as defined on o's class.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # If p_showFields is False, element (d) will not be rendered.
        self.showFields = showFields
        # If p_flex is True, a flex layout will be used instead of a grid layout
        self.flex = flex

    def getContainerStyle(self):
        '''Returns the CSS styles that must be applied to the grid container
           element.'''
        if self.flex:
            display = 'flex'
            specific = '; flex-wrap:wrap'
        else:
            display = 'grid'
            # Determine grid-specific parameters
            if self.cols:
                if self.colsAuto:
                    columns = ' '.join(['auto']*self.cols)
                else:
                    columns = 'repeat(%d,1fr)' % self.cols
            else:
                columns = 'repeat(auto-fill,minmax(%s,1fr))' % self.width
            specific = '; grid-template-columns:%s' % columns
        # Determine common parameters
        margin  = '; margin:%s' % self.margin if self.margin else ''
        justify = '; justify-content:%s;' % self.justifyContent \
                  if self.justifyContent else ''
        align   = '; align-content:%s;' % self.alignContent \
                  if self.alignContent else ''
        # Return the CSS code
        return 'display:%s; grid-gap:%s;%s%s%s%s' % \
               (display, self.gap, justify, align, specific, margin)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
