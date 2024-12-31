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
import re
from persistent.mapping import PersistentMapping

from appy.model.base import Base
from appy.ui.layout import Layouts
from appy.model.utils import Object as O
from appy.model.fields.string import String
from appy.model.fields.boolean import Boolean

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
REPL_DONE = 'Mover: %d replacements performed in %d/%d pages.'
REPL_TEST = 'Mover (dry run mode): %d replacements would have performed in ' \
            '%d/%d pages.'
REPL_NO   = 'Mover: no replacement performed, %d pages walked.'
REPL_NO_T = 'Mover (dry run mode): no replacement would have been performed, ' \
            '%d pages walked.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Mover(Base):
    '''Option class used to "move" a site from one URL to another'''

    # Concretely, it is used as an option class to update, within all rich
    # fields found within all Page instances, the base URL of all internal
    # links.

    @staticmethod
    def update(class_):
        '''The title is unused: hide it'''
        class_.fields['title'].show = False

    creators = True # Open instance creation
    indexable = False
    popup = ('500px', '400px')

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                            Main parameters
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    p = {'multiplicity': (1,1), 'label': 'Mover', 'layouts': Layouts.d}

    # The current base URL as present within Rich fields, in Page instances
    currentBase = String(validator=String.URL, **p)

    # The replacement base URL
    newBase = String(validator=String.URL, **p)

    # Dry run mode ?
    dryRun = Boolean(default=True, label='Mover', layouts=Boolean.Layouts.d)

    # A rex matching attributes that can hold a URL
    hrefRex = re.compile('(href|src)=\"(.*?)\"')

    # Texts to *o*utput or **log (bool #1, true if output), depending on the dry
    # run mode (bool #2, true if dry run) and actual effect (bool #3, true if
    # something actually happened).
    textsOL = {
     # UI   | Dry run  | Effect 
     True:  { False:   { True:  'Mover_done'  , False: 'action_null'},
              True:    { True:  'Mover_tested', False: 'action_null_test'}},
     False: { False:   { True:  REPL_DONE     , False: REPL_NO},
              True:    { True:  REPL_TEST     , False: REPL_NO_T}},
    }

    def patchHref(self, match, counts):
        '''Replaces the content of the p_match(ed) href attribute, if it
           corresponds to p_base, with p_new. Update p_counts.'''
        # Do no touch the attribute if not starting with p_self.currentBase
        url = match.group(2)
        if not url.startswith(self.currentBase):
            return match.group(0)
        # Compute the replacement URL
        url = self.newBase + url[len(self.currentBase):]
        counts.replacements += 1
        return '%s="%s"' % (match.group(1), url)

    def run(self):
        '''Performs the change in all Rich fields from all Page instances'''
        counts = O(
          total=0        , # The total number of pages walked
          updated=0      , # The number of pages being updated
          replacements=0 , # The total number of replacements made
        )
        dryRun = self.dryRun
        # Walk all pages
        for page in self.search('Page'):
            counts.total += 1
            if page.isEmpty('content'): continue
            content = page.content
            rcount = counts.replacements
            if isinstance(content, PersistentMapping):
                # This may happen for those having configured pages as being
                # multilingual.
                content = content.copy()
                for lang in content:
                    lcontent = content[lang]
                    if not lcontent: continue
                    content[lang] = self.hrefRex.sub(
                      lambda match: self.patchHref(match, counts), lcontent)
            else:
                content = self.hrefRex.sub(
                  lambda match: self.patchHref(match, counts), content)
            if counts.replacements > rcount:
                counts.updated += 1
                if not dryRun:
                    page.content = content
        # Return a message to the UI and log
        c = counts
        effect = bool(c.replacements) # Was there an actual effect ?
        if effect:
            map = counts.d()
            parts = (c.replacements, c.updated, c.total)
        else:
            map = None
            parts = c.total
        self.log(self.textsOL[False][dryRun][effect] % parts)
        return True, self.translate(self.textsOL[True][dryRun][effect],
                                    mapping=map)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
