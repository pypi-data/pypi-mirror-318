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

from appy.utils import asDict
from appy.utils.css import Styles
from appy.xml.escape import Escape
from appy.xml import Parser, XHTML_SC
from appy.utils.string import firstMatch

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TFM_KO = 'Transform function %s :: Error while transforming: "%s" :: %s'
IT_KO  = 'Error while trying to italicize text "%s" :: %s'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Cleaner(Parser):
    '''Cleans XHTML content, so it becomes ready to be stored into a
       Appy-compliant format.'''

    class InvalidText(Exception):
        '''Raised when invalid text is encountered in content to be cleaned by
           the Cleaner.'''

    # Tags that will never be in the result, content included, lax or strict
    tagsToIgnoreWithContent = ('style', 'head')
    tagsToIgnoreWithContentStrict = tagsToIgnoreWithContent + ('br',)

    # Tags that will be removed from the result, but whose content will be kept
    tagsToIgnoreKeepContent = ('x', 'html', 'body', 'font', 'center',
                               'blockquote')

    # Attributes to ignore, lax or strict
    attrsToIgnore = ('id', 'name', 'class', 'lang', 'rules')
    attrsToIgnoreStrict = attrsToIgnore + ('style',)

    # If the "styles" attribute is not ignored, what CSS properties, within
    # such attributes, must be kept ? In strict mode, only property
    # "background-color" is kept, because it is used by the Poor field to define
    # highlighted text.
    propertiesToKeepStrict = asDict(('background-color',))

    # Attrs to add, if not present, to ensure good formatting, be it at the web
    # or ODT levels.
    attrsToAdd = {'table': {'cellpadding':'6', 'cellspacing':'0', 'border':'1'},
                  'tr':    {'valign': 'top'}}
    attrsToAddStrict = {}

    # Tags that require a line break to be inserted after them
    lineBreakTags = asDict(('p', 'div', 'li', 'td', 'th',
                            'h1', 'h2', 'h3', 'h4', 'h5', 'h6'))

    # Tags to completely remove if being empty
    removeIfEmptyTags = asDict(('p', 'div', 'ul', 'li',
                                'h1', 'h2', 'h3', 'h4', 'h5', 'h6'))

    # List tags
    listTags = asDict(('ol', 'ul'))

    def __init__(self, env=None, caller=None, raiseOnError=True,
                 tagsToIgnoreWithContent=tagsToIgnoreWithContent,
                 tagsToIgnoreKeepContent=tagsToIgnoreKeepContent,
                 attrsToIgnore=attrsToIgnore, propertiesToKeep=None,
                 attrsToAdd=attrsToAdd, repair=False, invalidTexts=None,
                 transformText=None, toItalicize=None, logger=None):
        # Call the base constructor
        Parser.__init__(self, env, caller, raiseOnError)
        self.tagsToIgnoreWithContent = tagsToIgnoreWithContent
        if 'x' not in tagsToIgnoreKeepContent: tagsToIgnoreKeepContent += ('x',)
        self.tagsToIgnoreKeepContent = tagsToIgnoreKeepContent
        self.tagsToIgnore = tagsToIgnoreWithContent + tagsToIgnoreKeepContent
        self.attrsToIgnore = attrsToIgnore
        # CSS properties to keep, when "styles" attributes are not ignored.
        # If None is set, it means: any property is kept.
        self.propertiesToKeep = propertiesToKeep
        self.attrsToAdd = attrsToAdd
        # Potentially p_repair illegal tag configurations
        self.repair = repair
        # If passed, p_invalidTexts must be a tuple or list of regular
        # expressions. If textual content encountered by the cleaner matches one
        # of these regexes, an InvalidText exception will be raised. Note that
        # we are talking about non-exact matches here (ie, method regex.search
        # will be used, and not regex.match).
        self.invalidTexts = invalidTexts
        # You may pass a function in p_transformText. It will be called
        # everytime raw text is encountered and must be dumped into the result.
        # The function must accept a string as unique arg and must return a
        # string, being the parameter or a variant, transformed in some way.
        self.transformText = transformText
        # If passed, p_toItalicize must be, either:
        # - a set of terms that, if found in field content, will be
        #   italicized = surrounded by <i></i> tags, or
        # - a regular expression (regex) that represents such a set, in the
        #   form "word1|word2|...". Method Cleaner.getItalicizeRex produces such
        #   a regex from a set of words.
        self.toItalicize = self.getItalicizeRex(toItalicize)
        # A logger object can be passed if the cleaner has something to say (ie,
        # a p_transformText function produces an error).
        self.logger = logger

    def startDocument(self):
        # The result will be cleaned XHTML, joined from self.r
        Parser.startDocument(self)
        self.r = []

    def endDocument(self):
        self.r = ''.join(self.r)

    def log(self, text, type='info'):
        '''Logs this p_text, if a p_self.logger is available'''
        o = self.logger
        if o:
            o.log(text, type=type)

    def dump(self, something):
        '''Adds p_something to p_self.r'''
        e = self.env
        if not self.repair or e.insertIndex == -1:
            # Simply push p_something at the end of p_self.r
            self.r.append(something)
        else:
            # In the context of a repair, we are currently inserting content at
            # a specific place within p_self.r.
            i = e.insertIndex
            self.r.insert(i, something)
            # Update indexes
            e.insertIndex += 1
            indexes = e.listIndexes
            j = len(indexes) - 1
            while j >= 0:
                current = indexes[j]
                if current < i: break
                indexes[j] += 1
                j -= 1

    def getPrevious(self, withIndex=False):
        '''Returns the previous element within p_self.r'''
        # If p_withIndex is True, it returns a tuple (elem, index) instead
        r = self.r
        if not r: return (None, None) if withIndex else None
        # Compute the index of the previous element. If we are not performing a
        # repair, this index corresponds to the last element (-1).
        if not self.repair or self.env.insertIndex == -1:
            i = -1
        else:
            i = self.env.insertIndex -1
            if i == -1: return (None, None) if withIndex else None
        # Return the result
        r = r[i]
        return (r, i) if withIndex else r

    def manageConflicts(self, tag):
        '''This start p_tag has just been encountered. Is that a problem ?'''
        # Conflict management is disabled when p_self.repair is False
        if not self.repair: return
        e = self.env
        if tag == 'div' and e.listIndexes:
            # A div in a list: yes it is. Set the insert index to the last list
            # index. That way, the div will be inserted before the current list.
            e.insertIndex = e.listIndexes[-1]

    def updateIndexes(self, tag, start):
        '''If p_self.repair is True, this method updates the indexes stored on
           p_self.env after p_tag (start or end, depending on p_start) have been
           encountered.'''
        if not self.repair: return
        e = self.env
        isList = tag in Cleaner.listTags
        if start:
            if isList:
                e.listIndexes.append(len(self.r))
        else:
            if isList:
                e.listIndexes.pop()
            # Reinitialise self.env.insertIndex: once a tag is closed, the
            # conflict is considered being solved.
            e.insertIndex = -1

    def checkInvalidText(self, content):
        '''Raises an InvalidText exception if p_content contains invalid text'''
        patterns = self.invalidTexts
        if not patterns: return
        text = firstMatch(patterns, content)
        if text:
            raise Cleaner.InvalidText(text)

    @classmethod
    def getItalicizeRex(class_, words):
        '''Returns a regular expression made of all p_words to italicize'''
        # Maybe, there is nothing to italicize
        if not words: return
        # Maybe, p_word is already a regex
        if isinstance(words, re.Pattern): return words
        # Convert p_words, supposedly being a set of strings, to a regex
        r = []
        for word in words:
            r.append(re.escape(word))
        # Get longer words first
        r.sort(key=lambda word:-len(word))
        # Prevent words being parts of longer words from being matched, by:
        # (a) prefixing the regex by a negative lookbehind assertion ("the word
        #     may not be preceded by any alphanumeric char");
        alphaChar = r'[\w-]' # Include the dash
        prefix = f'(?<!{alphaChar})'
        # (b) suffixing the regex by a negative lookahead assertion ("the word
        #     may not be followed by any alphanumeric char").
        suffix = f'(?!{alphaChar})'
        words = '|'.join(r)
        return re.compile(f'{prefix}(?:{words}){suffix}')

    def italicize(self, match):
        '''This method surrounds, by an "i" tag, the p_match(ed) word'''
        return f'<i>{match.group(0)}</i>'

    def dumpCurrentContent(self, beforeEnd=None):
        '''Dumps (if any) the current content as stored on p_self.env'''
        # Do nothing if there is no current content
        e = self.env
        content = e.currentContent
        if not content: return
        # If the current content must be dumped before closing an end tag
        # representing a paragraph (p_beforeEnd), right-strip the content.
        if beforeEnd and beforeEnd in Cleaner.lineBreakTags:
            content = content.rstrip()
        # Ensure no invalid text is present
        self.checkInvalidText(content)
        # Apply some transform to v_content when relevant
        if self.transformText:
            try:
                content = self.transformText(content)
            except Exception as err:
                # This cleaner may be cleaning text to be stored in the
                # database. Any exception raised during this process should not
                # lead to text being lost.
                self.log(TFM_KO % (str(self.transformText), content, str(err)),
                         type='error')
        # Italicize words if required (and not already done)
        if self.toItalicize and not e.inI:
            try:
                content = self.toItalicize.sub(self.italicize, content)
            except Exception as err:
                # Same remark as hereabove: avoid losing data while saving the
                # current Appy object.
                self.log(IT_KO % (content, str(err)), type='error')
        # Add the current content to the result
        self.dump(content)
        # Reinitialise the current content to the empty string
        e.currentContent = ''

    def cleanStyleAttribute(self, value):
        '''Returns the cleaned version of the "style" attribute p_value,
           potentially modified, depending on p_self.propertiesToKeep.'''
        toKeep = self.propertiesToKeep
        # v_toKeep being None indicates to any vallue must be kept
        if toKeep is None: return value
        styles = Styles(**Styles.parse(value, asDict=True))
        return styles.asString(keep=Cleaner.propertiesToKeepStrict)

    def removeIfEmpty(self, tag):
        '''This ending p_tag has just been encountered: remove the entire tag if
           we are about dumping an empty tag.'''
        # Remove it only if appropriate
        if tag not in Cleaner.removeIfEmptyTags: return
        # Get the last dumped element
        prev, i = self.getPrevious(withIndex=True)
        if not prev: return
        prev = prev.strip()
        if prev == f'<{tag}>' or prev.startswith(f'<{tag} '):
            del self.r[i]
            r = True
        else:
            r = False
        return r

    def startElement(self, tag, attrs):
        e = self.env
        # Dump any previously gathered content if any
        self.dumpCurrentContent()
        # Are we in a "i" tag ?
        if tag == 'i': e.inI = True
        # Remember list tags
        self.updateIndexes(tag, True)
        # Manage tag conflicts, leading to repairs
        self.manageConflicts(tag)
        # Ignore this tag when appropriate
        if e.ignoreTag and e.ignoreContent: return
        if tag in self.tagsToIgnore:
            e.ignoreTag = True
            if tag in self.tagsToIgnoreWithContent:
                e.ignoreContent = True
            else: # v_tag is in p_self.tagsToIgnoreKeepContent
                e.ignoreContent = False
            e.currentTags.append( (tag, e.ignoreContent) )
            return
        # Add a line break before the start tag if required (ie: xhtml differ
        # needs to get paragraphs and other elements on separate lines).
        prefix = ''
        if tag in Cleaner.lineBreakTags:
            prev = self.getPrevious()
            if prev and prev[-1] != '\n':
                prefix = '\n'
        r = f'{prefix}<{tag}'
        # Include the found attributes, excepted those that must be ignored
        for name, value in attrs.items():
            if name in self.attrsToIgnore: continue
            # Clean "style" attribute, according to p_self.propertiesToKeep
            if name == 'style':
                value = self.cleanStyleAttribute(value)
            r = f'{r} {name}="{Escape.xml(value)}"'
        # Include additional attributes if required
        if tag in self.attrsToAdd:
            for name, value in self.attrsToAdd[tag].items():
                if name in attrs: continue
                r = f'{r} {name}="{value}"'
        # Close the tag if it is a no-end tag
        suffix = '/>' if tag in XHTML_SC else '>'
        self.dump(f'{r}{suffix}')

    def endElement(self, tag):
        e = self.env
        if e.ignoreTag and tag in self.tagsToIgnore and \
           tag == e.currentTags[-1][0]:
            # Dump possible content if it must not be ignored
            if not e.ignoreContent:
                self.dumpCurrentContent(beforeEnd=tag)
            # Pop the currently ignored tag
            e.currentTags.pop()
            if e.currentTags:
                # Keep ignoring tags
                e.ignoreContent = e.currentTags[-1][1]
            else:
                # Stop ignoring elems
                e.ignoreTag = e.ignoreContent = False
        elif e.ignoreTag and e.ignoreContent:
            # This is the end of a sub-tag within a region that we must ignore
            pass
        else:
            self.dumpCurrentContent(beforeEnd=tag)
            # Close the tag only if it is a no-end tag
            if tag not in XHTML_SC:
                # ... but do not close it, and even remove it entirely, if being
                #     empty and listed among "removeIfEmptyTags" tags.
                removed = self.removeIfEmpty(tag)
                if not removed:
                    # Add a line break after the end tag if required (ie: xhtml
                    # differ needs to get paragraphs and other elements on
                    # separate lines).
                    suffix = ''
                    if tag in Cleaner.lineBreakTags:
                        prev = self.getPrevious()
                        if prev and not prev.endswith('\n'):
                            suffix = '\n'
                    self.dump(f'</{tag}>{suffix}')
        # Pop list tags
        self.updateIndexes(tag, False)
        # Update flag p_e.inI
        if tag == 'i':
            e.inI = False

    def characters(self, content):
        e = self.env
        if e.ignoreContent: return
        # Remove leading whitespace
        current = e.currentContent
        if not current or current[-1] == '\n':
            toAdd = content.lstrip('\n\r\t')
        else:
            toAdd = content
        # Re-transform XML special chars to entities
        e.currentContent += Escape.xml(toAdd)

    def clean(self, s, wrap=True):
        '''Cleaning XHTML code p_s allows to produce a Appy-compliant,
           ZODB-storable string.'''
        # a. Every <p> or <li> must be on a single line (ending with a carriage
        #    return); else, appy.utils.diff will not be able to compute XHTML
        #    diffs;
        # b. Optimize size: HTML comments are removed
        #
        # The stack of currently parsed elements (will contain only ignored
        # ones).
        e = self.env
        e.currentTags = []
        # 'ignoreTag' is True if we must ignore the currently walked tag.
        e.ignoreTag = False
        # 'ignoreContent' is True if, within the currently ignored tag, we must
        # also ignore its content.
        e.ignoreContent = False
        # Are we currently walking a "i" tag ?
        e.inI = False
        # Repair-related data sructures
        if self.repair:
            # Remember the indexes, within p_self.r, where starting list tags
            # (ol, ul) are inserted.
            e.listIndexes = []
            # If the following index is not -1, it means that we are currently
            # dumping elements at this specific index in p_self.r and not at the
            # end of it.
            e.insertIndex = -1
        # If p_wrap is False, p_s is expected to already have a root tag. Else,
        # it may contain a sequence of tags that must be surrounded by a root
        # tag.
        s = f'<x>{s}</x>' if wrap else s
        return self.parse(s)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class StringCleaner:
    '''Ensure a string does not contain any char that would provoke SAX parser
       errors. Also propose a method for producing clean strings, for which
       those chars were removed.'''

    # Chars (some of the ASCII control characters) provoking SAX parse errors in
    # strings, once being part of a XML data structure that must be parsed with
    # a SAX parser.
    numbers = tuple(range(1,20)) + ('0e',)
    chars = '|'.join(['\\x%s' % str(n).zfill(2) for n in numbers])
    illegal = re.compile(chars)

    @classmethod
    def isParsable(class_, s, wrap='x'):
        '''Returns True if p_s is SAX-parsable. If p_s represents a chunk of
           XHTML code not being wrapped in a single root XML tag, it can be
           wrapped into p_wrap. Specify p_wrap = None for disabling such
           wrapping.'''
        # Wrap p_s if required
        if wrap: s = f'<{wrap}>{s}</{wrap}>'
        try:
            Parser().parse(s)
            return True
        except Exception:
            return False

    @classmethod
    def clean(class_, s):
        '''Return p_s whose illegal chars were removed'''
        if not s: return s
        return class_.illegal.sub('', s)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
