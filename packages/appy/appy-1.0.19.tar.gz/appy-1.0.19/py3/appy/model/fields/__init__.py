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
import copy, types, re
from DateTime import DateTime
from persistent.list import PersistentList

from appy.px import Px
from appy import utils
from appy.database import catalog
from appy.model.utils import Fake
from appy.model.totals import Totals
from appy.tr import FieldTranslations
from appy.utils import string as sutils
from appy.model.utils import Object as O
from appy.model.fields.phase import Page
from appy.ui.layout import Layout, Layouts
from appy.model.fields.group import Group, UiGroup

# In this file, names "list" and "dict" refer to sub-modules. To use Python
# builtin types, use __builtins__['list'] and __builtins__['dict']

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
XSS_DETECTED = 'Detected Javascript in user input.'
XSS_WARNING  = 'Your behaviour is considered a security attack. System ' \
               'administrator has been warned.'
UNINDEXED    = 'Field "%s": cannot retrieve catalog version of unindexed field.'
AJAX_EDITED  = 'Ajax-edited %s%s on %s.'
METH_ERROR   = 'Method %s:\n%s'
DEF_ERR      = 'Field %d.%s :: Error. %s'
MUST_IDX_MET = 'Value for parameter "mustIndex" must be a method.'
TYPE_KO      = 'Field %s :: Wrong type: %s (expected type: %s).'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Show:
    '''Provides some frequently used values for field's "show" attributes'''

    # Attribute Field:show allows to specify one or several layouts onto which a
    # field can be rendered. Here are the possible layouts.
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # "view"    | The standard page rendering an object and its fields
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # "edit"    | The standard page rendering the form allowing to edit an
    #           | object and its fields.
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # "result"  | A column within a list of objects being search results or tied
    #           | objects, or some similar zone on alternate views, like a grid.
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # "sub"     | On search/ref results, this zone corresponds to the range of
    #           | icons and/or buttons present besides every object, near its
    #           | title.
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # "buttons" | On an object view/edit page, it corresponds to the sub-zone
    #           | containing the range of icons, actions or other fields.
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # "xml"     | Special, non-graphical layout representing the (marshalled)
    #           | XML view of an object.
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # As a convention, a trailing underscore indicates a negation

    # All layouts but "edit". To use for users that can consult the field value
    # but cannot modify it. Also used for fields like some Ref fields that are
    # never manipulated via "edit" layouts.
    E_  = ('view', 'result', 'xml')
    ER_ = ('view', 'xml') # A variant, without "result"
    E_S = ('view', 'sub', 'xml') # A variant, with "sub" instead of "result"
    S   = ('edit', 'view', 'sub', 'xml')
    BS  = ('buttons', 'sub') # Both in pxButtons and within lists of objects
    BR  = ('buttons', 'result') # Appropriate for some fields like pods

    # All layouts but "view". To use typically when, on "view", the field value
    # is already shown as a part of some custom widget.
    V_  = ('edit', 'result', 'xml')
    V_B = ('edit', 'result', 'xml', 'buttons')

    # All layouts but "view" and "edit'. To use when you need both E_ and V_.
    RX = VE_ = ('result', 'xml')
    RXB = VE_B = RX + ('buttons',) # The same + "buttons"

    # This set is used for showing workflow transitions in lists of objects
    TR = ('view', 'result')

    # Show it on "pre" instead of "view", "result" also allowed
    PR  = ('pre', 'result')
    PRS = ('pre', 'result', 'sub')

    # This is, a.o., for custom widgets whose edit and view variants are not
    # that different, but that cannot be shown elsewhere (result, xml, etc).
    VE  = ('view'   , 'edit')
    VX  = ('view'   , 'xml')
    BX  = ('buttons', 'xml')
    EX  = ('edit'   , 'xml')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Initiator:
    '''From a given field on a given object, it is possible to trigger the
       creation of another object. The most obvious example is the creation of a
       tied object via a Ref field with add=True. An "initiator" represents the
       (object, field) that initiates the object creation.

       In order to customize initiator behaviour, every Field sub-class can
       propose an Initiator sub-class, by overriding its static attribute
       "initiator".'''

    # The concept of initiator can also be used in the context of visualizing
    # objects. For example, when displaying a tied object via a Ref, its
    # "initiator" is considered to be the source object and the source Ref.

    def __init__(self, tool, req, info):
        self.tool = tool
        self.req = req
        # Extract the initiator object and field from p_info, parsed from a
        # "nav" key in the request, or directly containing a tuple (o, field).
        if isinstance(info, str):
            self.info = info.split('.')
            self.o = tool.getObject(self.info[0])
            self.field = self.extractField(req)
        else:
            self.info = ''
            self.o, self.field = info
        # After having created the object, if we are back from a popup, the
        # initiator may force to go back to some URL.
        self.backFromPopupUrl = None

    def extractField(self, req):
        '''Tries to get the initiator field from the request'''
        r = self.o.getField(self.info[1])
        if r is None:
            # This can be an "objectless" initiator. In that case, p_self.o is
            # the tool and the field's class is specified at another index in
            # p_self.info.
            r = self.o.getField(self.info[1], className=self.info[2])
        return r

    def getUrl(self):
        '''Returns the URL for going back to the initiator object, on the page
           showing self.field.'''
        return self.o.getUrl(sub='view', page=self.field.pageName, nav='no')

    def checkAllowed(self, log=False):
        '''Checks that adding an object via this initiator is allowed'''
        return True

    def updateParameters(self, params):
        '''Add the relevant parameters to the object edition page, related to
           this initiator.'''

    def goBack(self):
        '''Once the object has been created, where must we come back ?'''
        # r_ can be:
        # - "view"      return to the "view" page of the created object ;
        # - "initiator" return to the page, on p_self.o, where p_self.field is.
        return 'view'

    def getNavInfo(self, new):
        '''If m_goBack is "view" and navigation-related information must be
           shown on the "view" page of the p_new object, this method returns
           it.'''

    def getBackUrl(self, o):
        '''Get the URL to go to after having initiated creation of object p_o'''
        if self.goBack() == 'view':
            # Stay on the "view" page of the newly created object p_o
            r = o.getUrl(nav=self.getNavInfo(o))
        else:
            # Go back to the initiator page
            r = self.getUrl()
        return r

    def manage(self, new):
        '''Once the p_new object has been created, the initiator must surely
           perform a given action with it (ie, for a Ref field, the new object
           must be linked to the initiator object. This is the purpose of this
           method.'''

    def isComplete(self):
        '''We may have thought that an initiator was there, but once parsed, the
           "nav" key may reveal that there is no initiator at all. When it is
           the case, this method returns False and the initiator is considered
           to be inexistent.'''
        return True

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Validator:
    '''Field-specific Validator class, used in the context of attribute
       Field.validate (see Field constructor).'''

    # Python < 3.7 does not have re.Pattern
    try:
        re.Pattern
    except AttributeError:
        re.Pattern = type(re.compile(''))

    # All types of custom validators one may define in attribute Field.validator
    types = (types.FunctionType, types.MethodType, re.Pattern)

    # This class is not to be confused with the homonym class in package
    # appy.ui.validator, used to validate data coming from an Appy object as
    # rendered on the web UI.

    def validate(self, value):
        '''Return a translated error message if p_value is not valid, True
           else.'''
        return True

    @classmethod
    def evaluateCustom(class_, field, o, value):
        '''Perform custom p_field validation on this p_value for this p_o(bject)
           if a custom validator has been defined on p_field.validator.'''
        # Do nothing if there is no valid custom validator defined on p_field
        types = class_.types
        validator = field.validator
        if not validator or type(validator) not in types: return
        # Get the storable value from the request p_value
        value = field.getStorableValue(o, value)
        if type(validator) == types[-1]:
            # It is a regular expression
            if not validator.match(value):
                return o.translate('field_invalid')
        else:
            # It is a custom function: execute it
            try:
                valV = validator(o, value)
                # If v_valV is a Validator object, delegate validation to its
                # "validate" method.
                if isinstance(valV, Validator):
                    valV = valV.validate(o, value)
                # Analyse the validation value v_valV
                if isinstance(valV, str) and valV:
                    # Validation failed: p_valV contains an error message
                    return valV
                else:
                    if not valV:
                        return o.translate('field_invalid')
            except Exception as e:
                return str(e)
            except:
                return o.translate('field_invalid')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Field:
    '''Basic abstract class for defining any field'''

    # Some elements will be traversable
    traverse = {}

    # Make some related classes available here
    Translations = FieldTranslations
    Layouts = Layouts

    # Some global static variables
    nullValues = (None, '', [], {}, ())
    labelTypes = ('label', 'descr', 'help')
    viewLayouts = ('view', 'cell')
    cellLayouts = ('cell', 'query', 'sub') # Cell-like layouts

    # Those attributes can be overridden by subclasses for defining,
    # respectively, names of CSS and Javascript files that are required by this
    # field, keyed by layout.
    cssFiles = {}
    jsFiles = {}

    # For most fields, getting its value on some object is automatically done at
    # the framework level. Fields for which this must be disabled override the
    # following static attribute.
    customGetValue = False

    # Some fields are "outer": they are composed or inner fields
    outer = False

    # In most cases, outer fields store persistent lists
    outerType = PersistentList

    # The initiator class related to the Field
    initiator = Initiator

    # The name of the index class storing values of this field in the catalog
    indexType = 'Index' # For most fields, the base Index class suits

    # By default, fields are supposed not to be "summable": they cannot be used
    # to compute totals via appy/model/totals::Totals instances.
    summable = False

    # Most fields are not "freezable". Being freezable means: a field value,
    # normally produced via some computation, can store the "hard-coded"
    # (frozen) result of this computation.
    freezable = False

    # Render a field. Optional vars:
    # * fieldName   can be given as different as field.name for fields included
    #               in outer fields: in this case, fieldName includes the row
    #               index.
    # * showChanges If True, a variant of the field showing successive changes
    #               made to it is shown.
    # * minimal     If True, the PX related to p_layout is directly called
    #               (view, cell, etc), instead of layout.pxRender. While this
    #               disables some functions like master/slave relationships, it
    #               returns a more lightweight code.

    pxRender = Px('''<x var="minimal=minimal|False;
      showChanges=showChanges|req.showChanges == 'True';
      layout=layout|req.layout;
      isSearch=layout == 'search';
      hostLayout=hostLayout|req.hostLayout;
      name=fieldName or field.name|field.name;
      widgetName=f'w_{name}' if isSearch else name;
      rawValue=field.getValueIf(o, name, layout, disable=isSearch);
      value=field.getFormattedValue(o, rawValue, layout, showChanges) 
            if not isSearch else None;
      requestValue=not isSearch and field.getStoredValue(o, name, True);
      inRequest=field.valueIsInRequest(o, req, name, layout);
      error=req[f'{name}_error'] or handler.validator.errors.get(name)|None;
      isMultiple=field.isMultiValued();
      masterCss=f'master_{name}' if field.slaves else '';
      tagCss=tagCss|None;
      tagCss=field.getTagCss(tagCss, layout);
      o=o or tool;
      tagId=f'{o.iid}_{name}';
      tagName='slave' if field.master else '';
      layoutTarget=field">:field.getPx(_ctx_)</x>''')

    def doRender(self, layout, o, name=None, minimal=False, tagCss=None,
                 specific=None):
        '''Allows to call pxRender from code, to display the content of this
           field on p_o in some specific context, for example in a Computed
           field.'''
        context = O(layout=layout, field=self, minimal=minimal,
                    name=name or self.name, o=o)
        if tagCss: context.tagCss = tagCss
        if specific: context.update(specific)
        # Get the current PX context, to copy some entries from it. If no such
        # context exists, create one.
        ctx = o.traversal.context or o.traversal.createContext(layout=layout)
        Px.copyContext(context, ctx)
        # Call pxRender
        return self.pxRender(context)

    # Show the field content for some object ("o") on a list of tied objects
    pxTied = Px('''
     <!-- The "title" field -->
     <x if="field.name == 'title'">
      <x if="mayView">
       <x if="not ifield.menuUrlMethod or
              (layout != 'cell')">:ifield.pxObjectTitle</x>
       <x if="ifield.menuUrlMethod and layout == 'cell'"
          var2="target,url=ifield.getMenuUrl(o, \
           tied)">::ui.Title.get(o, target=target, baseUrl=url)</x>
       <x if="not selector and guard.mayAct(o)">:ifield.pxObjectActions</x>
      </x>
      <div if="not mayView">🚫 <x>::mayView.msg | _('unauthorized')</x>
      </div>
     </x>

     <!-- Any other field -->
     <x if="mayView and field.name != 'title' and field.isShowable(o, 'result')"
        var2="layout='cell';
              fieldName=field.name;
              minimal=not field.inlineEdit">:field.pxRender</x>''')

    # Show the field content for some object on a list of results
    pxResult = Px('''
     <!-- The "title" field -->
     <x if="field.name == 'title'"
        var2="navInfo=mode.getNavInfo(currentNumber); target=mode.target;
             showActions=not popup and uiSearch.showActions and guard.mayAct(o);
            backHook=backHook|None; ohook=ohook|None">
      <x if="mayView"
         var2="pageName=o.getDefaultPage('view');
               selectJs=uiSearch.initiator.jsSelectOne(q, cbId,
                         req.onav) if popup else ''">
       <x if="hasattr(o, 'getSupTitle')">::o.getSupTitle(navInfo)</x>
       <x>::ui.Title.get(o, mode=uiSearch.getTitleMode(o, popup), nav=navInfo,
         target=target, page=pageName, popup=popup, selectJs=selectJs,
         pageLayout=uiSearch.search.pageLayoutOnView,
         highlight=True, backHook=backHook)</x>
       <span if="hasattr(o, 'getSubTitle')"
             style=":'display:%s'% ('inline' if mode.showSubTitles else 'none')"
             class="subTitle">::uiSearch.highlight(o.getSubTitle() or '')</span>

       <!-- Actions -->
       <div if="showActions" class=":class_.getSubCss(o, uiSearch)"
            var2="layout='sub';
                  toPopup=target and target.target != '_self';
                  editable=guard.mayEdit(o) and not (popup and toPopup);
                  iconsOnly=class_.getIconsOnly();
                  editPage=o.getDefaultPage('edit');
                  locked=o.Lock.isSet(o, editPage)">

        <!-- Fields on layout "sub" -->
        <x if="not popup and uiSearch.showActions == 'all'"
           var2="fields=o.getFields(layout)">
         <!-- Call cell and not pxRender to avoid having a table -->
         <x for="field in fields"
            var2="name=field.name;
                  value=field.getValueIf(o, name, layout)">:field.cell</x>
        </x>

        <!-- Transitions -->
        <x if="class_.showTransitions(o, 'result')"
           var2="workflow=o.getWorkflow()">:workflow.pxTransitions</x>

        <!-- Edit -->
        <div if="editable" class="ibutton" var2="text=_('object_edit')">
         <a if="not locked" class="iflex1" target=":target.target"
            onclick=":target.getOnClick(backHook or ohook)"
            href=":o.getUrl(sub='edit', page=editPage, nav=navInfo,
                            popup=toPopup)">
          <img src=":svg('edit')" class="iconS" title=":text"/>
         </a>
         <x if="locked" var2="lockStyle='iconS'; page='main'">::o.Lock.px</x>
         <div if="not iconsOnly" class="ibutton"
              onclick="this.previousSibling.click()">:text</div>
        </div>

        <!-- Delete -->
        <div if="not locked and guard.mayDelete(o)" class="ibutton"
             var2="text=_('object_delete')">
         <img class="clickable iconS" src=":svg('deleteS')" title=":text"
              onclick=":o.class_.getDeleteConfirm(o, q, mode.hook)"/>
         <div if="not iconsOnly" class="ibutton"
              onclick="this.previousSibling.click()">:text</div>
        </div>
       </div>
      </x>
      <x if="not mayView">
       <img src=":svg('password')" class="iconS"/>
       <x>:_('unauthorized')</x>
      </x>
     </x>
     <!-- Any other field -->
     <x if="mayView and field.name != 'title' and field.isShowable(o, 'result')"
        var2="layout='cell';
              fieldName=field.name;
              minimal=not field.inlineEdit">:field.pxRender</x>''')

    # Displays a field label
    pxLabel = Px('''<label if="field.hasLabel and field.renderLabel(layout)"
     lfor=":field.name">::_('label', field=field)</label>''')

    # Displays a field description
    pxDescription = Px('''<span if="field.hasDescr"
     class="discreet">::_('descr', field=field)</span>''')

    # Displays a field help (UiGroup has exaclty the same PX)
    pxHelp = UiGroup.pxHelp

    # Displays validation-error-related info about a field
    def validationPx(c):
        '''Python implementation of validation PX'''
        url = c.svg('warning')
        if c.error:
            r = f'<abbr title="{c.error}"><img src="{url}" class="iconS"/>' \
                f'</abbr>'
        else:
            r = f'<img src="{url}" class="iconS" style="visibility:hidden"/>'
        return r
    
    pxValidation = Px(validationPx)

    # Displays the fact that a field is required
    pxRequired = Px(lambda c: '<span class="required">*</span>')

    # Button for showing / hiding changes to the field
    pxChanges = Px('''
     <div if="not o.history.isEmpty(name)" style="margin-bottom: 5px">
      <input type="button"
        var="suffix='hide' if showChanges else 'show';
             label=_(f'changes_{suffix}');
             css=ui.Button.getCss(label);
             icon='changesNo' if showChanges else 'changes';
             bp='False' if showChanges else 'True'"
        class=":css" value=":label" style=":url(icon, bg=True)"
        onclick=":'askField(%s,%s,%s,null,%s)' % (q(tagId), q(o.url),
                                                  q('view'), q(bp))"/>
     </div>''')

    # Widgets for filtering objects (based on text) on search results
    pxFilterText = Px('''
     <div var="name=field.name;
          filterId=f'{mode.hook}_{name}';
          filterIdIcon=f'{filterId}_icon'" class="fhead">
      <!-- Pressing the "enter" key in the field clicks the icon (onkeydown) -->
        <input type="text" size=":field.fwidth" id=":filterId"
          value=":mode.filters.get(name, '')"
          placeholder=":_(col.phLabel) if col.phLabel else ''|''"
          onkeydown=":'if (event.keyCode==13) document.getElementById(%s).
                       click()' % q(filterIdIcon)"/>
      <img id=":filterIdIcon" class="clickable iconS" src=":svg('funnel')"
           onclick=":'askBunchFiltered(%s,%s)' % (q(mode.hook), q(name))"/>
     </div>''')

    # Representation of this field within a class-diagram' class box
    pxBox = Px('''
     <tr>
      <td><x>:field.name</x> : <x>:field.type</x>
          <x if="field.indexed">::field.getReindexAction(o)</x></td>
      <td></td>
     </tr>''')

    def __init__(self, validator, multiplicity, default, defaultOnEdit, show,
      renderable, page, group, layouts, move, indexed, mustIndex, indexValue,
      emptyIndexValue, searchable, filterField, readPermission, writePermission,
      width, height, maxChars, colspan, master, masterValue, focus, historized,
      mapping, generateLabel, label, sdefault, scolspan, swidth, sheight,
      persist, inlineEdit, view, cell, buttons, edit, custom, xml,
      translations):

        # The p_validator restricts which values may be defined. If p_validator
        # is :
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # a method  | the method must accept the value to validate as unique
        #           | arg, and must return True if the validation succeeds, or
        #           | an error message if it fails. The error message must be a
        #           | string containing a translated message. Alternately, the
        #           | method may also return a Validator object (see the
        #           | hereabove-defined Validator class). In that case, the
        #           | method delegates the validation logic to the Validator
        #           | object's "validate" method. This can be practical if the
        #           | validation logic must be configured: validation parameters
        #           | may be passed to the Validator constructor and used by the
        #           | "validate" method.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # a regex   | validation will succeed if the regex matches the value ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # Some fields, like the Select field, define additional or alternate
        # p_validator values, or define some predefined methods or Validator
        # sub-classes. Check every Field sub-class for details.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.validator = validator

        # p_multiplicity is a 2-tuple indicating the minimum and maximum
        # occurrences of values.
        self.multiplicity = multiplicity

        # Is the field required or not ? (derived from multiplicity)
        self.required = self.multiplicity[0] > 0

        # Default value
        self.default = default

        # Default value on layout "edit". If None, self.default is used instead.
        self.defaultOnEdit = defaultOnEdit

        # Must the field be visible or not ?
        self.show = show

        # Is the field renderable on some layout ? If p_renderable is None,
        # default rules apply for determining what field (depending on its type)
        # can be rendered on what layout (see m_isRenderable below, overridden
        # by some sub-classes). If you want to make an exception to these
        # standard rules for some fields, set a method in p_renderable. It will
        # accept a single arg (the current layout) and must return True or
        # False.
        self.renderable = renderable

        # When displaying/editing the whole object, on what page and phase must
        # this field value appear ?
        self.setPage(page)

        # Within self.page, in what group of fields must this one appear?
        self.group = Group.get(group)

        # The following attribute allows to move a field back to a previous
        # position (useful for moving fields above predefined ones).
        self.move = move

        # If indexed is True, a database index will be set on the field for
        # fast access.
        self.indexed = indexed

        # If "mustIndex", True by default, is specified, it must be a method
        # returning a boolean value. Indexation will only occur when this value
        # is True.
        self.mustIndex = mustIndex
        if not mustIndex and not callable(mustIndex):
            raise Exception(MUST_IDX_MET)

        # For an indexed field, the value stored in the index is deduced from
        # the field value and type. If you want to store, in the index, a value
        # being transformed in some way, specify, in parameter "indexValue" a
        # method, accepting the stored value as single arg, and returning the
        # transformed (or alternative) value. Note that this transform cannot
        # modify the type of data structure. For example, for a Ref, the
        # received data structure is a list of objects; the method must also
        # produce a list of objects.
        self.indexValue = indexValue

        # By default, an object having no value for this field will not be
        # indexed in the corresponding index (provided p_self is indexed). This
        # can be a problem if the index is used for sorting: in that case,
        # because one of the sort algorithms in use walks the index to perform
        # the sort, objects not being present in this index will not appear in
        # the sorted result, although present in the unsorted results. For that
        # purpose, the following attribute may hold, for an object having no
        # value for this field, a special value that will nevertheless be stored
        # in the index. This value must be of the same type as other values for
        # this field; else, comparisons used by the sort algorithms will produce
        # an error. Moreover, this special value can be used in searches. Here
        # are two examples.
        # 1. For a Ref field, suppose "emptyIndexValue" is (0,), which is the
        #    default. Indeed, a valid Ref value is a list or tuple of object
        #    IIDs (=integers). If you want to express a search like the
        #    following:
        # 
        #         or_(tiedObjectId1, tiedObjectId2, << no object at all >>)
        #
        #    you can write it using the special value representing no value:
        #
        #                or_(tiedObjectId1, tiedObjectId2, 0)
        #
        # 2. For a String, suppose emptyIndexValue is "-" (which is the default,
        #    because the "minus" sign is smaller that any digit or letter). If
        #    the field is named "name", you can get all objects having no name
        #    by writing
        #                       name='-'
        #
        # If you are sure you will not use your indexed field for sorting, then,
        # specify "emptyIndexValue" being None. Indeed, it will produce a
        # smaller index: objects with no value for this field will not be
        # present in the index. Note that p_emptyIndexValue will also be
        # (slighlty mis)used when sorting Ref objects. Indeed, starting with
        # Python 3, comparing value None to any other value raises an error.
        self.emptyIndexValue = emptyIndexValue

        # If specified "searchable", the field will be added to some global
        # index allowing to perform application-wide, keyword searches.
        self.searchable = searchable

        # You may need to specify another field for rendering a filter for
        # p_self. For example, by default in Appy, field "title" uses field
        # "searchable" as filter PX.
        self.filterField = filterField

        # The PX for filtering field values. If None, it means that the field is
        # not filterable. When a p_filterField is specified, its own filter PX
        # will be used for p_self instead of p_self.filterPx.
        self.filterPx = None

        # Normally, permissions to read or write every attribute in a class are
        # granted if the user has the global permission to read or write
        # instances of that class. Those global permissions are represented by
        # strings "read" and "write". If you want a given attribute, or a
        # sub-set of class attributes, to be protected by specific read and/or
        # write permissions, specify, for attributes "readPermission" and/or
        # "writePermission", alternate strings. When defining a workflow for
        # your class, do not forget to define, for every state and for every
        # custom permission you have mentioned in the following attributes, the
        # list of roles that are granted this permission.
        self.readPermission = readPermission
        self.writePermission = writePermission

        # Widget width and height
        self.width = width
        self.height = height

        # While width and height refer to widget dimensions, maxChars hereafter
        # represents the maximum number of chars that a given input field may
        # accept (corresponds to HTML "maxlength" property). "None" means
        # "unlimited".
        self.maxChars = maxChars or ''

        # If the widget is in a group with multiple columns, the following
        # attribute specifies on how many columns to span the widget.
        self.colspan = colspan or 1

        # The list of slaves of this field, if it is a master
        self.slaves = []

        # The behaviour of this field may depend on another, "master" field
        self.setMaster(master, masterValue)

        # If a field must retain attention in a particular way, set focus=True.
        # It will be rendered in a special way.
        self.focus = focus

        # If we must keep track of changes performed on a field, "historized"
        # must be set to True.
        self.historized = historized

        # Mapping is a dict of contexts that, if specified, are given when
        # translating the label, descr or help related to this field.
        self.mapping = self.formatMapping(mapping)

        # p_self's RAM id
        self.id = id(self)

        # The name of this type
        self.type = self.__class__.__name__

        # The true Python type of the values stored form p_self
        self.pythonType = None

        # While p_self.pythonType defines the main type that will characterize
        # most storable values, p_self.storableTypes can define more types. For
        # example, the Float field has p_self.pythonType = float, and
        # p_self.storableTypes = (float, int). If p_self.storableTypes is None,
        # the only storable type will be p_self.pythonType.
        self.storableTypes = None

        # Get the layouts. Consult layout.py for more info about layouts.
        self.layouts = layouts = Layouts.getFor(self, layouts)

        # Derive the following attributes from the layouts, determining the
        # presence of the various types of labels on this field.
        self.hasLabel = layouts.hasPart('l')
        self.hasDescr = layouts.hasPart('d')
        self.hasHelp  = layouts.hasPart('h')

        # Can this field have values that can be edited and validated?
        self.validable = True

        # By default, if the base label for a field is in use in at least one of
        # its layouts (in p_self.layouts), it will be generated automatically in
        # your app's .pot and .po files. That being said, if the base label is
        # not used in any layout, but you still want it to be generated, for
        # using it in some other, non standard place like a pod or a custom
        # report, set the following attribute to True.
        self.generateLabel = generateLabel

        # If you want to avoid generating translation labels for this field, and
        # use instead translations already defined on another field, use the
        # following attribute "label". A label is made of 2 parts: the prefix,
        # based on class name, and the name, which is the field name by default.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # If "label" is... | it will be understood as...
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # a string         | a new prefix = a new class name. Your field will
        #                  | use the label of an homonym field on another class.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # a tuple          | a tuple (prefix, name), defining both a new prefix
        #                  | and a new field name. Your field will get the label
        #                  | of a field from another class, having another name.
        #                  | And if you want to reuse labels of another field
        #                  | defined on the same class, use a tuple of the form
        #                  |                 (None, name)
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.label = label

        # When you specify a default value "for search" (= "sdefault"), on a
        # search screen, in the search field corresponding to this field, this
        # default value will be present.
        self.sdefault = sdefault

        # Colspan for rendering the search widget corresponding to this field.
        self.scolspan = scolspan or 1

        # Width and height for the search widget
        self.swidth = swidth or width
        self.sheight = sheight or height

        # "persist" indicates if field content must be stored in the database.
        # For some fields it is not wanted (ie, fields used only as masters to
        # update slave's selectable values). If you place a method in attribute
        # "persist", similarly, field value will not be stored, but your method
        # will receive it and you will do whatever you want with it.
        self.persist = persist

        # Can the field be inline-edited (on "view" or "cell" layouts)? A method
        # can be specified. If "inlineEdit" is or returns True, a click within
        # the field value as shown on the "view" or "cell" layout will switch
        # the widget to "edit" mode. If it returns 'icon', Switching to "edit"
        # will be done via an "edit" icon.
        self.inlineEdit = inlineEdit

        # Any alternate PX defined in the following attributes will be used in
        # place of the standard ones.
        if view    is not None: self.view    = view
        if cell    is not None: self.cell    = cell
        if buttons is not None: self.buttons = buttons
        if edit    is not None: self.edit    = edit

        # p_custom may hold a custom PX. It does not have a default PX (as is
        # the case for the previous attributes), because it represents a
        # completely custom addition one may define on a field, corresponding to
        # letter "x" in a layout.
        self.custom = custom

        # Standard marshallers are provided for converting values of this field
        # into XML. If you want to customize the marshalling process, you can
        # define a method in "xml" that will accept a field value and will
        # return a possibly different value. Be careful: do not return a chunk
        # of XML here! Simply return an alternate value, that will be
        # XML-marshalled.
        self.xml = xml

        # The standard system for getting field translations (label,
        # description, etc) is based on translations stored in persistent
        # Translation instances in tool.translations. But one may bypass this
        # system by placing an instance of class
        #            appy.fields.translations.FieldTranslations
        # in this attribute.
        self.translations = translations

    def init(self, class_, name):
        '''Lazy initialisation'''
        # The class into which this field is defined
        self.container = class_
        # The name of the field
        self.name = name
        # Remember master name on every slave
        for slave in self.slaves: slave.masterName = name
        # Determine ids of i18n labels for this field, excepted if translations
        # are already present in self.tranlations.
        if not self.translations:
            prefix = label = None
            if self.label:
                if isinstance(self.label, str):
                    prefix = self.label
                else: # It is a tuple (prefix, name)
                    prefix, label = self.label
            # Complete missing information
            prefix = prefix or class_.name
            label = label or self.name
            # Determine name to use for i18n
            self.labelId = f'{prefix}_{label}'
            self.descrId = f'{self.labelId}_descr'
            self.helpId  = f'{self.labelId}_help'

    def __repr__(self, start='‹', end='›'):
        '''Short string representation for this field'''
        # If p_self's repr goes to the UI, using surrounding chars "<" and ">"
        # may cause XHTML escaping problems.
        name = f'{self.container.name}::{self.name}' \
               if hasattr(self, 'container') else 'uninit'
        cname = self.__class__.__name__.lower()
        return f'{start}field {name} ({cname}){end}'

    def asString(self):
        '''p_self's alternate short string representation'''
        return self.__repr__(start='', end='')

    def isMultiValued(self):
        '''Does this type definition allow to define multiple values?'''
        maxOccurs = self.multiplicity[1]
        return maxOccurs is None or maxOccurs > 1

    def umlMultiplicities(self):
        '''Return p_self's multiplicities in UML format'''
        s, e = self.multiplicity
        if e is None:
            r = '*' if s == 0 else f'{s}..*'
        elif e == s:
            r = str(s)
        else:
            r = f'{s}..{e}'
        return r

    def isSortable(self, inRefs=False):
        '''Can fields of this type be used for sorting purposes, when sorting
           search results (p_inRefs=False) or when sorting Ref fields
           (inRefs=True) ?'''
        if not inRefs:
            # An empty index value is required, because, starting with Python 3,
            # comparison with None and something not being None raises an error.
            return self.indexed and self.emptyIndexValue is not None and \
                   not self.isMultiValued()
        # When p_inRef is True, this method will be overridden by fields for
        # which sort is allowed.

    def getFilterField(self):
        '''p_self may be the variant of another field: this latter must be used
           when it comes to filtering and sorting. This method returns this
           potential filter companion, or p_self if none is defined, together
           with the PX to use for filtering.'''
        target = self.filterField or self
        name = target.filterPx
        if name:
            r = target, getattr(target, name)
        else:
            r = self, None
        return r

    def isShowable(self, o, layout):
        '''When displaying p_o on a given p_layout, must we show this field ?'''
        # Check if the user has the permission to view or edit the field
        perm = self.writePermission if layout == 'edit' else self.readPermission
        if not o.allows(perm): return
        # Evaluate self.show
        if callable(self.show):
            r = self.callMethod(o, self.show)
        else:
            r = self.show
        # Take into account possible values 'view', 'edit', 'result', etc.
        if type(r) in utils.sequenceTypes:
            return layout in r
        elif r in Layouts.types:
            return r == layout
        # For showing a field on some layouts, they must explicitly be returned
        # by the "show" method.
        if layout not in Layouts.explicitTypes:
            return bool(r)

    def isRenderable(self, layout):
        '''Returns True if p_self can be rendered on this p_layout'''
        # In some contexts, computing m_isShowable can be a performance problem.
        # For example, when showing some object's fields on layout "buttons",
        # there are plenty of fields that simply can't be shown on this kind of
        # layout: it is no worth computing m_isShowable for those fields.
        # m_isRenderable is meant to define light conditions to determine,
        # before calling m_isShowable, if some field has a chance to be shown
        # or not.

        # In other words, m_isRenderable defines a "structural" condition,
        # independent of any object, while m_isShowable defines a contextual
        # condition, depending on some object.

        # That being said, if p_self.renderable is passed, it short-circuits
        # this structural condition for p_self.
        if self.renderable:
            r = self.renderable(layout)
        else:
            r = self.isRenderableOn(layout)
        return r

    def isRenderableOn(self, layout):
        '''Called by m_isRenderable when p_self.renderable is None'''
        # This method may be overridden, but not p_isRenderable itself
        return layout not in Layouts.restrictedTypes

    def isInnerable(self):
        '''May p_self be used as inner field within an outer field ?'''
        # Most of the time, yes. Child classes may override this.
        return True

    def isClientVisible(self, o):
        '''Returns True if p_self is visible according to master/slave
           relationships.'''
        masterData = self.getMasterData()
        if not masterData: return True
        else:
            master, masterValue = masterData
            if masterValue and callable(masterValue): return True
            # Get the master value from the request
            req = o.req
            if (master.name not in req) and (self.name in req):
                # The master is not there: we cannot say if the slave must be
                # visible or not. But the slave is in the request. So we should
                # not prevent this value from being taken into account.
                return True
            reqValue = master.getRequestValue(o)
            # reqValue can be a list or not
            if type(reqValue) not in utils.sequenceTypes:
                return reqValue in masterValue
            else:
                for m in masterValue:
                    for r in reqValue:
                        if m == r: return True

    def inGrid(self, layout='edit'):
        '''Is this field in a group with style "grid" ?'''
        if not self.group: return
        if isinstance(self.group, __builtins__['dict']):
            for lay, group in self.group.items():
                if lay != layout: continue
                return group and (group.style == 'grid')
            return
        return self.group.style == 'grid'

    def formatMapping(self, mapping):
        '''Creates a dict of mappings, one entry by label type (label, descr,
           help).'''
        if isinstance(mapping, __builtins__['dict']):
            # Is it a dict like {'label':..., 'descr':...}, or is it directly a
            # dict with a mapping?
            for k, v in mapping.items():
                if (k not in self.labelTypes) or isinstance(v, str):
                    # It is already a mapping
                    return {'label':mapping, 'descr':mapping, 'help':mapping}
            # If we are here, we have {'label':..., 'descr':...}. Complete
            # it if necessary.
            for labelType in self.labelTypes:
                if labelType not in mapping:
                    mapping[labelType] = None # No mapping for this value
            return mapping
        else:
            # Mapping is a method that must be applied to any i18n message
            return {'label':mapping, 'descr':mapping, 'help':mapping}

    def getPx(self, c):
        '''Returns the PX corresponding to p_c.layout'''
        layout = c.hostLayout or c.layout
        if c.minimal:
            # Call directly the layout-related PX on the field (bypass the
            # layout PX).
            r = getattr(self, layout)
        else:
            # Get the Layout object related to p_layout and render its PX
            if layout in Field.cellLayouts:
                table = self.Layouts.cell
            else:
                table = self.layouts[layout]
            # Add the layout in the context, it is required by its PX
            c.table = table
            r = table.pxRender
        # Before rendering the PX, compute totals if required
        if self.summable: Totals.updateAll(self, c)
        return r

    def setMandatoriness(self, required):
        '''Updating mandatoriness for a field is not easy, this is why this
           method exists.'''
        # Update attributes "required" and "multiplicity"
        self.required = required
        self.multiplicity = (1 if required else 0), self.multiplicity[1]
        # Update the "edit" layout. Clone the layouts: they may be shared by
        # other fields.
        layouts = self.layouts.clone()
        layouts['edit'].setRequired(required)
        self.layouts = layouts

    def setMaster(self, master, masterValue):
        '''Initialises the master and the master value if any'''
        self.master = master
        if master:
            # Several masters are allowed in some cases
            if isinstance(master, Field):
                master.slaves.append(self)
            else:
                for mas in master:
                    mas.slaves.append(self)
        # The semantics of attribute "masterValue" below is as follows:
        # - if "masterValue" is anything but a method, the field will be shown
        #   only when the master has this value, or one of it if multivalued;
        # - if "masterValue" is a method, the value(s) of the slave field will
        #   be returned by this method, depending on the master value(s) that
        #   are given to it, as its unique parameter.
        self.masterValue = utils.initMasterValue(masterValue)

    def setPage(self, page):
        '''Puts p_self into this p_page. If p_page is None, p_self will be
           rendered in the default page.'''
        if page:
            self.page = Page.get(page)
            self.pageName = self.page.name
        else:
            self.page = self.pageName = None

    def getCss(self, o, layout, r):
        '''Complete list p_r with the names of CSS files that are required for
           displaying widgets of self's type on a given p_layout. p_r is not a
           set because order of inclusion of CSS files may be important.'''
        if layout in self.cssFiles:
            for name in self.cssFiles[layout]:
                if name not in r:
                    r.append(name)

    def getJs(self, o, layout, r, config):
        '''Completes list p_r with the names of Javascript files that are
           required for displaying widgets of self's type on a given p_layout.
           p_r is not a set because order of inclusion of Javascript files may
           be important.'''
        if layout in self.jsFiles:
            for name in self.jsFiles[layout]:
                if name not in r:
                    r.append(name)

    def isInner(self):
        '''Returns True if p_self is an inner field within a container field'''
        return '*' in self.name

    def getValueAt(self, o, at):
        '''Gets p_self's stored value on this p_o(bject), p_at this moment (a
           DateTime object).'''
        # Return None if p_o does not store any value for p_at
        name = self.name
        if name not in o.values: return
        # Browse p_o's history (most recent first), looking for data changes
        r = None
        found = False # Will be True if a value has been found in p_o's history
        for event in o.history.iter(eventType='Change'):
            if event.date < at:
                # What occurred before p_at is not interesting
                break
            # Is there a value for p_self on this change ? If yes, get it
            elif event.hasField(name):
                r = event.getValue(name)
                found = True
        # Return the historical value, if found, the currently stored value else
        return r if found else o.values.get(name)

    def getStoredValue(self, o, name=None, fromReq=False, at=None):
        '''Gets the value in its form as stored in the database, or in the
           request if p_fromReq is True. It differs from calling
           m_getRequestValue because here, in the case of an inner field, the
           request value is searched within the outer value build and stored on
           the request.'''
        if self.isInner():
            # An inner field. In that case, p_name contains the row index.
            # Without it, it is impossible to get the value.
            if name is None: return
            # p_self is a sub-field into an outer field: p_name is of the form
            #            [outerName]*[name]*[rowId]
            outerName, name, rowId = name.split('*')
            if rowId == '-1': r = None # It is a template row
            else:
                # Get the outer value
                outer = o.getField(outerName)
                r = o.req[outerName] if fromReq else outer.getValue(o, at=at)
                # Access the inner value
                if r:
                    if outer.outerType == PersistentList:
                        # The row ID is the index of an element from a list
                        rowId = int(rowId)
                        if rowId < len(r):
                            r = getattr(r[rowId], name, None)
                        else:
                            r = None
                    else:
                        # The row ID is a key from a dict. Remove the -d- prefix
                        r = r.get(rowId[3:], None)
                        if r: r = r.get(name, None)
            # Return an empty string if p_fromReq is True
            if fromReq and r is None: r = ''
        else:
            # A standard, non-inner value
            if fromReq:
                r = self.getRequestValue(o, self.name)
            elif at:
                r = self.getValueAt(o, at)
            else:
                r = o.values.get(self.name)
        return r

    def getRequestValue(self, o, requestName=None):
        '''Gets a value for this field as carried in the request'''
        #  In the simplest cases, the request value is a single value whose name
        # in the request is the name of the field.

        # Sometimes, several request values must be combined (ie: see the
        # overriden method in the Date class).

        # Sometimes (ie, a field within a List/Dict), the name of the request
        # value(s) representing the field value does not correspond to the field
        # name (ie: the request name includes information about the container
        # field). In this case, p_requestName must be used for searching into
        # the request, instead of the field name (self.name).

        # Ensure multiplicities are respected
        r = o.req[requestName or self.name]
        if not isinstance(r, __builtins__['list']) and self.isMultiValued():
            r = [] if r is None else [r]
        return r

    def setRequestValue(self, o):
        '''Sets, in the request, field value on p_o in its "request" form (=the
           way the value is carried in the request).'''
        # Get a copy of the field value on p_o and put it in the request
        value = self.getCopyValue(o)
        if value is not None:
            o.req[self.name] = value

    def getRequestSuffix(self, o):
        '''In most cases, in the user interface, there is one homonym HTML
           element for representing this field. Sometimes, several HTML elements
           are used to represent one field (ie, for non-native dates: one field
           for the year, one for the month, etc). In this case, every HTML
           element's name has the form <field name><suffix>. This method returns
           the suffix of the "main" HTML element.'''
        return ''

    def getValue(self, o, name=None, layout=None, single=None, at=None):
        '''Gets, on p_o(bject), the value for this field (p_self)'''

        # Possible values for parameters are described hereafter.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # name    | p_name can be different from self.name if p_self is a
        #         | sub-field into a List: in this case, it includes the row
        #         | number.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # layout  | In most cases, we don't care about the layout for getting
        #         | the value of p_self on p_o. One exception is that a default
        #         | value can be defined specifically on layout "edit". In that
        #         | case, p_layout must be available in order to determine the
        #         | possible specific default value for this layout.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # single  | This attribute, although defined here at the most abstract
        #         | level, has only sense for "multi-values", like values from
        #         | the Ref field. Such values are always stored as lists or
        #         | tuples but, when field multiplicity is (x, 1), it is
        #         | sometimes convenient to retrieve the single stored value.
        #         | This can be achieved with p_single being True. If p_single
        #         | is None or False, the retrieved value will be the whole
        #         | list or tuple.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # at      | This attribute may hold a DateTime object. If it is the
        #         | case, m_getValue will get p_self's value on p_o at this
        #         | precise date (using p_o's history and its potential data
        #         | changes).
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # Get the value from the database
        value = self.getStoredValue(o, name, at=at)
        if self.isEmptyValue(o, value):
            # If there is no value, get the default value if any. Determine
            # which one must be used: p_self.default or p_self.defaultOnEdit.
            if layout == 'edit':
                default = self.defaultOnEdit
                if default is None: default = self.default
            else:
                default = self.default
            # Get the default value, which can be a method
            if callable(default):
                try:
                    # Caching a default value can lead to problems. For example,
                    # the process of creating an object from another one, or
                    # from some data, sometimes consists in (a) creating an
                    # "empty" object, (b) initializing its values and
                    # (c) reindexing it. Default values are computed in (a),
                    # but it they depend on values set at (b), and are cached
                    # and indexed, (c) will get the wrong, cached value.
                    default = self.callMethod(o, default, cache=False)
                except Exception as e:
                    o.log(DEF_ERR % (o.iid, self.name, str(e)), type='error')
                    # Do not raise the exception, because it can be raised as
                    # the result of reindexing the object in situations that are
                    # not foreseen by v_default.
                    default = None
            return default
        return value

    def getValueIf(self, o, name, layout, disable=False):
        '''Special method only called by the framework. For some fields (or
           according to some p_disable condition), value retrieval as performed
           here must be disabled.'''
        if disable or self.customGetValue: return
        return self.getValue(o, name, layout)

    def getCopyValue(self, o):
        '''Gets the value of this field on p_o as with m_getValue above. But
           if this value is mutable, get a copy of it.'''
        return self.getValue(o)

    def getComparableValue(self, o):
        '''Get the value of this field on p_o, as can be compared with its new
           version, coming from the validator.'''
        # For immutable values, it simply returns the currently stored value.
        # For mutable values, there are 2 cases:
        # (a) the value as produced by the validator completely overwrites the
        #     existing value. Thus, the previous and new versions can safely be
        #     compared, because being completely distinct. In this case, as for
        #     immutable values, the currently stored value can also be used
        #     as-is, as "comparable" value ;
        # (b) the value as produced by the validator updates the stored value.
        #     In this case, comparing the previous and new versions would lead
        #     to comparing the same value. Here, the "comparable" value must be
        #     a deep copy of the previous value and not the stored value itself.
        return self.getValue(o, single=False)

    def getFormattedValue(self, o, value, layout='view', showChanges=False,
                          language=None):
        '''p_value is a real p_o(bject) value from a field from this type. This
           method returns a pretty, string-formatted version, for displaying
           purposes. Needs to be overridden by some child classes. If
           p_showChanges is True, the result must also include the changes that
           occurred on p_value across the ages. If the formatting implies
           translating some elements, p_language will be used if given, the
           user language else.'''
        if self.isEmptyValue(o, value): return ''
        return value

    def getShownValue(self, o, value, layout='view', showChanges=False,
                      language=None):
        '''Similar to m_getFormattedValue, but in some contexts, only a part of
           p_value must be shown. For example, we may need to display only
           a language-specific part of a multilingual field (see overridden
           method in string.py).'''
        return self.getFormattedValue(o, value, layout, showChanges, language)

    def getXmlValue(self, o, value):
        '''This method allows a developer to customize the value that will be
           marshalled into XML. It makes use of attribute "xml".'''
        return value if not self.xml else self.xml(o, value)

    def updateHistoryValue(self, o, values):
        '''p_values is a dict of field values, of the form
                             ~{s_fieldName: fieldValue}~,
           containing values being stored on p_o prior to a change. Before
           storing this dict in p_o's history, it may be needed to modify, in
           this dict, the (key, value) pair corresponding to p_self.'''
        # In most cases, p_values can be stored as-is, no transform is required

    def getHistoryValue(self, o, value, i, language=None, empty='-'):
        '''Returns p_value as must be shown in the UI within p_o's history. If
           p_language is specified, p_value is the p_language-specific part of a
           multilingual field. p_value is in p_o's history, at entry whose index
           is p_i.'''
        if language is None:
            r = self.getFormattedValue(o, value)
        else:
            r = self.getUniFormattedValue(o, value, contentLanguage=language)
        # If p_r is a list, transform it into a HTML "ul" tag
        if isinstance(r, utils.sequenceTypes):
            lis = ''.join([f'<li>{v}</li>' for v in r])
            r = f'<ul>{lis}</ul>'
        elif not r:
            r = empty
        return r

    def getSearchValue(self, req, widgetName=None, value=None):
        '''Returns the search value (or interval of values) that has been
           encoded in a search form (in p_req) for matching values for this
           field. This value may already be passed in p_value.'''
        if value is not None: return value
        # The base search widget corresponding to p_self is prefixed with "w_".
        # p_widgetName can be specified to get the sub-value of another widget
        # that is part of the complete search widget for p_self.
        widgetName = widgetName or f'w_{self.name}'
        # p_req[widgetName] is the base (string) value encoded in the search
        # form. But the search value (or interval of values) can be made of
        # several form fields: overriden methods in Field sub-classes must build
        # search values from these parts, and also convert it to index-compliant
        # values.
        return req[widgetName] or ''

    def searchValueIsEmpty(self, req, widgetName=None):
        '''In some search form, must the search value or interval of values
           specified for this field (p_self) be considered as empty ?'''
        # If, for example, the search widget for this field is made of an
        # interval (from, to), p_widgetName can be given to correspond to the
        # widget part "to", while, by default, the specified part is "from". For
        # some Field sub-classes, the search widget may be even more complex and
        # made of more parts.
        widgetName = widgetName or f'w_{self.name}'
        # Conditions in overriden methods can be more complex. For example, if
        # an interval of values (min, max) is expected, specifying only "min" or
        # "max" will allow to perform a search. In this case, we will consider
        # the search value as empty if both "min" and "max" are not specified.
        value = req[widgetName]
        if value and isinstance(value, str): value = value.strip()
        return not value

    def getInlineEditableValue(self, o, value, layout, name=None,
                               language=None):
        '''Returns p_value as it must appear on a view layout, with code
           allowing to inline-edit it when relevant.'''
        # Disable inline-edition if not specified
        inlineEdit = self.getAttribute(o, 'inlineEdit')
        if not inlineEdit: return value
        # Disable inline-edition if the user can't modify the value
        if not o.allows(self.writePermission) or o.Lock.isSet(o, self.pageName):
            return value
        # Enable inline-edition, either via an additional icon or by clicking
        # in the value.
        suffix = f'_{language}' if language else ''
        hook = f'{o.iid}_{name or self.name}{suffix}'
        onClick= f'onclick="askField(\'{hook}\',\'{o.url}\',\'edit:{layout}\')"'
        if inlineEdit == 'icon':
            iconUrl = o.buildSvg('editS')
            iconText = o.translate('object_edit')
            r = f'<img src="{iconUrl}" title="{iconText}" class="inlineIcon ' \
                f'iconS" {onClick}/>{value}'
        else:
            r = f'<span class="editable" {onClick}>{value}</span>'
        return r

    def getFakeObject(self, value, req):
        '''Returns a fake object, to mimic an object storing this p_value for
           field p_self.'''
        return Fake(self, value, req)

    def getIndexType(self, class_=False):
        '''Returns the name of the class corresponding to the index used to
           store values of this field in a database catalog, or the class itself
           if p_class_ is True.'''
        r = self.indexType
        return eval(f'catalog.{r}') if class_ else r

    def getIndex(self, o):
        '''Gets the Index object corresponding to this field, or None if the
           field is not indexed.'''
        catalog = o.getCatalog(self.container)
        return catalog.get(self.name) if catalog else None

    def getReindexAction(self, o):
        '''Render an icon allowing to entirely reindex p_self's index'''
        index = self.getIndex(o)
        return index.getAction(o) if index else ''

    def getIndexValue(self, o, searchable=False, raw=False):
        '''Return a version for this field value on p_o being ready for indexing
           purposes.'''
        # If p_searchable is True, the value must be a string because it is
        # meant to be included in index "searchable".
        #
        # If p_raw is True, instead of returning the internal value ready to be
        # indexed, it returns the value before being converted to its internal
        # index representation.
        #
        # Must we produce an index value ?
        if not self.getAttribute(o, 'mustIndex'): return
        # The indexed value is based on the stored field value
        r = self.getValue(o)
        # Possibly transform the value
        if not searchable:
            r = self.indexValue(o, r) if self.indexValue else r
            # If there is no value to index, get the special value representing
            # an empty value.
            r = self.emptyIndexValue if self.isEmptyValue(o, r) else r
        # Return the value to index (or, if p_raw, the current value in "r")
        if raw: return r
        index = self.getIndexType(True)
        return index.toString(o, r) if searchable else index.toIndexed(r, self)

    def getCatalogValue(self, o, index=None):
        '''Returns the value being currently stored in the catalog for this
           field on p_o.'''
        if not self.indexed: raise Exception(UNINDEXED % self.name)
        # If the corresponding database p_index is not given, get it
        return (index or self.getIndex(o)).getByObject(o, self)

    def hasSortIndex(self):
        '''Some fields have indexes that prevents sorting (ie, list indexes).
           Those fields may define a secondary index, specifically for sorting.
           This is the case of Ref fields for example.'''

    def getSortValue(self, o):
        '''Return the value of p_self on p_o that must be used for sorting.
           While the raw p_value may be the value to use in most cases, it is
           not always true. For example, a string like "Gaëtan" could have
           "gaetan" as sort value.'''
        r = self.getValue(o)
        return self.emptyIndexValue if r is None else r

    def valueIsInRequest(self, o, req, name=None, layout='view'):
        '''Is there a value corresponding to this field in the request? p_name
           can be different from self.name (ie, if it is a field within another
           (List) field). In most cases, checking that this p_name is in the
           request is sufficient. But in some cases it may be more complex, ie
           for string multilingual fields.'''
        return (name or self.name) in req

    def getMasterInRequest(self, fields, o, req):
        '''Returns, among these p_fields, the first one having a value in the
           p_req(uest).'''
        # Is there a single master in p_fields ?
        single = isinstance(fields, Field)
        # Check first the presence of request key "_master_", being in the
        # request if ajax-triggered.
        masterName = req._master_
        if masterName:
            if single:
                return fields if fields.name == masterName else None
            else:
                for field in fields:
                    if field.name == masterName:
                        return field
        elif single:
            return fields if fields.valueIsInRequest(o, req) else None

    def getStorableValue(self, o, value, single=False):
        '''p_value is a valid value initially computed through calling
           m_getRequestValue. So, it is a valid representation of the field
           value coming from the request. This method computes the value
           (potentially converted or manipulated in some other way) as can be
           stored in the database.'''
        # More precisely, m_getStorableValue computes a value that can be used
        # as input for m_store. But this latter can further transform it. For
        # example, a value produced by p_getStorableValue for a Ref field is a
        # list of objects; method Ref.store will then go further and make
        # cross-links between them and p_o.
        if self.isEmptyValue(o, value): return
        return value

    def getFilterValue(self, value):
        '''Convert this p_value, being a raw value from the UI filter, into a
           value that can be used as parameter to perform a search.'''
        # In general, this can be achieved by converting p_value to a storable
        # value.
        return self.getStorableValue(None, value)

    def getValueFilter(self, value):
        '''Convert this p_value, produced by m_getFilterValue, into its form as
           manipulated by a UI filter.'''
        # This method is m_getFilterValue's mirror. In most cases, no transform
        # is required.
        return value

    def getInputValue(self, inRequest, requestValue, value):
        '''Gets the value that must be filled in the "input" widget
           corresponding to this field.'''
        if inRequest:
            return requestValue or ''
        else:
            return value or ''

    def isReadonly(self, o):
        '''Returns True if, when this field is rendered on an edit layout as an
           input field, it must have attribute "readonly" set.'''
        return bool(self.getAttribute(o, 'readonly'))

    def setSlave(self, slaveField, masterValue):
        '''Sets p_slaveField as slave of this field. Normally, master/slave
           relationships are defined when a slave field is defined. At this time
           you specify parameters "master" and "masterValue" for this field and
           that's all. This method is used to add a master/slave relationship
           that was not initially foreseen.'''
        slaveField.master = self
        slaveField.masterValue = utils.initMasterValue(masterValue)
        if slaveField not in self.slaves:
            self.slaves.append(slaveField)
        # Master's init method may not have been called yet
        slaveField.masterName = getattr(self, 'name', None)

    def getMasterData(self):
        '''Gets the master of this field (and masterValue) or, recursively, of
           containing groups when relevant.'''
        if self.master: return self.master, self.masterValue
        group = self.getGroup('edit')
        if group: return group.getMasterData()

    def getMasterTag(self, layout):
        '''Generally, for a field, the name of the tag serving as master for
           driving slave fields is the name of the field itself. But sometimes
           it can be different (see Field sub-classes).'''
        return self.name

    def getMasterCss(self, master, layout):
        '''Get the CSS class(es) to set on a tag corresponding to a field having
           this p_master.'''
        r = f'slave*{master.getMasterTag(layout)}*'
        if not callable(self.masterValue):
            r += '*'.join(self.masterValue)
        else:
            r += '+'
        return r

    def getTagCss(self, tagCss, layout):
        '''Gets the CSS class(es) that must apply to XHTML tag representing this
           field in the ui. p_tagCss may already give some base class(es).'''
        r = []
        isInner = self.isInner()
        if tagCss and not isInner:
            # For an inner tag, it has no sense to "inherit" from p_tagCss
            r.append(tagCss)
        # Add a special class when this field is the slave of another field
        master = self.master
        if master:
            if isinstance(master, Field):
                # A single master
                css = self.getMasterCss(master, layout)
            else: # Several masters
                css = ' '.join([self.getMasterCss(m, layout) for m in master])
            r.insert(0, css)
        # Define a base CSS class when the field is a sub-field in a List
        if isInner: r.append('no')
        return ' '.join(r)

    def getOnChange(self, o, layout, className=None):
        '''When this field is a master, this method computes the call to the
           Javascript function that will be called when its value changes (in
           order to update slaves).'''
        if not self.slaves: return ''
        url = o.url
        # When the field is on a search screen, we need p_className
        if className:
            name = f"'{className}'"
            url = f'{url}/@{className}'
        else:
            name = 'null'
        return f"updateSlaves(this,null,'{url}','{layout}',{name},true)"

    def isEmptyValue(self, o, value):
        '''Returns True if the p_value must be considered as an empty value'''
        return value in self.nullValues

    def isCompleteValue(self, o, value):
        '''Returns True if the p_value must be considered as "complete". While,
           in most cases, a "complete" value simply means a "non empty" value
           (see m_isEmptyValue above), in some special cases it is more subtle.
           For example, a multilingual string value is not empty as soon as a
           value is given for some language but will not be considered as
           complete while a value is missing for some language. Another example:
           a Date with the "hour" part required will not be considered as empty
           if the "day, month, year" part is present but will not be considered
           as complete without the "hour, minute" part.'''
        return not self.isEmptyValue(o, value)

    def validateValue(self, o, value):
        '''This method may be overridden by child classes and will be called at
           the right moment by m_validate defined below for triggering
           type-specific validation. p_value is never empty.'''
        return

    def securityCheck(self, o, value):
        '''This method performs some security checks on the p_value that
           represents user input.'''
        if not isinstance(value, str): return
        # Search Javascript code in the value (prevent XSS attacks)
        if '<script' in value:
            o.log(XSS_DETECTED, type='error')
            raise Exception(XSS_WARNING)

    def validate(self, o, value):
        '''Checks that p_value, coming from the request (p_o is being created or
           edited) and formatted through a call to m_getRequestValue defined
           above, is valid according to this type definition. If it is the case,
           None is returned. Else, a translated error message is returned.'''
        # If the value is required, check that a (complete) value is present
        if not self.isCompleteValue(o, value):
            if self.required and self.isClientVisible(o):
                # If the field is required, but not visible according to
                # master/slave relationships, we consider it not to be required.
                return o.translate('field_required')
            else:
                return
        # Perform security checks on p_value
        self.securityCheck(o, value)
        # Triggers the sub-class-specific validation for this value
        message = self.validateValue(o, value)
        if message: return message
        # Evaluate the custom validator if one has been specified
        return Validator.evaluateCustom(self, o, value)

    def store(self, o, value):
        '''Stores, on p_o, this p_value, that must comply to p_self's type
           definition. When p_value is None, (a) if p_delete is False, the
           stored value is left untouched; (b) if p_delete is True, the stored
           value is deleted.'''
        # When used by Appy itself, p_value is, in general, produced by
        # m_getStorableValue.
        persist = self.persist
        if not persist: return
        elif callable(persist):
            # Do not store the value but let this method do whatever she wants
            # with it.
            self.persist(o, value)
            return
        # Store p_value ...
        if value is not None:
            # Store the value on p_o. Perform a last type check if
            # p_self.[storableTypes|pythonType] is defined.
            type = self.storableTypes or self.pythonType
            if type is not None and not isinstance(value, type):
                typeS = type.__name__
                wrongS = value.__class__.__name__
                raise Exception(TYPE_KO % (self.name, wrongS, typeS))
            o.values[self.name] = value
        # ... or delete it
        elif self.name in o.values:
            del o.values[self.name]

    def storeValueFromAjax(self, o, value, currentValues):
        '''Called by m_storeValueFromAjax to save p_value on p_o'''
        self.store(o, self.getStorableValue(o, value))
        # Overridden methods may return some custom message part
        return ''

    traverse['storeFromAjax'] = 'perm:write'
    def storeFromAjax(self, o):
        '''Stores the new field value from an Ajax request, or do nothing if
           the action was canceled.'''
        # Be the operation a "save" or "cancel", remove the lock on the page
        # (if is was set).
        o.Lock.remove(o, field=self)
        # Do nothing more when canceling the ajax-save
        req = o.req
        if req.cancel == 'True': return
        # Get the new value
        reqValue = self.getRequestValue(o, requestName='fieldContent')
        # Are we working on a normal or inner field ?
        if not self.isInner():
            # A normal field. Remember its previous value if it is historized.
            isHistorized = self.getAttribute(o, 'historized')
            currentValues = o.history.getCurrentValues(o, self) \
                            if isHistorized else None
            # Validate the value
            if self.validate(o, reqValue):
                # Be minimalist: do nothing and return the previous value
                return
            # Store the new value on p_o
            part = self.storeValueFromAjax(o, reqValue, currentValues)
            # Update the object history when relevant
            if isHistorized and currentValues:
                o.history.historize(currentValues)
        else:
            # An inner field. No historization (yet) for it.
            part = ''
            # Retrieve the outer, inner fields and row number
            outer, inner, i = o.traversal.parts[-2].split('*')
            i = int(i)
            outer = o.getField(outer)
            # Update the value. Clone the row to ensure the ZODB will detect the
            # object change. Indeed, rows are instances of not-persistent class
            # appy.Object.
            value = outer.getValue(o)
            row = value[i]
            setattr(row, inner, self.getStorableValue(o, reqValue))
            value[i] = row.clone()
            # Store the complete value again on p_o
            o.values[outer.name] = value
        # Update p_o's last modification date and modifier
        o.history.noteUpdate()
        o.reindex()
        o.log(AJAX_EDITED % (self.name, part, o.id))

    def callMethod(self, o, method, cache=True):
        '''This method is used to call a p_method on p_o. p_method is part of
           this type definition (ie a default method, the method of a Computed
           field, a method used for showing or not a field...). Normally, those
           methods are called without any arg. But one may need, within the
           method, to access the related field. This method tries to call
           p_method with no arg *or* with the field arg.'''
        try:
            return o.H().methods.call(o, method, cache=cache)
        except TypeError as te:
            # Try a version of the method that would accept p_self as an
            # additional parameter. In this case, we do not try to cache the
            # value (we do not call utils.callMethod), because the value may be
            # different depending on the parameter.
            tb = utils.Traceback.get()
            try:
                return method(o, self)
            except Exception as e:
                o.log(METH_ERROR % (method.__name__, tb), type='error')
                # Raise the initial error
                raise te

    def getAttribute(self, o, name, cache=True):
        '''Gets the value of attribute p_name on p_self, which can be a simple
           value or the result of a method call on p_o.'''
        r = getattr(self, name)
        return self.callMethod(o, r, cache=cache) if callable(r) else r

    def getDisabled(self, o):
        '''For sub-classes that propose attribute "disabled", this method allows
           to answer the question: must p_self be disabled on the "edit"
           layout ?'''
        return self.getAttribute(o, 'disabled', cache=False)

    def getGroup(self, layout):
        '''Gets the group into wich this field is on p_layout'''
        # There may be...
        # (a) ... no group at all
        group = self.group
        if group is None: return
        # (b) ... the same group for all layouts
        elif isinstance(group, Group): return group
        # (c) a specific group for this p_layout
        elif layout in group: return group[layout]

    def getGroups(self):
        '''Returns groups as a list'''
        r = []
        if not self.group: return r
        if isinstance(self.group, Group):
            r.append(self.group)
        else: # A dict
            for group in self.group.values():
                if group and (group not in r):
                    r.append(group)
        return r

    def renderLabel(self, layout):
        '''Indicates if the existing label (if hasLabel is True) must be
           rendered by pxLabel. For example, if field is an action, the
           label will be rendered within the button, not by pxLabel.'''
        if not self.hasLabel: return
        # Label is always shown in search forms
        if layout == 'search': return True
        # If the field is within a "tabs" group, the label will already be
        # rendered in the corresponding tab. If the field is in a "grid" group,
        # the label is already rendered in a separate column.
        group = self.getGroup(layout)
        if group and group.style in ('tabs', 'grid'): return
        return True

    def getSelectSize(self, isSearch, isMultiple):
        '''If this field must be rendered as a HTML "select" field, get the
           value of its "size" attribute. p_isSearch is True if the field is
           being rendered on a search screen, while p_isMultiple is True if
           several values must be selected.'''
        if not isMultiple: return 1
        prefix = 's' if isSearch else ''
        height = getattr(self, f'{prefix}height')
        if isinstance(height, int): return height
        # "height" can be defined as a string. In this case it is used to define
        # height via a attribute "style", not "size".
        return ''

    def getInputSize(self, sizeAttr=True):
        '''Returns the width of the input field, either in the "size" attribute,
           (p_sizeAttr is True) or as a CSS "width" attribute (p_sizeAttr is
           False).'''
        # If the field width is expressed as a percentage, the width must be
        # specified via the CSS "width" attribute. In all other cases, it is
        # specified via the "size" tag attribute.
        width = self.width
        isPercentage = width and isinstance(width, str) and width.endswith('%')
        if sizeAttr:
            # Tag attribute "size"
            return '' if isPercentage else width
        else:
            # CSS attribute "width"
            return f'width:{width}' if isPercentage else ''

    def getSelectStyle(self, isSearch, isMultiple):
        '''If this field must be rendered as a HTML "select" field, get the
           value of its "style" attribute. p_isSearch is True if the field is
           being rendered on a search screen, while p_isMultiple is True if
           several values must be selected.'''
        prefix = 's' if isSearch else ''
        # Compute CSS attributes
        r = []
        # Height
        height = getattr(self, f'{prefix}height')
        if isMultiple and isinstance(height, str):
            r.append(f'height:{height}')
            # If height is an integer value, it will be dumped in attribute
            # "size", not in CSS attribute "height".
        # Width
        width = getattr(self, f'{prefix}width')
        if isinstance(width, str):
            r.append(f'width:{width}')
            # If width is an integer value, it represents a number of chars
            # (usable for truncating the shown values), not a width for the CSS
            # attribute.
        return ';'.join(r)

    def getWidgetStyle(self, prefix=''):
        '''If this field must be rendered as any widget not being a select
           widget (managed by m_getSelectStyle hereabove), and if its width
           and/or height are specified as strings, restrict the visible part of
           the widget to these values, with a scrollbar when appropriate.'''
        # Prefix can be "s" (*s*earch) or "f" (*f*ilter)
        r = []
        width = getattr(self, f'{prefix}width')
        if isinstance(width, str):
            r.append(f'width:{width};overflow-x:auto')
        height = getattr(self, f'{prefix}height')
        if isinstance(height, str):
            # Use "max-height" and not "height", because, if the widget content
            # is reduced, forcing the height will be ugly.
            r.append(f'max-height:{height};overflow-y:auto')
        return ';'.join(r)

    def getWidthInChars(self, isSearch):
        '''If attribute "width" contains an integer value, it contains the
           number of chars shown in this field (a kind of "logical" width). If
           it contains a string, we must convert the value expressed in px
           (or in another CSS-compliant unit), to a number of chars.'''
        prefix = 's' if isSearch else ''
        width = getattr(self, f'{prefix}width')
        if isinstance(width, int): return width
        r = 30
        if isinstance(width, str):
            if width.endswith('px'):
                r = int(int(width[:-2]) / 5)
            elif width.endswith('em'):
                # "float" is hidden by module appy.model.fields.float
                r = int(__builtins__['float'](width[:-2]) * 2)
        return r # Other units are currently not supported

    def getListHeader(self, c):
        '''When p_self is used as inner-field, within a table-like rendered
           container field, this method returns the content of the header row
           corresponding to this inner field.'''
        return c._('label', field=self)

    def getValueIfEmpty(self, o):
        '''Get the value to display if the field is empty'''
        # This is only available for fields defining non-standard attrbute
        # "valueIfEmpty".
        r = self.valueIfEmpty
        if callable(r): r = r(o)
        return r

    @classmethod
    def asXhtml(class_, o, fields=None, css='small', ignoreEmpty=True,
                custom=None, thWidth='40%'):
        '''Renders a HTML table containing field values for this o_o(bject)'''
        # If p_fields is not None, it contain names of fields that will be part
        # of the result. If None, all p_o(bject) fields will be part of the
        # result.
        #
        # p_css is the name of the CSS class that will be applied to the main
        # "table" tag.
        #
        # If p_ignoreEmpty is True, any field whose value is empty on p_o will
        # be ignored.
        #
        # If p_custom is passed, it is a dict of functions allowing to produce a
        # custom rendering for some fields. If you want to produce a custom
        # rendering for field named "f1", pass, in p_custom, a dict having a
        # entry whose key is "f1" and whose value is a function. This latter
        # must accept, as args, (1) the concerned object and (2) the Field
        # object whose name is "f1", and must return a string containing a
        # complete "tr" tag and sub-tags (as a string) that must represent the
        # field label and its value, in any form. Note that a standard entry in
        # the table has 2 cells: the first one (a "th") contains field labels
        # and the second one (a "td") contains field values.
        #
        # Width for the 1st column is determined by p_thWidth.
        rows = []
        fields = fields or o.class_.fields.values()
        first = True
        for field in fields:
            # p_field can be a Field object or the name of a field (as a string)
            field = o.getField(field) if isinstance(field, str) else field
            name = field.name
            # Ignore empty values
            if ignoreEmpty and o.isEmpty(name): continue
            # Get the row content
            thStyle = f' style="width:{thWidth}"' if first else ''
            if custom and name in custom:
                row = custom[name](o, field)
            else:
                # Standard content: dump 2 cells: one containing the field
                # label, the second containing the field value.
                text = o.translate('label', field=field)
                value = o.getShownValue(name)
                if isinstance(value, __builtins__['list']):
                    value = ', '.join(value)
                row = f'<tr><th{thStyle}>{text}</th><td>{value}</td></tr>'
                first = False
            rows.append(row)
        rows = '\n'.join(rows)
        return f'<table class="{css}">{rows}</table>'
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
