'''The root class representing the whole application model'''

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
from appy.model.workflow import Role

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Model:
    '''Represents an application's model = the base Appy model, completed and
       extended by the application model.'''

    class Error(Exception): pass

    # Names of base classes forming the base Appy model, in package appy.model,
    # and standard workflows defined in package appy.model.workflows.standard.
    # These classes and workflows are injected into any app's model.

    baseClasses = ('Page', 'User', 'Group', 'Tool', 'Translation', 'Carousel',
                   'Document', 'Query', 'Mover', 'Place')

    baseWorkflows = ('Anonymous', 'Authenticated', 'Owner', 'TooPermissive')

    def __init__(self, config, classes, workflows):
        '''The unique Model instance is created by the
           appy.model.loader.Loader.'''
        # The app's global config
        self.config = config
        # All Appy classes, keyed by their name
        self.classes = classes # ~{s_className: appy.model.meta.Class}~
        # All Appy worfklows, keyed by their name
        self.workflows = workflows # ~{s_className: appy.model.meta.Workflow}~
        # The global, grantable roles (will be computed later, at run-time only)
        self.grantableRoles = None

    def getClasses(self, type=None):
        '''Returns a list of classes (sorted by alphabetical order of their
           name) from self.classes. If p_type is:
           - None:       all classes are returned;
           - "class":    only Appy classes are iterated;
           - "workflow": only Appy workflows are iterated.
        '''
        if type is None:
            attributes = ('classes', 'workflows')
        else:
            attributes = ('classes',) if (type == 'class') else ('workflows',)
        # Build the result list
        r = []
        for name in attributes:
            r += list(getattr(self, name).values())
        r.sort(key=lambda k: k.name.lower())
        return r

    def getRootClasses(self):
        '''Returns the list of root classes for this app'''
        r = self.config.model.rootClasses
        if r is None: return () # No root class at all
        if not r:
            # We consider every "app" class as being a root class
            r = [c for c in self.getClasses(type='class') if c.type == 'app']
        else:
            r = [self.classes[name] for name in r]
        return r

    def getRoles(self, base=None, local=None, grantable=None, sorted=False):
        '''Produces a list of all the roles used within all workflows and
           classes defined in this app.'''
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # If p_base is...
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # True  | it keeps only standard Appy roles;
        # False | it keeps only roles which are specific to this app;
        # None  | it has no effect (so it keeps both roles).
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # If p_local is...
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # True  | it keeps only local roles. A local role is granted to a user
        #       | or group, is stored and applies on a single object only;
        # False | it keeps only global roles. A global role is granted to a
        #       | group or user and applies everywhere throughout the app,
        #       | independently of any object;
        # None  | it has no effect (so it keeps both roles).
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # If p_grantable is...
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # True  | it keeps only roles that a Manager can grant;
        # False | if keeps only ungrantable roles (ie those that are implicitly
        #       | granted by the system like role "Authenticated";
        # None  | it has no effect (so it keeps both roles).
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        r = {} # ~{s_roleName: Role_role}~
        # Collect roles from workflow states and transitions
        for workflow in self.workflows.values():
            for name in workflow.attributes.keys():
                for elem in getattr(workflow, name).values():
                    for role in elem.getUsedRoles():
                        r[role.name] = role
        # Gather roles from "creators" attributes from every class
        for class_ in self.classes.values():
            creators = class_.getCreators()
            if not creators: continue
            for role in creators:
                r[role.name] = role
        # Get additional roles from the config
        for role in self.config.model.additionalRoles:
            if isinstance(role, str):
                role = Role(role)
            r[role.name] = role
        # Filter the result according to parameters and return a list
        r = [role for role in r.values() if role.match(base,local,grantable)]
        if sorted:
            r.sort(key= lambda r:r.name.lower())
        return r

    def getGrantableRoles(self, o, namesOnly=False, checkManager=False,
                          forced=None):
        '''Returns the list of global roles that can be granted to a user'''
        # If p_checkManager is True, role "Manager", if among the result, is
        # removed from it if the logged user is not a manager itself.
        #
        # By default, these roles are retrieved from p_self.grantableRoles,
        # excepted if another list of roles is passed in p_forced.
        roles = self.grantableRoles if forced is None else forced
        r = []
        for role in roles:
            name = role if isinstance(role, str) else role.name
            # Ignore role "Manager" when appropriate
            if checkManager and name == 'Manager' and \
               not o.user.hasRole('Manager'): continue
            # Add the role to v_r, in the appropriate format
            info = name if namesOnly else (name, o.translate(f'role_{name}'))
            r.append(info)
        return r

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                                  PX
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    view = Px('''
     <x var="className=req.className; model=o.model">
      <h2>Root classes (+tool)</h2>

      <!-- Class selector -->
      <select name="classes" var="murl=f'{tool.url}/view?page=model'"
        onchange=":'goto(&quot;%s&amp;className=&quot; + this.value)' % murl">
       <option value="">-</option>
       <option for="class_ in model.getRootClasses()" var2="name=class_.name"
               value=":name" selected=":name == className">:name</option>
       <option value="Tool">Tool</option>
      </select>

      <!-- The current class -->
      <x if="className"
         var2="class_=model.classes[className]">:class_.pxBox</x>
     </x>''',

     css='''
      .mbox>tbody>tr>:nth-child(2) { border:none; background-color:transparent;
        padding-left:0 }
      .mbox>tbody>tr>th { text-transform:none; font-size:100%;
                          text-align:center }
      .mbox>tbody>tr>td { border-bottom:none; border-top:none }
      .mbox>tbody>tr:last-child>td:first-child
        { border-bottom:1px solid darkgrey }
      a.bref, a.bref:visited {
        padding:0 0.4em; border: 1px solid black; font-weight:bold;
        background-color:|darkColor|; color:|brightColor| }
      .boxIcon { width:1.4em; float:right; padding-top:2px }
      .boxIconR { width:1.3em; padding:0 0 0.2em 0.2em }
     ''')
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
