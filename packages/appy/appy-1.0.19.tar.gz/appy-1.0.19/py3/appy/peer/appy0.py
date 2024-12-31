'''Import data from a Appy 0.x site to an Appy 1.x site'''

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
from appy.peer import Peer
from appy.peer.importer import Importer, UserImporter

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
LROLES_KO  = '%s object: no local roles found. Distant is: %s.'
E_LC_KO    = 'No local roles found on distant object.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Importer0(Importer):
    '''Base object importer for Appy 0'''

    # If, for some concrete importer, you want, for some transitions, use
    # alternate names on the target site (Appy 1 is more strict and does not
    # allow as much names as Appy 0), override static attribute "transitionMap"
    # and specify a dict of the form ~{s_sourceName: s_targetName}~.
    transitionsMap = None

    def getTransitionName(self, name):
        '''Gets, on the targte site, the name of the transition that must be
           used for representing the distant transition whose name is p_name.'''
        map = self.transitionsMap
        if map is None: return name
        return map.get(name) or name

    def setHistory(self):
        '''Imports Appy 0's history from p_self.distant and populate the
           corresponding Appy 1 data structure on p_self.local.'''
        history = self.local.history
        # History events in Appy 0 are chronologically sorted
        i = -1
        for event in self.distant.history:
            i += 1
            if i == 0:
                # Creator, created & modified will be set by m_setFields.
                # Nevertheless, a potential comment can be retrieved from the
                # initial distant transition.
                if event.comments:
                    history[-1].comment = event.comments
                # Flag "local roles only", in Appy 0, is potentially stored on
                # this first event.
                if event.local:
                    self.local.localRoles.only = True
                continue
            # Get parameters being common to all history events
            params = {'state': event.review_state, 'date': event.time,
                      'login': event.actor, 'comment': event.comments}
            action = event.action
            if action == '_datachange_':
                eventType = 'Change'
                # Convert the "changes" dict to Appy 1
                changes = {}
                for name, vals in event.changes.items():
                    # Manage multilingual fields
                    key = tuple(name.rsplit('-', 1)) if '-' in name else name
                    changes[key] = vals[0]
                params['changes'] = changes
            elif action == '_dataadd_':
                eventType = 'Link'
                # No idea if addition must be True or False: this subtelty was
                # not present in Appy 0.
                params['addition'] = False
                params['field'] = 'unknown' # Idem
            elif action == '_datadelete_':
                eventType = 'Unlink'
                # No idea if addition must be True or False: this subtelty was
                # not present in Appy 0.
                params['deletion'] = False
                params['field'] = 'unknown' # Idem
            elif action.startswith('_action'):
                # A custom event
                eventType = 'Custom'
                params['label'] = action.strip('_')
            else:
                # A workflow transition
                eventType = 'Trigger'
                params['transition'] = self.getTransitionName(action)
            history.add(eventType, **params)

    def setLocalRoles(self):
        '''Sets local roles on p_self.local as defined on p_self.distant'''
        o = self.local
        localRoles = o.localRoles
        # Delete local role granted to technical user "system" when the local
        # object has been created.
        localRoles.delete('system')
        # Get the distant local roles
        droles = self.distant.localRoles
        if droles is None:
            o.log(LROLES_KO % (o.class_.name, str(self.distant)), type='error')
            raise Exception(E_LC_KO)
        # Set the local roles on the local object
        for login, roles in droles.items():
            localRoles.add(login, roles)

    def customize(self):
        '''Manage "creator", "created" and "modified" fields, being stored
           differently in Appy 0 and Appy 1.'''
        o = self.local
        d = self.distant
        o.setCreator(d.creator)
        o.history[-1].date = d.created
        o.history.modified = d.modified

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class UserImporter0(Importer0, UserImporter):
    '''Appy 0 User-specific importer'''

    def customize(self):
        '''Perform Appy 0 AND User-specific customization'''
        Importer0.customize(self)
        UserImporter.customize(self)

    @classmethod
    def getAction(class_, distant):
        '''Bypass Python's standard depth-first search inheritance and call
           UserImporter.getAction.'''
        return UserImporter.getAction(distant)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Appy0(Peer):
    '''Represents a peer Appy 0.x site'''

    # Declare the base object importer for Appy 0
    baseImporter = Importer0

    # In Appy 0, the ID of the tool is 'config' and not 'tool'
    distantToolName = 'config'

    def __init__(self, *args, **kwargs):
        # Call the base constructor
        super().__init__(*args, **kwargs)
        # Update importers
        self.importers['User'] = UserImporter0

    def getSearchUrl(self, tool, className):
        '''Return the URL allowing to retrieve URLs of all instances from a
           given p_className on a distant site.'''
        # Get the name of the distant class corresponding to this local
        # p_className.
        distantName = self.classNames.get(className) or className
        return '%s/config?do=searchAll&className=%s' % (self.url, distantName)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
