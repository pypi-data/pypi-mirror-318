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
import sys, re, os.path

from persistent.list import PersistentList

from appy.px import Px
from appy import ui, utils
from appy.ui import LinkTarget
from appy.ui.colset import ColSet
from appy.model.batch import Batch
from appy.xml.escape import Escape
from appy.ui.columns import Columns
from appy.model.searches import Search
from appy.utils import string as sutils
from appy.model.utils import Object as O
from appy.ui.layout import Layout, Layouts
from appy.database.operators import Operator
from appy.model.fields import Field, Initiator

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ATTR_EXISTS = 'Attribute "%s" already exists on class "%s". Note that ' \
              'several back Refs pointing to the same class must have ' \
              'different names, ie: back=Ref(attribute="every_time_a_' \
              'distinct_name",...).'
ADD_LK_KO   = 'Parameters "add" and "link" can only be used together for ' \
              'mono-valued forward Refs, with attribute "link" being "popup".'
BACK_COMP   = 'Only forward Refs may be composite.'
BACK_1_COMP = 'The backward Ref of a composite Ref must have an upper ' \
              'multiplicity of 1. Indeed, a component can not be contained ' \
              'in more than one composite object.'
LK_POP_ERR  = 'When "link" is "popup", "select" must be a instance of ' \
              'appy.fields.search.Search instance or a method that returns ' \
              'such an instance.'
WRITE_KO    = "User can't write Ref field %s::%s. %s."
UNLINK_KO   = 'field.unlinkElement prevents you to unlink this object.'
SEARCH_KO   = 'Ref "%s": attribute "searches" contains at least one unnamed ' \
              'Search instance.'
RADIOS_KO   = "This field can't be rendered as radio buttons because it may " \
              "contain several values (max multiplicity is higher than 1)."
CBS_KO      = "This field can't be rendered as checkboxes because it can " \
              "only contain a single value (max multiplicity is 1)."
DDOWN_KO    = 'A Ref with link="dropdown" must have a max multiplicity being 1.'
E_VAL_KO    = 'With "indexAttribute" being "%s", "emptyIndexValue" can only ' \
              'hold one of these values: %s.'
HIST_O_KO   = '%s :: Ref "%s" :: Tied object %d (%s) mentioned in object ' \
              'history was not found.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def setAttribute(class_, name, value):
    '''Sets on p_class_ attribute p_name having some p_value. If this attribute
       already exists, an exception is raised.'''
    if hasattr(class_, name):
        raise Exception(ATTR_EXISTS % (name, class_.__name__))
    setattr(class_, name, value)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Position:
    '''When inserting some object among a list of tied objects, this class gives
       information about where to insert it.'''

    def __init__(self, place, o):
        # p_o is an object among tied objects that will be the reference point
        # for the insertion.
        self.insertObject = o
        # p_place can be "before" or "after" and indicates where to insert the
        # new object relative to p_o.
        self.place = place

    def getInsertIndex(self, refs):
        '''Gets the index, within tied objects p_refs, where to insert the newly
           created object.'''
        r = refs.index(self.insertObject)
        if self.place == 'after':
            r += 1
        return r

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class RefInitiator(Initiator):
    '''When an object is added via a Ref field, this class gives information
       about the initiator Ref field and its object.'''

    def __init__(self, tool, req, info):
        Initiator.__init__(self, tool, req, info)
        # We may have information about the place to insert the newly created
        # object into the Ref.
        self.insertInfo = req.insert
        if self.insertInfo:
            place, objectId = self.insertInfo.split('.')
            o = tool.getObject(objectId)
            self.position = Position(place, o)
        else:
            self.position = None

    def checkAllowed(self, log=False):
        '''Checks that adding an object via self.field is allowed'''
        return self.field.checkAdd(self.o, log=log)

    def updateParameters(self, params):
        '''Add the relevant parameters to the object edition page, related to
           this initiator.'''
        # Get potential information about where to insert the object
        if self.insertInfo: params['insert'] = self.insertInfo

    def goBack(self):
        '''After the object has been created, go back to its "view" page or go
           back to the initiator.'''
        return 'view' if self.field.viewAdded else 'initiator'

    def getNavInfo(self, new):
        '''Compute the correct nav info at the newly inserted p_new object'''
        # At what position is p_new among tied objects ?
        o = self.o
        position = self.field.getIndexOf(o, new) + 1
        total = o.countRefs(self.field.name)
        return self.field.getNavInfo(o, position, total)

    def manage(self, new):
        '''The p_new object must be linked with the initiator object and the
           action must potentially be historized.'''
        o = self.o
        # Link the new object to the initiator. p_new will be reindexed, with
        # all its fields, so it is useless to reindex the back reference in the
        # call hereafter.
        self.field.linkObject(o, new, at=self.position, secure=True,
                              reindex=True, reindexBack=False)
        # Record this change into the initiator's history when relevant
        if self.field.getAttribute(o, 'historized'):
            o.history.add('Link', addition=True, field=self.field.name,
                          comment=new.strinG(translated=True, path=False))

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Separator:
    '''Withins lists of tied objects, one may need to insert one or several
       separator(s). If you need this, specify, in attribute Ref.separator, a
       method that will return an instance of this class.'''

    def __init__(self, label=None, translated=None, css=None):
        # If some text must be shown within the separator, you can specify an
        # i18n p_label for it, or a translated text in p_translated. If
        # p_translated is provided, p_label will be ignored.
        self.label = label
        self.translated = translated
        # The CSS class(es) to apply to the separator
        self.css = css

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Ref(Field):
    # Some elements will be traversable
    traverse = Field.traverse.copy()

    # Make sub-classes available here
    Position = Position
    Separator = Separator

    # Ref-specific layouts
    class Layouts(Layouts):
        '''Ref-specific layouts'''
        base = 'lrv-f'
        # The unique, static cell layout
        cell = Layout('f|', width='100%', css='no')
        # Layouts for a Ref with link=True
        l = Layouts(edit=Layout(base, width=None), view=Layout('l-f'))
        gld = Layouts(edit=Layout('d2-lf;rv=', width=None), view='f')
        # Wide layout for a Ref with add=True: it must be 100% wide
        # "t": with *t*op space
        t = Layouts(Layout(base, css='topSpace'))
        a = Layouts(edit=Layout(base), view=Layout(base))
        # "d" stands for "description": a description label is added, on view
        baseW = 'l-d-f'
        wd = Layouts(view=Layout(baseW))
        wdt = Layouts(view=Layout(baseW, css='topSpace')) # *t*op
        wdb = Layouts(view=Layout(baseW, css='bottomSpace')) # *b*ottom
        wdtb = Layouts(view=Layout(baseW, css='tbSpace')) # *t*op + *b*ottom
        # Wide, but not on edit
        w_e = Layouts(edit=Layout(base, width=None), view=Layout(base))

        @classmethod
        def getDefault(class_, field):
            '''Default layouts for this List p_field'''
            if field.inGrid(): return class_.g
            return class_.l if field.link else class_.a

    # Getting a ref value is something special: disable the standard Appy
    # machinery for this.
    customGetValue = True

    # A Ref has a specific initiator class
    initiator = RefInitiator

    # Its is more practical if the empty value is iterable
    empty = ()

    # Possible values for attribute "emptyIndexValue"
    validIndexEmptyValues = {
      True:  (None, 0  ), # if the "index attribute" is "iid"
      False: (None, '-')  # if it is any another attribute
    }

    # The name of the index class storing values of this field in the catalog
    indexType = 'RefIndex'

    # "Getting *P*ossible *V*alues" may have the following meanings :
    PV_EDIT = 0    # get objects to possibly select them as tied objects for
                   # some base object / ref ;
    PV_SEARCH = 1  # get objects to select them as values for searching base
                   # objects having these values as tied objects ;
    PV_FILTER = 2  # get objects to select them as values for filtering base
                   # objects having these values as tied objects.

    # Every type of "PV" corresponds to an attribute used to retrieve objects
    pvMap = {PV_EDIT: 'select', PV_SEARCH: 'sselect', PV_FILTER: 'fselect'}

    # Constant for defining a self-reference (see doc in Ref constructor,
    # attribute "back").
    SELF = 1

    # This PX displays the title of a referenced object, with a link on it to
    # reach the consult view for this object. If we are on a back reference, the
    # link allows to reach the correct page where the forward reference is
    # defined. If we are on a forward reference, the "nav" parameter is added to
    # the URL for allowing to navigate from one object to the next/previous one.

    pxObjectTitle = Px('''
     <x var="navInfo=ifield.getNavInfo(io, batch.start+currentNumber,
                                       batch.total, inPickList, inMenu);
             pageName=ifield.back.pageName if ifield.isBack else 'main';
             titleMode=ifield.getTitleMode(o, selector);
             selectJs='onSelectObject(%s,%s,%s,%s)' % (q(cbId),
                         q(selector.initiatorHook), q(selector.initiator.iid),
                         q(selector.ckNum)) if selector else ''">
      <x if="not selectable">::ifield.getSupTitle(io, o, navInfo) or ''</x>
      <x>::ui.Title.get(o, mode=titleMode, nav=navInfo, target=target,
                        page=pageName, popup=popup, selectJs=selectJs)</x>
      <x if="not selectable">
       <span style=":'display:%s' % ('inline' if showSubTitles else 'none')"
             class="subTitle" var="sub=ifield.getSubTitle(io, o)"
             if="sub">::sub</span>
      </x></x>''')

    # Buttons triggering global actions on several linked objects: delete many,
    # unlink many, etc.

    pxGlobalActions = Px('''
     <div class="globalActions" if="not popup">

      <!-- Insert several objects (if in pick list) -->
      <input if="mayEdit and inPickList"
             var2="action='link'; label=_('object_link_many');
                   css=ui.Button.getCss(label)"
             type="button" class=":css" value=":label"
             onclick=":'onLinkMany(%s,%s,%s,%s)' %
                        (q(action), q(o.url), q(hook), q(batch.start))"
             style=":svg('linkMany', bg='18px 18px')"/>

      <!-- Unlink several objects -->
      <input if="mayEdit and mayUnlink and not selector"
             var2="iname='unlinkManyUp' if linkList else 'unlinkMany.svg';
                   action='unlink'; label=_('object_unlink_many');
                   css=ui.Button.getCss(label)"
             type="button" class=":css" value=":label"
             onclick=":'onLinkMany(%s,%s,%s,%s)' %
                        (q(action), q(o.url), q(hook), q(batch.start))"
             style=":url(iname, bg='18px 18px', ram=iname.endswith('.svg'))"/>

      <!-- Delete several objects -->
      <input if="mayEdit and field.delete and not selector"
             var2="action='delete'; label=_('object_delete_many');
                   css=ui.Button.getCss(label)"
             type="button" class=":css" value=":label"
             onclick=":'onLinkMany(%s,%s,%s,%s)' %
                        (q(action), q(o.url), q(hook), q(batch.start))"
             style=":svg('deleteMany', bg='18px 18px')"/>

      <!-- Custom actions -->
      <div for="action in field.getActions(o)"
           var2="checkHook=f'{o.iid}_{field.name}';
                 fieldName=f'{field.name}*{action.name}'; field=action;
                 multi=action.getMulti(hook, checkHook);
                 smallButtons=True">:action.pxRender</div>
     </div>

     <!-- Select objects and close the popup -->
     <div class="globalActions"
          if="popup and mayEdit and selector and selector.cbShown">
      <input type="button" style=":svg('linkMany', bg='18px 18px')"
        var="label=_('object_link_many'); css=ui.Button.getCss(label)"
        value=":label" class=":css"
        onclick=":'onSelectObjects(%s,%s,%s,%s,%s)' %
                  (q(f'{o.iid}_{field.name}'), q(selector.initiatorHook),
                   q(selector.initiator.url), q(selector.initiatorMode),
                   q(selector.onav))"/>
     </div>''')

    # Icons for moving objects up / down

    pxMoveIcons = Px('''
     <!-- Move to top -->
     <div if="objectIndex &gt; 1">
      <img class="clickable iconS" src=":svg('arrows')" title=":_('move_top')"
           style="transform:rotate(180deg)" onclick=":js % q('top')"/>
     </div>

     <!-- Move to bottom -->
     <div if="objectIndex &lt; (batch.total-2)">
      <img class="clickable iconS" src=":svg('arrows')"
           title=":_('move_bottom')" onclick=":js % q('bottom')"/>
     </div>

     <!-- Move up -->
     <div if="objectIndex &gt; 0">
      <img class="clickable iconS" src=":svg('arrow')" title=":_('move_up')"
           style="transform: rotate(180deg)" onclick=":js % q('up')"/>
     </div>

     <!-- Move down -->
     <div if="objectIndex &lt; (batch.total-1)">
      <img class="clickable iconS" src=":svg('arrow')" title=":_('move_down')"
           onclick=":js % q('down')"/>
     </div>''')
    
    # Icons for triggering actions on some tied object (edit, delete, etc)

    pxObjectActions = Px('''
     <div var="showActions=ifield.getAttribute(io, 'showActions')"
          if="showActions"
          var2="inCell=layout=='cell';
                layout='sub';
                toPopup=target and target.target != '_self';
                editable=guard.mayEdit(o) and not (popup and toPopup);
                class_=field.container;
                iconsOnly=tiedClass.getIconsOnly();
                locked=o.Lock.isSet(o, 'main')"
          class=":class_.getSubCss(o, ifield, objectIndex, inPickList)">

      <!-- Fields on layout "sub" -->
      <x if="not popup and showActions == 'all'"
         var2="fields=o.getFields(layout);
               ajaxSingle=False">
       <!-- Call px "cell" and not "render" to avoid having a table -->
       <x for="field in fields"
          var2="name=field.name;
                value=field.getValueIf(o, name, layout)">:field.cell</x>
      </x>

      <!-- Workflow transitions -->
      <x if="tiedClass.showTransitions(o, 'result')"
         var2="workflow=o.getWorkflow()">:workflow.pxTransitions</x>

      <!-- Edit -->
      <div if="editable and not popup and not inCell" class="ibutton"
           var2="text=_('object_edit')">
       <a if="not locked"
          var2="navInfo=ifield.getNavInfo(io, batch.start + currentNumber,
                                          batch.total) if not inMenu else 'no'"
          href=":o.getUrl(sub='edit', page='main', nav=navInfo, popup=toPopup)"
          target=":target.get(popup, toPopup)" onclick=":target.onClick">
        <img src=":svg('edit')" class="iconS" title=":text"/>
       </a>
       <x if="locked" var2="lockStyle='iconS'; page='main'">::o.Lock.px</x>
       <div if="not iconsOnly" class="ibutton"
            onclick="this.previousSibling.click()">:text</div>
      </div>

      <!-- Delete -->
      <div class="ibutton"
           var="delViaField=inPickList or ifield.delete;
                text=_('object_delete')"
           if="not locked and mayEdit and delViaField and guard.mayDelete(o)">
       <a title=":text" class="clickable"
          var2="back=(backHook or ohook) if inMenu else hook"
          onclick=":o.class_.getDeleteConfirm(o, q, back)">
        <img class="iconS" src=":svg('deleteS')"/>
       </a>
       <div if="not iconsOnly" class="ibutton"
            onclick="this.previousSibling.click()">:text</div>
      </div>

      <!-- Unlink -->
      <div if="mayUnlink and ifield.mayUnlinkElement(io, o)"
           class="ibutton" var2="text=_('object_unlink')">
       <img var="iname='unlinkUp' if linkList else 'unlink'"
            class="clickable iconS" title=":text" src=":svg(iname)"
            onClick=":ifield.getOnUnlink(_ctx_)"/>
       <div if="not iconsOnly" class="ibutton"
            onclick="this.previousSibling.click()">:text</div>
      </div>

      <!-- Insert (if in pick list) -->
      <div if="inPickList" class="ibutton"
           var2="text=_('object_link'); action='link'">
       <img class="clickable iconS" title=":text" src=":svg(action)"
            onclick=":'onLink(%s,%s,%s,%s)' % (q(action), q(io.url),
                       q(ifield.name), q(id))"/>
       <div if="not iconsOnly" class="ibutton"
            onclick="this.previousSibling.click()">:text</div>
      </div>

      <!-- Insert another object before this one -->
      <div if="not inPickList and mayAdd == 'anywhere'" class="ibutton">
       <img if="not createFromSearch"
            src=":url('addAbove')" class="clickable"
            title=":_('object_add_above')"
            onclick=":'onAdd(%s,%s,%s)'% (q('before'), q(addFormName), q(id))"/>
       <a if="createFromSearch" target="appyIFrame"
          href=":tiedClass.getCreateLink(tool, createVia, addFormName,
                  sourceField=prefixedName, insert='before.%s' % id)">
        <img src=":svg('addAbove')" class="clickable iconS"
             title=":_('object_add_above_from')"
             onclick="openPopup('iframePopup')"/>
       </a>
      </div>

      <!-- Arrows for moving objects up or down -->
      <div if="batch.total &gt; 1 and changeOrder and not inPickList and
             (not inMenu) and objectIndex is not None" class="moveIcons"
           var2="js='askBunchMove(%s,%s,%s,%%s)' %
                 (q(batch.hook),q(batch.start),q(id))">:ifield.pxMoveIcons</div>
     </div>''')

    # Button allowing to add a new object through a Ref field, if it has been
    # declared as addable and if multiplicities allow it.

    pxAdd = Px('''
     <x var="toPopup=target.target != '_self'"
        if="mayAdd and not inPickList and not (popup and toPopup)">
      <form class=":'addFormMenu' if inMenu else 'addForm'"
            name=":addFormName" id=":addFormName" target=":target.target"
            action=":f'{o.url}/new'">
       <input type="hidden" name="className" value=":tiedClass.name"/>
       <input type="hidden" name="template_" value=""/>
       <input type="hidden" name="insert" value=""/>
       <input type="hidden" name="nav"
              value=":field.getNavInfo(o, 0, batch.total)"/>
       <input type="hidden" name="popup"
              value=":'True' if toPopup else 'False'"/>

       <!-- The button, prefixed by, or containing, its icon -->
       <x if="not createFromSearch">
        <img if="field.iconOut" src=":field.getIconUrl(url)"
             class=":'clickable %s' % field.iconCss"
             onclick="this.nextSibling.click()"/>
        <input type=":field.getAddButtonType(createVia)"
               var="addLabel=_(field.addLabel);
                    label=tiedClassLabel if inMenu else addLabel;
                    css=ui.Button.getCss(label, iconOut=field.iconOut)"
               class=":css" value=":label" title=":addLabel"
               style=":field.getIconUrl(url, asBG=True) if addIcon else ''"
               onclick=":field.getOnAdd(_ctx_)"/>
       </x>

      </form>
      <!-- Button for creating an object from a template when relevant -->
      <x if="createFromSearch"
         var2="fromRef=True; class_=tiedClass; className=class_.name;
               iconOut=field.iconOut;
               sourceField=prefixedName">:class_.pxAddFrom</x>
     </x>''')

    # Button allowing to select, from a popup, objects to be linked via the Ref

    pxLink = Px('''
     <x if="not popup"
        var="repl=popupMode == 'repl';
             labelId='search_button' if repl else field.addLabel;
             icon='search.svg' if repl else field.addIcon;
             isInner=field.isInner();
             label=_(labelId)">
      <img if="field.iconOut" src=":o.buildUrl(icon, ram=True)"
           class=":f'clickable {field.iconCss}'"
           onclick="this.nextSibling.click()"/>
      <a target="appyIFrame" href=":field.getPopupLink(o, popupMode, name)"
         onclick="openPopup('iframePopup')"><x if="isInner">🔍</x>
       <div if="not isInner" var="css=field.getLinkClass(_ctx_)"
            style=":field.getLinkStyle(_ctx_)" class=":css">:label</div>
      </a>
     </x>''')

    # This PX displays, in a cell header from a ref table, icons for sorting the
    # ref field according to the field that corresponds to this column.

    pxSortIcons = Px('''
     <x if="changeOrder and (len(objects) &gt; 1) and \
            refField.isSortable(inRefs=True)">
      <img src=":svg('asc')" class="clickable iconST"
           var="js='askBunchSortRef(%s,%s,%s,%s)' %
                  (q(hook), q(batch.start), q(refField.name), q('False'))"
           onclick=":'askConfirm(%s,%s,%s)' % (q('script'), q(js,False),
                                               q(sortConfirm))"/>
      <img src=":svg('asc')" class="clickable iconST"
           style="transform:rotate(180deg)"
           var="js='askBunchSortRef(%s,%s,%s,%s)' %
                  (q(hook), q(batch.start), q(refField.name), q('True'))"
           onclick=":'askConfirm(%s,%s,%s)' % (q('script'), q(js,False),
                                               q(sortConfirm))"/>
     </x>''')

    # Shows the object number in a numbered list of tied objects

    pxNumber = Px('''
     <x if="not changeNumber">:objectIndex+1</x>
     <div if="changeNumber" class="dropdownMenu"
          var2="id='%s_%d' % (hook, objectIndex);
                imgId='%s_img' % id;
                inputId='%s_v' % id"
          onmouseover="toggleDropdown(this)"
          onmouseout="toggleDropdown(this,'none')">
      <input type="text" size=":numberWidth" id=":inputId" class="nbref"
             value=":objectIndex+1" onclick="this.select()"
             onkeydown=":'if (event.keyCode==13) \
                              document.getElementById(%s).click()' % q(imgId)"/>
      <!-- The menu -->
      <div class="dropdown">
       <img class="clickable" src=":url('move')" id=":imgId"
            title=":_('move_number')"
            onclick=":'askBunchMove(%s,%s,%s,this)' %
                       (q(batch.hook), q(batch.start), q(o.iid))"/>
      </div>
     </div>''')

    # Part of pxList displaying the list of tied objects

    pxSub = Px('''
     <!-- (Top) navigation -->
     <div align=":dright" if="batch.showNav()">:batch.pxNavigate</div>

     <!-- No object is present -->
     <p class="discreet" if="not objects">::_(field.noObjectLabel)</p>

     <!-- Linked objects -->
     <x if="objects"
        var2="initiator=field.initiator(tool, req, (o, field));
              tableWidth=field.width or field.layouts['view'].width;
              columns=field.getCurrentColumns(colset, colsets);
              genCss=columns.getCss(field.showHeaders, initiator.field.rowAlign,
                                    tableWidth);
              genName=columns.name if genCss else None;
              currentNumber=0">
      <style if="genCss">::genCss</style>
      <table id=":collapse.id" style=":collapse.style"
             class=":field.getListCss(_ctx_)">
       <tr if="field.showHeaders">
        <x for="col in columns" var2="refField=col.field">:col.pxHeaderRef</x>
       </tr>

       <!-- Loop on every (tied or selectable) object -->
       <x for="o in objects"
          var2="@currentNumber=currentNumber + 1">
        <x if="field.separator">::field.dumpSeparator(initiator.o,
                                  loop.o.previous, o, columns)</x>
        <x>:o.pxTied</x></x>
      </table>
     </x>

     <!-- Global actions -->
     <x if="checkboxes and field.getAttribute(o,
             'showGlobalActions')">:field.pxGlobalActions</x>

     <!-- (Bottom) navigation -->
     <div align=":dright" class="bottomSpace" if="batch.showNav()"
          var2="scrollTop='payload'">:batch.pxNavigate</div>

     <!-- Init checkboxes if present -->
     <script if="checkboxes">:'initCbs(%s)' % q(hook)</script>''')

    # PX displaying tied objects as a list, with controls

    pxList = Px('''
     <div id=":hook"
          var="subLabel=field.getListLabel(inPickList);
               colsets=field.getColSets(o, tiedClass,
                addNB=numbered and not inPickList and not selector,
                addCB=checkboxes)">

      <!-- Top controls -->
      <div if="field.showControls and (mayAdd or mayLink or layout == 'view')
               and not popup" class="topSpaceF">
       <x if="field.collapsible and objects">:collapse.px</x>
       <span if="subLabel" class="discreet">:_(subLabel)</span>
       <span if="batch.length &gt; 1" class="discreet">
        <span class="navSep">//</span><x>:batch.total</x>
       </span>
       <x if="not selector">:field.pxAdd</x>

       <!-- Button: open a popup for linking additional objects -->
       <x if="mayLink and not inPickList and not selector and field.linkInPopup"
          var2="popupMode='add'">:field.pxLink</x>

       <!-- The search selector if searches are defined -->
       <select var="searches=field.getSearches(o)" if="searches" class="refSel"
               id=":f'{o.iid}_{field.name}_ssel'"
               var2="sdef=field.getCurrentSearch(req, searches)"
               onchange=":f'askBunchSwitchSearch({q(hook)},{q(field.name)},'
                          f'this.value)'">
         <!-- The first option is used to select the default pxSub -->
         <option value="" selected=":sdef==''">:_('standard_view')</option>
         <option for="name, rs in searches.items()"
                 selected=":name==sdef" value=":name">:rs.translated</option>
       </select>

       <!-- The search button if field is queryable -->
       <div if="objects and field.queryable">
        <img if="field.iconOut" src=":field.getIconUrl(url, add=False)"
             class=":'clickable %s' % field.iconCss"
             onclick="this.nextSibling.click()"/>
        <input type="button" style=":field.getIconUrl(url,add=False,asBG=True)"
               var2="label=_('search_button');
                     css=ui.Button.getCss(label, iconOut=field.iconOut)"
               value=":label" class=":css"
               onclick=":'goto(%s)' % 
                q('%s/Search/advanced?className=%s&amp;ref=%d:%s' % 
                (tool.url, tiedClass.name, o.iid, field.name))"/>
       </div>

       <!-- The colset selector if multiple colsets are available -->
       <select if="len(colsets) &gt; 1" class="refSel"
               onchange=":'askBunchSwitchColset(%s,this.value)'% q(hook)">
        <option for="cset in colsets" value=":cset.identifier"
                selected=":cset.identifier==colset">:_(cset.label)</option>
       </select>
      </div>

     <script>:field.getAjaxData(hook, o, popup=popup, colset=colset, 
              start=batch.start, total=batch.total)</script>

      <!-- The tied objects -->
      <x>:field.getListPx(o)</x>
     </div>''')

    # PX that displays referred objects as dropdown menus

    pxMenu = Px('''
     <!-- The menu head, containing an icon or text -->
     <x>::menu.head</x>
     <!-- Nb of objects in the menu -->
     <b class=":mcss">:len(menu.objects)</b>''')

    pxMenus = Px('''
     <div var="inMenu=True" class="rmenu">
      <!-- One menu for every object type -->
      <div class="dropdownMenu"
           for="menu in field.getLinkedObjectsByMenu(o, objects)"
           var2="singleObject=len(menu.objects) == 1"
           onmouseover="toggleDropdown(this)"
           onmouseout="toggleDropdown(this,'none')">

       <!-- The menu name and/or icon, that is clickable if there is a single
            object in the menu. -->
       <x if="singleObject" var2="tied=menu.objects[0]; mcss=''">
        <x if="field.menuUrlMethod"
           var2="mUrl,mTarget=field.getMenuUrl(
                  o,tied,target)">::ui.Title.get(tied, target=mTarget,
                  baseUrl=mUrl, linkTitle=tied.getShownValue(),
                  title=field.pxMenu)</x>
        <x if="not field.menuUrlMethod"
           var2="linkInPopup=popup or target.target != '_self';
                 baseUrl=tied.getUrl(nav='no',
                   popup=linkInPopup)">::ui.Title.get(tied, target=target,
               baseUrl=baseUrl, css='dropdownMenu',
               linkTitle=tied.getShownValue(), title=field.pxMenu)</x>
       </x>
       <x if="not singleObject"
          var2="mcss=field.getMenuCss('menu', o, menu)">:field.pxMenu</x>

       <!-- The dropdown menu containing tied objects -->
       <div class=":field.getMenuCss('dropdown', o, menu,
                                     base='dropdown rdrop')">
        <div for="tied in menu.objects"
             style=":'flex-wrap:%swrap' % ('' if field.menuItemWrap else 'no')"
             var2="batch=field.getBatchFor(str(o.iid), menu.objects);
                   tiedId=tied.iid">
         <!-- A specific link may have to be computed from
              field.menuUrlMethod -->
         <x if="field.menuUrlMethod"
            var2="mUrl, mTarget=field.getMenuUrl(o, tied,
               target)">::ui.Title.get(tied, target=mTarget, baseUrl=mUrl)</x>

         <!-- Show standard pxObjectTitle else -->
         <x var="ifield=field; io=o; o=tied">
          <x if="not field.menuUrlMethod">:field.pxObjectTitle</x>
          <x if="guard.mayAct(tied)"
             var2="currentNumber=0;
                   objectIndex=None">:ifield.pxObjectActions</x>
         </x>
        </div>
       </div>
      </div>
      <x>:field.pxAdd</x></div>''')

    # Simplified widget for fields with render="minimal"

    pxMinimal = Px('''
     <x><x>::field.renderMinimal(o, objects, popup)</x>
      <!-- If this field is a master field -->
      <input type="hidden" if="masterCss and layout == 'view'|False"
             name=":name" id=":name" class=":masterCss"
             value=":[str(o.iid) for o in objects] if objects else ''"/></x>''')

    # Simplified widget for fields with render="links"

    pxLinks = Px('''
     <x>::field.renderMinimal(o, objects, popup, links=True)</x>''')

    # Displays tied objects through this field.
    # In mode link="list", if request key "scope" is:
    # - not in the request, the whole field is shown (both available and already
    #   tied objects);
    # - "objs", only tied objects are rendered;
    # - "poss", only available objects are rendered (the pick list).
    # ! scope is forced to "objs" on non-view "inner" (cell, buttons) layouts.

    pxPerRender = {'list': pxList, 'menus': pxMenus,
                   'minimal': pxMinimal, 'links': pxLinks}

    view = cell = buttons = Px('''
     <x var="*=field.initPx(o, req, _ctx_)">
      <!-- JS tables storing checkbox statuses if checkboxes are enabled -->
      <script if="checkboxesEnabled and scopeAll and \
                  render == 'list'">:field.getCbJsInit(o)</script>
      <!-- The list of available objects -->
      <x if="linkList and scopeAll and mayEdit"
         var2="scope='poss'; layout='view'">:field.view</x>
      <!-- The list of tied or available objects -->
      <x if="not (inPickList and not objects)">:field.pxPerRender[render]</x>
     </x>''')

    # Edit widget, for Refs with links being True (select widget)

    pxEditSelect = Px('''
     <select var="objects=field.getPossibleValues(o);
             ids=[str(po.iid) for po in field.getValue(o, name, single=False,
                                                       layout=layout)];
             charsWidth=field.getWidthInChars(False)"
        name=":name" id=":name" multiple=":isMultiple"
        size=":field.getSelectSize(False, isMultiple)"
        style=":field.getSelectStyle(False, isMultiple)"
        onchange=":field.getOnChange(o, layout)">
      <option value="" if="not isMultiple">:_(field.noValueLabel)</option>
      <option for="tied in objects"
       var2="id=str(tied.iid);
             title=field.getReferenceLabel(o, tied, unlimited=True)"
       selected=":field.valueIsSelected(id,inRequest,ids,requestValue)"
       value=":id" title=":title">:Px.truncateValue(title, charsWidth)</option>
     </select>''')

    # Edit widget, for Refs with links being 'radio' (R) or 'checkbox' (C)

    pxEditRC = Px('''
     <div var="objects=field.getPossibleValues(o);
               radios=field.link == 'radio';
               ids=[str(o.iid) for o in field.getValue(o, name, single=False,
                                                       layout=layout)]"
          style=":field.getWidgetStyle()">

      <!-- (Un)check all -->
      <div if="field.checkAll and not radios and len(objects) &gt;1"
           class="divAll" var="allId=f'{name}_all'">
       <input type="checkbox" class="checkAll" id=":allId" name=":allId"
              onclick="toggleCheckboxes(this)"/>
       <label lfor=":allId">:_('check_uncheck')</label>
      </div>

      <!-- Radios or checkboxes -->
      <div for="tied in objects" class="flex1"
           var2="id=str(tied.iid);
                 vid=f'{name}_{id}';
                 text=field.getReferenceLabel(o, tied, unlimited=True);
                 selected=field.valueIsSelected(id,inRequest,ids,requestValue)">
       <input type=":field.link" name=":name" id=":vid" value=":id"
              class=":masterCss" onchange=":field.getOnChange(o, layout)"
              checked=":selected" onClick="refShowClearRadio(this)"/>
       <label lfor=":vid" class="subLabel">::text</label>
       <span if="radios" class="clickable discreet" title=":_('clean_all')"
             style=":'display:%s' % ('block' if selected else 'none')"
             onclick="refClearRadio(this)">✖</span>
      </div>

      <!-- If there is no selectable element -->
      <div if="not objects and field.noSelectableLabel"
           class="discreet">:_(field.noSelectableLabel)</div>
     </div>''',

     js='''
       refShowClearRadio = function(input) {
         // Ensure first all "clean" icons are hidden
         const widget = input.parentNode.parentNode;
         for (const radio of widget.getElementsByTagName('INPUT')) {
           radio.nextSibling.nextSibling.style.display = 'none';
         }
         input.nextSibling.nextSibling.style.display = 'block';
       }

       refClearRadio = function(span) {
         span.previousSibling.previousSibling.checked = false;
         span.style.display = 'none';
       }''')

    # Edit widget, for Refs with link starting with "popup" or "dropdown"

    pxEditPopup = Px('''
     <div var="objects=field.getPopupObjects(o, name, req, requestValue);
               onChangeJs=field.getOnChange(o, layout);
               charsWidth=field.getWidthInChars(False);
               dropdown=field.link == 'dropdown'" class="rhead">

      <!-- The dropdown showing results when typing keywords -->
      <x if="dropdown"
         var2="pre=f'{o.iid}_{name}';
               className=field.class_.meta.name;
               liveCss='lsRef'">:tool.Search.live</x>

      <!-- The select field allowing to store the selected objects -->
      <x if="objects">
       <select name=":name" id=":name" multiple="multiple"
               size=":field.getSelectSize(False, isMultiple)"
               style=":field.getSelectStyle(False, isMultiple)"
               onchange=":onChangeJs">
        <option for="tied in objects" value=":tied.iid" selected="selected"
                var2="title=field.getReferenceLabel(o, tied, unlimited=True)"
                title=":title">:Px.truncateValue(title, charsWidth)</option>
       </select>
       <!-- Clean the selection -->
       <span class="clickable" onclick="refClearSelect(this)"
             title=":_('clean_all')">✖</span>
      </x>

      <!-- The button for opening the popup -->
      <x if="not dropdown" var="popupMode='repl'">:field.pxLink</x>

      <!-- Back from a popup, force executing onchange JS code above, for
           updating potential master/slave relationships. -->
      <script if="objects and \
         ('semantics' in req)">:'getNode(%s,true).onchange()' % q(name)</script>
      <span if="not objects">-</span>
     </div>''',

     css='''.inputRef { vertical-align: top; margin-left: 10px !important} ''',

     js='''
       refClearSelect = function(span) {
         span.previousSibling.remove();
         span.innerText = '-';
       }''')

    edit = Px('''<x>:field.editPx</x>''')

    search = Px('''
     <!-- The "and" / "or" radio buttons -->
     <x if="field.multiplicity[1] != 1"
        var2="operName='o_%s' % name;
              orName='%s_or' % operName;
              andName='%s_and' % operName">
      <input type="radio" name=":operName" id=":orName" checked="checked"
             value="or"/>
      <label lfor=":orName">:_('search_or')</label>
      <input type="radio" name=":operName" id=":andName" value="and"/>
      <label lfor=":andName">:_('search_and')</label><br/>
     </x>
     <!-- The list of values -->
     <select var="objects=field.getPossibleValues(tool, usage=field.PV_SEARCH);
                  charsWidth=field.getWidthInChars(True)"
             name=":widgetName" multiple="multiple"
             size=":field.getSelectSize(True, True)"
             style=":field.getSelectStyle(True, True)"
             onchange=":field.getOnChange(tool, 'search', className)">
      <option if="field.emptyIndexValue is not None"
              value=":field.emptyIndexValue">:_('no_object')</option>
      <option for="tied in objects" value=":getattr(tied, field.indexAttribute)"
              var2="title=field.getReferenceLabel(o, tied, unlimited=True)"
              title=":title">:Px.truncateValue(title, charsWidth)</option>
     </select>''')

    # Widget for filtering object values on search results

    pxFilterSelect = Px('''
     <div class="dropdownMenu fdrop"
          var="name=field.name;
               charsWidth=field.getWidthInChars(True);
               emptyVal=field.emptyIndexValue;
               objects=field.getPossibleValues(tool, usage=field.PV_FILTER)"
          if="objects"
          onmouseover="toggleDropdown(this)"
          onmouseout="toggleDropdown(this,'none')">
      <img src=":svg('fdrop')"/>
      <span if="name in mode.filters">›</span>

      <!-- The menu -->
      <div class="dropdown fdown"
           style=":field.getWidgetStyle('f')"
           var="js='askBunchFiltered(%s,%s,%%s)' % (q(mode.hook), q(name))">

       <!-- Get objects having any value -->
       <div><a onclick=":js % q('')">:_('everything')</a></div>

       <!-- Get objects having no value -->
       <div if="emptyVal is not None and not field.required">
        <x if="mode.inFilter(name, emptyVal)">→ </x> 
        <a onclick=":js % q(emptyVal)">:_('no_object')</a></div>

       <!-- Filter objects having a particular value -->
       <div for="tied in objects"
            var2="idVal=str(getattr(tied, field.indexAttribute));
                  title=field.getReferenceLabel(o, tied, unlimited=True,
                                                usage='filter')">
         <x if="mode.inFilter(name, idVal)">→ </x>
         <a onclick=":js % q(idVal)"
            title=":title">::Px.truncateValue(title, charsWidth)</a>
       </div>
      </div>
     </div>''')

    def __init__(self, class_=None, attribute=None, validator=None,
      composite=False, multiplicity=(0,1), default=None, defaultOnEdit=None,
      add=False, addConfirm=False, delete=None, createVia='form', viaPopup=None,
      creators=None, link=True, unlink=None, linkMethod=None,
      unlinkElement=None, unlinkConfirm=True, insert=None, beforeLink=None,
      afterLink=None, afterUnlink=None, back=None, backSecurity=True, show=True,
      renderable=None, page='main', group=None, layouts=None, showHeaders=False,
      shownInfo=None, fshownInfo=None, select=None, maxPerPage=30, move=0,
      indexed=False, mustIndex=True, indexValue=None, emptyIndexValue=0,
      indexAttribute='iid', searchable=False, filterField=None,
      readPermission='read', writePermission='write', width=None, height=5,
      maxChars=None, colspan=1, master=None, masterValue=None, focus=False,
      historized=False, mapping=None, generateLabel=None, label=None,
      queryable=False, queryFields=None, queryNbCols=1, searches=None,
      navigable=False, changeOrder=True, numbered=False, checkboxes=True,
      checkboxesDefault=False, sdefault='', scolspan=1, swidth=None,
      sheight=None, fwidth='7em', fheight='14em', sselect=None, fselect=None,
      persist=True, render='list', renderMinimalSep=', ', listCss=None,
      menuIdMethod=None, menuInfoMethod=None, menuUrlMethod=None, menuCss=None,
      dropdownCss=None, menuItemWrap=False, view=None, cell=None, buttons=None,
      edit=None, custom=None, xml=None, translations=None, showActions='all',
      actionsDisplay='block', showGlobalActions=True, collapsible=False,
      titleMode='link', viewAdded=True, noValueLabel='choose_a_value',
      noObjectLabel='no_ref', noSelectableLabel='no_selectable',
      addLabel='object_add', addFromLabel='object_add_from', addIcon='add.svg',
      iconOut=False, iconCss='iconS', filterable=True, supTitle=None,
      subTitle=None, toggleSubTitles=None, separator=None, rowAlign='top',
      showControls=True, actions=None, checkAll=True):

        # The class whose tied objects will be instances of
        self.class_ = class_

        # Specify "attribute" only for a back reference: it will be the name
        # (a string) of the attribute that will be defined on self's class and
        # will allow, from a linked object, to access the source object.
        self.attribute = attribute

        # If this Ref is "composite", it means that the source object will be
        # a composite object and tied object(s) will be its components.
        self.composite = composite

        # May the user add new objects through this ref ? "add" may hold the
        # following values:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  True      | (boolean value): the object will be created and inserted
        #            | at the place defined by parameter "insert" (see below);
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "anywhere" | (string) the object can be inserted at any place in the
        #            | list of already linked objects ("insert" is bypassed);
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # <a method> | a method producing one of the hereabove values.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.add = add

        # When the user adds a new object, must a confirmation popup be shown ?
        self.addConfirm = addConfirm

        # May the user delete objects via this Ref?
        self.delete = delete
        if delete is None:
            # By default, one may delete objects via a Ref for which one can
            # add objects.
            self.delete = bool(self.add)

        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # If "createVia"| When clicking the "add" button / icon to create an
        # is ...        | object through this ref ...
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #    "form"     | (the default) an empty form will be shown to the user
        #               | (p_self.class_' "edit" layout);
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #   "noForm"    | the object will be created automatically, and no
        #               | creation form will be presented to the user. Code
        #               | p_self.class_' m_onEdit to initialise the object
        #               | according to your needs;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #   a Search    | the user will get a popup and will choose some object
        #   instance    | among search results; this object will be used as base
        #               | for filling the form for creating the new object.
        #               |
        #               | Note that when specifying a Search instance, value of
        #               | attribute "addConfirm" will be ignored.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "createVia" may also hold a method returning one of the above-
        # mentioned values.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.createVia = createVia

        # When a page related to a tied object must be shown, for creating,
        # editing or simply viewing it, its target (=where it is rendered, in
        # the current window or in the popup window) depends on attribute
        # "popup" as defined on the referenced p_self.class_. This attribute
        # also determines the popup dimensions. You can override this attribute
        # in the context of this Ref field by using attribute "viaPopup"
        # hereafter. Allowed values for this attribute are similar to those for
        # attribute p_self.class_.popup. Values that can be used for p_viaPopup
        # as well as p_self.class_.popup are the following. If p_viaPopup is a:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # string  | the tied object will be shown in a popup whose width is
        #         | specified in pixels, as in '500px' ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # 2-tuple | the tied object will be shown in a popup whose dimensions
        #         | are passed, as a 2-tuple of strings of the form
        #         | ~(s_width, s_height)~, as, for example:
        #         |
        #         |                   ('500px', '450px')
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # p_viaPopup can also hold these specific values. If p_viaPopup is:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # None    | it is ignored and p_self.class_.popup will be used instead ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # False   | it is taken into account and the form will not be opened in
        #         | a popup, even if p_self.class_.popup exists and is not
        #         | empty.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # a 3-    | the link to the tied object will NOT display the tied object
        # tuple   | in a popup, but an additional icon will allow to display it
        #         | in a popup, whose dimensions are passed in the 2 last tuple
        #         | elements. Passing a 3-tuple thus enables both ways to show
        #         | tied object. Such a tuple must be of the form
        #         | ~(False, s_width, s_height)~. Here is an example:
        #         |
        #         |                (False, '-50px', '-50px')
        #         |
        #         | This latter example also demonstrates that a dimension
        #         | (width and/or height) can be specified as a negative number
        #         | of pixels. In that case, the actual dimension will be
        #         | computed as the window dimension minus the specified number
        #         | of pixels.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.viaPopup = viaPopup

        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # If "creators"  | people allowed to create instances of p_self.klass
        # is...          | in the context of this Ref, will be...
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #      None      | (the default) those having one of the global roles as
        #                | listed in p_self.klass.creators;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #     a list     | those having, locally on the ref's source object, one
        #  of role names | of the roles from this list.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.creators = creators

        # May the user link existing objects through this Ref ? If "link" is:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #    True    | the user will, on "edit", choose objects from an HTML
        #            | select widget, rendered as a dropdown list if max
        #            | multiplicity is 1 or as a selection box if several values
        #            | can be chosen ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  "radio"   | the user will, on "edit", choose objects from radio
        #            | buttons. This mode is valid for fields with a max
        #            | multiplicity being 1 ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "checkbox" | the user will, on "edit", choose objects from checkboxes.
        #            | This mode is valid for fields with a max multiplicity
        #            | being higher than 1.
        #            | ~
        #            | Note that choosing "radio"/"checkbox" instead of boolean
        #            | value "True" is appropriate if the number of objects from
        #            | which to choose is low ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #   "list"   | the user will, on "view", choose objects from a list of
        #            | objects which is similar to those rendered in pxViewList;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  "popup"   | the user will, on "view" or "edit", choose objects from a
        #            | popup window. In this case, parameter "select" can hold a
        #            | Search instance or a method ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "dropdown" | the user will, on "edit", choose objects by typing some
        #            | chars in an input text field: in a dropdown, the first
        #            | matching objects will be shown and will be selectable.
        #            | The set of possible objects shown in the dropdown must be
        #            | defined by a Search instance in attribute "select". On
        #            | this search instance, you can use attribute "maxPerLive"
        #            | to configure the maximum number of matched objects
        #            | appearing in the dropdown.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "popupRef" | the user will choose objects from a popup window, that
        #            | will display objects tied via a Ref field. In this case,
        #            | parameter "select" must hold a method returning a tuple
        #            | (o, name), v_o being the source object of the Ref field
        #            | whose name is in v_name.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.link = link
        self.linkInPopup = False

        # Determine the PX to use when editing a Ref, based on attribute "link"
        if link is True:
            px = Ref.pxEditSelect
        elif link in ('radio', 'checkbox'):
            px = Ref.pxEditRC
        elif link in ('popup', 'dropdown', 'popupRef'):
            px = Ref.pxEditPopup
            self.linkInPopup = True
        else: # link == 'list'
            px = None
        self.editPx = px

        # If you place a method in the following attribute, the user will be
        # able to link or unlink objects only if the method returns True.
        self.linkMethod = linkMethod

        # May the user unlink existing objects?
        self.unlink = unlink
        if unlink is None:
            # By default, one may unlink objects via a Ref for which one can
            # link objects.
            self.unlink = bool(self.link)

        # "unlink" above is a global flag. If it is True, you can go further and
        # determine, for every linked object, if it can be unlinked or not by
        # defining a method in parameter "unlinkElement" below. This method
        # accepts the linked object as unique arg.
        self.unlinkElement = unlinkElement

        # If "unlinkConfirm" is True (the default), when unlinking an object,
        # the user will get a confirm popup.
        self.unlinkConfirm = unlinkConfirm

        # When an object is inserted through this Ref field, where is it
        # inserted ? If "insert" is:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #   None    | it will be inserted at the end of tied objects ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "start"   | it will be inserted at the start of the tied objects ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # a method  | (called with the object to insert as single arg), its
        #           | return value (a number or a tuple of numbers) will be used
        #           | to insert the object at the corresponding position (this
        #           | method will also be applied to other objects to know where
        #           | to insert the new one) among tied objects ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # a tuple   | it will be inserted among tied objects; then, the passed
        # ('sort',  | method (called with the object to insert as single arg)
        #  method)  | will be used to sort tied objects and will be given as
        #           | param "key" of the standard Python method "sort" applied
        #           | on the list of tied objects ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # a tuple   | [only if link="popup"] the passed method, called with no
        # ('field', | arg, must return a tuple (o, field): the object(s) to
        #   method) | insert will be added into this field rather than into the
        #           | current one. This is only appropriate with a Ref field
        #           | being addadble (add=True) *and* linkable (link="popup"):
        #           | if the user creates a new object to link, this object must
        #           | not necessarily be added as tied object via the current
        #           | Ref.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # With the ('sort', method) tuple, a full sort is performed and may
        # completely change the order of tied objects; with value "method"
        # alone, the tied object is inserted at some given place: other tied
        # objects are more maintained in the order of their insertion.
        self.insert = insert

        # Immediately before an object is going to be linked via this Ref field,
        # method potentially specified in "beforeLink" will be executed and will
        # take the object to link as single parameter. If the method returns
        # False, the object will not be linked.
        self.beforeLink = beforeLink

        # Immediately after an object has been linked via this Ref field, method
        # potentially specified in "afterLink" will be executed and will take
        # the linked object as single parameter.
        self.afterLink = afterLink

        # Immediately after an object as been unlinked from this Ref field,
        # method potentially specified in "afterUnlink" will be executed and
        # will take the unlinked object as single parameter.
        self.afterUnlink = afterUnlink

        # Manage the p_back reference
        self.initBack(attribute, back, class_)

        # When (un)linking a tied object from the UI, by defaut, security is
        # checked. But it could be useful to disable it for back Refs. In this
        # case, set "backSecurity" to False. This parameter has only sense for
        # forward Refs and is ignored for back Refs.
        self.backSecurity = backSecurity

        # When displaying a tabular list of referenced objects, must we show
        # the table headers?
        self.showHeaders = showHeaders

        # "shownInfo" is a tuple or list (or a method producing it) containing
        # the names of the fields that will be shown when displaying tables of
        # tied objects. Field "title" should be present: by default, it is a
        # clickable link to the "view" page of every tied object. "shownInfo"
        # can also hold a tuple or list (or a method producing it) containing
        # appy.ui.colset.ColSet instances. In this case, several sets of columns
        # are available and the user can switch between those sets when viewing
        # the field.
        if shownInfo is None:
            self.shownInfo = ['title']
        elif isinstance(shownInfo, tuple):
            self.shownInfo = list(shownInfo)
        else:
            self.shownInfo = shownInfo
        # "fshownInfo" is the variant used in filters
        self.fshownInfo = fshownInfo or self.shownInfo

        # If a method is defined in this field "select", it will be used to
        # return the list of possible tied objects. Be careful: this method can
        # receive, in its first argument ("self"), the tool instead of an
        # instance of the class where this field is defined. This little cheat
        # is:
        #  - not really a problem: in this method you will mainly use methods
        #    that are available on a tool as well as on any object (like
        #    "search");
        #  - necessary because in some cases we do not have an instance at our
        #    disposal, ie, when we need to compute a list of objects on a
        #    search screen.
        # "select" can also hold a Search instance.
        #
        # Note that when a method is defined in field "masterValue" (see parent
        # class "Field"), it will be used instead of select (or sselect below).
        self.select = select
        if not select and self.link == 'popup':
            # Create a search for getting all objects
            max = maxPerPage if isinstance(maxPerPage, int) else 30
            self.select = Search(sortBy='title', maxPerPage=max)

        # If you want to specify, on the search form, a list of objects being
        # different from the one produced by self.select, define an alternative
        # (method or Search instance) in attribute "sselect" below.
        self.sselect = sselect or self.select

        # If you want to define, in a search filter, a list of objects being
        # different than p_self.sselect, define an alternative in attribute
        # "fselect" below.
        self.fselect = fselect or self.sselect

        # Maximum number of referenced objects shown at once. It can be directly
        # expressed as an integer value, or by a method accepting the source Ref
        # object as unique arg and returning this integer value.
        self.maxPerPage = maxPerPage

        # If param p_queryable is True, the user will be able to perform
        # searches from the UI within referenced objects. A Ref being queryable
        # requires an index. Two possibilities exist:
        # - your queryable Ref is composite (p_composite=True). In that case,
        #   the index used to restrict searches to Ref elements will be the
        #   special container index "cid";
        # - your queryable Ref has a mirror Ref being indexed. The mirror Ref is
        #   a forward Ref's back Ref or a back Ref's forward Ref.
        # If none of these conditions is met, the performed searches will
        # produce wrong results or errors.
        self.queryable = queryable

        # Here is the list of fields that will appear on the search screen.
        # If None is specified, by default we take every indexed field
        # defined on referenced objects' class.
        self.queryFields = queryFields

        # The search screen will have this number of columns
        self.queryNbCols = queryNbCols

        # If the field is p_queryable, you may specify, in attribute "searches":
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # 1 | a dict of Search instances, or a method producing it. Keys must be
        #   | names (following Python variable naming conventions) and values
        #   | must be Search objects;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # 2 | a single Search object, or a method producing it.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # When displaying the Ref on the "view" layout, if we are in case:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # 1 | results of the default search from the dict will be shown, instead
        #   | of the standard Ref rendering. A dropdown list will allow to
        #   | switch to the standard view or to results from other searches in
        #   | the list. This allows to produce alternate or partial views of the
        #   | referred objects, via searches and their related facilities, like
        #   | sorting and filtering.
        #   | 
        #   | By "default search", we mean: the one whose attribute "default" is
        #   | set to True. If no search as default=True, the standard Ref view
        #   | will be shown.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # 2 | the standard Ref view is completely abandoned, and results from
        #   | the single specified Search becomes the unique way to display tied
        #   | objects.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # On every specified Search instance (the unique one of case 2, or any
        # dict value from case 1), it is useless to specify a name, or the
        # attribute corresponding to the index allowing to restrict the search
        # to this Ref's tied objects: it will be added automatically. On the
        # other hand, for case 1, you must define translations for its name
        # (and, optionally, for its longer description), in its attributes named
        # "translated" and "translatedDescr".
        self.searches = searches

        # Within the portlet, will referred elements appear ?
        self.navigable = navigable

        # If "changeOrder" is or returns False, it even if the user has the
        # right to modify the field, it will not be possible to move objects or
        # sort them.
        self.changeOrder = changeOrder

        # If "numbered" is or returns True, a leading column will show the
        # number of every tied object. Moreover, if the user can change order of
        # tied objects, an input field will allow him to enter a new number for
        # the tied object. If "numbered" is or returns a string, it will be used
        # as width for the column containing the number. Else, a default width
        # will be used.
        self.numbered = numbered

        # If "checkboxes" is or returns True, every linked object will be
        # "selectable" via a checkbox. Global actions will be activated and will
        # act on the subset of selected objects: delete, unlink, etc.
        self.checkboxes = checkboxes

        # Default value for checkboxes, if enabled
        self.checkboxesDefault = checkboxesDefault

        # There are different ways to render a bunch of tied objects:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  "list"   | (the default) renders them as a list (=a XHTML table);
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  "menus"  | renders them as a series of popup menus, grouped by type.
        #           | Note that render mode "menus" will only be applied in
        #           | "cell" and "buttons" layouts. Indeed, we need to keep the
        #           | "list" rendering in the "view" layout because the "menus"
        #           | rendering is minimalist and does not allow to perform all
        #           | operations on linked objects (add, move, delete, edit...);
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "minimal" | renders a list not-even-clickable data about the tied
        #           | objects (according to shownInfo);
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  "links"  | renders a list of clickable comma-separated data about the
        #           | tied objects (according to shownInfo).
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.render = render

        # When render is "minimal" or "links", the separator used between linked
        # objects is defined here.
        self.renderMinimalSep = renderMinimalSep

        # If render is "list", you may specify, in p_listCss, a default CSS
        # class to apply to the xhtml table tag that will hold the list of
        # object. If no CSS class is defined, the one declared by the tied
        # class, in its "styles" static attribute, will be used.
        self.listCss = listCss

        # If render is "menus", 2 methods must be provided.
        # "menuIdMethod" will be called, with every linked object as single arg,
        # and must return an ID that identifies the menu into which the object
        # will be inserted.
        self.menuIdMethod = menuIdMethod

        # "menuInfoMethod" will be called with every collected menu ID (from
        # calls to the previous method) to get info about this menu. This info
        # must be a chunk of XHTML code, as a string, that must contain the name
        # of the menu. Here are some examples of such a name:
        # - a "span" tag containing a short text;
        # - a "src" tag containing an icon, whose "title" attribute contains a
        #   short text;
        # - a "span" tag containing an utf8 sumbol, whose "title" attribute
        #   contains short text.
        #
        # Take care of xhtml-escaping your texts, using this method:
        # appy.xml.escape.Escape::xhtml. This can be used that way
        #
        #     from appy.xml.escape import Escape
        #     escaped = Escape.xhtml(yourText)
        #
        self.menuInfoMethod = menuInfoMethod

        # "menuUrlMethod" is an optional method that allows to compute an
        # alternative URL for the tied object that is shown within the menu
        # (when render is "menus"). It can also be used with render being "list"
        # as well. The method can return a URL as a string, or, alternately, a
        # tuple (url, target), "target" being a string that will be used for
        # the "target" attribute of the corresponding XHTML "a" tag.
        self.menuUrlMethod = menuUrlMethod

        # "menuCss" is an optional CSS (list of) class(es) (or a method
        # producing it) that will be applied to menu titles (when p_render is
        # "menus") for menus containing more than 1 object. If the menu contains
        # a single object, the applied CSS class will be applied to the tied
        # object's title. If p_menuCss is a method, it must accept a single arg,
        # being the list of objects being shown in the current menu.
        self.menuCss = menuCss

        # Similar to p_menuCss, p_dropdownCss allows to define a CSS class for
        # each dropdown menu.
        self.dropdownCss = dropdownCss

        # Every menu entry corresponds to an object. Its standard parts will be
        # shown (when relevant): title, sub-title, actions, etc. All those parts
        # will be rendered in a flex layout. You may choose if this flex will
        # have CSS property "flex-wrap" being "wrap" or "nowrap". The default is
        # "nowrap". If the quantity of info becomes too large (ie, your
        # getSubTitle method returns some data), a rendering with "nowrap" will
        # produce better results.
        self.menuItemWrap = menuItemWrap

        # p_showActions determines if we must show or not actions on every tied
        # object. Values can be:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #    'all'    | All actions are shown: standard ones (move up/down,
        #             | edit, delete... the precisely shown set of actions
        #             | depends on user's permissions and other settings
        #             | like p_changeOrder) and actions whose layout is
        #             | "sub" and whose page is "main".
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  'standard' | Only standard actions are shown (see above).
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #    False    | No action is shown.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # p_showActions can also be a method producing one of these values
        self.showActions = showActions

        # When actions are shown (see p_showActions hereabove), p_actionsDisplay
        # determines how they are rendered.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  'block'  | Actions are shown in a "div" tag with CSS attribute
        #           | "display:block", so it will appear below the item title.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  'inline' | The "div" tag has CSS attribute "display:inline": it
        #           | appears besides the item's title and not below it,
        #           | producing a more compact list of results.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  'right'  | Similar to 'inline', but actions are right-aligned. Nice
        #           | rendering when the column containing the title and its
        #           | actions is not too large.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.actionsDisplay = actionsDisplay

        # It may be inappropriate to show global actions. "showGlobalActions"
        # can be a boolean or a method computing and returning it.
        self.showGlobalActions = showGlobalActions

        # If "collapsible" is True, a "+/-" icon will allow to expand/collapse
        # the tied or available objects.
        self.collapsible = collapsible

        # Normally, tied objects' titles are clickable and lead to tied object's
        # view pages: this behaviour corresponds to arg p_titleMode being
        # "link". All possible values are described below.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # If ...   | The title for every tied object ...
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "link"   | (the default) is a clickable link to object/view ;
        # "plink"  | is a clickable link to a variant of the tied object' URL,
        #          | allowing to view it on the "public" page ;
        # "text"   | is simple, unclickable, text.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # Note that p_titleMode can also be a method, accepting the tied object
        # as unique arg, that must return one of the above-mentioned values.
        self.titleMode = titleMode

        # When creating a new tied object from this ref, we will redirect the
        # user to the initiator's view page, excepted if this parameter is True.
        self.viewAdded = viewAdded

        # When selecting a value from a "select" widget, the entry representing
        # no value is translated according to this label. The default one is
        # something like "[ choose ]", but if you prefer a less verbose version,
        # you can use "no_value" that simply displays a dash, or your own label.
        self.noValueLabel = noValueLabel

        # When displaying tied objects, if there is no object, the following
        # label is used to produce a message (which can be as short as a simple
        # dash or an empty string).
        self.noObjectLabel = noObjectLabel

        # When displaying lists of objects to link, if there is no object, the
        # following label will be used to display a message. Set this attribute
        # to None if you don't want anything to appear in that case.
        self.noSelectableLabel = noSelectableLabel

        # Labels for the "add" and "add from" buttons
        self.addLabel = addLabel
        self.addFromLabel = addFromLabel

        # Icon for the "add" button (SVG please)
        self.addIcon = addIcon

        # If p_iconOut is False, the icon within the "add" button will be
        # integrated as a background-image inside it. Else, it will be
        # positioned outside the button.
        self.iconOut = iconOut
        # The CSS class to apply to the button icon, in "icon out" mode
        self.iconCss = iconCss

        # When displaying column "title" within lists of tied objects, methods
        # m_getSupTitle and m_getSubTitle from the tied object's class are
        # called for producing custom zones before and after rendering the
        # object title. If you want to particularize these zones for this
        # specific ref, instead of using the defaults methods from the tied
        # object's class, specify alternate methods in attributes "supTitle" and
        # "subTitle".
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # supTitle | may hold a method accepting 2 args: the tied object and
        #          | the navigation string;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # subTitle | may hold a method accepting the tied object as single arg.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.supTitle = supTitle
        self.subTitle = subTitle

        # Similarly, you can particularize attribute "toggleSubTitles" for this
        # Ref instead of using the static attribute as defined on tied object's
        # class. Ref attribute p_toggleSubTitles will be used if not None and
        # can hold values True, False, or a method, accepting the tool as single
        # arg and returning True of False.
        self.toggleSubTitles = toggleSubTitles

        # "separator" can accept a method that will be called before rendering
        # every tied object, to render a separator when the method returns
        # a Separator instance (see class above). This method must accept 2
        # args: "previous" and "next", and must return a Separator instance if a
        # separator must be inserted between the "previous" and "next" tied
        # objects. When the first tied object is rendered, the method is called
        # with parameter "previous" being None. Specifying a separator has only
        # sense when p_render is "list".
        self.separator = separator

        # When tied objects are rendered as a list, this attribute specifies
        # each row's vertical alignment.
        self.rowAlign = rowAlign

        # This attribute allows to hide, when rendering tied objects as a list
        # on "view", all standard controls tied to this Ref (icons/buttons for
        # adding or linking objects, etc). Use this only if you are sure you do
        # not use these controls, or if you display them elsewhere, in a custom
        # PX.
        self.showControls = showControls

        # These p_actions fields will be shown as global actions. For every such
        # action, attribute "show" must hold or return value "field" as unique
        # possible layout. This virtual layout means that the Ref field will
        # choose where to render this action within itself (ie, at the bottom of
        # tied objects, together with global actions).
        self.actions = actions

        # By default, for an indexed Ref field, the corresponding index stores
        # the IID of tied object(s). If you want to choose another attribute,
        # specify it here. This other attribute must represent a logical
        # identifier and must store a string value for every tied object.
        # Note that such a value cannot be an integer encoded as a string (ie,
        # method isdigit() must return False). Moreover, if your
        # p_indexAttribute is not "iid", p_emptyIndexValue must also be a non-
        # digit string.
        self.indexAttribute = indexAttribute

        # When link="checkbox", by default, an additional checkbox will be
        # rendered, allowing to select or unselect all possible values. If this
        # global checkbox must not be rendered, set the following attribute to
        # False.
        self.checkAll = checkAll

        # Call the base constructor
        super().__init__(validator, multiplicity, default, defaultOnEdit, show,
          renderable, page, group, layouts, move, indexed, mustIndex,
          indexValue, emptyIndexValue, searchable, filterField, readPermission,
          writePermission, width, height, None, colspan, master, masterValue,
          focus, historized, mapping, generateLabel, label, sdefault, scolspan,
          swidth, sheight, persist, False, view, cell, buttons, edit, custom,
          xml, translations)
        self.validable = bool(self.link)

        # Initialise filterPx when relevant. If you want to disable filtering
        # although it could be proposed, set p_filterable to False. This can be
        # useful when there would be too many values to filter.
        if self.link in (True, 'checkbox') and indexed and filterable:
            self.filterPx = 'pxFilterSelect'
        # The *f*ilter width and height
        self.fwidth = fwidth
        self.fheight = fheight
        self.checkParameters()

    def init(self, class_, name):
        '''Ref-specific lazy initialisation'''
        Field.init(self, class_, name)
        if not self.isBack and self.back:
            # Set the class for the back reference
            self.back.class_ = class_.python

    def initBack(self, attribute, back, class_):
        '''Initialise the back reference'''
        self.back = None
        if not attribute:
            # It is a forward reference
            self.isBack = False
            # Initialise the backward reference (if found)
            if not back: return
            elif back is Ref.SELF:
                # This is a self-reference: the back reference is the forward
                # reference itself.
                self.back = self
                return
            # Manage a standard back reference
            self.back = back
            back.back = self
            # p_class_ may be None in the case we are defining an auto-Ref to
            # the same class as the class where this field is defined. In this
            # case, when defining the field within the class, write
            #
            # myField = Ref(None, ...)
            #
            # and, at the end of the class definition (name it K), write:
            # autoref(K, K.myField)
            #
            if class_: setAttribute(class_, back.attribute, back)
            # A composite ref must have a back ref having an upper
            # multiplicity = 1
            if self.composite and back.multiplicity[1] != 1:
                raise Exception(BACK_1_COMP)
        else:
            self.isBack = True
            if self.composite: raise Exception(BACK_COMP)

    def initPx(self, o, req, c):
        '''Create context variables in v_r for layout "view"'''
        r = O()
        r.iid = o.iid
        r.layout = c.layout or req.layout or 'view'
        r.colset = c.colset or 'main'
        r.render = self.getRenderMode(r.layout)
        r.name = c.name or self.name
        r.prefixedName = f'{r.iid}:{r.name}'
        r.selector = self.getSelector(o, req)
        r.selectable = bool(r.selector) and c.popup
        r.linkList = self.link == 'list'
        r.scope = (c.scope or 'all') if r.layout == 'view' else 'objs'
        r.scopeAll = r.scope == 'all'
        r.inPickList = r.scope == 'poss'
        r.createVia = self.getAttribute(o, 'createVia')
        r.createFromSearch = not isinstance(r.createVia, str)
        r.ajaxSuffix = 'poss' if r.inPickList else 'objs'
        r.hook = f'{r.iid}_{r.name}_{r.ajaxSuffix}'
        r.inMenu = False
        batch = self.getBatch(o, r.render, req, r.hook)
        r.batch = batch if (c.ajaxSingle and c.layout != 'cell') else \
                  self.getViewValues(o, r.name, r.scope, batch, r.hook)
        r.objects = r.batch.objects
        total = r.batch.total
        r.numberWidth = len(str(total))
        r.tiedClass = c.handler.server.model.classes.get(self.class_.__name__)
        r.tiedClassLabel = c._(r.tiedClass.name)
        if not c.ajaxSingle:
            # If we are rendering a cell, we are within search or Ref results:
            # a back hook can be defined.
            r.backHook = c.ohook if r.layout == 'cell' else None
            r.target = ui.LinkTarget(self.class_, r.backHook, self.viaPopup)
        # else: ohook, backHook and target are specific to each tied object
        r.mayEdit = r.layout != 'edit' and \
                    c.guard.mayEdit(o, self.writePermission)
        r.mayEd = not r.inPickList and r.mayEdit
        r.mayAdd = r.mayEd and self.mayAdd(o, checkMayEdit=False)
        r.addFormName = f'{r.iid}_{self.name}_add' if r.mayAdd else ''
        r.mayLink = r.mayEd and self.mayAdd(o, mode='link', checkMayEdit=False)
        r.mayUnlink = r.mayLink and self.getAttribute(o, 'unlink')
        r.addConfirmMsg = c._(f'{self.labelId}_addConfirm') \
                          if self.addConfirm else ''
        r.addIcon = True # Set an icon on button "add"
        r.changeOrder = r.mayEd and self.getAttribute(o, 'changeOrder')
        r.sortConfirm = c._('sort_confirm') if r.changeOrder else ''
        r.numbered = not r.inPickList and bool(self.isNumbered(o))
        r.gotoNumber = r.numbered and not r.selectable and total > 1
        r.changeNumber = not r.inPickList and not r.selectable and r.numbered \
                         and r.changeOrder and total > 3
        r.checkboxesEnabled = self.getAttribute(o, 'checkboxes')
        r.checkboxes = r.checkboxesEnabled and total
        r.collapse = self.getCollapseInfo(o, r.inPickList)
        r.showSubTitles = req.showSubTitles in ('True', None)
        # Add more variables if we are in the context of a single object
        # retrieved via Ajax.
        if c.ajaxSingle:
            r.colsets = self.getColSets(o, r.tiedClass,
              addNB=r.numbered and not r.inPickList and not r.selector,
              addCB=r.checkboxes)
            r.columns = self.getCurrentColumns(r.colset, r.colsets)
        return r

    def getDefaultSearch(self, searches, nameOnly=False):
        '''Returns, among this dict of p_searches, the one being the default'''
        r = ''
        for name, search in searches.items():
            if search.default:
                r = name if nameOnly else search
                break
        return r

    def getSearches(self, o, dictOnly=True):
        '''Gets the unique Search instance or the dict of Search instances
           as defined or computed via attribute "searches". If p_dictOnly is
           True, the method returns None if the result is a unique search.'''
        r = self.getAttribute(o, 'searches')
        if not r: return
        # Do not return the unique instance if p_dictOnly is True
        unique = isinstance(r, Search)
        if unique and dictOnly:
            # Do not return the search, but indicate, in the request, that this
            # will be the unique search.
            o.req[self.getCurrentSearchKey()] = '_default_'
            return
        # Define the Search container, being p_self.class_
        class_ = self.class_.meta
        # Lazy-initialise the search(es)
        if unique:
            r.init(class_)
        else:
            for search in r.values():
                search.init(class_)
        return r

    def getSearch(self, o, name):
        '''Returns, among, p_self.searches, the one having this p_name'''
        all = self.getSearches(o, dictOnly=False)
        # Return the unique search
        if isinstance(all, Search): return all
        # Return the search whose name is p_name
        return self.getDefaultSearch(all) if name == '_default_' else all[name]

    def getCurrentSearchKey(self):
        '''In the context of a ref having p_self.searches, returns the key
           storing, in the request, the currently selected search.'''
        return f'{self.name}_view'

    def getCurrentSearch(self, req, searches):
        '''Returns the name of the currently selected search, from this dict of
           p_searches.'''
        key = self.getCurrentSearchKey()
        # The absence of that key means: use the default one. Note that "r" can
        # be the empty string: in that case, the standard view must be shown.
        if key in req:
            r = req[key]
        else:
            r = req[key] = self.getDefaultSearch(searches, True)
        return r

    def getListPx(self, o):
        '''Get the sub-PX to display inside pxList'''
        # In most cases, display the list of tied objects as is
        if not self.searches: return self.pxSub
        # If attribute "searches" is not None, we may have to show search
        # results from one of the searches defined in it, or the standard list
        # of tied objects, depending on some request key.
        req = o.req
        if isinstance(self.searches, Search):
            # We have a unique search in front of the ref: use it
            searchName = '_default_'
        else:
            key = self.getCurrentSearchKey()
            searchName = req[key] if key in req else ''
        # If no search was found, show the standard list of tied objects
        if not searchName: return self.pxSub
        # If we are here, we must render the PX for rendering the found search.
        # Inject the appropriate keys in the request, simulating a call to a
        # search PX.
        req.className = self.class_.meta.name
        # Key "search" allows to find the Search from the request
        req.search = f'{o.iid},{self.name},search*{searchName}'
        # Key "ref" allows to restrict seach results to ref's tied objects
        req.ref = f'{o.iid}:{self.name}'
        context = o.traversal.context
        Px.injectRequest(context, req, o.tool, specialOnly=True)
        context.className = req.className # Not automatically injected
        return context.uiSearch.search.results

    def getListCss(self, c):
        '''Get the CSS classes to apply to the main tag for a Ref rendered as a
           list.'''
        if self.listCss:
            # Use the CSS class(es) defined at the Ref level, plus a potential
            # CSS class generated from column layouts.
            r = self.listCss
            if c.genName:
                r = f'{r} {c.genName}'
        else:
            # Use the CSS class(es) as defined on the tied class
            r = c.tiedClass.getCssFor(c.tool, 'list', add=c.genName)
        return r

    def checkParameters(self):
        '''Ensures this Ref is correctly defined'''
        linkPopup = self.link == 'popup'
        # Attributes "add" and "link" can be used altogether, but only for
        # forward monovalued Refs with link == "popup".
        if self.add and self.link:
            if self.isBack or not linkPopup or self.isMultiValued():
                raise Exception(ADD_LK_KO)
        # If link is "popup", "select" must hold a Search instance
        if linkPopup and \
           (not isinstance(self.select, Search) and not callable(self.select)):
            raise Exception(LK_POP_ERR)
        # Valid link modes depend on multiplicities
        multiple = self.isMultiValued()
        if multiple and self.link == 'radio':
            raise Exception(RADIOS_KO)
        if not multiple and self.link == 'checkbox':
            raise Exception(CBS_KO)
        # A Ref with link="dropdown" must have max multiplicity being 1
        if multiple and self.link == 'dropdown':
            raise Exception(DDOWN_KO)
        # Ensure validity of p_self.emptyIndexValue
        ivalid = Ref.validIndexEmptyValues[self.indexAttribute == 'iid']
        iempty = self.emptyIndexValue
        if iempty not in ivalid:
            raise Exception(E_VAL_KO % (self.indexAttribute,
                                        ', '.join([str(v) for v in ivalid])))

    def isShowable(self, o, layout):
        '''Showability for a Ref adds more rules w.r.t base field rules'''
        r = Field.isShowable(self, o, layout)
        if not r: return r
        # Ther are specific Ref rules for preventing to show the field under
        # inappropriate circumstances.
        if layout == 'edit':
            if not self.editPx or self.isBack: return
        return r

    def isRenderableOn(self, layout):
        '''Only Ref fields with render = "menus" can be rendered on restricted
           layouts.'''
        if self.render == 'menus':
            return layout in Layouts.buttonLayouts
        return super().isRenderableOn(layout)

    def valueIsSelected(self, id, inRequest, dbValue, requestValue):
        '''In PX "Edit", is object whose ID is p_id selected ?'''
        if inRequest:
            # The request value can be a single or multiple value
            r = (id in requestValue) if isinstance(requestValue, list) \
                                     else (id == requestValue)
        else:
            r = id in dbValue
        return r

    def getValue(self, o, name=None, layout=None, single=True, start=None,
                 batch=False, maxPerPage=None, at=None):
        '''Returns the objects linked to p_o through this Ref field.

           * If p_start is None, it returns all referred objects;
           * if p_start is a number, it returns p_maxPerPage objects (or
             self.maxPerPage if p_maxPerPage is None), starting at p_start.

           If p_single is True, it returns the single reference as an object and
           not as a list.

           If p_batch is True, it returns an instance of appy.model.utils.Batch
           instead of a list of references. When single is True, p_batch is
           ignored.
        '''
        # Get the value from the database
        r = super().getValue(o, name, layout, at=at)
        # Return an empty tuple or Batch object if there is no object
        if not r: return Ref.empty if not batch else Batch()
        # The defaut value may not be a list. Ensure v_r is a list.
        if not isinstance(r, utils.sequenceTypes): r = [r]
        # Manage p_single
        if single and self.multiplicity[1] == 1: return r[0]
        total = len(r)
        # Manage p_start and p_maxPerPage
        if start is not None:
            maxPerPage = maxPerPage or self.getAttribute(o, 'maxPerPage')
            # Create a sub-list containing only the relevant objects
            sub = []
            i = start
            total = len(r)
            while i < (start + maxPerPage):
                if i >= total: break
                sub.append(r[i])
                i += 1
            r = sub
        # Manage p_batch
        if batch:
            r = Batch(r, total, size=maxPerPage, start=start or 0)
        return r

    def getCopyValue(self, o):
        '''Return a copy: it can be dangerous to give the real database value'''
        return self.getValue(o, single=False)[:]

    def setRequestValue(self, o):
        '''The "request form" for a Ref value is a list of string-encoded
           iids.'''
        value = self.getValue(o, single=False)
        if value != Ref.empty:
            o.req[self.name] = [str(tied.iid) for tied in value]

    def getComparableValue(self, o):
        '''Return a copy of field value on p_o'''
        # Because a new value does not overwrite but updates the stored value,
        # the comparable value must be a copy of the stored value.
        return self.getCopyValue(o)

    def getFormattedValue(self, o, value, layout='view', showChanges=False,
                          language=None):
        '''Return p_value's string representation'''
        # Use m_renderMinimal to achieve the result
        return self.renderMinimal(o, value, False)

    def getXmlValue(self, o, value):
        '''The default XML value for a Ref is the list of tied object URLs'''
        # Bypass the default behaviour if a custom method is given
        return self.xml(o, value) if self.xml \
                                  else [f'{tied.url}/xml' for tied in value]

    def normalizeSearchValue(self, val):
        '''Converts this individual search p_val(ue) to an int if it is a
           string-encoded int.'''
        return int(val) if val.isdigit() else val

    def getSearchValue(self, req, value=None):
        '''Values from a search form are tied object's IIDS encoded as strings,
           or another attribute as defined in p_self.indexAttribute. If IIDS,
           convert them to integers and manage an and/or operator.'''
        r = Field.getSearchValue(self, req, value=value)
        norm = self.normalizeSearchValue
        if isinstance(r, list):
            # It is a list of values. Get the operator to use.
            oper = Operator.fromRequest(req, self.name)
            r = oper(*[norm(v) for v in r])
        elif r:
            r = norm(r)
        else:
            r = None
        return r

    def updateHistoryValue(self, o, values):
        '''Store, in p_values, tied object's iids and titles instead of the
           objects themselves.'''
        objects = values[self.name]
        val = PersistentList()
        for tied in objects:
            val.append((tied.iid, tied.getShownValue()))
        values[self.name] = val

    def getHistoryValue(self, o, value, i, language=None, empty='-'):
        '''Returns p_self's p_value, as stored in p_o's history at index p_i, as
           must be shown in the UI.'''
        # Return p_empty if p_value is empty
        if not value: return empty
        # p_value is a persistent list of object IIDs and titles, as produced
        # by m_updateHistoryValue hereabove. This method also manages the
        # deprecated format, where p_value is a list of object titles.
        if isinstance(value[0], str):
            # The old format
            lis = ''.join([f'<li>{title}</li>' for title in value])
        else:
            lis = ''.join([f'<li>{title}</li>' for iid, title in value])
        return f'<ul>{lis}</ul>'

    def getValueAt(self, o, at):
        '''Gets p_self's value on this p_o(bject) p_at this date'''
        r = super().getValueAt(o, at)
        if not r: return r
        i = len(r) - 1
        while i >= 0:
            # If p_r comes from p_o's history, p_r items may need conversion
            item = r[i]
            if isinstance(item, str):
                # [Deprecated] v_item is a string. leave it as is: we have no
                # way to find the corresponding object.
                pass
            elif isinstance(item, tuple):
                # The standard (i_iid, s_text) format from an object history, as
                # produced by m_updateHistoryValue hereabove. Convert it to an
                # object.
                iid, text = item
                tied = o.getObject(iid)
                if tied:
                    r[i] = tied
                else:
                    o.log(HIST_O_KO % (o.strinG(), self.name, iid, text))
                    del r[i]
            # Else, it is a Appy object: leave it untouched
            i -= 1
        return r

    def getSelect(self, o, usage=PV_EDIT):
        '''p_self.select can hold a Search instance or a method. In this latter
           case, call the method and return its result, that can be a Search
           instance or a list of objects.'''
        # If no search is defined, get a custom search
        select = getattr(self, Ref.pvMap[usage]) or Search('customSearch')
        r = select if isinstance(select, Search) else self.callMethod(o, select)
        if isinstance(r, Search) and not r.container:
            # Ensure the class is set for this search
            r.init(self.class_.meta)
        return r

    def getPossibleValues(self, o, start=None, batch=False, removeLinked=False,
                          maxPerPage=None, usage=PV_EDIT):
        '''This method returns the list of all objects that can be selected
           to be linked as references to p_o via p_self.'''

        # It is applicable only for Ref fields with link!=False. If master
        # values are present in the request, we use field.masterValues method
        # instead of self.[s|f]select.

        # If p_start is a number, it returns p_maxPerPage objects (or
        # self.maxPerPage if p_maxPerPage is None), starting at p_start. If
        # p_batch is True, it returns an instance of appy.model.utils.Batch
        # instead of returning a list of objects.

        # If p_removeLinked is True, we remove, from the result, objects which
        # are already linked. For example, for Ref fields rendered as a dropdown
        # menu or a multi-selection box (with link=True), on the edit page, we
        # need to display all possible values: those that are already linked
        # appear to be selected in the widget. But for Ref fields rendered as
        # pick lists (link="list"), once an object is linked, it must disappear
        # from the "pick list".

        # p_usage can be one of the PV_* constants as defined above.
        req = o.req
        paginated = start is not None
        maxPerPage = maxPerPage or self.getAttribute(o, 'maxPerPage')
        isSearch = False
        master = self.master
        if master and callable(self.masterValue):
            # This field is an ajax-updatable slave
            if usage == Ref.PV_FILTER:
                # A filter will not get any master. We need to display all the
                # slave values from all the master values the user may see.
                objects = None
                for masterValue in master.getPossibleValues(o):
                    if objects is None:
                        objects = self.masterValue(o, masterValue)
                    else:
                        # Ensure there is no duplicate among collected objects
                        for mo in self.masterValue(o, masterValue):
                            if mo not in objects:
                                objects.append(mo)
                objects = objects or []
            else:
                # Usage is PV_EDIT or PV_SEARCH. Get the master value...
                inReq = self.getMasterInRequest(master, o, req)
                if inReq:
                    # ... from the request if available
                    requestValue = inReq.getRequestValue(o)
                    masterValues = inReq.getStorableValue(o, requestValue,
                                                          single=True)
                elif usage == Ref.PV_EDIT:
                    # ... or from the database if we are editing an object
                    inDb = master if isinstance(master, Field) else master[0]
                    masterValues = inDb.getValue(o, layout='edit')
                else: # usage is PV_SEARCH and we don't have any master value
                    masterValues = None
                # Get the possible values by calling self.masterValue
                if masterValues:
                    objects = self.masterValue(o, masterValues)
                else:
                    objects = []
        else:
            # Get the possible values from the appropriate attribute
            select = getattr(self, Ref.pvMap[usage])
            if not select:
                # No select method or search has been defined: we must retrieve
                # all objects of the referred type that the user is allowed to
                # access.
                objects = o.search(self.class_.__name__, secure=True)
            else:
                # "[s|f]select" can be/return a Search object or return objects
                search = self.getSelect(o, usage)
                if isinstance(search, Search):
                    isSearch = True
                    start = start or 0
                    objects = search.run(o.H(), start=start, batch=paginated)
                else:
                    # "[s|f]select" has returned objects
                    objects = search
        # Remove already linked objects if required
        if removeLinked:
            linked = o.values.get(self.name)
            if linked:
                # Browse objects in reverse order and remove linked objects
                objs = objects if usage == Ref.PV_EDIT else objects.objects
                i = len(objs) - 1
                while i >= 0:
                    if objs[i] in linked: del objs[i]
                    i -= 1
        # If possible values are not retrieved from a Search, restrict (if
        # required) the result to "maxPerPage" starting at p_start. Indeed, in
        # this case, unlike m_getValue, we already have all objects in
        # "objects": we can't limit objects "waking up" to at most "maxPerPage".
        isBatch = isinstance(objects, Batch)
        total = objects.total if isBatch else len(objects)
        if paginated and not isBatch:
            objects = objects[start:start + maxPerPage]
        # Return the result, wrapped in a Batch instance if required
        if batch:
            r = objects if isBatch else Batch(objects, total, maxPerPage, start)
        else:
            r = objects.objects if isBatch else objects
        return r

    def getViewValues(self, o, name, scope, batch, hook):
        '''Gets the values as must be shown on px "view". If p_scope is "poss",
           it is the list of possible, not-yet-linked, values. Else, it is the
           list of linked values. In both cases, we take the sub-set starting at
           p_batch.start.'''
        if scope == 'poss':
            r = self.getPossibleValues(o, start=batch.start, batch=True,
                                       removeLinked=True, maxPerPage=batch.size)
        else:
            # Return the list of already linked values
            r = self.getValue(o, name=name, start=batch.start, batch=True,
                              maxPerPage=batch.size, single=False)
        r.hook = hook
        return r

    def getLinkedObjectsByMenu(self, o, objects):
        '''This method groups p_objects into sub-lists of objects, grouped by
           menu (happens when self.render == 'menus').'''
        if not objects: return ()
        r = []
        # We store in "menuIds" the already encountered menus:
        # ~{s_menuId : i_indexInRes}~
        menuIds = {}
        # Browse every object from p_objects and put them in their menu
        # (within "r").
        for tied in objects:
            menuId = self.menuIdMethod(o, tied)
            if menuId in menuIds:
                # We have already encountered this menu
                menuIndex = menuIds[menuId]
                r[menuIndex].objects.append(tied)
            else:
                # A new menu
                menu = O(id=menuId, objects=[tied])
                r.append(menu)
                menuIds[menuId] = len(r) - 1
        # Complete information about every menu by calling self.menuInfoMethod
        for menu in r:
            menu.head = self.menuInfoMethod(o, menu.id) or '?'
        return r

    def getLinkStyle(self, c):
        '''Gets the CSS styles to apply for rendering the "search" button that
           opens the popup for linking objects.'''
        # Get the value for CSS attribute "float". 
        if self.iconOut:
            # The icon has already been rendered outside the button
            r = ''
        else:
            # Inlay the image as background
            icon = c.icon
            r = '%s;background-position:10%% 50%%' % \
                 (c.url(icon, bg='18px 18px', ram=icon.endswith('.svg')))
        return r

    def getLinkClass(self, c):
        '''Return the CSS classes to apply to the "search button" (link)'''
        r = c.ui.Button.getCss(c.label, iconOut=self.iconOut)
        # Add a specific class for a left- or right-aligned button. On the
        # "edit" layout, always put the button on the right.
        if c.layout == 'edit':
            css = 'rbutton'
        else:
            css = 'rbutton' if self.multiplicity[1] == 1 else 'lbutton'
        return f'{css} {r}'

    def getAddButtonType(self, createVia):
        '''Returns the type of the input tag representing the "add" button'''
        if self.addConfirm or createVia == 'noForm':
            r = 'button'
        else:
            r = 'submit'
        return r

    def getIconUrl(self, url, add=True, asBG=False):
        '''Returns the URL to p_self's "add" or "search" icon (depending on
           p_add), to be used as a background image or not (depending on
           p_asBG).'''
        # In "icon out" mode, no background image must be present
        if asBG and self.iconOut: return ''
        # If p_asBG, get the background image dimensions
        icon = self.addIcon if add else 'search.svg'
        bg = '18px 18px' if asBG else False
        return url(icon, ram=icon.endswith('.svg'), bg=bg)

    def getColSets(self, o, tiedClass, usage=None, addNB=False, addCB=False):
        '''Gets the ColSet instances corresponding to every showable set of
           columns.'''
        attr = 'fshownInfo' if usage == 'filter' else 'shownInfo'
        info = self.getAttribute(o, attr)
        # We can have either a list of strings or Col instances (a single set)
        # or a list of ColSet instances.
        if not isinstance(info[0], ColSet):
            # A single set
            columns = Columns.get(o, tiedClass, info, addNB, addCB)
            return [ColSet('main', '', columns)]
        # Several sets
        r = []
        for colset in info:
            columns = Columns.get(o, tiedClass, colset.columns, addNB, addCB)
            r.append(ColSet(colset.identifier, colset.label, columns))
        return r

    def getCurrentColumns(self, identifier, colsets):
        '''Gets the columns defined for the current colset, whose p_identifier
           is given. The list of available p_colsets is also given.'''
        for cset in colsets:
            if cset.identifier == identifier:
                return cset.columns
        # If no one is found, return the first one, considered the default
        return colsets[0].columns

    def isNumbered(self, o):
        '''Must we show the order number of every tied object ?'''
        r = self.getAttribute(o, 'numbered')
        if not r: return r
        # Returns the column width
        return r if isinstance(r, str) else '15px'

    def getMenuUrl(self, o, tied, target):
        '''We must provide the URL of the p_tied object, when shown in a Ref
           field in render mode 'menus'. If self.menuUrlMethod is specified,
           use it. Else, returns the "normal" URL of the view page for the tied
           object, but without any navigation information, because in this
           render mode, tied object's order is lost and navigation is
           impossible.'''
        if self.menuUrlMethod:
            r = self.menuUrlMethod(o, tied)
            if r is None:
                # There is no specific link to build
                return None, target
            elif isinstance(r, str):
                # The method has just returned an URL
                return r, LinkTarget()
            else:
                # The method has returned a tuple (url, target)
                target = LinkTarget()
                target.target = r[1]
                return r[0], target
        return tied.getUrl(nav='no'), target

    def getMenuCss(self, zone, o, menu, base=None):
        '''Gets the CSS class that will be applied to this p_zone'''
        # Return only this p_base CSS class if no custom CSS is specified
        css = getattr(self, f'{zone}Css')
        if not css: return base or ''
        # Return the base + custom CSS
        r = css(o, menu.objects) if callable(css) else css
        if not r: return base or ''
        return f'{base} {r}' if base else r

    def getBatch(self, o, render, req, hook):
        '''This method returns a Batch instance in the single objective of
           collecting batch-related information that might be present in the
           request.'''
        r = Batch(hook=hook)
        # The total nb of elements may be in the request (when ajax-called)
        total = req.total
        if total: r.total = int(total)
        # When using any render mode, "list" excepted, all objects must be shown
        if render != 'list':
            r.size = None
            return r
        # Get the index of the first object to show
        r.start = int(req[f'{hook}_start'] or req.start or 0)
        # Get batch size
        r.size = int(req.maxPerPage or self.getAttribute(o, 'maxPerPage'))
        return r

    def getBatchFor(self, hook, objects):
        '''Return a Batch instance for a p_total number of objects'''
        return Batch(objects, size=None, hook=hook, total=len(objects))

    def hasSortIndex(self):
        '''An indexed Ref field is not sortable. So an additional index is
           required.'''
        return True

    def validateValue(self, o, value):
        if not self.link: return
        # Only "link" Refs are checked, because, in edit views, "add" Refs are
        # not visible. So if we check "add" Refs, on an "edit" view we will
        # believe that there is no referred object even if there is.
        # Also ensure that multiplicities are enforced.
        if not value:
            nbOfRefs = 0
        elif isinstance(value, str):
            nbOfRefs = 1
        else:
            nbOfRefs = len(value)
        minRef = self.multiplicity[0]
        maxRef = self.multiplicity[1]
        if maxRef is None:
            maxRef = sys.maxsize
        if nbOfRefs < minRef:
            return o.translate('min_ref_violated')
        elif nbOfRefs > maxRef:
            return o.translate('max_ref_violated')

    def linkObject(self, o, p, back=False, secure=False, executeMethods=True,
                   at=None, reindex=False, reindexBack=None):
        '''Links object p_p (which can be a list of objects) to object p_o
           through this Ref field.'''
        # When linking 2 objects via a Ref, m_linkObject must be called twice:
        # once on the forward Ref and once on the backward Ref. p_back indicates
        # if we are calling it on the forward or backward Ref. If p_secure is
        # False, we bypass security checks (has the logged user the right to
        # modify this Ref field ?). If p_executeMethods is False, we do not
        # execute methods that customize the object insertion (parameters
        # insert, beforeLink, afterLink...). This can be useful while migrating
        # data or duplicating an object. If p_at is specified, it is a Position
        # object or an integer index indicating where to insert the object: it
        # then overrides self.insert. The method returns the effective number
        # of linked objects.
        #
        # Security check
        if secure: o.guard.mayEdit(o, self.writePermission, raiseError=True,
                                   info=self)
        # p_value can be a list of objects
        if isinstance(p, utils.sequenceTypes):
            count = 0
            for q in p:
                # Here, m_linkObject is called with "reindex" being False, even
                # if p_reindex is True, in order to avoid reindexing the Ref for
                # each new value being inserted. But the back reference for
                # these objects, if indexed, must be reindexed.
                count += self.linkObject(o, q, back, secure, executeMethods, at,
                                         reindex=False, reindexBack=reindex)
            # Reindex p_self on p_o if indexed
            if reindex and self.indexed: o.reindex(fields=(self.name,))
            return count
        # Get or create the list of tied objects
        if self.name in o.values:
            refs = o.values[self.name]
        else:
            refs = o.values[self.name] = PersistentList()
        # Stop here if the object is already there
        if p in refs: return 0
        # Execute self.beforeLink if present
        if executeMethods and self.beforeLink:
            r = self.beforeLink(o, p)
            # Abort object linking if required by p_self.beforeLink
            if r == False: return 0
        # Where must we insert the object ?
        insert = self.insert
        if at is not None:
            if isinstance(at, int):
                # p_at is already the index where to insert v_p
                i = at
            elif at.insertObject in refs:
                # Insertion logic is overridden by this Position object, that
                # imposes p_o's position within tied objects.
                i = at.getInsertIndex(refs)
            else:
                # The object mentioned in p_at is not (anymore) among v_refs.
                # Insert v_p at the end.
                i = len(refs)
            refs.insert(i, p)
        elif not insert or not executeMethods:
            refs.append(p)
        elif insert == 'start':
            refs.insert(0, p)
        elif callable(insert):
            # It is a method. Use it on every tied object until we find where to
            # insert the new object.
            insertOrder = insert(o, p)
            i = 0
            inserted = False
            while i < len(refs):
                if insert(o, refs[i]) > insertOrder:
                    refs.insert(i, p)
                    inserted = True
                    break
                i += 1
            if not inserted: refs.append(p)
        elif isinstance(insert, tuple):
            refs.append(p)
            if insert[0] == 'sort':
                # It is a tuple ('sort', method). Perform a full sort.
                refs.sort(key=lambda q: insert[1](o, q))
        # Update the back reference (if existing)
        if not back and self.back:
            # Disable security when required
            if secure and not self.backSecurity: secure = False
            indexBack = reindex if reindexBack is None else reindexBack
            self.back.linkObject(p, o, True, secure, executeMethods,
                                 reindex=indexBack)
        # Execute self.afterLink if present
        if executeMethods and self.afterLink: self.afterLink(o, p)
        # Reindex p_self on p_o if indexed
        if reindex and self.indexed: o.reindex(fields=(self.name,))
        return 1

    def unlinkObject(self, o, p, back=False, secure=False, executeMethods=True,
                     reindex=False, reindexBack=None):
        '''Unlinks p_p (which can be a list of objects) from p_o through this
           Ref field and return the number of objects truly unlinked.'''
        # For an explanation about parameters p_back, p_secure and
        # p_executeMethods, check m_linkObject above.
        #
        # Security check
        if secure:
            o.guard.mayEdit(o, self.writePermission, raiseError=True)
            if executeMethods:
                self.mayUnlinkElement(o, p, raiseError=True)
        # p_p can be a list of objects
        if isinstance(p, utils.sequenceTypes):
            count = 0
            for q in p:
                count += self.unlinkObject(o, q, back, secure, executeMethods,
                                           reindex=False, reindexBack=reindex)
            # Reindex p_self on p_o if indexed
            if reindex and self.indexed: o.reindex(fields=(self.name,))
            return count
        refs = o.values.get(self.name)
        if not refs or p not in refs: return 0
        # Unlink p_p
        refs.remove(p)
        # Update the back reference (if existing)
        if not back and self.back:
            # Disable security when required
            if secure and not self.backSecurity: secure = False
            indexBack = reindex if reindexBack is None else reindexBack
            self.back.unlinkObject(p, o, True, secure, executeMethods,
                                   reindex=indexBack)
        # Execute self.afterUnlink if present
        if executeMethods and self.afterUnlink: self.afterUnlink(o, p)
        # If p_self is indexed, update the index when appropriate
        if reindex and self.indexed: o.reindex(fields=(self.name,))
        return 1

    def getStorableValue(self, o, value, single=False):
        '''Convert this p_value, being a object ID or a list of object IDs, to a
           list of objects.'''
        # From some places (ie, a filter), p_o may not be there, preventing
        # conversion of IDs into objects.
        if not value or not o: return value
        r = PersistentList()
        if isinstance(value, str):
            r.append(o.getObject(value))
        else:
            for id in value:
                r.append(o.getObject(id))
        # Return a single object when required
        if single and self.multiplicity[1] == 1:
            r = r[0]
        return r

    def store(self, o, value, secure=True):
        '''Stores on p_o, the p_value, which can be:
           * None;
           * an object ID (as a string);
           * a list of object IDs (=list of strings). Generally, IDs or lists
             of IDs come from Ref fields with link:True edited through the web;
           * an Appy object;
           * a list of Appy objects.'''
        if not self.persist: return
        # Standardize p_value into a list of Appy objects
        objects = value or []
        if not isinstance(objects, utils.sequenceTypes): objects = [objects]
        for i in range(len(objects)):
            tied = objects[i]
            if isinstance(tied, str) or isinstance(tied, int):
                # We have an (I)ID here
                objects[i] = o.getObject(tied)
        # Unlink objects that are not referred anymore
        tiedObjects = o.values.get(self.name, ())
        if tiedObjects:
            i = len(tiedObjects) - 1
            while i >= 0:
                tied = tiedObjects[i]
                if tied not in objects:
                    self.unlinkObject(o, tied, secure=secure)
                i -= 1
        # Link new objects
        if objects: self.linkObject(o, objects, secure=secure)

    def mayLink(self, o):
        '''If p_self defines a link method, this method evaluates it and returns
           its result. Else, the method returns True.'''
        method = self.linkMethod
        return True if method is None else self.getAttribute(o, 'linkMethod')

    def mayAdd(self, o, mode='create', checkMayEdit=True):
        '''May the user create (if p_mode == "create") or link
           (if mode == "link") (a) new tied object(s) from p_o via this Ref ?
           If p_checkMayEdit is False, it means that the condition of being
           allowed to edit this Ref field has already been checked somewhere
           else (it is always required, we just want to avoid checking it
           twice).'''
        # We can't (yet) do that on back references
        if self.isBack: return utils.No('is_back')
        r = True
        # Check if this Ref is addable/linkable
        if mode == 'create':
            r = self.getAttribute(o, 'add')
            if not r: return utils.No('no_add')
        elif mode == 'link':
            if not self.link or not self.isMultiValued() or not self.mayLink(o):
                return
        # Have we reached the maximum number of referred elements ?
        if self.multiplicity[1] is not None:
            objects = o.values.get(self.name)
            count = len(objects) if objects else 0
            if count >= self.multiplicity[1]: return utils.No('max_reached')
        # May the user edit this Ref field ?
        if checkMayEdit:
            if not o.guard.mayEdit(o, self.writePermission):
                return utils.No('no_write_perm')
        # May the user create instances of the referred class ?
        if mode == 'create':
            if self.creators:
                checkInitiator = True
                initiator = RefInitiator(o.tool, o.req, (o, self))
            else:
                checkInitiator = False
                initiator = None
            if not o.guard.mayInstantiate(self.class_.meta, checkInitiator, \
                                          initiator):
                return utils.No('no_create_perm')
        return r

    def checkAdd(self, o, log=False):
        '''Compute m_mayAdd above, and raise an Unauthorized exception if
           m_mayAdd returns False.'''
        may = self.mayAdd(o)
        if not may:
            message = WRITE_KO % (self.container.name, self.name, may)
            if log: o.log(message, type='error')
            o.raiseUnauthorized(message)

    def getOnAdd(self, c):
        '''Computes the JS code to execute when button "add" is clicked'''
        q = c.q
        if c.createVia == 'noForm':
            # Ajax-refresh the Ref with a special param to link a newly created
            # object.
            r = f"askAjax('{c.hook}', null, {{'start':'{c.batch.start}', " \
                f"'action':'doCreateWithoutForm'}})"
            if self.addConfirm:
                r = "askConfirm('script', %s, %s)" % \
                    (q(r, False), q(c.addConfirmMsg))
        else:
            # In the basic case, no JS code is executed: target.onClick is
            # empty and the button-related form is submitted in the main page.
            r = c.target.onClick
            if self.addConfirm and not r:
                r = "askConfirm('form','%s',%s)" % \
                    (c.formName, q(c.addConfirmMsg))
            elif self.addConfirm and r:
                r = "askConfirm('form+script',%s,%s)" % \
                      (q(c.formName + '+' + r, False), q(c.addConfirmMsg))
            elif 'onAddJs' in c:
                # The developer may specify a custom JS call
                r = c.onAddJs
        return r

    def getOnUnlink(self, c):
        '''Computes the JS code to execute when button "unlink" is clicked'''
        o = c.io
        batch = c.batch
        js = f"onLink('unlink','{o.url}','{self.name}','{c.id}'," \
             f"'{batch.hook}','{batch.start}')"
        if not self.unlinkConfirm: return js
        q = c.q
        text = c._('action_confirm')
        return f"askConfirm('script',{q(js, False)},{q(text)})"

    def getAddLabel(self, o, addLabel, tiedClassLabel, inMenu):
        '''Gets the label of the button allowing to add a new tied object. If
           p_inMenu, the label must contain the name of the class whose instance
           will be created by clincking on the button.'''
        return tiedClassLabel if inMenu else o.translate(self.addLabel)

    def getListLabel(self, inPickList):
        '''If self.link == "list", a label must be shown in front of the list.
           Moreover, the label is different if the list is a pick list or the
           list of tied objects.'''
        if self.link != 'list': return
        return 'selectable_objects' if inPickList else 'selected_objects'

    def mayUnlinkElement(self, o, p, raiseError=False):
        '''May we unlink p_p from p_o via this Ref field ?'''
        if not self.unlinkElement: return True
        r = self.unlinkElement(o, p)
        if r: return True
        else:
            if not raiseError: return
            # Raise an exception
            o.raiseUnauthorized(UNLINK_KO)

    def getCbJsInit(self, o):
        '''When checkboxes are enabled, this method defines a JS associative
           array (named "_appy_objs_cbs") that will store checkboxes' statuses.
           This array is needed because all linked objects are not visible at
           the same time (pagination).'''

        # Moreover, if self.link is "list", an additional array (named
        # "_appy_poss_cbs") is defined for possible values.

        # Semantics of this (those) array(s) can be as follows: if a key is
        # present in it for a given linked object, it means that the checkbox is
        # unchecked. In this case, all linked objects are selected by default.
        # But the semantics can be inverted: presence of a key may mean that the
        # checkbox is checked. The current array semantics is stored in a
        # variable named "_appy_objs_sem" (or "_appy_poss_sem") and may hold
        # "unchecked" (initial semantics) or "checked" (inverted semantics).
        # Inverting semantics allows to keep the array small even when checking/
        # unchecking all checkboxes.

        # The mentioned JS arrays and variables are stored as attributes of the
        # DOM node representing this field.

        # The initial semantics depends on the checkboxes default value
        default = 'unchecked' if self.getAttribute(o, 'checkboxesDefault') \
                              else 'checked'
        code = "\nnode['_appy_%%s_cbs']={};\nnode['_appy_%%s_sem']='%s';" % \
               default
        poss = (code % ('poss', 'poss')) if self.link == 'list' else ''
        return "var node=findNode(this, '%d_%s');%s%s" % \
               (o.iid, self.name, code % ('objs', 'objs'), poss)

    def getAjaxData(self, hook, o, **params):
        '''Initializes an AjaxData object on the DOM node corresponding to this
           Ref field.'''
        # Complete params with default parameters
        params['hook'] = hook;
        params['scope'] = hook.rsplit('_', 1)[-1]
        req = o.req
        selector = req.selector
        if selector: params['selector'] = selector
        # Carry the currently selected search, if p_self.searches are defined
        key = self.getCurrentSearchKey()
        if key in req: params[key] = req[key]
        # Carry ckeditor-specific parameters
        if req.CKEditor:
            params['CKEditor'] = req.CKEditor
            params['CKEditorFuncNum'] = req.CKEditorFuncNum
        params['onav'] = req.nav or ''
        params = sutils.getStringFrom(params)
        return "new AjaxData('%s/%s/view', 'GET', %s, '%s')" % \
               (o.url, self.name, params, hook)

    def getHookFor(self, o):
        '''When p_o is shown as a tied object from p_self, this method computes
           the ID of the ajax-refreshable hook tag containing p_o (row in a
           list, div in a grid...).'''
        return '%s_%d' % (self.name, o.iid)

    def getAjaxDataRow(self, o, ohook, parentHook, inPickList, **params):
        '''Initializes an AjaxData object on the DOM node corresponding to
           p_parentHook = a row within the list of referred objects.'''
        # If in the pick list, set appropriate parameters
        if inPickList:
            params['scope'] = 'poss'
            params['layout'] = 'view'
        return "new AjaxData('%s/pxTied','GET',%s,'%s','%s')" % \
               (o.url, sutils.getStringFrom(params), ohook, parentHook)

    traverse['moveObject'] = 'perm:write'
    def moveObject(self, o):
        '''Moves a tied object up/down/top/bottom'''
        req = o.req
        # How to move the item ?
        move = req.move
        # Get the object to move
        tied = o.getObject(req.tiedId)
        objects = getattr(o, self.name, ())
        i = objects.index(tied)
        if move == 'up':
            i -= 1
        elif move == 'down':
            i += 1
        elif move == 'top':
            i = 0
        elif move == 'bottom':
            i = len(objects) - 1
        elif move.startswith('index'):
            # New index starts at 1 (old index starts at 0)
            try:
                i = int(move.split('_')[1]) - 1
            except ValueError:
                i = -1
        # If the new index is negative, the move can't occur
        if i > -1:
            objects.remove(tied)
            objects.insert(i, tied)

    traverse['doCreateWithoutForm'] = 'perm:write'
    def doCreateWithoutForm(self, o):
        '''This method is called when a user wants to create a object from a
           reference field, automatically (without displaying a form).'''
        o.create(self.name)

    xhtmlToText = re.compile('<.*?>', re.S)

    def getReferenceLabel(self, o, tied, unlimited=False, usage=None):
        '''Only works for a Ref with link=True. Displays, on an edit view, the
           p_tied object in the select field allowing the user to choose which
           object(s) to link through the Ref. The information to display may
           only be the object title or more if "shownInfo" is used.'''
        r = ''
        # p_o may not be the tool if we are on a search screen
        for col in self.getColSets(o, tied.class_, usage=usage)[0].columns:
            # Ignore special columns
            if col.special: continue
            name = col.name
            refType = tied.getField(name)
            value = getattr(tied, name)
            value = refType.getShownValue(tied, value) or '-'
            if refType.type == 'Rich':
                value = self.xhtmlToText.sub(' ', value)
            elif isinstance(value, utils.sequenceTypes):
                value = ', '.join(value)
            prefix = ' | ' if r else ''
            r += prefix + value
        if unlimited: return r
        maxWidth = self.width or 30
        if len(r) > maxWidth:
            r = Px.truncateValue(r, maxWidth)
        return r

    def getIndexOf(self, o, tied, raiseError=True, notFoundValue=None):
        '''Gets the position of p_tied object within this field on p_o'''
        # If the object is not found, the method will raise an error, excepted
        # if p_raiseError is False: in that case, it will return
        # p_notFoundValue.
        try:
            return self.getValue(o, single=False).index(tied)
        except ValueError:
            if raiseError: raise IndexError()
            return notFoundValue

    def getPageIndexOf(self, o, tied):
        '''Returns the index of the first object of the page where p_tied is'''
        index = self.getIndexOf(o, tied)
        maxPerPage = self.getAttribute(o, 'maxPerPage')
        return int(index/maxPerPage) * maxPerPage

    traverse['sort'] = 'perm:write'
    def sort(self, o):
        '''Called by the UI to sort the content of this field'''
        req = o.req
        o.sort(self.name, sortKey=req.sortKey, reverse=req.reverse == 'True')

    traverse['gotoTied'] = 'perm:read'
    def gotoTied(self, o):
        '''Redirect to the object tied to p_o via p_self, whose position is
           given by request key "number".'''
        # Get all tied objects
        objects = o.values[self.name]
        # Get the tied object of interest
        req = o.req
        number = int(req.number) - 1
        tied = objects[number]
        # Build this object's URL, with navigation info
        url = tied.getUrl(nav=self.getNavInfo(o, number+1, len(objects)),
                          popup=req.popup or 'False')
        return o.goto(url)

    def getRenderMode(self, layout):
        '''Gets the render mode, determined by self.render and some
           exceptions.'''
        r = self.render
        if r == 'menus' and layout == 'view':
            r = 'list'
        elif r == 'list' and layout == 'cell':
            # Having a complete list rendering within an outer list, is an
            # undesirable UI experience and may lead to name clashes or other
            # problems.
            r = 'links'
        return r

    def getTitleMode(self, o, selector):
        '''How will we render the tied objects' titles ?'''
        if selector: return 'select'
        mode = self.titleMode
        return mode(o) if callable(mode) else mode

    def getPopupLink(self, o, popupMode, name):
        '''Gets the link leading to the page to show in the popup for selecting
           objects.'''
        # Transmit the original navigation when existing
        nav = o.req.nav
        suffix = f'&onav={nav}' if nav else ''
        if self.link in ('popup', 'dropdown'):
            # Go to the page for querying objects
            cname = self.class_.meta.name
            r = f'{o.tool.url}/Search/results?className={cname}&search=' \
                f'{o.iid},{name},{popupMode}&popup=1{suffix}'
        elif self.link == 'popupRef':
            # Go to the page that displays a single field
            po, fieldName = self.select(o) # "po" = the *p*opup *o*bject
            max = self.getAttribute(o, 'maxPerPage')
            r = f'{po.url}/pxField?name={fieldName}&pageLayout=w-b&popup=True&'\
                f'maxPerPage={max}&selector={o.iid},{name},{popupMode}{suffix}'
        return r

    def getSelector(self, o, req):
        '''When this Ref field is shown in a popup for selecting objects to be
           included in an "originator" Ref field, this method gets info from the
           request about this originator.'''
        if 'selector' not in req: return
        id, name, mode = req.selector.split(',')
        initiator = o.getObject(id)
        initiatorField = initiator.getField(name)
        # If several objects can be selected, show their checkboxes
        cbShown = initiatorField.isMultiValued()
        cbClass = '' if cbShown else 'hide'
        return O(initiator=initiator, initiatorField=initiatorField,
                 initiatorMode=mode, onav=req.onav or '',
                 initiatorHook=f'{initiator.iid}_{name}',
                 cbShown=cbShown, cbClass=cbClass,
                 # The originator can also be a rich field for which images must
                 # be browsed. In that case, we transmit "ckNum", a number being
                 # internal to the originating ckeditor.
                 ckNum=req.CKEditorFuncNum or '')

    def getRequestObjects(self, o, requestValue):
        '''Get a list of objects from p_requestValue'''
        # Depending on the cases, p_requestValue can hold an object, an object
        # ID, a list of object IDs or a list of objects.
        # ~
        # Ensure it is a persistent list
        r = requestValue
        if not isinstance(r, utils.listTypes):
            r = [r]
        # Ensure every list item is an object
        i = 0
        while i < len(r):
            if isinstance(r[i], str):
                r[i] = o.getObject(r[i])
            i += 1
        return r

    def getPopupObjects(self, o, name, req, requestValue):
        '''Gets the list of objects that were selected in the popup (for fields
           with link="popup" or "popupRef").'''
        # If there is a request value, We are validating the form. Return the
        # request value instead of the popup value.
        if requestValue: return self.getRequestObjects(o, requestValue)
        # No object can be selected if the popup has not been opened yet
        if 'semantics' not in req:
            # In this case, display already linked objects if any
            return self.getValue(o, name=name, single=False) or []
        r = []
        ids = req.selected.split(',')
        tool = o.tool
        if req.semantics == 'checked':
            # Simply get the selected objects from their uid
            return [o.getObject(id) for id in ids]
        else:
            # If link=popup, replay the search in self.select to get the list of
            # ids that were shown in the popup. If link=popupRef, simply get
            # the list of tied object ids for this Ref.
            if self.link == 'popup':
                search = self.getSelect(o)
                r = search.run(o.H(), batch=False, sortBy=req.sortKey,
                               sortOrder=req.sortOrder,
                               filters=self.class_.meta.getFilters(tool))
            elif self.link == 'popupRef':
                io, iname = self.select(o)
                r = getattr(io, iname)
        return r

    traverse['onSelectFromPopup'] = 'perm:write'
    def onSelectFromPopup(self, o):
        '''This method is called on Ref fields with link=popup[Ref], when
           a user has selected objects from the popup, to be added to existing
           tied objects, from the view widget.'''
        for tied in self.getPopupObjects(o, self.name, o.req, None):
            self.linkObject(o, tied, secure=True, reindex=True)

    def getLinkBackUrl(self, o, req):
        '''Get the URL to redirect the user to after having (un)linked an object
           via this Ref.'''
        # Propagate key(s) of the form "*_start" and "page"
        params = {}
        for name, val in o.req.items():
            if name.endswith('start') or name == 'page':
                params[name] = val
        if 'page' not in params:
            params['page'] = self.page.name
        return o.getUrl(sub='view', **params)

    traverse['onLink'] = 'perm:write'
    def onLink(self, o):
        '''Links or unlinks an object whose id is in the request'''
        o.H().commit = True
        req = o.req
        # What is the precise action to perform ?
        action = req.linkAction
        msg = None
        if not action.endswith('_many'):
            method = getattr(self, f'{req.linkAction}Object')
            tied = o.getObject(int(req.targetId))
            r = method(o, tied, secure=True, reindex=True)
        else:
            # "link_many", "unlink_many", "delete_many". Get the (un-)checked
            # objects from the request.
            if not req.targetId:
                ids = {}
            else:
                ids = {int(sid):None for sid in req.targetId.split(',')}
            unchecked = req.semantics == 'unchecked'
            if action == 'link_many':
                # Get possible values
                values = self.getPossibleValues(o, removeLinked=True)
            else:
                # Get current values
                values = o.values.get(self.name) or ()
            # Collect the objects onto which the action must be performed
            targets = []
            for value in values:
                id = value.iid
                if unchecked:
                    # Keep only objects not among ids
                    if id in ids: continue
                else:
                    # Keep only objects being in uids
                    if id not in ids: continue
                targets.append(value)
            if not targets:
                msg = o.translate('action_null')
            else:
                # Perform the action on every target. Count the number of failed
                # operations.
                failed = 0
                singleAction = action.split('_')[0]
                mustDelete = singleAction == 'delete'
                guard = o.guard
                for target in targets:
                    if mustDelete:
                        # Delete
                        if guard.mayDelete(target):
                            target.delete(historize=True)
                        else: failed += 1
                    else:
                        # Link or unlink. For unlinking, we need to perform an
                        # additional check.
                        if singleAction == 'unlink' and \
                           not self.mayUnlinkElement(o, target):
                            failed += 1
                        else:
                            method = eval(f'self.{singleAction}Object')
                            method(o, target, reindex=True)
                if failed:
                    msg = o.translate('action_partial', mapping={'nb':failed})
        # Redirect the user and display a message
        text = msg or o.translate('action_done')
        if o.H().isAjax():
            o.say(text)
        else:
            o.goto(self.getLinkBackUrl(o, req), message=text)

    def renderMinimal(self, o, objects, popup, links=False):
        '''Render tied p_objects in render mode "minimal" (or "links" if p_links
           is True).'''
        if not objects: return o.translate(self.noObjectLabel)
        r = []
        for tied in objects:
            # p_tied can be a string if it comes from the object history
            if isinstance(tied, str):
                title = tied
                tied = None
            else:
                title = self.getReferenceLabel(o, tied, True)
            if links and tied and tied.allows('read'):
                # Wrap the title in a link
                target = '_parent' if popup else '_self'
                title = f'<a href="{tied.url}/view" target="{target}" ' \
                        f'style="padding:0">{title}</a>'
            r.append(title)
        return self.renderMinimalSep.join(r)

    def getNavInfo(self, o, nb, total, inPickList=False, inMenu=False):
        '''Gets the navigation info allowing to navigate from tied object number
           p_nb to its siblings.'''
        if self.isBack or inPickList or inMenu: return 'no'
        # If p_nb is None, we want to produce a generic nav info into which we
        # will insert a specific number afterwards.
        if nb is None: return 'ref.%d.%s.%%d.%d' % (o.iid, self.name, total)
        return 'ref.%d.%s.%d.%d' % (o.iid, self.name, nb, total)

    def getCollapseInfo(self, o, inPickList):
        '''Returns a Collapsible instance, that determines if the "tied objects"
           or "available objects" zone (depending on p_inPickList) is collapsed
           or expanded.'''
        # Create the ID of the collapsible zone
        suffix = 'poss' if inPickList else 'objs'
        id = '%s_%s_%s' % (o.class_.name, self.name, suffix)
        return ui.Collapsible(id, o.req, default='expanded', display='table')

    def getSupTitle(self, o, tied, nav):
        '''Returns the custom chunk of info that must be rendered just before
           the p_tied object's title.'''
        # A sup-title may be defined directly on this Ref...
        if self.supTitle: return self.supTitle(o, tied, nav)
        # ... or on p_tied's class itself
        return tied.getSupTitle(nav) if hasattr(tied, 'getSupTitle') else None

    def getSubTitle(self, o, tied):
        '''Returns the custom chunk of info that must be rendered just after
           the p_tied object's title.'''
        # A sub-title may be defined directly on this Ref...
        if self.subTitle: return self.subTitle(o, tied)
        # ... or on p_tied's class itself
        return tied.getSubTitle() if hasattr(tied, 'getSubTitle') else None

    def dumpSeparator(self, o, previous, next, columns):
        '''r_eturns a Separator instance if one must be inserted between
           p_previous and p_next objects.'''
        if not self.separator: return ''
        sep = self.separator(o, previous, next)
        if not sep: return ''
        css = ' class="%s"' % sep.css if sep.css else ''
        return '<tr><td colspan="%d"><div%s>%s</div></td></tr>' % \
               (len(columns), css, sep.translated or o.translate(sep.label))

    def getActions(self, o):
        '''Return the custom actions that must be shown among global actions'''
        actions = self.actions
        if not actions: return ()
        r = []
        i = 0
        for action in actions:
            show = action.show
            show = show(o) if callable(show) else show
            if show:
                i += 1
                # Lazy-init the action if not done yet
                if not hasattr(action, 'name'):
                    name = 'action%d' % i
                    action.init(o.class_, name)
                    # Add the action among class fields in the metamodel, Else,
                    # it will not be traversable as any other field.
                    o.class_.fields[name] = action
                r.append(action)
        return r

    def getField(self, subName):
        '''Returns the sub-field whose name in p_subName, among
           p_self.actions.'''
        actions = self.actions
        if not actions: return
        for action in actions:
            if subName == action.name:
                return action

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #      Representation of this field within a class-diagram' class box
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    pxBox = Px('''<tr><td></td><td>::field.getAssocLine(tool)</td></tr>''')

    def getAssocLine(self, tool):
        '''Returns the chunk of code allowing to render this Ref as an
           association within a class diagram.'''
        # What kind of association ? Composite or not ?
        assoc = '◆―' if self.composite else '⸺'
        # Can this field be reindexed ?
        reindex = self.getReindexAction(tool) if self.indexed else ''
        # Compute back information
        back = self.back
        if back:
            sback = f' {back.umlMultiplicities()} {back.name}'
            assoc2 = '―◆' if back.composite else '⸺'
            breindex = back.getReindexAction(tool) if back.indexed else ''
        else:
            sback = ''
            assoc2 = '⸺'
            breindex = ''
        cname = self.class_.__name__
        return f'{assoc}{sback}{breindex} ⸻ {self.name}{reindex} ' \
               f'{self.umlMultiplicities()} {assoc2}<a class="bref" ' \
               f'href="{tool.url}/view?page=model&className={cname}">{cname}'\
               f'</a>'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def autoref(class_, field):
    '''Defines, a posteriori, a Ref from one class the same one, or to another
       one but that could not be directly declared because it would have led to
       a circular import.'''

    # class_.field is a Ref to p_class_. This kind of auto-reference can't be
    # declared in the "normal" way, like this:

    # class A:
    #     attr1 = Ref(A)

    # because at the time Python encounters the static declaration
    # "attr1 = Ref(A)", class A is not completely defined yet.

    # This method allows to overcome this problem. You can write such auto-
    # reference like this:

    # class A:
    #     attr1 = Ref(None)
    # autoref(A, A.attr1)

    # This function can also be used to avoid circular imports between 2 classes
    # from 2 different packages. Imagine class P1 in package p1 has a Ref to
    # class P2 in package p2; and class P2 has another Ref to p1.P1 (which is
    # not the back Ref of the previous one: it is another, independent Ref).

    # In p1, you have

    # from p2 import P2
    # class P1:
    #     ref1 = Ref(P2)

    # Then, if you write the following in p2, Python will complain because of a
    # circular import:

    # from p1 import P1
    # class P2:
    #     ref2 = Ref(P1)

    # The solution is to write this. In p1:

    # from p2 import P2
    # class P1:
    #     ref1 = Ref(P2)
    # autoref(P1, P2.ref2)

    # And, in p2:
    # class P2:
    #     ref2 = Ref(None)
    field.class_ = class_
    back = field.back
    if back: setAttribute(class_, back.attribute, back)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
