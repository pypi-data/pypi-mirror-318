'''Transforms a portion of text, originating from XHTML code, into a target
   text, being conform to typographic rules of some natural language.'''

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
from html.entities import entitydefs as htmlEntities

from appy.xml.escape import Escape

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Transform:
    '''Abstract class being general to any natural language'''

    entity = re.compile(r'&(\w+);')

    @classmethod
    def resolveEntity(class_, match):
        '''Resolves this p_match(ed) entity'''
        return htmlEntities.get(match.group(1)) or '?'

    @classmethod
    def resolveEntities(class_, text):
        '''Convert explicit XML entities to their ASCII char'''
        return class_.entity.sub(class_.resolveEntity, text)

    @classmethod
    def apply(class_, text):
        '''Applies the transforms, managing XML entities'''
        # DO NOT override this method: override m_run and/or m_runAfterEscape
        # instead.
        #
        # Resolve entities as a preamble
        text = class_.resolveEntities(text)
        # Apply a set of transforms
        text = class_.run(text)
        # Reify entities
        text = Escape.xml(text)
        # Then, potentially apply a second round of transforms that produce XML
        # chars that must not be escaped. These transforms must be able to
        # handle XHTML entities being potentially found within v_text.
        return class_.runAfterEscape(text)

    @classmethod
    def run(class_, text):
        '''Applies any transforms on this p_text, that does not produce any XML
           char that must not be escaped.'''
        return text

    @classmethod
    def runAfterEscape(class_, text):
        '''Applies any transform that does produce any XML char not-to-be-
           escaped.'''
        return text

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class French(Transform):
    '''Text transformer applying typographic rules as applicable to french'''

    # Punctuation chars in front of which an unbreakable space must be inserted
    spaced = re.compile(r'([\w\d])[  ]*(!|\?|:|;|%)')

    # Management of *q*uotes and *d*ashes
    charsQD = re.compile("(.)?(\"|'|«|»|“|”|‘|’|-|–|—| )(.)?")

    # Persons' titles, and other words that must be followed by a non breakable
    # space.
    titles = re.compile(r'(M\.[  ]le|Mme[  ]la|M\.|MM\.|Mme|Mmes|Doc.) ')

    # Numbers, expressed as arab or roman numerals. For roman numbers, the
    # objective is restricted to matching centuries.
    figures = re.compile(r'(\d+|[IVX]{1,6})(er|re|e)(?!\w)(.)?')

    # Manage abbreviation "N°" or "n°"
    no = re.compile('(N|n)°(.)?')

    # In some cases, it may be appropriate to convert the "degree" char, "°", to
    # a lower "o" char, surrounded by "sup" tags. If you want this, set the
    # following static attribute to True.
    noToSup = False

    # Chars to be replaced in any case, with their replacement char
    replacements = {
      "'": '’', # A straight apos must be come a curved one
      ' ':' ',  # A thin space must become an unbreakable one
      # English-tyle quotes must, in the end, be replaced with angle quotes.
      # Start by converting them to straight double quotes.
      '“': '"', '”': '"', '‘': '"'}

    # Dashes
    dashes = ('-', '–', '—')

    # Whitespace, being breakable or not
    whitespace = (' ', ' ')

    # Angle quotes
    angle = ('«', '»')

    @classmethod
    def manageSpaced(class_, match):
        '''Standardize a punctuation char'''
        return f'{match.group(1)} {match.group(2)}'

    @classmethod
    def manageDash(class_, pre, char, post):
        '''Manage a p_char being a dash'''
        # As a preamble, convert any long dash with a shorter one
        if char == '—': char = '–'
        # Manage whitespace surrounding dashes
        white = class_.whitespace
        if char == '-':
            if pre in white and post in white:
                # This should be a longer dash, without any non breakable space
                pre = post = ' '
                char = '–'
            elif post == ',':
                # In that case, also replace it with a longer dash; ensure v_pre
                # is a space.
                char = '–'
                if pre and pre not in white:
                    pre = f'{pre} '
        elif char == '–':
            # Ensure it is surrrounded by spaces
            if pre and pre not in white:
                pre = f'{pre} '
            if post and post not in white and post != ',':
                post = f' {post}'
        return pre, char, post

    @classmethod
    def manageCurved(class_, pre, char, post):
        '''Manages the ending curved quote'''
        # The objective here is to standardize curved quotes, like in this
        # example: ‘amusant’ must become "amusant". But too many conflicts occur
        # with the ending curved quote (’), also being the result of converting
        # a single quote ('). Consequently, currently, the ending curved quote
        # stays unchanged.
        return char
        # Is this a simple quote that must stay as is (like in: L’eau) or must
        # it be converted to an angle quote ? (like in: Il se dit ‘amusant’) ?
        if pre.isalnum() and (post.isalnum() or post == ')' or post == 'œ'):
            r = char
            # Examples of ending curved quotes that must not be converted
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - "L'article (n’) est (pas) amendé": the "(n’)" part must stay as
            #   is (well managed).
            # - "La main d’œuvre" (well managed, but special char œ must be
            #   explicitly specified: method string.isalnum does not consider it
            #   as an alphanumeric char).
            # - "d’« anticiper" is wrongly converted to "d »« anticiper".
            # - There are probably more wrong cases.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        else:
            r = '"'
            # This will be converted by the appropriate angle char by
            # m_manageAngleQuote.
        return r

    @classmethod
    def manageAngleQuote(class_, pre, char, post):
        '''Ensure angle quote p_char has its companion non breakable space'''
        if char == '«':
            if post == ' ':
                post = ' ' # Convert a space into a non breakable
            elif post == ' ' or not post:
                pass # Everything is OK
            else:
                post = f' {post}' # Insert a non-breakable before v_post
        elif char == '»':
            if pre == ' ':
                pre = ' ' # Convert a space into a non breakable
            elif pre == ' ' or not pre:
                pass # Everything is OK
            else:
                pre = f'{pre} ' # Insert a non-breakable after v_pre
        return pre, char, post

    @classmethod
    def manageQD(class_, match):
        '''Standardize a quote and its surroundings'''
        char = match.group(2)
        # Perform char replacements
        pre = match.group(1) or ''
        post = match.group(3) or ''
        char = class_.replacements.get(char) or char
        # Convert quote symbols into angle quotes
        if char == '’':
            char = class_.manageCurved(pre, char, post)
        if char == '"':
            if pre.isalnum() or pre == ' ':
                char = '»'
            elif post.isalnum() or post == ' ':
                char = '«'
        # Manage angle quotes
        if char in class_.angle:
            pre, char, post = class_.manageAngleQuote(pre, char, post)
        # Manage dashes
        elif char in class_.dashes:
            pre, char, post = class_.manageDash(pre, char, post)
        return f'{pre}{char}{post}'

    @classmethod
    def manageTitle(class_, match):
        '''Ensure non-breakable spaces are in use among people's titles'''
        title = match.group(1).replace(' ', ' ')
        return f'{title} '

    @classmethod
    def setUnbreakable(class_, char, insert=True):
        '''Returns a variant of p_char, starting with or being an unbreakable
           space.'''
        if not char: return char or ''
        if char == ' ':
            r = ' ' # A normal space is converted to an unbreakable one
        elif char == ' ':
            r = char # Already unbreakable, this is fine
        else:
            # Insert, when relevant, an unbreakable space before any other char
            r = f' {char}' if insert else char
        return r

    @classmethod
    def manageFigure(class_, match):
        '''Ensure letters after a figure are put in exponent'''
        post = class_.setUnbreakable(match.group(3), insert=False)
        return f'{match.group(1)}<sup>{match.group(2)}</sup>{post}'

    @classmethod
    def manageNo(class_, match):
        '''Ensure an unbreakable space follows chars "N°" or "n°"'''
        post = class_.setUnbreakable(match.group(2))
        # Convert char ° to letter "o" surrounded by tag "sup" if appropriate
        o = '<sup>o</sup>' if class_.noToSup else '°'
        return f'{match.group(1)}{o}{post}'

    @classmethod
    def run(class_, text):
        '''Applies the transforms'''
        # Manage punctuation chars
        text = class_.spaced.sub(class_.manageSpaced, text)
        # Manage quotes and dashes
        text = class_.charsQD.sub(class_.manageQD, text)
        # Manage persons' titles
        return class_.titles.sub(class_.manageTitle, text)

    @classmethod
    def runAfterEscape(class_, text):
        '''Manage transforms that produce not-to-be-escaped XML chars'''
        # Manage figures
        text = class_.figures.sub(class_.manageFigure, text)
        # Manage "N°/n°"
        text = class_.no.sub(class_.manageNo, text)
        return text
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
