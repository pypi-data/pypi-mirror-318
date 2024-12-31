'''Takes care of importing one object from one Appy site to another'''

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
import types, time, shutil
from DateTime import DateTime
from persistent.list import PersistentList

from appy.model.workflow import history
from appy.model.utils import Object as O

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
IMP_START = '%s %d %s instances(s) in %s:%s...'
REF_OBJS  = '%s:%s > %s objects'
ADD_DONE  = ' %d created ¤ %d ignored ¤ %d linked.'
U_NO_PWD  = 'Imported user %s has no password.'
IDX_ERR   = 'Error while indexing %s object based on distant object: %s.'
D_N_FOUND = 'Object@%s not found.'
FROZEN_DP = '%s %s: %d frozen document(s) dumped.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Importer:
    '''Imports a single object from one Appy site to another'''

    # Depending on importing needs, sub-classes of this class may be defined and
    # used by sub-classes of class appy.peer.Peer.

    @classmethod
    def getClassName(class_):
        '''Gets the name of the class for which p_class is an importer'''
        return class_.__name__[:-8]

    # If the database IDs defined on distant objects were custom and if it has
    # sense to keep then as IDS for locally created objects, set this flag to
    # True on your Importer sub-class. You may also speciry a classmethod
    # accepting the distant ID as unique arg.
    keepDistantIds = False

    @classmethod
    def mustKeepDistantId(class_, id):
        '''Must this distant p_ID be used as ID for the local object ?'''
        keep = class_.keepDistantIds
        return keep(id) if callable(keep) else keep

    # Non-keywords args for Event sub-classes
    eventsNonKeyword = ('login', 'state', 'date', 'className')

    def __init__(self, tool, peer, local=None, distant=None, distantUrl=None,
                 importHistory=True, importLocalRoles=True, importFields=True):
        # The local tool and the request object
        self.tool = tool
        self.req = tool.req
        # A link to the Peer instance driving the import process
        self.peer = peer
        # The local object. It may already exist prior to the import process
        # (ie, it is a default object like the tool) or it may have been created
        # prior to calling this constructor.
        self.local = local
        # The p_distant object, in the form of a appy.model.utils.Object
        # instance, unmarshalled from the distant site by the
        # appy.xml.unmarshaller. Either this p_distant object is passed,
        # previously imported and unmarshalled, or a p_distantUrl is passed, and
        # the first task of this importer will be to download and unmarshall it.
        self.distant = distant
        self.distantUrl = distantUrl
        # Must object history be imported ?
        self.importHistory = importHistory
        # Must object's local roles be imported ?
        self.importLocalRoles = importLocalRoles
        # Must object fields be imported ? A concrete importer may want to
        # disable it in order to propose a custom way to import didtant object
        # fields.
        self.importFields = importFields
        # Must the local object be reindexed after the import ? True by default,
        # this may be set to False if, for example, the local object already
        # exists and does not need to be imported nor synchronized.
        self.reindexLocal = True

    # During the import process, everytime an object is about to be imported
    # because mentioned in a Ref:add=True, one of the following actions can be
    # performed.
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    CREATE = 0 # Create a local object corresponding to the distant one
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    IGNORE = 1 # Do not do anything, simply ignore the distant object
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    FIND   = 2 # Find a local object corresponding to the distant one, but
    #            ignore distant data.
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SYNC   = 3 # Find a local object corresponding to the distant one and update
    #            the local object with distant data.
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    @classmethod
    def getAction(class_, distant):
        '''What action must be performed with this p_distant object ?'''

        # The method returns a tuple (action, detail):
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # action | must be one of the hereabove constants ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # detail | if action is CREATE or IGNORE, action is ignored;
        #        |
        #        | if action is FIND or SYNC:
        #        |   * if "detail" is None, the local object will be found based
        #        |     on the distant object's ID ;
        #        |   * if "detail" is a dict, it will be considered as a unique
        #        |     combination of attributes allowing to perform a search
        #        |     and find a unique local object corresponding to the
        #        |     distant one. For example, for a user it could be
        #        |
        #        |                     {'login': 'admin'}
        #        |
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # By default, any distant object found via a Ref:add=True must be
        # locally created.
        return class_.CREATE, None

    def log(self, message):
        '''Logs this m_message'''
        return self.tool.log(message)

    def get(self, url, params=None):
        '''Perform a HTTP get on this p_url'''
        return self.peer.get(url, params=params)

    def addableRef(self, field):
        '''Is this Ref p_field addable ?'''
        # Check first in the peer config
        addable = self.peer.addable
        if addable:
            fields = addable.get(self.local.class_.name)
            if fields and field.name in fields:
                return fields[field.name]
        # Deduce addability
        if field.add:
            r = True
        elif field.link:
            r = False
        elif field.composite:
            r = True
        else:
            r = False
        return r

    def getDistantRefs(self, field):
        '''Retrieve, on p_self.distant, info about the tied objects'''
        # Most of the time, this info is a list of URLs, every URL pointing to
        # a distant tied object. But it can sometimes also be:
        # - a single URL ;
        # - the distant ID of a distant object, instead of its full URL ;
        # - a list of distant IDs ;
        # - an object made of attributes "url" and "id" .
        # Moreover, a name clash can occur between the p_field.name and one of
        # the standard methods of the appy.model.utils.Object class, used to
        # represent p_self.distant (ie, names like "items", "values", etc). In
        # that case, Ref info is of the form [<bound method xx>, <value>]: a
        # list of 2 elements, whose first one contains the homonym method, and
        # whose second one contains the Ref info in itself.
        # ~
        # This method "resolves" such name clashes and ensures the result is a
        # list.
        # ~
        # Get info on the distant object
        r = getattr(self.distant, field.name, None)
        if not r: return
        # Manage name clashes
        if isinstance(r, list) and len(r) == 2:
            # Detect name clashes
            if isinstance(r[0], types.MethodType):
                r = r[1]
            elif isinstance(r[1], types.MethodType):
                r = r[0]
        if isinstance(r, types.MethodType):
            # There is no data: v_r is probably just an Object method
            r = None
        # Ensure the result is a list
        if isinstance(r, str): r = [r]
        return r

    def setRef(self, field):
        '''Links distant objects defined @p_self.distant.<p_field.name> to
           p_self.local via this Ref p_field.'''
        # Get the list of distant object URLs on p_self.distant
        urls = self.getDistantRefs(field)
        if not urls: return
        # Unwrap some variables
        o = self.local
        imported = self.peer.localObjects
        add = self.addableRef(field)
        name = field.name
        peer = self.peer
        # Browse URLs of distant objects. For lisibility, reduce the log to a
        # single letter when linking an existing object.
        verb = 'Creating' if add else 'L'
        tiedClass = field.class_.meta
        if add:
            o.log(IMP_START % (verb, len(urls), tiedClass.name, o.class_.name,
                               field.name))
        else:
            self.peer.printInfo(f'{verb}:{field.name}:')
        # Count the number of objects that will be created, linked, ignored, and
        # those being unresolved at this step.
        counts = O(created=0, linked=0, ignored=0, unresolved=0, current=0)
        total = len(urls)
        for url in urls:
            counts.current += 1
            # Get the distant ID from the URL
            if isinstance(url, O):
                # In some cases, distant info may be an object already made of
                # the distant URL and its ID.
                distantId = url.id
                url = url.url
            else:
                # v_url should be a URL, but it could also simply be an ID
                if '/' in url:
                    distantId = peer.getIdFromUrl(url)
                else:
                    distantId = url
            if add:
                peer.printSymbol(counts.current, total)
                # Get the distant object
                distant = peer.get(url)
                # Get an importer class for this type of objects
                importer = peer.getImporter(tiedClass)
                # What to do with this distant object ?
                action, detail = importer.getAction(distant)
                if action == importer.IGNORE:
                    # Ignore it
                    counts.ignored += 1
                    continue
                elif action == importer.CREATE:
                    # Create a local object corresponding to the distant one
                    id = distantId if importer.mustKeepDistantId(distantId) \
                                   else None
                    tied = o.create(name, id=id, executeMethods=False,
                                    indexIt=False)
                    # Add it to the dict of already imported objects
                    imported[distantId] = tied
                    # Fill local object's attributes from distant ones
                    importer(self.tool, peer, tied, distant).run()
                    counts.created += 1
                elif action in (importer.FIND, importer.SYNC):
                    # Find the local objet corresponding to the distant one
                    classT = tiedClass.name
                    if detail is None:
                        tied = o.getObject(distant.id, className=classT)
                    else:
                        tied = o.search1(classT, **detail)
                    # Add it to the dict of already imported objects
                    imported[distantId] = tied
                    # Fill, when appropriate, local object's attributes from
                    # distant ones.
                    if action == importer.SYNC:
                        importer(self.tool, peer, tied, distant).run()
                    counts.linked += 1
            else:
                # Find the object among the already imported objects
                if distantId not in imported:
                    # The object has not been imported yet
                    peer.unresolved.add(o, field, distantId)
                    counts.unresolved += 1
                else:
                    tied = imported[distantId]
                    o.link(name, tied, executeMethods=False)
                    counts.linked += 1
        # Log the end of this operation
        if add:
            prefix = REF_OBJS % (o.class_.name, field.name, tiedClass.name)
            suffix = ADD_DONE % (counts.created, counts.ignored, counts.linked)
            o.log(f'{prefix}:{suffix}')
        else:
            info = str(counts.linked)
            unresolved = counts.unresolved
            if unresolved:
                info = f'{info}(U={unresolved})'
            self.peer.printInfo(info)

    def setInnerRefs(self, field, row):
        '''Search, among this p_row of inner data, any p_field's inner-field
           being a Ref. For every found Ref, convert the list of distant IDs
           into a persistent list of local objects.'''
        peer = self.peer
        o = self.local
        # Scan sub-fields and manage those being Refs
        for name, sub in field.fields:
            if sub.type == 'Ref' and name in row:
                # A sub-field being a Ref was found. Has it a value on p_row ?
                distantIds = getattr(row, name)
                if not distantIds: continue
                # Yes. Convert this list of distant IDs into a list of local
                # objects.
                localObjects = peer.localObjects
                r = PersistentList()
                for id in distantIds:
                    if id in localObjects:
                        r.append(localObjects[id])
                    else:
                        # Must be resolved at the very end of the data
                        # migration. Leave the ID as is for the moment.
                        r.append(id)
                        peer.unresolved.add(o, (field, sub), id)
                setattr(row, name, r)

    def setFields(self):
        '''Copy values from p_self.distant fields'''
        o = self.local
        d = self.distant
        for name, field in self.local.class_.fields.items():
            # Ignore non-persistent fields
            if not field.persist: continue
            if field.type == 'Ref':
                # Ignore back Refs: they will be automatically reconstituted by
                # linking object via forward Refs.
                if field.isBack: continue
                self.setRef(field)
            elif field.outer:
                # Use a persistent data structure and manage inner-fields being
                # Refs.
                value = getattr(d, name)
                if value:
                    # Transform p_value into a persistent data structure
                    value = field.outerType(value)
                    # Search for inner fields being Refs
                    if field.type == 'List':
                        # Scan every row of data and manage any found Ref value
                        for row in value:
                            self.setInnerRefs(field, row)
                    elif field.type == 'Dict':
                        for row in value.values():
                            self.setInnerRefs(field, row)
                    # Set the value on p_o
                    setattr(o, name, value)
            else:
                # Simply copy the field value
                value = getattr(d, name)
                if value is not None:
                    setattr(o, name, value)

    def setHistory(self, copyBase=True, copy=True, state=None, add=None):
        '''Copies p_self.distant's history to p_self.local's history, excepted
           if p_copy is False.'''
        # p_copyBase refers to basic attributes: creator, created and modified.
        # If p_state is set, p_self.local's state will be set to this state,
        # independently of p_self.distant's state. If p_add is passed, it must
        # correspond to the name of a valid workflow transition for which is an
        # event will be added in p_self.local's history.
        d = self.distant
        o = self.local
        hist = o.history
        # Copy base history-related attributes
        if copyBase:
            hist[-1].login = d.creator or '?'
            hist[-1].date = d.created or DateTime()
            hist.modified = d.modified or DateTime()
            if d.modifier:
                hist.modifier = d.modifier
        if copy and d.record:
            initial = hist.pop()
            # Get and copy distant events
            for devent in d.record.data:
                # Ignore the initial event, already created locally
                if devent.transition == '_init_': continue
                # Create the appropriate Event sub-class instance
                class_ = eval(f'history.{devent.className}')
                login, state, date = devent.login, devent.state, devent.date
                params = devent.__dict__
                for name in self.eventsNonKeyword:
                    del params[name]
                event = class_(login, state, date, **params)
                hist.append(event)
            # Put the initial event at the end
            hist.append(initial)
        # Add the p_add trigger event if defined
        if add: hist.add('Trigger', transition=add)
        # Force v_o's current state to p_state, if passed
        if state: hist[0].state = state

    def setLocalRoles(self):
        '''To implement'''

    def setFrozen(self, name):
        '''Retrieve, from p_self.distant, frozen documents if defined in
           attribute having this p_name.'''
        # This method is not automatically called: a concrete importer must
        # explicitly call it, if needed.
        # ~
        # Abort if no frozen doc is found
        frozen = self.distant[name]
        if not frozen: return
        # Ensure the disk folder exists for p_self.local
        o = self.local
        folder = o.getFolder(create=True)
        # Walk UnmarshalledFile instances
        for ufile in frozen:
            # Write this file in v_folder, with the right name
            fname = f'{str(folder)}/{ufile.name}'
            if ufile.location:
                shutil.copyfile(ufile.location, fname)
            else:
                with open(fname, 'wb') as f: f.write(ufile.value)
        o.log(FROZEN_DP % (o.class_.name, o.id, len(frozen)))

    def customize(self):
        '''To be overridden by sub-class to tailor the import of self.p_local'''

    def run(self):
        '''Performs the import from p_self.distant to p_self.local'''
        # Import the distant object if not done yet
        if self.distantUrl:
            self.distant = self.peer.get(self.distantUrl)
            if not self.distant:
                self.log(D_N_FOUND % self.distantUrl)
                return
        # If the local object was previously created, we follow the standard
        # process, consisting in syncing its fields with its distant
        # counterpart.
        if self.local:
            # Set history, local roles and fields when required
            if self.importHistory: self.setHistory()
            if self.importLocalRoles: self.setLocalRoles()
            if self.importFields: self.setFields()
        # Perfom custom processing, if any. If p_self.local did not exist, we
        # are in a custom import process: m_customize must do the whole job,
        # starting with creating the local object, or finding it and syncing it,
        # or whatever. During this custom processing, standard methods like
        # m_setHistory, p_setLocalRoles or p_setFields, must, if required, be
        # explicitly called by m_customize.
        self.customize()
        # Reindex the object if appropriate
        o = self.local
        if o and self.reindexLocal and o.class_.isIndexable():
            try:
                o.reindex()
            except Exception as err:
                o.log(IDX_ERR % (o.class_.name, str(self.distant)))
                raise err
        return o

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class UserImporter(Importer):
    '''Specific importer for importing users'''

    # Logins of users that must not be imported
    unimportable = ('anon', 'system')

    def customize(self):
        '''Manage special field "encrypted" storing the encrypted password'''
        encrypted = self.distant.encrypted
        o = self.local
        if encrypted:
            o.values['password'] = encrypted.encode()
        elif o.source == 'zodb':
            o.log(U_NO_PWD % o.login, type='error')

    @classmethod
    def getAction(class_, distant):
        '''Special users "system" and "anon" must not be imported; user "admin"
           must be found locally but not synced.'''
        login = distant.login
        if login in class_.unimportable:
            r = class_.IGNORE, None
        elif login == 'admin':
            r = class_.FIND, {'login': 'admin'}
        else:
            r = class_.CREATE, None
        return r
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
