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
from appy.model.base import Base
from appy.model.user import User
from appy.model.fields import Show
from appy.model.query import Query
from appy.xml.escape import Escape
from appy.model.fields.pod import Pod
from appy.model.fields.rich import Rich
from appy.model.fields.file import File
from appy.model.fields.info import Info
from appy.model.document import Document
from appy.model.carousel import Carousel
from appy.model.fields.group import Group
from appy.ui.layout import Layout, Layouts
from appy.model.fields.select import Select
from appy.model.fields.string import String
from appy.model.fields.boolean import Boolean
from appy.model.fields.integer import Integer
from appy.model.fields.ref import Ref, autoref
from appy.model.fields.computed import Computed
from appy.model.fields.phase import Page as FPage
from appy.model.workflow.standard import Anonymous

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
EXPR_ERR = 'Page "%s" (%s): error while evaluating page expression "%s" (%s).'
EDITED   = 'Page %d %s within %s.'
DELETED  = 'Web page %s deleted.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Page(Base):
    '''Base class representing a web page'''

    # By default, web pages are public
    workflow = Anonymous

    pa = {'label': 'Page'}

    @staticmethod
    def getListColumns(tool):
        '''Show minimal info for the anonymous user'''
        if tool.user.isAnon(): return ('title',)
        return ('title', 'expression', 'next', 'selectable*100px|',
                'podable*80px|', 'viewCss*100px|')

    listColumns = getListColumns

    # An alternate, shorter list of columns
    listColumnsShort = 'title', 'expression', 'next', 'state'

    # The POD ouput
    doc = Pod(template='*model/pod/Page.odt', formats=('pdf',), show=False,
              layouts=Pod.Layouts.inline, freezeTemplate=lambda o,tpl: ('pdf',))

    @staticmethod
    def update(class_):
        '''Configure field "title"'''
        title = class_.fields['title']
        title.show = Show.EX
        title.label = 'Page'
        title.page.show = lambda o: True if o.allows('write') else 'view'
        title.page.sticky = True

    # The POD output appears inline in the sub-breadcrumb
    def getSubBreadCrumb(self):
        '''Display an icon for downloading this page (and sub-pages if any) as a
           POD.'''
        if self.podable: return self.getField('doc').doRender('view', self)

    def getSubTitle(self):
        '''Render a link to the tied carousel and/or search'''
        r = []
        esc = Escape.xhtml
        for name in ('carousel', 'query'):
            if not self.isEmpty(name):
                o = getattr(self, name)
                label = self.translate(self.getField(name).labelId)
                r.append('<div class="discreet">%s: <a href="%s">%s</a></div>' \
                         % (esc(label), o.url, esc(o.getShownValue())))
        return '\n'.join(r)

    def getTitle(self, maxChars=None, nbsp=False):
        '''Returns p_self's title, shortened'''
        r = self.getShownValue()
        maxChars = maxChars or self.config.ui.pageChars
        r = Px.truncateValue(r, width=maxChars)
        if nbsp: r = r.replace(' ', ' ')
        return r

    # A warning: image upload is impossible while the page is temp
    warning = Info(show=lambda o: 'edit' if o.isTemp() else None,
                   focus=True, layouts=Info.Layouts.n, **pa)

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                           Linked carousel
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def showCarousel(self):
        '''Show field "carousel" if carousels are defined'''
        if self.tool.isEmpty('carousels'): return
        # Do not show it (except on "edit") if there is no tied carousel
        return True if not self.isEmpty('carousel') else 'edit'

    carousel = Ref(Carousel, add=False, link=True, render='links',
      select=lambda o: o.tool.carousels, shownInfo=Carousel.pageListColumns,
      show=showCarousel, layouts=Layouts.fvd,
      view=Px('''<x var="o=o.carousel">:o.pxView</x>'''),
      back=Ref(attribute='pages', multiplicity=(0,None), render='links',
               group=Carousel.mainGroup, label='Carousel'), **pa)

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                            Page content
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    content = Rich(documents='documents', height='350px', inject=True,
                   show=lambda o: 'edit' if o.isEmpty('content') else True,
                   viewCss=lambda o: o.viewCss, viewSingle=True,
                   layouts=Rich.Layouts.f, **pa)

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                           Linked search
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def showQuery(self):
        '''Show field "query" if queries are defined'''
        if self.tool.isEmpty('queries'): return
        # Do not show it (except on "edit") if there is no tied carousel
        return True if not self.isEmpty('query') else 'edit'

    query = Ref(Query, add=False, link=True, render='links',
      select=lambda o: o.tool.queries, shownInfo=Query.pageListColumns,
      show=showQuery, layouts=Layouts.fvd,
      view=Px('''<x var="o=o.query">:o.pxView</x>'''),
      back=Ref(attribute='pages', multiplicity=(0,None), render='links',
               group=Query.mainGroup, label='Query'), **pa)

    def forRootOnEdit(self):
        '''Determines visibility of some fields, on the "edit" layout, for root
           pages only.'''
        return Show.V_ if self.isRoot() else None

    # Is this (root) page selectable in the main dropdown ?
    selectable = Boolean(default=True, show=forRootOnEdit,
                         layouts=Boolean.Layouts.d, **pa)

    # Is PDF POD export enabled for this page ? Sub-pages can be individually
    # exported.
    podable = Boolean(layouts=Boolean.Layouts.d, show=Show.V_, **pa)

    # Maximum width for images uploaded and rendered within the XHTML content
    maxWidth = Integer(default=700, show=False)

    # If this Python expression returns False, the page can't be viewed
    def showExpression(self):
        '''Show the expression to managers only'''
        # Do not show it on "view" if empty
        if self.isEmpty('expression'): return Show.V_
        return self.allows('write')

    expression = String(layouts=Layouts.d, show=showExpression, **pa)

    # Name of the CSS class applied to the page content, when rendered on view
    # or cell layouts.
    viewCss = String(default='xhtml', layouts=Layouts.d, show=Show.V_, **pa)

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                           Inner images
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # The images (or other documents) that may be included in field "content"
    documents = Ref(Document, add=True, link=False, multiplicity=(0,None),
      composite=True, back=Ref(attribute='page', show=False, label='Document'),
      showHeaders=True, shownInfo=Document.listColumns, actionsDisplay='inline',
      page=FPage('images', show=lambda o:'view' if o.allows('write') else None),
      rowAlign='middle', **pa)

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                         Background image
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # In most cases, when a page is shown, like any other object, the background
    # image possibly applied is baseBG.jpg. On public root pages, no background
    # is shown: the one uploaded here may be used instead.
    bip = {'page': FPage('bg', show=lambda o: o.allows('write') and o.isRoot()),
           'group': Group('main', style='grid', hasLabel=False),
           'layouts': Layouts.gd }
    bip.update(pa)

    backgroundImage = File(isImage=True, viewWidth='700px', cache=True, **bip)

    # When the background image hereabove is used, the following parameter
    # determines how it is rendered. It is the equivalent of CSS attribute
    # "background-size".
    backgroundSize = Select(validator=('cover', 'auto'), default='cover', **bip)

    def initialiseLocalPage(self, req):
        '''A page can be specifically rendered as a root public page or as
           an inner page of such a root page. In these cases, the rendering
           context must be adapted.'''
        # p_self may propose a specific background image
        if not self.isEmpty('backgroundImage'):
            style = 'background-image:url(%s/backgroundImage/download); ' \
                    'background-repeat:no-repeat; background-size:%s' % \
                    (self.url, self.backgroundSize)
        else:
            style = None
        # Use a minimal page layout that only includes the "w" part (=widgets)
        req.pageLayout = Layout('w', style=style)
        # Avoid including global page elements: they have already been included
        # by the enclosing element.
        req.notGlobal = True

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                            Next page
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Pages can be chained, in order to produce a single, composite page.
    # Chained pages must all be in the same container object.

    def listSiblings(self):
        '''Returns the pages being p_self's siblings'''
        return [page for page in self.container.pages if page != self]

    def hasContainer(self):
        '''Some fields can't be shown while a page has no container, which can
           happen when creating a page from the porlet.'''
        return Show.V_ if self.container else None

    next = Ref(None, add=False, link=True, layouts=Layouts.fvd, render='links',
               back=Ref(attribute='previous', render='links',
                        label='Page', show=Show.VE_),
               show=hasContainer, select=listSiblings, **pa)

    def getChain(self):
        '''Returns the list of pages being chained to p_self via "next" fields,
           recursively.'''
        r = [self]
        next = self.next
        return r + next.getChain() if next else r

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                            Sub-pages
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # A page can contain sub-pages
    def showSubPages(self):
        '''For non-writers, show sub-pages only if present'''
        if self.allows('write'):
            # Show it, unless the page is rendered as the next page of a
            # previous one.
            return not self.req.notGlobal
        if not self.isEmpty('pages'): return 'view'

    pages = Ref(None, multiplicity=(0,None), add=True, link=False,
      composite=True, back=Ref(attribute='parent', show=False, **pa),
      showHeaders=True, actionsDisplay='inline', show=showSubPages,
      numbered=True, checkboxes=lambda o: o.allows('write'),
      titleMode=lambda o: 'plink' if o.container.inPublic(True) else 'link',
      toggleSubTitles=False, **pa)

    def getParents(self, includeMyself=True):
        '''Returns, as a set, p_self's parents, including p_self itself if
           p_includeMyself is True.'''
        r = {self} if includeMyself else set()
        return r if self.isRoot() else r.union(self.container.getParents())

    def mayView(self):
        '''In addition to the workflow, evaluating p_self.expression, if
           defined, determines p_self's visibility.'''
        expression = self.expression
        if not expression: return True
        user = self.user
        try:
            return eval(expression)
        except Exception as err:
            message = EXPR_ERR % (self.title, self.id, expression, str(err))
            self.log(message, type='error')
            return True

    def getMergedContent(self, r=None, level=1):
        '''Returns a list of chunks of XHTML code, one for p_self and one for
           each of its sub-pages, recursively.'''
        # More precisely, the r_result is a list of tuples of the form
        #
        #                   ~(xhtmlChunk, i_delta)~
        #
        #, "delta" being the delta to apply to the title's outline levels,
        # depending on the depth of the page within the complete tree of pages.
        #
        # p_level is the current level of recursion, while p_r is the current
        # list under creation. Indeed, in order to avoid concatenating lists, at
        # each m_getMergedContent call, the current p_r(esult) is passed.
        #
        # This method is notably called by appy/model/pod/Page.odt
        if r is None:
            # We are at the start of a recursive merge: there is no result yet.
            # Create it.
            r = []
        # Two pieces of information must be collected about p_self: its title
        # and content.
        if level > 1:
            # At level 1, do not dump the title
            title = self.getValue('title', type='shown')
            r.append(('<h1>%s</h1>' % Escape.xhtml(title), level-2))
        # Add p_self's content
        if not self.isEmpty('content'):
            r.append((self.getValue('content', type='shown'), level-1))
        # Add sub-pages
        if not self.isEmpty('pages'):
            for page in self.pages:
                page.getMergedContent(r, level=level+1)
        return r

    # Link allowing, when a sub-page is shown in the "public" PX, to go back to
    # the parent page.

    def showToParent(self):
        '''Show link "to parent" on for a sub-page being rendered via the
           "public" PX.'''
        return 'view' if self.parent and self.inPublic() else None

    def getToParent(self):
        '''Get a link allowing to navigate to p_self's parent page'''
        text = self.getLabel('toParent')
        url = self.parent.getAccessUrl()
        return f'<a href="{url}">↥ {text}</a>'

    toParent = Computed(show=showToParent, method=getToParent, layouts='f')

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                                Editors
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # "Editors" are users being allowed to edit this page and its sub-pages.
    # These users are granted local role Owner on the page and its sub-pages. If
    # you use an alternate worklow for pages, ensure role Owner may edit pages.

    def linkEditor(self, user):
        '''Set this new editor as p_self's owner'''
        self.localRoles.add(user.login, 'Owner')
        for page in self.pages:
            page.linkEditor(user)

    def unlinkEditor(self, user):
        '''ungrant to p_user the possibility to edit p_self'''
        if user.login != self.creator:
            self.localRoles.delete(user.login, 'Owner')
        for page in self.pages:
            page.unlinkEditor(user)

    # Users allowed to edit this page and its sub-pages
    editors = Ref(User, add=False, link='popup', multiplicity=(0,None),
      afterLink=linkEditor, afterUnlink=unlinkEditor,
      back=Ref(attribute='editablePages', multiplicity=(0,None),
               page=FPage('editablePages', show=User.showEPages),
               layouts=Layouts.dv, actionsDisplay='inline',
               showHeaders=True, shownInfo=listColumnsShort, label='User'),
      showHeaders=True, shownInfo=User.listColumnsShort,
      actionsDisplay='inline', layouts=Layouts.dv,
      page=FPage('editors',
                 show=lambda o: 'view' if o.user.hasRole('Manager') else None),
      **pa)

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #                               Main methods
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    # The URL path to the public PX
    publicPath = ['tool', 'public']

    def getAccessUrl(self, forcePublic=False):
        '''Return the URL being appropriate to access p_self, one of p_self.url
           and the one shown via the tool's public PX.'''
        if self.config.ui.discreetLogin:
            public = forcePublic
        else:
            public = self.user.isAnon()
        return f'{self.tool.url}/public?rp={self.iid}' if public else self.url

    def inPortlet(self, selected, level=0):
        '''Returns a chunk of XHTML code for representing this page in the
           portlet, in a root class zone.'''
        # Is this page currently selected ? A selected page is the page being
        # currently consulted on the site or any of its parent pages.
        isSelected = self in selected
        # A specific CSS class wil be applied for a selected page
        css = ' class="current"' if isSelected else ''
        # If p_self has parents, we must render it with a margin-right
        style = f' style="margin-left:{level*8}px"' if level else ''
        url = self.getAccessUrl()
        title = Escape.xhtml(self.getShownValue())
        r = [f'<div{style}><a href="{url}"{css}>{title}</a></div>']
        if isSelected and not self.isEmpty('pages'):
            for sub in self.pages:
                r.append(sub.inPortlet(selected, level+1))
        return ''.join(r)

    def isRoot(self):
        '''Is p_self a root page ?'''
        # A page created from the portlet (if class Page is declared as root)
        # has no container when under creation.
        container = self.container
        return not container or container.class_.name != 'Page'

    def inPublic(self, orParent=False):
        '''Is p_self (or one of its parents if p_orParent is True) currently
           shown on the "public" page ?'''
        # Get the ID of the page being currently shown on the "public" page
        rp = self.req.rp
        if not rp: return
        # Does v_rp correspond to p_self ?
        r = rp == str(self.iid)
        if r: return r
        # [only if p_orParent is True] Does p_rp correspond to some ancestor of
        #                              p_self ?
        if orParent and self.parent:
            r = self.parent.inPublic(orParent=True)
        return r

    def onEdit(self, created):
        '''Link the page among root pages if created from the portlet'''
        if created and not self.initiator:
            self.tool.link('pages', self)
        verb = 'created' if created else 'edited'
        self.log(EDITED % (self.id, verb, self.container.iid))

    def onDelete(self):
        '''Log the page deletion'''
        self.log(DELETED % self.id)

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #  PXs
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    # This selector allows to choose one root page among published tool.pages
    pxSelector = Px('''
      <a for="page in pagesL" title=":page.getShownValue()"
         href=":page.url if inlaidHeader else page.getAccessUrl(True)">
       <span class=":'upage' if page.inPublic() else
         ('current' if o==page else '')">:page.getTitle(nbsp=True)</span>
      </a>
      <select onchange="gotoURL(this)" if="pagesO">
       <option value="">:_('goto_link')</option>
       <option for="page in pagesO"
               value=":page.url if inlaidHeader else page.getAccessUrl(True)"
               selected=":o == page if inlaidHeader else page.inPublic()"
               title=":page.getShownValue()">:page.getTitle(
                 maxChars=config.ui.pageCharsS)</option>
      </select>''',

     css = '''.upage { text-decoration:underline #afb8d4;
                       text-underline-offset:6px }''',
     js='''
       function gotoURL(select) {
         var url = select.value;
         if (url) goto(url);
       }''')

    # PX showing all root pages in the portlet, when shown for pages
    portletBottom = Px('''
     <div class="topSpaceS"
          var="pages=tool.OPage.getRoot(tool, mobile, splitted=False)">
      <x if="pages"
         var2="selected=o.getParents() if o.class_.name == 'Page' else {}">
       <x for="page in pages">::page.inPortlet(selected)</x>
      </x>
      <i if="not pages">:_('no_page')</i>
     </div>''')

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #  Class methods
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    @classmethod
    def getRoot(class_, tool, mobile, splitted=True):
        '''Return the root, selectable pages being visible by the logged user,
           among the site's root pages from p_tool.pages.'''
        # If p_splitted is True, pages will be returned in 2 distinct lists:
        # - the first one will contain those that must be rendered as "a" tags;
        # - the second one will contain those that must be rendered as options
        #   in a HTML "select" control.
        #
        # Choosing which page to put in which list is determined by parameter
        # p_tool.config.expandedRootPages.
        #
        # Return the cached version (for the p_splitted variant only), if
        # available.
        key = 'appyRootPagesS' if splitted else 'appyRootPages'
        cache = tool.cache
        if key in cache: return cache[key]
        if splitted:
            # Compute 2 sub-lists
            links = []
            options = []
            # Determine the maximum number of pages to render as links
            linksCount = 0 if mobile else tool.config.ui.expandedRootPages
        else:
            # Return a single list
            r = []
        # Walk root pages
        guard = tool.guard
        for page in tool.pages:
            # Ignore the page, if unselectable or unviewable
            if not page.selectable or not guard.mayView(page): continue
            if splitted:
                # Put the page in v_links or v_options
                if linksCount == 0:
                    options.append(page)
                else:
                    links.append(page)
                    linksCount -= 1
            else:
                r.append(page)
        # Cache and return the result
        if splitted:
            r = (links, options)
        cache[key] = r
        return r

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
autoref(Page, Page.next)
autoref(Page, Page.pages)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
