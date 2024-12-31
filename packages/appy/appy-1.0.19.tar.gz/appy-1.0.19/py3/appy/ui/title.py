'''Object's field "title" requires a specific treatment in order to be rendered
   in the user interface.'''

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
from appy.ui.criteria import Criteria

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Title:
    '''Manages the zone, within lists and grids, rendering the title of an
       object and everything around it (sup- and sub-titles).'''

    @staticmethod
    def showToggleSub(class_, field, tool, from_=None):
        '''Show icon "toggle sub-titles" when toggling sub-titles is enabled'''
        return field.name == 'title' and class_.toggleSubTitles(tool, from_)

    # Icon for hiding / showing the "sub-title" zone under an object's title
    pxToggleSub = Px('''
     <span onClick="toggleSubTitles()" class="clickable iconS">👀</span>''',

     js='''
      // Function that sets a value for showing/hiding sub-titles
      setSubTitles = function(value, tag) {
        createCookie('showSubTitles', value);
        // Get the sub-titles
        var subTitles = document.getElementsByClassName('subTitle');
        if (subTitles.length == 0) return;
        // Define the display style depending on p_tag
        var displayStyle = 'inline';
        if (tag == 'tr') displayStyle = 'table-row';
        for (var i=0; i < subTitles.length; i++) {
          if (value == 'True') subTitles[i].style.display = displayStyle;
          else subTitles[i].style.display = 'none';
        }
      }

      // Function that toggles the value for showing/hiding sub-titles
      toggleSubTitles = function(tag) {
        // Get the current value
        var value = readCookie('showSubTitles') || 'True';
        // Toggle the value
        var newValue = (value == 'True')? 'False': 'True';
        if (!tag) tag = 'div';
        setSubTitles(newValue, tag);
      }''')

    @classmethod
    def getClassAttribute(class_, base, more, isSelect):
        '''Create the "class" attribute for the title link, based on CSS classes
           potentially defined in p_base and p_more.'''
        # p_isSelect is True if we are in "select" mode (see p_get)
        r = base or ''
        if more:
            space = ' ' if r else ''
            r = f'{r}{space}{more}'
        if isSelect:
            space = ' ' if r else ''
            r = f'{r}{space}clickable'
        return f' class="{r}"' if r else ''

    @classmethod
    def getIcon(class_, o, base, params, target):
        '''Compute, when appropriate, a companion, iconic link, for opening the
           same link, but in a popup.'''
        if not target.otherClick: return ''
        params['popup'] = 'True'
        return f'<a href="{class_.getUrl(o, base, params)}" class="pop" ' \
               f'target="appyIFrame" onclick="{target.otherClick}">◳</a>'

    @classmethod
    def getUrl(class_, o, base, params):
        '''Builds the URL to p_o'''
        # Build the standard URL to p_o or patch p_base URL, if passed
        if base is None:
            r = o.getUrl(sub='view', **params)
        else:
            r = o.H().server.patchUrl(base, **params)
        return r

    @classmethod
    def get(class_, o, mode='link', nav='no', target=None, page='main',
            popup=False, baseUrl=None, title=None, linkTitle=None, css=None,
            selectJs=None, highlight=False, backHook=None, maxChars=None,
            pageLayout=None):
        '''Gets p_o's title as it must appear in lists of objects (ie in
           lists of tied objects in a Ref, in search results...).'''

        # In most cases, a title must appear as a link that leads to the object
        # view layout. In this case (p_mode == "link"):
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # p_nav        | is the navigation parameter allowing navigation between
        #              | this object and others;
        # p_target     | specifies if the link must be opened in the popup or
        #              | not. It is an instance of appy.ui.LinkTarget;
        # p_page       | specifies which page to show on the target object view;
        # p_popup      | indicates if we are already in the popup or not;
        # p_baseUrl    | indicates a possible alternate base URL for accessing
        #              | the object;
        # p_title      | specifies, if given, an alternate content for the "a"
        #              | tag (can be a PX);
        # p_linkTitle  | specifies a possible value for attribute "link" for the
        #              | "a" tag (by default this attribute is not dumped);
        # p_css        | can be the name of a CSS class to apply (also for other
        #              | modes);
        # p_maxChars   | gives an (optional) limit to the number of visible
        #              | title chars.
        # p_pageLayout | allows to override the standard "view" page layout as
        #              | defined on p_o's class.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        # Another p_mode is "select". In this case, we are in a popup for
        # selecting objects: every title must not be a link, but clicking on it
        # must trigger Javascript code (in p_selectJs) that will select this
        # object.
        isSelect = mode == 'select'

        # The last p_mode is "text". In this case, we simply show the object
        # title but with no tied action (link, select). If we are already in the
        # popup and the target is the popup, because we have a single level of
        # popups for now on, displaying a link will not be possible.
        toPopup = target and target.target != '_self' and not isSelect
        if popup and toPopup: mode = 'text'

        # If p_highlight is True, keywords will be highlighted if we are in the
        # context of a query with keywords.

        # If the class_ whose elements must be listed has an attribute
        # "uniqueLinks" being True, in "link" mode, the generated link will
        # include an additional parameter named "_hash". This parameter will
        # ensure that the link will be different every time it is generated.
        # This is useful for short-circuiting the a:visited CSS style when an
        # app wants to manage link's style in some specific way.
        handler = o.H()
        oclass = o.class_

        # Compute the "class" attribute
        tcss = oclass.getCssFor(o, 'title')
        classAttr = class_.getClassAttribute(tcss, css, isSelect)

        # Get the title, with highlighted parts when relevant
        titleIsPx = False
        if not title:
            title = oclass.getListTitle(o, nav)
        elif isinstance(title, Px):
            title = title(handler.traversal.context)
            titleIsPx = True
        if highlight and not titleIsPx:
            title = Criteria.highlight(handler, title)
        if maxChars: title = Px.truncateText(title, width=maxChars)
        if mode == 'plink':
            # A link to stay in the public part of the site
            url = f'{o.tool.url}/public?rp={o.iid}'
            r = f'<a href="{url}">{title}</a>'
        elif mode.endswith('link'): # "link" or "dlink"
            params = {'page': page, 'nav': nav, 'popup': toPopup,
                      'unique': oclass.produceUniqueLinks()}
            if pageLayout: params['pageLayout'] = pageLayout
            # Build the link URL, or patch the given p_baseUrl
            url = class_.getUrl(o, baseUrl, params)
            # Define attribute "onClick"
            if target.onClick:
                oc = target.getOnClick(backHook or str(o.iid), o)
                onClick = f' onclick="{oc}"'
            else:
                onClick = ''
            # Set a "title" parameter when relevant
            lt = f' title="{linkTitle}"' if linkTitle else ''
            # Add a companion icon when appropriate
            icon = class_.getIcon(o, baseUrl, params, target)
            if mode[0] == 'd':
                # Wrap the link into a "div". In that case, the CSS class(es)
                # apply to the div.
                start = f'<div{classAttr}>{icon}<a'
                end = '</a></div>'
            else:
                start = f'{icon}<a{classAttr}'
                end = '</a>'
            # Link target: land if we are in the popup and we must not go to it
            r = f'{start} name="title" href="{url}" ' \
                f'target="{target.get(popup, toPopup)}"' \
                f'{onClick}{lt}>{title}{end}'
        elif isSelect:
            r = f'<span onclick="{selectJs}"{classAttr}>{title}</span>'
        elif mode == 'text':
            r = f'<span{classAttr}>{title}</span>'
        return r
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
