#!/usr/bin/env python3

'''This script allows to perform a "grep" command that will be applied on files
   content.xml and styles.xml within all ODF files (odt and ods) found within a
   given folder.'''

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
import re, os.path, difflib

from appy.bin import Program
from appy.utils.zip import zip, unzip
from appy.utils import path as putils
from appy.model.utils import Object as O
from appy.xml.cleaner import StringCleaner

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
OPT_C_V  = "Options -c and -v can't be used altogether."
FF_KO    = '%s does not exist.'
S_CLEAN  = '%d styled text part(s) %scleaned.'
F_CORR   = 'XML corruption in %s::%s - The file was left untouched.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
bn = '\n'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Note:
    '''Represents an ODF Note, be it included in an ODS or ODT template'''

    # Regex defining a paragraph within a note
    paraRex = re.compile('<text:p(.*?)>(.*?)</text:p>')

    # Regex for splitting metadata from real content within a note
    contentRex = re.compile('(.*?)(<text:(?:p|list).*)')

    # Regex used to remove formatting possibly found in notes
    spanRex = re.compile('<text:span[^>]*>(.*?)</text:span>')

    # On old templates, self-closing span tags may be found in notes
    spanSc = re.compile('<text:span[^>]*?/>')

    # Regex for parsing metadata present in a note
    metadataRex = re.compile('.*?(<dc:creator>.*?</dc:creator>)?' \
                             '<dc:date>(.*?)</dc:date>.*', re.S)

    # Regex representing an overstructured text-list note
    listRex = re.compile('<text:list.*?>(.*?)</text:list>')
    itemRex = re.compile('<text:list-item.*?>(.*?)</text:list-item>')

    @classmethod
    def extractMetadata(class_, content):
        '''Extract, from this note p_content, metadata from real payload'''
        match = class_.contentRex.match(content)
        return match.group(1), match.group(2)

    @classmethod
    def parseMetadata(class_, metadata):
        '''Extract p_metadata'''
        if not metadata: return None, None
        match = class_.metadataRex.match(metadata)
        creator, date = match.groups()
        if creator: creator = creator[12:-13]
        creator = (creator or 'unknown').strip()
        return creator, date

    @classmethod
    def extractListParas(class_, match):
        '''If this p_note has a text-list overstructure, extract and returns
           standard paragraphs from it.'''
        # Extract paragraphs from list-items found in this p_match
        return class_.itemRex.sub(lambda m:m.group(1), match.group(1))

    @classmethod
    def clean(class_, note, cleanMethod):
        '''Returns the content of this p_note, where any formatting and ODF tag
           has been removed (even text:p tags).'''
        # Preambles
        # (a) Remove self-closing span tags potentially found in old templates
        note = class_.spanSc.sub('', note)
        # (b) Remove text-list overstructure, illegal now but possibly found in
        #     old templates.
        note = class_.listRex.sub(class_.extractListParas, note)
        # Clean the note
        note = class_.spanRex.sub(cleanMethod, note)
        # Remove any paragraph
        r = []
        style = None # Remember the style of at least one paragraph
        for attrs, content in class_.paraRex.findall(note):
            style = attrs or style
            r.append(content)
        return bn.join(r), style

    @classmethod
    def reify(class_, note, paraStyle):
        '''Re-create a series of "text:p" tags from this naked p_note, made of
           carriage-return-separated lines of text.'''
        r = []
        style = paraStyle or ''
        for line in note.split(bn):
            r.append(f'<text:p{style}>{line}</text:p>')
        return ''.join(r)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Condition:
    '''Represents a conditional field storing a POD expression'''

    # Name of the attribute storing the expression
    trueAttr = 'text:string-value-if-true'

    # Regex representing the attribute storing the "true" condition
    trueRex = re.compile(f'{trueAttr}="(.+?)"')

    # The expression may be surrounded with double quotes
    quote = '&quot;'

    @classmethod
    def reifyAttribute(class_, match, expression):
        '''Recreates the attribute sotirng the true condition, containing the
           new p_expression.'''
        # Get the current expression
        current = match.group(1)
        # Surround the new expression with double quotes if the current one was
        if current.startswith(class_.quote):
            r = f'{class_.quote}{expression}{class_.quote}'
        else:
            r = expression
        return f'{class_.trueAttr}="{r}"'

    @classmethod
    def replace(class_, attrs, expression):
        '''Replace, within this series of condition p_attributes, the "true"
           expression with this p_expression.'''
        fun = lambda match: class_.reifyAttribute(match, expression)
        return class_.trueRex.sub(fun, attrs, count=1)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Cell:
    '''Represents a cell within an ODS sheet'''

    # Name of the attributes storing the POD expression
    formulaAttr = 'table:formula'
    valueAttr = 'office:string-value'

    # Regex representing the attributes storing the POD expression
    formulaRex = re.compile(f'{formulaAttr}="(.+?)"')
    valueRex = re.compile(f'{valueAttr}="(.+?)"')

    @classmethod
    def replace(class_, attrs, content, expr):
        '''Replace, within this series of cell p_attributes and this cell
           p_content, the POD expression with this new p_expr(ession).'''
        # Crazy: the POD expression is stored at 3 different places in the cell:
        # 2 within cell attributes and 1 more in the cell content.
        c = class_
        # Perform replacements within p_attrs
        attrs = c.formulaRex.sub(
          lambda m: f'{c.formulaAttr}="of:=&quot;{expr}&quot;"',
          attrs, count=1)
        attrs = c.valueRex.sub(lambda m: f'{c.valueAttr}="{expr}"',
          attrs, count=1)
        # Perform the replacement within p_content
        return attrs, content

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Match:
    '''When a Grep is ran with inContent=False (see class c_Grep), one of its
       outputs is the list of matches within every found ODF document. Every
       match is represented by an instance of class Match.'''

    # Start/end markers and colors to use for delimiting diff zones
    markers = O(
      xhtml = O(start='<span style="color:%s">', end='</span>'),
      term  = O(start='\x1b[3%sm', end='\x1b[0m')
    )
    colors = O(
      xhtml = O(insert='green', delete='red'),
      term  = O(insert='2', delete='1')
    )

    def __init__(self, keyword, tag, metadata, content, patched=None,
                 dryRun=False, kwString=False, isVerbose=False,
                 outputType='raw'):
        # The matched keyword (as a string)
        self.keyword = keyword
        # Is p_keyword built fom a plain string or from a regular expression ?
        self.kwString = kwString
        # The precise matched tag
        self.tag = tag
        # The type of tag (= "target") whose content has been (or could be)
        # patched.
        self.target = 'note' if tag == 'office:annotation' else 'field'
        # The tag metadata (creator, date, etc), for notes only
        self.metadata = metadata
        # Note-specific metadata, that will be extracted from p_metadata
        self.creator, self.date = Note.parseMetadata(metadata)
        # In the context of a replacement, the version of p_content after
        # replacements were done.
        if patched is not None:
            self.patched = self.parseContent(patched)
        else:
            self.patched = None
        # Are we in the context of a dry run ?
        self.dryRun = dryRun
        # Verbose __repr__ for a match ?
        self.isVerbose = isVerbose
        # Output type, defining the way to render the diff between the content
        # before and after the replacement.
        self.outputType = outputType
        # Extract payload from p_content
        self.content = self.parseContent(content)

    def unescape(self, content):
        '''Unescape special chars from p_content'''
        return content.replace('&apos;', "'")

    def parseNote(self, note):
        '''Within this p_note, unescape some entities'''
        return self.unescape(note)

    def parseField(self, field):
        '''Parses the content of this ODF p_field'''
        # Remove the end of the start tag
        i = field.find('>')
        return self.unescape(field[i+1:])

    def parseContent(self, content):
        '''Parses this p_content and returns its payload'''
        if self.target == 'note':
            r = self.parseNote(content)
        elif self.target == 'field':
            r = self.parseField(content)
        else:
            r = content
        return r

    def getDiff(self, type='raw'):
        '''Returns a diff between self.content and self.patched'''
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # If p_type | the output
        # is ...    | will be ...
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #   "raw"   | (default) raw text as outputed by standard module difflib
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #   "term"  | colorized output to be rendered in a Unix-like terminal
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #   "xhtml" | a colorized chunk of XHTML code, in a "div" tag
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #   "data"  | a list of data about insertions, deletions and
        #           | replacements, as returned by method
        #           |        difflib.SequenceMatcher::get_opcodes
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        if type == 'raw':
            # Get the diff as raw text
            differ = difflib.Differ()
            r = list(differ.compare(self.content.split(bn),
                                    self.patched.split(bn)))
            r = bn.join(r)
        else:
            # Get the diff as xhtml or colored text for a terminal
            r = []
            a = self.content
            b = self.patched
            matcher = difflib.SequenceMatcher(None, a, b)
            markers = self.markers[type]
            colors = self.colors[type]
            changes = matcher.get_opcodes()
            if type == 'data':
                # Return the data structures representing changes, as-is
                r = changes
            else:
                # Format data according to p_type
                for opcode, a0, a1, b0, b1 in changes:
                    if opcode == 'equal':
                        r.append(a[a0:a1])
                    elif opcode == 'insert':
                        start = markers.start % colors.insert
                        r.append(f'{start}{b[b0:b1]}{markers.end}')
                    elif opcode == 'delete':
                        start = markers.start % colors.delete
                        r.append(f'{start}{a[a0:a1]}{markers.end}')
                    elif opcode == 'replace':
                        dstart = markers.start % colors.delete
                        istart = markers.start % colors.insert
                        r.append(f'{dstart}{a[a0:a1]}{markers.end}')
                        r.append(f'{istart}{b[b0:b1]}{markers.end}')
                r = ''.join(r)
                if type == 'xhtml':
                    r = f'<div>{r}</div>'
        return r

    def __repr__(self, spaces=2, nb=None):
        '''p_self's string representation'''
        isVerbose = self.isVerbose
        sep = ' ' * spaces
        # Add, for a note, a line of text containing its creator and creation
        # date.
        if self.target == 'note' and isVerbose:
            part = f'{bn}{sep}By {self.creator} on {self.date}{bn}'
        else:
            part = ''
        prefix = f'{bn}{sep}' if isVerbose else ''
        if self.patched is None:
            # No replacement
            info = f'{prefix}Content:{bn}{bn}{self.content}'
        else:
            # A replacement: display a diff
            verb = 'would have been' if self.dryRun else 'were'
            diff = self.getDiff(type=self.outputType)
            info = f'{prefix}These changes {verb} done:{bn}{bn}{diff}'
        # If v_isVerbose, add the target of the match (note or field) and repeat
        # the keyword(s) entered.
        if isVerbose:
            targetType = f'Match::on::{self.target} (tag {self.tag}){bn}'
            kwType = 'string' if self.kwString else 'regex'
            keywords = f'{sep}Keyword(s) ({kwType}): {self.keyword}'
            vinfo = f'{sep}{targetType}{keywords}'
        else:
            vinfo = ''
        return f'{vinfo}{part}{sep}{info}'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Matches(list):
    '''List of Match instances found in a given file'''

    def __init__(self, fileName, *args, **kwargs):
        list.__init__(self, *args, **kwargs)
        self.fileName = fileName

    def __repr__(self):
        '''p_self's string representation'''
        if len(self) == 1:
            prefix = '1 match'
        else:
            prefix = f'{len(self)} matches'
        r = [f':: {prefix} for {self.fileName} ::']
        i = 0
        for match in self:
            i += 1
            r.append(match.__repr__(nb=i))
        return f'{(bn*2).join(r)}{bn}'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Grep(Program):
    '''Perform UNIX grep-like searches within ODF files'''

    toGrep = ('content.xml', 'styles.xml')
    toUnzip = ('ods', 'odt')

    # Messages ~{ b_replace: { b_match: s_message }}~
    messageTexts = { True:  { True:  '%s: %d replacement(s) done.',
                              False: 'No replacement was made.'},
                     False: { True:  '%s matches %d time(s).',
                              False: 'No match found.'}}

    # ODF tags used by POD statements or expressions
    podTags = {
      'odt': ('office:annotation', 'text:conditional-text', 'text:text-input'),
      # In ODS templates, office:annotation tags are contained within table
      # cells. Consequently, they do not appear at the first level.
      'ods': ('table:table-cell',),
      'inner': ('office:annotation',)
    }

    # Regex allowing to detect mentions, in the replacement string, to groups
    # defined in the keywords regex.
    groupsRex = re.compile('\\\(\d)+')

    # Regex for parsing a POD expression within an ODS formula
    formulaRex = re.compile('table:formula="of:=&quot;(.*?)&quot;"')

    # Help messages
    HELP_K    = 'is the regular expression (or string if -s) to search ' \
                'within the file(s). From the command-line, special chars ' \
                'possibly included in the keyword (and also the replacement ' \
                'string, if passed) must be escaped. For example, ' \
                'cus(tom)_(agenda) must be written as  cus\(tom\)_\(agenda\).' \
                ' \\2_\\1 must be written as \\\\2_\\\\1.'
    HELP_P    = 'is the path to a file or folder. If a file is passed, you ' \
                'must pass the path to an ODF file (odt or ods). ogrep will ' \
                'be run on this file only. If a folder is passed, ogrep will ' \
                'be run on all ODF files found in this folder and sub-folders.'
    HELP_R    = 'if this replacement string is passed, within matched ODF ' \
                'files, the keyword will be replaced with it. The ' \
                'replacement string may contain references to groups ' \
                'possibly defined within the "keyword" regular expression, ' \
                'but only via the "\<nb>" notation.'
    HELP_V    = 'dump more info about the find/replace zones (only available ' \
                'if option "-c" is not used).'
    HELP_VV   = 'similar to -v, must with even more *v*erbosity.'
    HELP_D    = 'in the context of a replacement, if this option is set, no ' \
                'replacement will actually be performed, but output will ' \
                'give info (detailed if -v, minimal if not) about what ' \
                'replacements would have been performed without this option.'
    HELP_IC   = 'if unset, the find/replace process will only apply to the ' \
                'POD-controlled zones of POD template(s): notes and fields. ' \
                'If the option is set, it will occur in any part of the ' \
                'template(s).'
    HELP_S    = 'by default, keyword is interpreted as a regular expression. ' \
                'If you want it to be a plain *s*tring instead, set this ' \
                'option.'
    HELP_N    = 'if set in conjunction with -v or -vv, changes (being ' \
                'effective or potential, depending on -d) will be colorized. ' \
                'Else, changes will be rendered as standard diff output.'

    def defineArguments(self):
        '''Define the allowed arguments for this program'''
        add = self.parser.add_argument
        # Positional arguments
        add('keyword', help=Grep.HELP_K)
        add('path'   , help=Grep.HELP_P)
        # Optional arguments
        p = {'action': 'store_true'}
        # The (optional) replacement text
        add('-r' , '--repl'      , dest='repl'     , help=Grep.HELP_R)
        add('-v' , '--verbose'   , dest='verbose'  , help=Grep.HELP_V , **p)
        add('-vv',                 dest='vverbose' , help=Grep.HELP_VV, **p)
        # In dry-run mode, a replacement is not truly done: output indicates
        # what replacement(s) would have been performed.
        add('-d' , '--dry-run'   , dest='dryRun'   , help=Grep.HELP_D , **p)
        # (If repl) Find/replace keyword in raw ODF content, or in
        # POD-controlled zones (fields, statements) ?
        add('-c' , '--in-content', dest='inContent', help=Grep.HELP_IC, **p)
        add('-s' , '--as-string' , dest='asString' , help=Grep.HELP_S , **p)
        add('-n' , '--nice'      , dest='nice'     , help=Grep.HELP_N , **p)

    # ODF representation for possible input chars
    odfEntities = {"'": '&apos;', '"': '&quot;'}

    def odfCompliantKeyword(self, keyword):
        '''Transform the p_keyword the way it can be found within an ODF
           document.'''
        r = keyword
        for char, entity in self.odfEntities.items():
            r = r.replace(char, entity)
        return r

    def analyseArguments(self):
        '''Check and store arguments'''
        # Get args as p_self's attributes
        args = self.args
        for name, value in args.__dict__.items():
            setattr(self, name, value)
        # Identify incompatible args
        if (self.verbose or self.vverbose) and self.inContent:
            self.exit(OPT_C_V)
        # Transform p_self.keyword (and p_self.repl if it exists) into its ODF-
        # compliant form.
        self.keyword = word = self.odfCompliantKeyword(self.keyword)
        if self.repl:
            self.repl = self.odfCompliantKeyword(self.repl)
        # Remember the keyword as a string
        self.skeyword = word
        # If p_self.asString is True, p_self.keyword is interpreted as a plain
        # string. Else, it is interpreted as a regular expression.
        if self.asString:
            word = re.escape(word)
        self.keyword = re.compile(word, re.S)
        # If find/replace must occur in POD-controlled zones, define these zones
        # via regular expressions: one for ODT templates, one for ODS templates.
        inContent = self.inContent
        self.zoneRex = {
          'odt': self.getZoneRex(inContent, 'odt'),
          'ods': self.getZoneRex(inContent, 'ods'),
          # Sub-rex for ODS notes within cells
          'inner': self.getZoneRex(inContent, 'inner'),
        }
        # Must lists of matches be built for every found ODF document ?
        if not inContent:
            # Yes
            self.matches = {} # ~{s_filePath:[Match]}~
        # If called programmatically, we don't want any output on stdout
        self.silent = getattr(args, 'silent', False)
        if self.silent:
            self.messages = []
        # When replacing, count the number of styled text parts whose style was
        # removed (see Note::clean).
        self.cleaned = 0
        # Verbosity: 0 (less) to 3 (more). 0 means: no output at all, fatal
        # errors excepted. 1 is the default. 2 and 3 produce more detailed
        # output.
        verbose = 1
        if self.verbose:
            verbose = 2
        if self.vverbose:
            verbose = 3
        self.verbose = verbose
        # In dry-run mode, force verbosity to be at least 2
        if self.dryRun and self.verbose < 2:
            self.verbose = 2
        # When a p_repl(acement) is specified and outputed (depending on
        # p_verbose), how must be rendered the diff representing the
        # replacement ? More info in method Match::getDiff.
        type = getattr(args, 'outputType', None)
        if type:
            self.outputType = type
        else:
            self.outputType = 'term' if self.nice else 'raw'

    def getZoneRex(self, inContent, fileType):
        '''Return, if p_inContent is False, the regex representing pod zones
           within content|styles.xml.'''
        if inContent: return
        # Build the regex
        tags = '|'.join(self.podTags[fileType])
        # Negative lookahead assertion (?!-) is used to prevent matching tag
        # "office:annotation-end".
        rex = f'<(?P<tag>{tags})(?!-)(.*?)>(.*?)</(?P=tag)>'
        return re.compile(rex, re.S)

    def dump(self, message, raiseError=False):
        '''Dumps a p_message, either on stdout or in self.messages if we run in
           silent mode.'''
        # Raise an exception if requested
        if raiseError: raise Exception(message)
        # Log or store the p_message, depending on p_silent
        if self.silent:
            self.messages.append(message)
        else:
            print(message)

    def getMessage(self):
        '''Returns self.messages, concatenated in a single string'''
        messages = getattr(self, 'messages', None)
        if not messages: return ''
        return '\n'.join(messages)

    def getReplacement(self, match, counts=None):
        '''In the context of a replacement, this method returns p_self.repl,
           that will replace the matched p_self.keyword. In the context of a
           simple grep, the method returns the matched content, left untouched.
           In both contexts, p_counts about matches are updated.'''
        if counts is not None:
            counts.inXml += 1
        if self.repl:
            fun = lambda m: match.group(int(m.group(1)))
            r = self.groupsRex.sub(fun, self.repl)
        else:
            # The replacement has just been triggered to build self.matches.
            # Return the matched zone unchanged.
            r = match.group(0)
        return r

    def addMatch(self, path, imatch):
        '''Adds this p_imatch concerning the file p_path among p_self.matches'''
        matches = self.matches
        fileName = str(path)
        if fileName in matches:
            matches[fileName].append(imatch)
        else:
            matches[fileName] = Matches(fileName, [imatch])

    def cleanStyle(self, match):
        '''A styled text part has been found in p_match. Clean it and update the
           count in p_self.cleaned.'''
        if self.repl:
            self.cleaned += 1
        return match.group(1)

    def findIn(self, path, match, counts):
        '''A POD zone has been found, in m_match, in the file @path. Perform
           replacements within this zone.'''
        # Remember the current count of matches
        initialCount = counts.inXml
        initialCleaned = self.cleaned
        originalContent = match.group(0)
        tag = match.group(1)
        attrs = match.group(2)
        content = code = match.group(3)
        search = True
        metadata = ''
        subCount = 0
        isFormula = isNote = isCond = False
        if tag == 'office:annotation':
            # Further split v_content into *pure* content (=Python code) and
            # meta-data, like note creator and creation date.
            metadata, code = Note.extractMetadata(content)
            # Ensure there is no formatting in the note before applying the
            # replacement.
            code, paraStyle = Note.clean(code, self.cleanStyle)
            isNote = True
        elif tag == 'table:table-cell':
            # In an ODS template, a table cell may contain an expression (as a
            # formula) and also an annotation.
            # (a) Manage a potential inner annotation
            fun = lambda subMatch: self.findIn(path, subMatch, counts)
            content = self.zoneRex['inner'].sub(fun, content)
            subCount = counts.inXml - initialCount
            # (b) Manage a potential POD expression
            fmatch = Grep.formulaRex.search(attrs)
            if not fmatch:
                search = False # No POD expression here
            else:
                code = fmatch.group(1)
                isFormula = True
        elif tag == 'text:conditional-text':
            isCond = True
        # When a table cell only contains a note, the job is already done
        if search:
            r = self.keyword.sub(lambda m: self.getReplacement(m, counts), code)
            matched = counts.inXml > (initialCount + subCount)
            if matched:
                # p_self.keyword has matched. Create a Match instance.
                if self.repl:
                    patched = r # A true replacement was done
                else:
                    patched = None # There was a match, but v_r repeats
                                   # v_content, because we are not in the
                                   # context of a replacement.
                m = Match(self.skeyword, tag, metadata, code, patched,
                          self.dryRun, self.asString, self.verbose > 2,
                          self.outputType)
                self.addMatch(path, m)
                # Count the number of matches instead of the number of
                # individual replacements.
                counts.inXml = initialCount + 1
            else:
                # Cleaning for this file will finally not be applied, so set the
                # count to the one that existed before managing this file.
                self.cleaned = initialCleaned
            # Reinsert v_r at the right place when reifying the whole tag
            if matched and self.repl:
                if isFormula:
                    attrs, content = Cell.replace(attrs, content, r)
                elif isNote:
                    content = Note.reify(r, paraStyle)
                elif isCond:
                    content = r
                    attrs = Condition.replace(attrs, r)
                else:
                    content = r
            elif isNote and self.repl:
                # Even if there was no match in some note, every note is cleaned
                # in any case, so, must be reified.
                content = Note.reify(r, paraStyle)
        return f'<{tag}{attrs}>{metadata}{content}</{tag}>'

    def grepFileContent(self, path, tempFolder, contents):
        '''Finds self.keyword among p_tempFolder/content.xml and
           p_tempFolder/styles.xml, whose content is in p_contents and was
           extracted from file @p_path, and return the number of matches. If
           Match objects must be built, p_self.matches are updated accordingly.

           If self.repl is there, and if there is at least one match, the method
           replaces self.keyword by self.repl for all matches, re-zips the ODF
           file whose parts are in p_tempFolder and overwrites the original file
           in p_path.'''
        # Initialise counts
        counts = O(
          inXml = 0,    # The number of matches within the currently analysed
                        # XML file (content.xml or styles.xml) within p_path
          inFile = 0,   # The number of matches within p_path (sums all inner
                        # counts from content.xml and styles.xml)
          corrupted = 0 # The number of XML files whose content is not
                        # SAX-parsable anymore after replacements have been
                        # performed
        )
        fileType = path.suffix[1:].lower()
        fileName = str(path)
        zoneRex = self.zoneRex[fileType]
        for name in self.toGrep:
            # Get the file content
            content = contents[name]
            # Step #1: find (and potentially replace) matches in the content of
            #          the file as loaded in a string, in v_content...
            if not zoneRex:
                # ... either in the full document ...
                found = self.keyword.findall(content)
                if not found: continue
                counts.inXml = len(found)
                if self.repl:
                    # Make the replacement
                    fun = lambda match: self.getReplacement(match)
                    content = self.keyword.sub(fun, content)
            else:
                # ... or within every POD expression or statement
                counts.inXml = 0 # Reinitialise the XML count
                fun = lambda match: self.findIn(path, match, counts)
                content = zoneRex.sub(fun, content)
                if not counts.inXml: continue
            counts.inFile += counts.inXml
            # Step #2: actually perform replacements on the file on disk, if a
            #          p_self.repl(acement) is required, if at least one
            #          replacement can be performed and if p_content has not
            #          been corrupted.
            if counts.inXml and self.repl and not self.dryRun:
                # Output a warning if p_content has been corrupted
                if not StringCleaner.isParsable(content, wrap=None):
                    self.dump(F_CORR % (fileName, name))
                    counts.corrupted += 1
                    # Remove the matches
                    if fileName in self.matches: del self.matches[fileName]
                    # Nothing will be cleaned
                    self.cleaned = 0
                else:
                    # Overwrite the file on disk
                    tempFileName = os.path.join(tempFolder, name)
                    with open(tempFileName, 'w') as f: f.write(content)
        # Re-zip the result when relevant
        if counts.inFile and self.repl and not self.dryRun and \
           counts.corrupted == 0:
            zip(fileName, tempFolder, odf=True)
        return counts.inFile

    def grepFile(self, path):
        '''Unzip the .xml files from file @p_path and perform a grep on it'''
        # Unzip the file in the temp folder
        tempFolder = putils.getOsTempFolder(sub=True)
        # Unzip the file in its entirety
        fileName = str(path)
        contents = unzip(fileName, tempFolder, odf=True, asBytes=False)
        nb = self.grepFileContent(path, tempFolder, contents)
        if nb and self.verbose == 1:
            # If verbose is 2 or more, Match instances will all be dumped at the
            # end.
            msg = self.messageTexts[bool(self.repl)][bool(nb)] % (fileName, nb)
            self.dump(msg)
        # Delete the temp folder
        putils.FolderDeleter.delete(tempFolder)
        return nb

    def run(self):
        '''Performs the "grep" on self.path'''
        nb = 0
        path = Path(self.path)
        if path.is_file():
            nb += self.grepFile(path)
        elif path.is_dir():
            # Grep on all files found in this folder
            for ext in Grep.toUnzip:
                for od in path.glob(f'**/*.{ext}'):
                    nb += self.grepFile(od)
        else:
            # Dump this error message, whatever verbose is
            self.dump(FF_KO % str(path))
        verbose = self.verbose
        if not nb and verbose > 0:
            self.dump(self.messageTexts[bool(self.repl)][False])
        elif verbose > 1:
            # Dump the match instances
            matches = getattr(self, 'matches', None)
            if matches:
                for match in matches.values():
                    self.dump(repr(match))
        if self.cleaned and verbose > 0:
            verb = 'would have been ' if self.dryRun else ''
            self.dump(S_CLEAN % (self.cleaned, verb))
        return nb

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == '__main__': Grep().run()
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
