'''The UiSearch class and satellite classes constitute a runtime layer on top
   of the Search class.'''

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
from appy.model.searches.modes import Mode
from appy.model.searches import initiators

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class MayAdd:
    '''This class answers the question: may the user create a new instance of
       some class on a page showing search results ?'''

    # The answer to the question is not simply "yes" or "no"
    NO     = 0
    SEARCH = 1 # Yes: we are on a search with add=True: instances can be
               # created from it, to be tied to the current container object
    REF    = 2 # Yes: we are in a popup for selecting an object to be tied via a
               # Ref, but the object we want does not exist and it can be
               # created by the user.

    def __init__(self, ui):
        # May instances be added? One of the hereabove constants is stored here.
        self.value = MayAdd.NO
        # If yes (MayAdd.REF) and if the object must not be created in the
        # initiator Ref, store info about the alternate initiator.
        self.io = self.ifield = None
        # If MayAdd.REF, the JS code to execute when coming back from the popup
        # is not the standard one: the specific code to execute will be stored
        # in the following attribute.
        self.backCode = None
        # When MayAdd.REF, the "inav" (*i*nitiator *nav*igation) string allows
        # to remember the Ref object being at the start of the whole process.
        # While "backCode" is meant to be used by the browser, inav is meant to
        # be used by the web server.
        self.inav = ''
        self.compute(ui)

    def compute(self, ui):
        '''Compute p_self.value for the current c.uiSearch'''
        if ui.search.add:
            # We are in the case SEARCH
            self.value = MayAdd.SEARCH
        else:
            # Are we in the case REF ? In other words, is the search used to
            # select objects to be inserted into a Ref field being add=True ?
            init = ui.initiator
            if not init or not isinstance(init, initiators.RefInitiator): return
            ifield = init.field
            if not ifield.add: return
            # Get the base object and field from which to create this object,
            # if different from the current Ref.
            insert = ifield.insert
            if isinstance(insert, tuple) and insert[0] == 'field':
                io, ifield = insert[1](init.o)
                # Ensure the user is allowed to modify this Ref
                if io.allows(ifield.writePermission):
                    self.io = io
                    self.ifield = ifield
                    self.value = MayAdd.REF
                else:
                    self.value = MayAdd.NO
            else:
                # The user is already selecting an object to insert in the
                # current Ref: consequently, he is already allowed to modify it.
                self.value = MayAdd.REF
            # Initialise attributes "backCode" and "inav" when relevant
            if self.value:
                self.backCode = "setBackCode('%s','%s',id)" % \
                                (init.hook, init.o.iid)
                self.inav = init.o.req.search

    def __bool__(self): return bool(self.value)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class UiSearch:
    '''Instances of this class are generated on-the-fly for manipulating a
       Search instance from the User Interface.'''

    # Make some classes available here
    Mode = Mode
    MayAdd = MayAdd

    # Rendering a search
    view = Px('''
     <div class="portletSearch">
      <a href=":'%s?className=%s&amp;search=%s' % \
                 (queryUrl, className, search.name)"
         class=":'current' if search.name == currentSearch else ''"
         onclick="clickOn(this)"
         title=":search.translatedDescr">:search.translated</a>
     </div>''')

    # Render search results
    pxResult = Px('''
     <x var="layout='view';
             batch=mode.batch;
             empty=mode.empty;
             search=uiSearch.search;
             class_=search.container;
             mayAdd=uiSearch.MayAdd(uiSearch);
             showNewSearch=showNewSearch|True;
             showHeaders=showHeaders|True;
             showTop=not popup or mayAdd;
             showNav=batch and batch.showNav();
             descr=uiSearch.translatedDescr;
             totals=uiSearch.getRunningTotals(mode);
             specific=uiSearch.getResultsTop(mode, ajax)">

     <!-- Application, class-specific code before displaying results -->
     <x if="specific">::specific</x>

     <!-- Search results -->
     <div id=":mode.hook">
      <script>::mode.getAjaxData()</script>

      <!-- The top zone -->
      <div if="showTop" class=":'' if popup else 'sTop'">

       <!-- Title -->
       <div if="not popup and search.showTitle" class="pageTitle">
        <x>::uiSearch.translated</x>
        <x if="mode.batch and not empty">
         <span var="css=class_.getCssFor(tool, 'sep')"
               class=":f'navSep {css}' if css else 'navSep'">//</span>
         <span class="btot">:mode.batch.total</span>
        </x>
        <!-- Search description -->
        <img if="descr" src=":svg('detail')" class="sdetail" title=":descr"/>

        <!-- Class-specific colored border (*t*itle *bot*tom) -->
        <div var="css=class_.getCssFor(tool, 'tbot')"
             if="css" class=":f'tbot {css}'"></div>
       </div>

       <!-- Search description in the popup -->
       <div class="discreet" if="popup and descr">::descr</div>

       <!-- Icons -->
       <x if="search.showTitle">

        <!-- Switch mode -->
        <div if="not mode.empty and len(resultModes) &gt; 1" class="smodes">
         <img for="cls in mode.getClasses(resultModes)"
              if="mode.name != cls.name" name=":cls.name"
              title=":cls.getText(_)" src=":svg(cls.icon)"
              class="clickable iconM" onclick="switchMode(this)"/>
        </div>

        <!-- Add a new object -->
        <div if="mayAdd and guard.mayInstantiate(class_)"
             var2="buttonType='small'; label=search.addLabel;
                   viaPopup=False if mayAdd else search.viaPopup;
                   nav=mode.getNavInfo(batch.total, mayAdd); inav=mayAdd.inav;
                   onClick=mayAdd.backCode">:class_.pxAdd</div>

        <!-- Perform a new search -->
        <div if="showNewSearch and mode.newSearchUrl">
         <a href=":mode.newSearchUrl">:_('search_new')</a>
         <x if="mode.fromRef and not mode.inField">&nbsp;&mdash;&nbsp; 
          <a href=":mode.getRefUrl()">:_('goto_source')</a></x>
        </div>
       </x>

       <!-- (Top) navigation -->
       <div if="showNav and uiSearch.showTopNav and not mayAdd" class="snav"
            style=":search.getNavMargins()">:mode.batch.pxNavigate</div>

       <!-- Pod templates -->
       <x if="not empty and not popup and search.showPods and mode.objects">
        <div var="info=class_.getListPods(tool)" class="spod" if="info">
          <x var="o=mode.objects[0]" for="field, visible in info.items()"
             var2="fieldName=field.name">:field.pxRender</x>
        </div>
       </x>
      </div>

      <!-- Results -->
      <x if="not empty" var2="currentNumber=0">:mode.px</x>

      <!-- (Bottom) navigation -->
      <div if="not empty and showNav and uiSearch.showBottomNav"
           class="snab" var2="scrollTop='payload'"
           align=":search.navAlign">:mode.batch.pxNavigate</div>

      <!-- No result -->
      <div if="empty">::_(search.noResultLabel)</div>
     </div></x>''')

    def __init__(self, search, tool, ctx, initiator=None, name=None):
        self.search = search
        self.container = search.container
        self.tool = tool
        self.req = tool.req
        self.dir = ctx.dir
        self.popup = ctx.popup
        # "name" can be more than the p_search name, ie, if the search is
        # defined in a field.
        self.name = name or search.name
        self.type = 'search'
        self.colspan = search.colspan
        self.showActions = search.showActions
        self.actionsDisplay = search.actionsDisplay
        self.showTopNav = search.showNav in ('top', 'both')
        self.showBottomNav = search.showNav in ('bottom', 'both')
        className = self.container.name
        if search.translated:
            self.translated = search.translated
            self.translatedDescr = search.translatedDescr or ''
        else:
            # The label may be specific in some special cases
            labelDescr = ''
            if search.name == 'allSearch': label = f'{className}_plural'
            elif search.name == 'customSearch': label = 'search_results'
            elif not search.name: label = None
            else:
                label = f'{className}_{search.name}'
                labelDescr = f'{label}_descr'
            _ = tool.translate
            self.translated = _(label) if label else ''
            self.translatedDescr = _(labelDescr) if labelDescr else ''
        # Strip the description (a single space may be present)
        self.translatedDescr = self.translatedDescr.strip()
        # An initiator instance if the search is in a popup
        self.initiator = initiator
        # When search results are shown in a popup, checkboxes must be present
        # even when not shown. Indeed, we want them in the DOM because object
        # ids are stored on it.
        if initiator:
            self.checkboxes = True
            self.checkboxesDefault = False
        else:
            cb = search.checkboxes
            cb = cb(tool) if callable(cb) else cb
            self.checkboxes = cb
            self.checkboxesDefault = search.checkboxesDefault

    def getRootHook(self):
        '''If there is an initiator, return the hook as defined by it. Else,
           return the name of the search.'''
        init = self.initiator
        return init.popupHook if init else (self.search.name or 'search')

    def showCheckboxes(self):
        '''When must checkboxes be shown ?'''
        init = self.initiator
        return init.showCheckboxes() if init else self.checkboxes

    def useCbJs(self, mode):
        '''Do not use (and, consequently, include) checkboxes-related JS data
           structures if p_self is in front of a Ref that already defines it.'''
        # One exception: if we are on custom search results, JS data structures
        # must be computed because the Ref wrapper is not part of the result.
        if not mode.fromRef: return True
        return self.name == 'customSearch'

    def getCbJsInit(self, hook):
        '''Returns the code that creates JS data structures for storing the
           status of checkboxes for every result of this search.'''
        default = 'unchecked' if self.checkboxesDefault else 'checked'
        return '''var node=findNode(this, '%s');
                  node['_appy_objs_cbs'] = {};
                  node['_appy_objs_sem'] = '%s';''' % (hook, default)

    def getModes(self):
        '''Gets all the modes applicable when displaying search results (being
           instances of p_class_) via this search (p_self). r_ is a list of
           names and not a list of Mode instances.'''
        r = self.search.resultModes or self.container.getResultModes() or \
            Mode.default
        return r if not callable(r) else r(self.tool)

    def getMode(self):
        '''Gets the current mode'''
        return Mode.get(self)

    def getTitleMode(self, o, popup):
        '''How titles to search results, being instances of p_class_, must be
           rendered ?'''
        # Possible r_return values are the following.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # If...    | Every search result's title is rendered as ...
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "link"   | links allowing to go to instances' view pages;
        # "dlink"  | links, as for "link", but the link is wrapped in a "div";
        # "plink"  | links, as for "link", but *p*ublic links = a special URL
        #          | allowing to render object content in a specific way, on the
        #          | "public" PX.
        # "select" | objects, that can be selected from a popup;
        # "text"   | simple, unclickable text.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        if popup: return 'select'
        # Check if the title mode is specified on the container class
        mode = self.container.getTitleMode()
        if not mode: return 'link'
        return mode(o) if callable(mode) else mode

    def getResultsTop(self, mode, ajax):
        '''If p_class_ defines something to display on the results page just
           before displaying search results, returns it.'''
        # Get this only on the main page, not when ajax-refreshing search
        # results.
        if ajax: return
        return self.container.getResultsTop(self.tool, self.search, mode)

    def highlight(self, text):
        '''Highlight search results within p_text'''
        return Criteria.highlight(self.tool.H(), text)

    def getRunningTotals(self, mode):
        '''If totals must be computed, returns a Running* object'''
        search = self.search
        if not search.totalRows or not mode.isSummable(): return
        return search.Totals.init(search, 'o', mode.columns, search.totalRows)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
