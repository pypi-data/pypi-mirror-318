'''This module defines classes allowing to store an object's history'''

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
# Most of an object's history is related to its workflow. This is why this
# module lies within appy.model.workflow. That being said, object history also
# stores not-workflow-based events like data changes.

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import persistent
from DateTime import DateTime
from persistent.list import PersistentList
from persistent.mapping import PersistentMapping

from appy.px import Px
from appy.model.batch import Batch
from appy.xml.escape import Escape
from appy.utils import string as sutils
from appy.xml.cleaner import StringCleaner

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class EventIterator:
    '''Iterator for history events'''

    def __init__(self, history, eventType=None, condition=None,
                 context=None, chronological=False, i=None):
        # The history containing the events to walk
        self.history = history
        # The types of events to walk. None means that all types are walked.
        # When specified, p_eventType must be the name of a concrete Event
        # class, or a list/tuple of such class names.
        self.eventType = (eventType,) if isinstance(eventType, str) \
                                      else eventType
        # An additional condition, as a Python expression (getting "event" in
        # its context) that will dismiss the event if evaluated to False.
        self.condition = condition
        # A context that will be given to the condition
        self.context = context
        # If chronological is True, events are walked in chronological order.
        # Else, they are walked in their standard, anti-chronological order.
        self.chronological = chronological
        # The index of the currently walked event
        if i is None:
            self.i = len(history) - 1 if chronological else 0
        else:
            self.i = i

    def increment(self):
        '''Increment p_self.i, or decrement it if we walk events in
           chronological order.'''
        if self.chronological:
            self.i -= 1
        else:
            self.i += 1

    def typeMatches(self, event):
        '''Has p_event the correct type according to p_self.eventType ?'''
        # If no event type is defined, p_event matches
        if self.eventType is None: return True
        return event.__class__.__name__ in self.eventType

    def conditionMatches(self, event):
        '''Does p_event matches p_self.condition ?'''
        # If no condition is defined, p_event matches
        if self.condition is None: return True
        # Update the evaluation context when appropriate
        if self.context:
            locals().update(self.context)
        return eval(self.condition)

    def __iter__(self): return self
    def __next__(self):
        '''Return the next matching event'''
        # Stop iterating if p_self.i is negative
        if self.i < 0: raise StopIteration
        try:
            event = self.history[self.i]
        except IndexError:
            # There are no more events, we have walked them all
            raise StopIteration
        # Does this event match ?
        if self.typeMatches(event) and self.conditionMatches(event):
            # Yes
            self.increment()
            return event
        else:
            # Try to return the next element
            self.increment()
            return self.__next__()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Event(persistent.Persistent):
    '''An object's history is made of events'''

    # A format for representing dates at various (non ui) places
    dateFormat = '%Y/%m/%d %H:%M'

    # Some events can be deleted from the ui, but most aren't
    deletable = False

    # The PX displaying details about an event (basically the event's comment)
    pxDetail = Px('''
     <x var="eventId=event.getId();
             editable=o.class_.mayEditEventComment(o,event, user, isManager)">
      <img if="editable" class="clickable iconS" style="float:right"
           src=":svg('edit')" title=":_('object_edit')"
           onclick=":'onHistoryEvent(%s,%s,%s)' %
                      (q('modify'), q(eventId), q(eventId))"/>
      <span id=":eventId">::event.getComment(escaped=editable)</span>
     </x>''')

    def __init__(self, login, state, date, comment=None):
        # The login of the user that has triggered the event
        self.login = login
        # The name of the state into which the object is after the event
        # occurred. It means that an object's current state is stored in this
        # attribute, on the most recent event in its history.
        self.state = state
        # When did this event occur ?
        self.date = date
        # A textual optional comment for the event
        self.comment = StringCleaner.clean(comment)

    def clone(self):
        '''Create an return a clone from myself'''
        params = self.__dict__.copy()
        login = params.pop('login')
        state = params.pop('state')
        date = params.pop('date')
        return self.__class__(login, state, date, **params)

    def completeComment(self, comment, sep='<br/><br/>'):
        '''Appends p_comment to the existing p_self.comment'''
        if not self.comment:
            self.comment = comment
        else:
            self.comment = f'{self.comment}{sep}{comment}'

    def getTypeName(self, short=False):
        '''Return the class name, possibly completed with sub-class-specific
           information.'''
        # The p_short variant is used for searching events, in methods like
        # History.getLast.
        r = self.__class__.__name__
        return r.lower() if short else r

    def getLabel(self, o):
        '''Returns the i18n label for this event'''
        # To be overridden

    def getComment(self, empty='-', escaped=True):
        '''Returns p_self.comment, ready to be included in a chunk of XHTML'''
        r = self.comment or empty
        return Escape.xhtml(r) if escaped else r

    def getId(self):
        '''Return an ID for this history p_event, based on its date '''
        return str(self.date.millis())

    def getUser(self, o, title=True, expression=None):
        '''Returns the complete name of the user with this p_self.login'''
        login = self.login
        if not login:
            return '?' if title else None
        user = o.search1('User', login=login)
        if not user:
            return '?' if title else None
        # Return the found user or its p_title
        if title:
            r = eval(expression) if expression else (user.getTitle() or login)
        else:
            r = user
        return r

    def __repr__(self):
        '''p_self's string representation'''
        date = self.date.strftime(Event.dateFormat)
        return f'‹{self.getTypeName()} by {self.login} on {date}, ' \
               f'state {self.state}›'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Trigger(Event):
    '''This event represents a transition being triggered'''

    def __init__(self, login, state, date, **params):
        # Extract the name of the transition from p_params
        self.transition = params.pop('transition')
        super().__init__(login, state, date, **params)

    def getTypeName(self, short=False):
        '''Return the class name and the transition name'''
        r = self.transition
        return r if short else f'Trigger {r}'

    def getLabel(self, o):
        '''Returns the label for the corresponding transition'''
        if self.transition == '_init_':
            r = 'Base_creator'
        else:
            transition = o.getWorkflow().transitions.get(self.transition)
            r = transition.labelId if transition else self.transition
        return r

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Action(Event):
    '''This event represents an action (field) being performed'''

    def __init__(self, login, state, date, **params):
        # Extract the name of the action from p_params
        self.action = params.pop('action')
        super().__init__(login, state, date, **params)

    def getTypeName(self, short=False):
        '''Return the class name and the transition name.'''
        r = self.action
        return r if short else f'Action {r}'

    def getLabel(self, o):
        '''Returns the label for the corresponding action'''
        return o.getField(self.action).labelId

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Change(Event):
    '''This event represents a data change'''

    # Due to the mess sometimes occurring within XHTML diffs, it may be
    # preferable to forget about the change by allowing the user to delete the
    # corresponding event.
    deletable = True

    # Types of entries in a diff
    diffEntries = ('insert', 'delete')

    # Showing details about a change = displaying the previous values of the
    # fields whose values were modified in this change.
    pxDetail = Px('''
     <table class="changes" width="100%" if="event.changes">
      <tr>
       <th align=":dleft">:_('modified_field')</th>
       <th align=":dleft">:_('previous_value')</th>
      </tr>
      <tr for="name, value in event.changes.items()" valign="top"
          var2="fname=name if isinstance(name, str) else name[0];
                lg=None if isinstance(name, str) else name[1];
                field=o.getField(fname)">
       <td><x>::_(field.labelId) if field else fname</x>
           <x if="lg">:f' ({ui.Language.getName(lg)})'</x></td>
       <td>
        <x>::field.getHistoryValue(o, value, history.data.index(event), lg) \
             if field else value</x>
       </td>
      </tr>
     </table>
     <!-- A comment may coexist with the change in itself -->
     <div var="comment=event.getComment(empty='', escaped=False)"
          if="comment">::comment</div>''')

    def __init__(self, login, state, date, **params):
        '''Extract changed fields from p_params'''
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # Attribute "changes" stores, in a dict, the previous values of fields
        # whose values have changed. If the dict's key is of type...
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # str   | it corresponds to the name of the field; 
        # tuple | it corresponds to a tuple (s_name, s_language) and stores the
        #       | part of a multilingual field corresponding to s_language.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.changes = PersistentMapping(params.pop('changes'))
        # Call the base constructor
        super().__init__(login, state, date, **params)

    def hasField(self, name, language=None):
        '''Is there, within p_self's changes, a change related to a field whose
           name is p_name ?'''
        if name in self.changes: return True
        # Search for a key of the form (name, language)
        for key in self.changes.keys():
            if isinstance(key, tuple) and key[0] == name and \
               (not language or language == key[1]):
                return True

    def getValue(self, name, language=None):
        '''Gets the value as stored on this change, for field name p_name, or
           its p_language part.'''
        key = (name, language) if language else name
        return self.changes.get(key)

    def getLabel(self, o):
        '''Returns the i18n label for a data change'''
        return 'event_Change'

    def getDiffTexts(self, o):
        '''Returns a tuple (insertText, deleteText) containing texts to show on,
           respectively, inserted and deleted chunks of text in a XHTML diff.'''
        user = o.search1('User', login=self.login)
        mapping = {'userName': user.getTitle() if user else self.login}
        r = []
        tool = o.tool
        for type in self.diffEntries:
            msg = o.translate(f'history_{type}', mapping=mapping)
            date = tool.Date.format(tool, self.date, withHour=True)
            r.append(f'{date}: {msg}')
        return r

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Custom(Event):
    '''Represents a custom event, for which the label is chosen by the
       developer.'''

    def __init__(self, login, state, date, **params):
        # Extract the label to use to name the event
        self.label = params.pop('label')
        super().__init__(login, state, date, **params)

    def getLabel(self, o):
        '''Returns the i18n label for a data change'''
        return self.label

    def getTypeName(self, short=False):
        '''Return the class name, completed with p_self.label'''
        return self.label if short else f'Custom::{self.label}'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Link(Event):
    '''Represents a link, via a Ref field, between 2 objects. The event is
       stored in the source object's history.'''

    # Although it may seem similar to a Change, it does not inherit from it.
    # Indeed, the complete list of previously linked objects is not stored:
    # instead, the title of the newly linked object is set as comment in this
    # Link event.

    # The name of specific attribute added by this class. It is not "hardcoded"
    # in the constructor, because a sub-class may define another one. For class
    # Link, boolean "addition" tells if we have linked an existing object
    # (addition==False) or a newly created one (addition==True).
    attribute = 'addition'

    def __init__(self, login, state, date, **params):
        # We may have linked an existing object or a newly created one
        attribute = self.attribute
        setattr(self, attribute, params.pop(attribute))
        # The name of the Ref field on which the operation was performed
        self.field = params.pop('field')
        # Call the base constructor
        super().__init__(login, state, date, **params)

    def getTypeName(self, short=False):
        '''Return the class name + type-specific info'''
        r = self.attribute if getattr(self, self.attribute) else ''
        field = getattr(self, 'field', None) # May be absent from old DBs
        cname = self.__class__.__name__
        if short:
            r = f'{cname.lower()}{r}'
        else:
            suffix = f' ({field})' if field else ''
            r = f'{cname}{r.capitalize()}{suffix}'
        return r

    def getLabel(self, o):
        '''Returns the i18n label for a link'''
        type = 'Addition' if self.addition else 'Link'
        return f'event_{type}'

class Unlink(Link):
    '''Represents an object being unlinked from another one via a Ref field'''

    # The name of specific attribute added by this class. This boolean indicates
    # if we have simply unlinked an object (deletion==False) or if it has been
    # completely deleted (deletion==True).
    attribute = 'deletion'

    def getLabel(self, o):
        '''Returns the i18n label for an unlink'''
        type = 'Deletion' if self.deletion else 'Unlink'
        return f'event_{type}'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class History(PersistentList):
    '''Object history is implemented as a list, sorted in antichronological
       order, of history events.'''

    traverse = {}

    # This PX displays history events
    events = Px('''
     <div var="history=o.history;
               batchSize=historyMaxPerPage|req.maxPerPage;
               batch=history.getBatch(o, batchSize);
               isManager=user.hasRole('Manager')"
          if="batch.length" id=":batch.hook">
      <script>:history.getAjaxData(batch)</script>

      <!-- Navigate between history pages -->
      <div align=":dright" if="batch.showNav()">:batch.pxNavigate</div>

      <!-- History -->
      <table width="100%" class="history">
       <tr>
        <th align=":dleft">:_('object_action')</th>
        <th align=":dleft">:_('object_author')</th>
        <th align=":dleft">:_('action_date')</th>
        <th align=":dleft">:_('action_comment')</th>
       </tr>
       <tr for="event in batch.objects" valign="top">
        <td><x>:_(event.getLabel(o))</x>
         <img if="isManager and event.deletable" class="clickable iconS"
              src=":svg('deleteS')"
              onclick=":'onHistoryEvent(%s,%s)' % 
                        (q('delete'), q(event.getId()))"/></td>
        <td>:event.getUser(o)</td>
        <td>:tool.Date.format(tool, event.date, withHour=True)</td>
        <td>:event.pxDetail</td>
       </tr>
      </table>
     </div>''',

     js='''
      function onHistoryEvent(action, eventId, commentId) {
        var showComment = action == 'modify',
            comment = null,
            params="'action':'history*"+action+"','eventId':'"+eventId+"'";
        // Manage comment
        if (commentId) {
          comment = html2text(document.getElementById(commentId).innerHTML);
          params = params + ",'comment':encodeURIComponent(comment)"
        }
        askConfirm('script', "askAjax('history',null,{" + params + "})",
                   action_confirm, showComment, null, null, comment);
      }''')

    view = Px('''
     <div if="not o.isTemp() and layout !='xml'"
       var2="history=o.history; hasHistory=not history.isEmpty();
             createComment=history[-1].comment">
      <table width="100%" class="header" cellpadding="0" cellspacing="0">
       <tr>
        <td colspan="2" class="by">
         <!-- Creator and last modification date -->
         <x>:_('Base_creator')</x> 
          <x>:user.getTitleFromLogin(o.creator)</x> 

         <!-- Creation and last modification dates -->
         <x>:_('date_on')</x>
         <x var="created=o.created; modified=o.modified">
          <x>:tool.Date.format(tool, created, withHour=True)</x>
          <x if="modified != created">&mdash;
           <x>:_('Base_modifier')</x> <x>:o.getModifier()</x> 
           <x>:_('date_on')</x> 
           <x>:tool.Date.format(tool, modified, withHour=True)</x>
          </x>
         </x>

         <!-- State -->
         <x> &mdash; <x>:_('Base_state')</x> : 
            <b>:_(o.getLabel(o.state, field=False))</b></x>

         <!-- Initial comment -->
         <div if="createComment" class="topSpace">::createComment</div>
        </td>
       </tr>

       <!-- History entries -->
       <tr if="hasHistory"><td colspan="2">:history.events</td></tr>
      </table>
     </div>''',

     css='''
      .header { margin:|histMargin|; background-color:#f3f3f7;
                border:3px solid white }
      .by { padding:7px }
      .history>tbody>tr>td { padding:8px }
      .history>tbody>tr:nth-child(odd) { background-color:|oddColor| }
      .history>tbody>tr:nth-child(even) { background-color:|evenColor| }
      .history>tbody>tr>th { font-style:italic; text-align:left;
                             padding:10px 5px; background-color:white }
      .changes { margin: 4px 0 }
      .changes>tbody>tr>td, .changes>tbody>tr>th { border:1px solid #e0e0e0;
                                                   padding:5px }
     ''')

    def __init__(self, o):
        super().__init__()
        # A reference to the object for which p_self is the history
        self.o = o
        # The last time the object has been modified
        self.modified = None
        # The login og the last user having modified the object
        self.modifier = None

    def noteUpdate(self):
        '''p_self.o has just been updated: note it'''
        self.modified = DateTime()
        self.modifier = self.o.user.login

    def add(self, type, state=None, **params):
        ''''Adds a new event of p_type (=the name of an Event sub-class) into
            the history.'''
        # Get the login of the user performing the action
        if 'login' in params:
            login = params.pop('login')
        else:
            # If we are called during the authentication process, the guard and
            # current user may not exist yet.
            try:
                login = self.o.guard.userLogin
            except AttributeError as err:
                login = 'system'
        # Get the date and time of the action
        if 'date' in params:
            date = params.pop('date')
        else:
            date = DateTime()
        # For a trigger event, p_state is the new object state after the
        # transition has been triggered. p_state is a name (string) and not a
        # State instance. The name of the triggering transition must be in
        # p_params, at key "transition".
        # For a change event, no state is given, because there is no state
        # change, but we will copy, on the change event, the state from the
        # previous event. That way, the last event in the history will always
        # store the object's current state.
        state = state or self[0].state
        # Create the event
        event = eval(type)(login, state, date, **params)
        # Insert it at the first place within the anti-chronological list
        self.insert(0, event)
        # Initialise self.modifie[d|r] if still None
        if self.modified is None:
            self.modified = event.date
            self.modifier = login
        return event

    def iter(self, **kwargs):
        '''Returns an iterator for browsing p_self's events'''
        return EventIterator(self, **kwargs)

    def isEmpty(self, name=None):
        '''Is this history empty ? If p_name is not None, the question becomes:
           has p_self.o an history for field named p_name ?'''
        # An history containing a single entry is considered empty: this is the
        # special _init_ virtual transition representing the object creation.
        if len(self) == 1: return True
        # At this point, the complete history can be considered not empty
        if name is None: return
        # Check if history is available for field named p_name
        empty = True
        for event in self.iter(eventType='Change', \
                               condition=f"event.hasField('{name}')"):
            # If we are here, at least one change concerns the field
            empty = False
            break
        return empty

    def getCurrentValues(self, o, fields):
        '''Called before updating p_o, this method remembers, for every
           historized field from p_fields, its current value.'''
        r = {} # ~{s_fieldName: currentValue}~
        # p_fields can be a list of fields or a single field
        fields = fields if isinstance(fields, list) else [fields]
        # Browse fields
        for field in fields:
            if not field.getAttribute(o, 'historized'): continue
            r[field.name] = field.getComparableValue(o)
        return r

    def getNewer(self, field, value, i, language=None):
        '''Find the newer version of this p_field p_value in p_self, starting at
           index p_i, or, if not found, take the value as currently stored on
           p_self.o.'''
        # p_value was found in this history, at index p_i+1
        found = False
        name = field.name
        for event in self.iter(eventType='Change', chronological=True, i=i):
            if event.hasField(name, language=language):
                # A newer version exists in this history
                newer = event.getValue(name, language)
                found = True
                break
        # If no newer version was found in p_o's history, take the value being
        # currently stored on p_o for p_self.
        if not found:
            newer = getattr(self.o, name, None)
        return newer

    def historize(self, previous, comment=None):
        '''Records, in self.o's history, potential changes on historized fields.
           p_previous contains the values, before an update, of the historized
           fields, while p_self.o already contains the (potentially) modified
           values.'''
        o = self.o
        # Remove, from p_previous, any value that was not changed
        for name in list(previous.keys()):
            prev = previous[name]
            field = o.getField(name)
            curr = field.getValue(o, single=False)
            if prev == curr or (prev is None and curr == '') or \
               (prev == '' and curr is None):
                del(previous[name])
                continue
            # The previous value may need to be formatted
            field.updateHistoryValue(o, previous)
        # Add the entry in the history (if not empty)
        if previous:
            self.add('Change', changes=previous, comment=comment)

    def getEvents(self, type, notBefore=None):
        '''Gets a subset of history events of some p_type. If specified, p_type
           must be the name of a concrete Event class or a list/tuple of such
           names.'''
        cond = 'not notBefore or (event.date >= notBefore)'
        return [event for event in self.iter(eventType=type, condition=cond, \
                                             context={'notBefore':notBefore})]

    def getEvent(self, id):
        '''Get the event with this p_id or None if not found'''
        for event in self:
            if event.getId() == id:
                return event

    def getLast(self, name, notBefore=None, history=None, eventType='Trigger'):
        '''Return the last event that occurred in p_self (or in p_history if
           passed), having this p_name.'''

        # See event methods m_getTypeName(short=True) to know what "name" refers
        # to. For a Trigger event, it is the name of the fired transition.
        #
        # p_name can be a list: in that case, it returns the most recent
        # occurrence of the corresponding events, being anti-chronologically
        # walked. If p_notBefore is given (an event name, too), it corresponds
        # to a kind of start event for the search: we will not search in the
        # history preceding the last occurrence of this event. Note that
        # p_notBefore can also hold a list.
        #
        # If p_eventType is passed, only events of this type will be taken into
        # account. If it is none, all history events, of any type, are walked.
        #
        # If p_history is passed, it is used instead of p_self.o.history.
        #
        # Walk events, in anti-chronological order
        for event in (history or self).iter(eventType=eventType):
            ename = event.getTypeName(short=True)
            if notBefore:
                if isinstance(notBefore, str):
                    condition = ename == notBefore
                else:
                    condition = ename in notBefore
                if condition: return
            if isinstance(name, str):
                condition = ename == name
            else:
                condition = ename in name
            if condition: return event

    def getEventLogins(self, transitions):
        '''Returns the list of user logins responsible for having triggered, for
           the last time, p_transitions on p_self.'''
        r = set()
        for transition in transitions:
            # Get the last event with this transition
            event = self.getLast(transition)
            if event:
                r.add(event.login)
        return r

    def setEvents(self, other):
        '''Replace p_self's events with clones from p_other's events'''
        # Empty p_self's history first
        while len(self): del(self[0])
        # Create clones from p_other's events and insert them into p_self
        for event in other:
            self.append(event.clone())

    def getBatch(self, o, size):
        '''Returns the Batch instance allowing to navigate within p_o's
           history.'''
        # Compute the batch start and size
        size = int(size) if isinstance(size, str) else (size or 30)
        start = int(o.req.start or 0)
        return Batch(objects=self.data[start:start + size], total=len(self),
                     size=size, start=start, hook='history')

    def getAjaxData(self, batch):
        '''Gets data allowing to ajax-ask paginated history data'''
        params = {'start': batch.start, 'maxPerPage': batch.size}
        # Convert params into a JS dict
        params = sutils.getStringFrom(params)
        hook = batch.hook
        return f"new AjaxData('{self.o.url}/history/events','GET',{params}," \
               f"'{hook}')"

    def replaceLogin(self, old, new):
        '''Replace, in all events, login p_old with login p_new. Returns the
           number of replacements done.'''
        r = 0
        for event in self:
            if event.login == old:
                event.login = new
                r += 1
        return r

    # The list of event types being, by default, excluded from the XHTML
    # version of the history, as produced by m_asXhtml below.
    xhtmlDefaultExclude = ('change', '_init_')

    def asXhtml(self, exclude=xhtmlDefaultExclude, userExpression=None,
                noLabelFor=('comment',), escapeComments=True,
                chronological=False, css='sahist'):
        '''Produce a XHTML version of this history, in the form of a discussion
           thread, suitable to be injected as various places: in methods
           getSubTitle, in PODs, etc.'''

        # p_exclude lists the event types that will not be part of the result.

        # If p_userExpression is None, user will be shown via standard method
        # User::getTitle. Else, user will be shown according to this expression,
        # that will be evaluated with name "user" in its context.

        # p_noLabelFor gives a tuple of event types for which no label will be
        # rendered. Typically, for a transition named "comment", it is useless
        # to show its translated name.

        # Browse history events
        r = []
        o = self.o
        esc = Escape.xhtml
        tool = o.tool
        fmt = tool.Date.format
        for event in self.iter(chronological=chronological):
            # Ignore inappropriate events
            type = event.getTypeName(short=True)
            if exclude and type in exclude: continue
            # Define a prefix, being the name of the event
            if noLabelFor and type in noLabelFor:
                prefix = ''
            else:
                suffix = esc(o.translate(event.getLabel(o)))
                prefix = f' – <b>{suffix}</b> '
            # Get the comment when present
            comment = event.comment or ''
            if comment and escapeComments: comment = esc(comment)
            # Create the message line
            dateText = fmt(tool, event.date, withHour=True)
            userText = esc(event.getUser(o, expression=userExpression))
            msg = f'<i>{dateText}</i>{prefix} – {userText}'
            if comment:
                msg = f'{msg} – « {comment} »'
            r.append(msg)
        css = f' class="{css}"' if css else ''
        return f'<div{css}>{"<br/>".join(r)}</div>'

    traverse['delete'] = 'Manager'
    def delete(self, o):
        '''Delete a history event whose ID is in the request'''
        # Find the event given its ID being in the request
        event = self.getEvent(o.req.eventId)
        if not event: return o.translate('missing_event')
        self.remove(event)
        return o.translate('object_deleted')

    traverse['modify'] = 'perm:read'
    def modify(self, o):
        '''Update a history event whose ID is in the request'''
        event = self.getEvent(o.req.eventId)
        if not event: return o.translate('missing_event')
        # Is the user allowed to modify this event ?
        user = o.user
        allowed = o.class_.mayEditEventComment(o, event, user,
                                               user.hasRole('Manager'))
        
        if not allowed: return o.translate('unauthorized')
        event.comment = StringCleaner.clean(o.req.comment)
        return o.translate('object_saved')
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
