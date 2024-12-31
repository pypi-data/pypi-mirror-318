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

from appy.xml.escape import Escape
from appy.xml import Parser, XHTML_SC

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Modifier(Parser):
    '''Allows to perform modifications on XHTML content'''

    # Regular expression for replacing special markers (see "replacementFun"
    # attribute below).
    replaceRex = re.compile(r'\*(.+?)\*')

    def __init__(self, env=None, caller=None, raiseOnError=False, p='p',
                 prefix='', replacements=None, tagReplacements=None,
                 replacementsFun=None, preListClass=None, lastLiClass=None,
                 tagsToIgnoreKeepContent=None):
        # Call the base constructor
        Parser.__init__(self, env, caller, raiseOnError)
        # p_p indicates which tag is mainly used in p_s for paragraphs. It could
        # also be "div".
        self.p = p
        # p_prefix is some chunk of text that must be inserted at the start of
        # the first found paragraph (p_p) in p_s.
        self.prefix = prefix
        # Currently usused
        self.replacements = replacements
        # Tag replacements, if passed, is a dict indicating which tag must be
        # replaced with another one. For example, if p_tagReplacements is
        #
        #                           {'div': 'span'}
        #
        # This input:
        #                        <div class="B">A</div>
        #
        # will be replaced with
        #
        #                       <span class="B">A</span>
        #
        self.tagReplacements = tagReplacements
        # If a p_replacementFun(ction) is defined, texts to modify can contain
        # special markers of the form
        #
        #                              *<name>*
        #
        # Evertytime such marker will be encountered, p_replacementFun will be
        # called, with "name" as unique arg, and must return the replacement
        # text for this name.
        self.replacementsFun = replacementsFun
        # The CSS class to set to the paragraph being immediately before a list
        # (="ul" tag).
        self.preListClass = preListClass
        # The CSS class to set to the last "li" tag within a "ul" tag.
        self.lastLiClass = lastLiClass
        # Tags listed here will not be part of the result, but their content,
        # yes.
        self.tagsToIgnoreKeepContent = tagsToIgnoreKeepContent

    def startDocument(self):
        # The result will be updated XHTML, joined from self.r
        Parser.startDocument(self)
        self.r = []

    def endDocument(self):
        self.r = ''.join(self.r)

    def dumpCurrentContent(self):
        '''Dump currently collected content if any'''
        e = self.env
        if e.currentContent:
            # Apply replacements when appropriate
            fun = self.replacementsFun
            text = e.currentContent
            if fun:
                text = Modifier.replaceRex.sub(fun, text)
            self.r.append(text)
            e.currentContent = ''

    def applyCss(self, css, tag, notBefore=None):
        '''Apply the CSS class to the last p_tag found on p_self.r. If
           p_notBefore is passed, within p_self.r, ignore p_tag if found
           immediately before tag p_notBefore.'''
        r = self.r
        if not r: return
        prefix = '<%s' % tag
        if notBefore:
            prefixP = '<%s' % notBefore
        # Remember the previously walked element in p_self.r
        previous = None
        # Walk element from p_self.r, in reverse order
        i = len(r) - 1
        while i >= 0:
            part = r[i]
            tagFound = part.startswith(prefix)
            if notBefore:
                condition = tagFound and \
                            (previous and not previous.startswith(prefixP))
            else:
                condition = tagFound
            if condition:
                j = part.index('>')
                start = part[:j]
                # Avoid adding the p_css class if one is already set
                if 'class=' not in start:
                    r[i] = '%s class="%s">%s' % (start, css, part[j+1:])
                break
            previous = r[i]
            i -= 1

    def getResultTag(self, tag):
        '''Get the p_tag to dump for this p_tag. It may not be p_tag itself,
           depending on p_self.tagReplacements.'''
        repls = self.tagReplacements
        if not repls: return tag
        return repls.get(tag) or tag

    def startElement(self, tag, attrs):
        # Ignore this start p_tag if relevant
        if tag in self.tagsToIgnoreKeepContent: return
        e = self.env
        # Dump any previously gathered content if any
        self.dumpCurrentContent()
        # Step #1: reify tag attributes
        r = ''
        for name, value in attrs.items():
            r += ' %s="%s"' % (name, Escape.xml(value))
        # Step #2: reify the whole start tag. Close it if it is a no-end tag.
        suffix = '/>' if tag in XHTML_SC else '>'
        r = '<%s%s%s' % (self.getResultTag(tag), r, suffix)
        # Step #3: insert p_self.prefix when appropriate
        if tag == self.p and not e.firstParaMet:
            e.firstParaMet = True
            # Insert p_self.prefix if present
            if self.prefix:
                r += self.prefix
        # Step #4: apply the pre-list class when appropriate
        if self.preListClass and tag == 'ul':
            # Ignore a potential last paragraph that would wrap this ul
            self.applyCss(self.preListClass, self.p, notBefore=tag)
        self.r.append(r)

    def endElement(self, tag):
        # Ignore this end p_tag if relevant
        if tag in self.tagsToIgnoreKeepContent: return
        e = self.env
        # Dump any previously gathered content if any
        self.dumpCurrentContent()
        # Close the tag only if it is a no-end tag
        if tag not in XHTML_SC:
            self.r.append('</%s>' % self.getResultTag(tag))
        # Apply a CSS class on the last li when appropriate
        if self.lastLiClass and tag == 'ul':
            self.applyCss(self.lastLiClass, 'li')

    def characters(self, content):
        # Re-transform XML special chars to entities
        self.env.currentContent += Escape.xml(content)

    def modify(self, s):
        '''Returns p_s, modified'''
        # Add variables to the environment
        # ~
        # Have I already encountered the first paragraph ?
        self.env.firstParaMet = False
        # Parse (wrapped) p_s
        r = self.parse('<x>%s</x>' % s)
        # Return the modified (unwrapped) result
        return r[3:-4]
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
