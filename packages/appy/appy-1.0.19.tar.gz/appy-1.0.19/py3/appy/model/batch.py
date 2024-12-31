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
from appy.utils import string as sutils

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Batch:
    '''Represents a list of objects being part of a wider list, ie:
        * page 2 displaying objects 30 to 60 from a search matching 1110
          results;
        * page 1 displaying objects 0 to 20 from a list of 43 referred objects.
    '''
    def __init__(self, objects=None, total=0, size=30, start=0, hook=None):
        # The objects being part of this batch
        self.objects = objects
        # The effective number of objects in this batch
        self.length = len(objects) if objects is not None else 0
        # The total number of objects from which this batch is only a part of
        self.total = total
        # The normal size of a batch. If p_size is None, all objects are shown.
        # "length" can be less than "size". Example: if total is 12 and batch
        # size is 10, the batch representing objects 0 to 9 will have
        # length=size=10, but the second batch representing objects 10 to 12
        # will have size (3) < length (10).
        self.size = size
        # The index of the first object in the current batch
        self.start = start
        # When this batch is shown in the ui, the ID of the DOM node containing
        # the list of objects.
        self.hook = hook

    def setObjects(self, objects):
        '''p_objects may no have been added at construction time'''
        self.objects = objects
        self.length = len(objects)

    def getInfo(self, condition, nb, c):
        '''Returns info about the current navigation icon to produce'''
        # Return info is a 2-tuple (s_cssClasses, s_onClick)
        if not condition:
            css = 'disabled iconS'
            js = ''
        else:
            css = 'clickable iconS'
            q = c.q
            scrollTop = q(c.scrollTop) if c.scrollTop else 'null'
            js = 'askBunch(%s,%s,%s,%s)' % (q(self.hook), q(nb), q(self.size),
                                            scrollTop)
        return css, js

    # Input field for going to element number x
    pxGotoNumber = Px('''
     <x var2="label=_('goto_number');
              gotoName=f'{o.iid}_{field.name}_goto'">
      <span class="gotoLab">:label</span>
      <input type="text" id=":gotoName" name=":gotoName" class="gotoNum"
             size=":max(len(str(total))-1, 1)" onclick="this.select()"
             onkeydown="if (event.keyCode==13) this.nextSibling.click()"/>
      <img class="clickable"
             onclick=":'gotoTied(%s,%s,this.previousSibling,%s,%s)' % \
                 (q(sourceUrl), q(field.name), total, q(popup))"
             src=":url('gotoNumber')" title=":label"/></x>''',

      css='''.gotoNum { text-align:center; color:white;
                        mix-blend-mode:difference }
             .gotoLab { padding:0 0.5em; font-size:90% }''')

    pxNavigate = Px('''
     <!-- Go to the first page -->
     <img var="cond=batch.start != 0 and batch.start != batch.size;
               css,js=batch.getInfo(cond, 0, _ctx_)"
          class=":css" src=":svg('arrows')" onclick=":js"
          title=":_('goto_first')" style="transform:rotate(90deg)"/>

     <!-- Go to the previous page -->
     <img var="cond=batch.start != 0;
               sNumber=batch.start - batch.size;
               css,js=batch.getInfo(cond, sNumber, _ctx_)"
          class=":css" src=":svg('arrow')" onclick=":js"
          title=":_('goto_previous')" style="transform:rotate(90deg)"/>

     <!-- Explain which elements are currently shown -->
     <span class="navText"> 
      <x>:batch.start + 1</x> ⇀
      <x>:batch.start + batch.length</x> <span class="navSep">//</span> 
      <span class="btot">:batch.total</span>
     </span>

     <!-- Go to the next page -->
     <img var="sNumber=batch.start + batch.size;
               cond=sNumber &lt; batch.total;
               css,js=batch.getInfo(cond, sNumber, _ctx_)"
          class=":css" src=":svg('arrow')" title=":_('goto_next')"
          style="transform:rotate(270deg)" onclick=":js"/>

     <!-- Go to the last page -->
     <img var="lastIncomplete=batch.total % batch.size;
               complete=int(batch.total / batch.size);
               counted=complete if lastIncomplete else complete-1;
               sNumber= counted * batch.size;
               cond=(batch.start != sNumber) and
                    (batch.start != (sNumber-batch.size));
               css,js=batch.getInfo(cond, sNumber, _ctx_)"
          class=":css" src=":svg('arrows')" onclick=":js"
          title=":_('goto_last')" style="transform: rotate(270deg)"/>

     <!-- Go to the element number... -->
     <x var="gotoNumber=gotoNumber|False" if="gotoNumber"
        var2="sourceUrl=o.url; total=batch.total">:batch.pxGotoNumber</x>''')

    def store(self, search, name=None):
        '''Returns the Javascript code allowing to store objects from this batch
           in the browser's session storage.'''
        # Get the key at which we will store object IDs in the local storage
        key = search.getSessionKey(name=name)
        # Get the dict of IDs to store ~{i_index:i_id}~
        i = self.start
        value = {}
        for o in self.objects:
            value[i] = o.iid
            i += 1
        value = sutils.getStringFrom(value)
        return "sessionStorage.setItem('%s',JSON.stringify(%s))" % (key, value)

    def isComplete(self):
        '''Does this batch contain all objects ?'''
        return self.length == self.total

    def showNav(self):
        '''Show the navigation only when appropriate'''
        return self.total > self.size

    def __repr__(self):
        '''String representation'''
        data = 'start=%d,length=%d,size=%s,total=%d' % \
               (self.start, self.length, self.size, self.total)
        if self.hook: data = 'hook=%s,%s' % (self.hook, data)
        return '<Batch %s>' % data
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
