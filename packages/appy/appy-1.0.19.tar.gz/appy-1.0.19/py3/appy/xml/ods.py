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

from appy.xml import Parser
from appy.utils.zip import unzip
from appy.utils import path as putils

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Sheet:
    '''Represents a single sheet within a spreadsheet document'''

    def __init__(self, name):
        self.name = name
        # Rows, as a list of lists
        self.rows = []

    def __repr__(self):
        '''p_self as a short string'''
        return f'‹Sheet {self.name} • {len(self.rows)} row(s)›'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Ods(Parser):
    '''Parses an ODS file and produces a dict of Sheet objects, keyed by sheet
       names.'''

    # Within an ODS file, at the end of a row, LibreOffice may define a cell
    # with a very high column-repeat-number. This technique reveals a fake
    # number that will be ignored if higher than the following value.
    COL_REP_MAX = 200

    def startDocument(self):
        '''Initialises the result'''
        super().startDocument()
        self.r = {} # ~{s_name: Sheet}~
        # The currently walked sheet
        self.currentSheet = None
        # The currently walked row within the currently walked sheet
        self.currentRow = None
        # Are we parsing a cell ?
        self.inCell = False
        # How many rows does the current cell span ?
        self.rowSpan = 1
        # Within a cell, are we in a paragraph ?
        self.inP = False
        # Content for the currently walked cell within the currently walked row
        self.currentContent = ''

    def getRowSpan(self, attrs):
        '''Extracts the row span from p_attrs, found on a table:table-cell
           tag.'''
        r = attrs.get('table:number-columns-repeated')
        if r:
            r = int(r)
            if r > Ods.COL_REP_MAX:
                r = 1
        else:
            r = 1
        return r

    def startElement(self, tag, attrs):
        '''This start p_tag has been encountered, with these p_attrs'''
        if tag == 'table:table':
            # A new sheet is encountered
            name = attrs['table:name']
            sheet = Sheet(name)
            self.r[name] = sheet
            self.currentSheet = sheet
        elif tag == 'table:table-row':
            # A new row is encountered
            self.currentRow = row = []
            self.currentSheet.rows.append(row)
        elif tag == 'table:table-cell':
            self.inCell = True
            self.currentContent = ''
            self.rowSpan = self.getRowSpan(attrs)
        elif tag == 'text:p':
            self.inP = True

    def endElement(self, tag):
        '''This end p_tag has been encountered'''
        if tag == 'table:table':
            self.currentSheet = None
        elif tag == 'table:table-row':
            self.currentRow = None
        elif tag == 'table:table-cell':
            # Dump as many cells as p_self.rowSpan
            for i in range(self.rowSpan):
                self.currentRow.append(self.currentContent)
            self.currentContent = ''
            self.inCell = False
        elif tag == 'text:p':
            self.inP = False

    def characters(self, content):
        '''This tag p_content was encountered'''
        if self.inCell and self.inP:
            self.currentContent = f'{self.currentContent}{content}'

    def parse(self, path, port=None):
        '''Parses an ODS, XLS or XLSX file at this p_path, being the file's
           absolute path expressed as a string or pathlib.Path object. Returns a
           list of Sheet objects.'''
        # When p_path is an Excel file, LibreOffice will be called on localhost,
        # on this p_port, to convert the file to ODS. If p_port is None, a
        # default one will be used, as defined in appy/pod/converter.py.
        #
        # Ensure p_path is a Path object
        if isinstance(path, str):
            path = Path(path)
        # Create a folder in the OS temp folder
        folder = putils.getOsTempFolder(sub=True, asPath=True)
        # Convert the file to ODS if it is an XLS or XLSX file
        name = path.name.lower()
        if name.endswith('.xls') or name.endswith('.xlsx'):
            from appy.pod.converter import Converter
            ods = folder / f'{path.stem}.ods'
            Converter(str(path), str(ods), port=port).run()
            path = ods
        # Extract the content.xml file within the ODS file being a zip file
        contentXml = unzip(path, folder, odf=True)['content.xml']
        # Delete p_folder and its content
        putils.FolderDeleter.delete(folder)
        # Parse content.xml and produce the result
        return super().parse(contentXml)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
