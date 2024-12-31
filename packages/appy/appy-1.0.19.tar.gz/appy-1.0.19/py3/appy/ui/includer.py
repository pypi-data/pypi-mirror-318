'''Includes external static files (CSS, JS) into HTML pages'''

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
F_FILE_KO   = 'Appy does not have custom font "%s".'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Includer:
    '''Produces chunks of XHTML for including external files like CSS and
       Javascript files.'''

    # Custom Appy fonts
    fonts = {'NimbusSans-NBV': 'appy/NimbusSans-NBV.otf'}

    @classmethod
    def css(class_, url, version=None):
        '''Produces a chunk of XHTML for including CSS file with this p_url'''
        v = f'?{version}' if version else ''
        return f'<link rel="stylesheet" type="text/css" href="{url}{v}"/>'

    @classmethod
    def js(class_, url, version=None):
        '''Produces a chunk of XHTML for including JS file with this p_url'''
        v = f'?{version}' if version else ''
        return f'<script src="{url}{v}"></script>'

    @classmethod
    def vars(class_, tool):
        '''Defines the global Javascript variables being declared in every Appy
           page.'''
        return f'<script>var siteUrl="{tool.siteUrl}", sameSite="' \
               f'{tool.config.server.sameSite}"</script>'

    @classmethod
    def getFontFaces(class_, tool, fonts):
        '''Generate font-face at-rules, for every font defined in p_fonts'''
        r = ''
        for font in fonts:
            fontFile = class_.fonts.get(font)
            if not fontFile:
                tool.log(F_FILE_KO % font, type='warning')
                continue
            url = f'{tool.siteUrl}/static/{fontFile}'
            r = f'{r}@font-face {{font-family:"{font}"; src:url("{url}") ' \
                f'format("opentype")}}'
        return f'<style>{r}</style>'

    @classmethod
    def getGlobal(class_, handler, config, dir):
        '''Returns a chunk of XHTML code for including, within the main page
           template, CSS and Javascript files.'''
        r = []
        tool = handler.tool
        sconfig = config.server.static
        # Get CSS files
        ltr = dir == 'ltr'
        # Get global CSS files from dict Static.ram. Indeed, every CSS file is
        # patched from a template and stored in it.
        for name in handler.Static.ram.keys():
            if name.endswith('.css'):
                # Do not include appyrtl.css, the stylesheet specific to
                # right-to-left (rtl) languages, if the language is
                # left-to-right.
                if ltr and name == 'appyrtl.css':
                    continue
                r.append(class_.css(tool.buildUrl(name, ram=True),
                                    version=sconfig.versions.get(name)))
        # Get CSS include for Google Fonts, when some of them are in use
        ui = config.ui
        if ui.googleFonts:
            r.append(class_.css(ui.getFontsInclude()))
        # Get Javascript files
        for base, path in sconfig.map.items():
            for jsFile in path.glob('*.js'):
                r.append(class_.js(tool.buildUrl(jsFile.name, base=base),
                                   version=sconfig.versions.get(jsFile.name)))
        # Get font-face declarations, when relevant
        if ui.customFonts:
            r.append(class_.getFontFaces(tool, ui.customFonts))
        # Initialise global JS variables
        r.append(class_.vars(tool))
        return '\n'.join(r)

    @classmethod
    def getUrl(class_, url, tool):
        '''Gets an absolute URL based on p_url, that can already be absolute or
           not.'''
        return url if url.startswith('http') else tool.buildUrl(url)

    @classmethod
    def getSpecific(class_, tool, css, js):
        '''Returns a chunk of XHTML code for including p_css and p_js files
           specifically required by some fields.'''
        r = []
        if css:
            for url in css: r.append(class_.css(class_.getUrl(url, tool)))
        if js:
            for url in js:  r.append(class_.js(class_.getUrl(url, tool)))
        return '\n'.join(r)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
