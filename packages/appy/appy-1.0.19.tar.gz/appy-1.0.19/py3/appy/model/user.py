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
import time, base64
from DateTime import DateTime

from appy.px import Px
from appy.model.base import Base
from appy.model.fields import Show
from appy.ui.layout import Layouts
from appy.model.searches import Search
from appy.database.operators import or_
from appy.utils import string as sutils
from appy.model.fields.date import Date
from appy.utils.string import Normalize
from appy.model.utils import Object as O
from appy.model.fields.phase import Page
from appy.model.fields.group import Group
from appy.model.fields.string import String
from appy.model.fields.action import Action
from appy.model.fields.boolean import Boolean
from appy.model.fields.computed import Computed
from appy.model.fields.password import Password
from appy.model.workflow import standard as workflow
from appy.model.fields.select import Select, Selection

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
SCAN_DB    = 'Scanning all database objects...'
LOGIN_RN   = 'User "%s" has new login "%s".'
LOGIN_OP   = "Login change: local roles and/or history updated in %d/%d " \
             "object(s). Done in %.2f''."
O_WALKED   = '%d objects walked so far...'
USR_CONV   = 'User "%s" converted from "%s" to "%s".'
SSO_USR_KO = 'SSO user "%s" could not be authenticated.'
COOKIE_KO  = 'Unreadable cookie (%s).'
SOL_KO     = 'When p_solely is True, p_role must be a single role and p_o ' \
             'must be None.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class User(Base):
    '''Base class representing a user'''

    workflow = workflow.Owner
    noLoginUsers = ('system', 'anon')
    specialUsers = noLoginUsers + ('admin',)
    searchAdvanced = Search('advanced', actionsDisplay='inline')
    listColumns = ('title', 'name*15%|', 'login*20%|', 'roles*20%|',
                   'state*10%|')
    listColumnsShort = ('title', 'login')

    # The following users are always present in any Appy database
    defaultUsers = {'admin': ('Manager',), 'system': ('Manager',), 'anon': ()}

    def isAnon(self):
        '''Is the logged user anonymous ?'''
        return self.login == 'anon'

    def isSpecial(self, includeAdmin=True):
        '''Is this user a predefined user ?'''
        attr = 'specialUsers' if includeAdmin else 'noLoginUsers'
        return self.login in getattr(User, attr)

    @staticmethod
    def update(class_):
        '''Hide the title'''
        title = class_.fields['title']
        title.show = 'xml'
        title.page.icon = 'pageProfile.svg'

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #                               Password
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    # This page contains the single field "password" allowing to edit a local
    # user's password.

    def showPassword(self):
        '''Field "password" must be shown only for the local user allowed to
           modify it.'''
        mayEdit = self.source == 'zodb' and self.user.login == self.login
        return 'edit' if mayEdit else None

    def showCancel(self):
        '''Do not show the "cancel" button on page "passwords" if the user is
           forced to change its password.'''
        return not self.changePasswordAtNextLogin

    pagePassword = Page('password', show=showPassword, showCancel=showCancel,
                        label='User_page_password', icon='pagePassword.svg')

    password = Password(multiplicity=(1,1), show=showPassword, label='User',
                        placeholder=lambda o: o.translate('password_type_new'),
                        page=pagePassword, autofocus=True)

    # The encrypted password, carriable via the XML layout
    def showEncrypted(self):
        '''Allow to show encrypted password to admins only, via the xml
           layout.'''
        if self.user.login == 'admin' and self.source != 'sso' and \
           'password' in self.values:
            return 'xml'

    encrypted = Computed(show=showEncrypted, label='User',
                         method=lambda o: o.values.get('password'))

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #                         Title, name, first name
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    baseGroup = Group('main', ['15%','85%'], style='grid', hasLabel=False)

    pm = {'page': Page('main', label='User_page_main', icon='pageProfile.svg'),
          'width': 28, 'layouts': Layouts.g, 'label': 'User',
          'historized': True, 'group': baseGroup}

    def getTitle(self, normalized=False, useName=True, nameFirst=False,
                 nameTransform=None, firstNameTransform=None):
        '''Returns a nice name for this user, based on available information:
           "first name"/"name" (if p_useName is True) or title or login. If
           p_normalized is True, special chars (like accents) are converted to
           ascii chars. When p_useName is True, if p_nameFirst is True, the
           result will be "name" / "first name", else it will be
           "first name" / "name".'''
        # A specified transform ("upper", "capitalize", etc) can be specified in
        # p_nameTransform and/or p_firstNameTransform.
        login = self.login
        r = None
        if useName:
            firstName = self.firstName
            name = self.name
            if firstName and name:
                # Apply a transform if requested
                if nameTransform:
                    name = eval(f'name.{nameTransform}()')
                if firstNameTransform:
                    firstName = eval(f'firstName.{firstNameTransform}()')
                # Concatenate first and last names in the right order
                r = f'{name} {firstName}' if nameFirst else \
                    f'{firstName} {name}'
        r = r or self.title or login
        return Normalize.accents(r) if normalized else r

    def getTitleFromLogin(self, login, *args, **kwargs):
        '''Similar to p_getTitle, but for a user whose l_login is given (not
           p_self). If no user with this login exists, p_login is returned.'''
        user = self.search1('User', secure=False, login=login)
        return user.getTitle(*args, **kwargs) if user else login

    def updateTitle(self):
        '''Sets a title for this user'''
        self.title = self.getTitle(nameFirst=True)

    def getSupTitle(self, nav):
        '''Display a specific icon if the user is a local copy of an external
           (ldap/sso) user.'''
        if self.source == 'zodb': return
        # For external users, note the source and last synchronization date in
        # the icon's title.
        sdate = self.syncDate
        url = self.buildUrl('external')
        suffix = f' - sync@ {self.tool.formatDate(sdate)}' if sdate else ''
        return f'<img src="{url}" title="{self.source.upper()}{suffix}" ' \
               f'class="help"/>'

    def ensureAdminIsManager(self):
        '''User "admin" must always have role "Manager"'''
        if self.id != 'admin': return
        roles = self.roles
        if 'Manager' not in roles:
            if not roles: roles = ['Manager']
            else: roles.append('Manager')
            self.roles = roles

    def showName(self):
        '''Name and first name, by default, can not be edited for non-local
           users.'''
        return True if self.source == 'zodb' else Show.E_

    name = String(show=showName, **pm)
    firstName = String(show=showName, **pm)

    def getFirstName(self):
        '''Return p_self's first name, or call m_getTitle if the first name is
           undefined.'''
        return self.firstName or self.getTitle()

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #                                 Login
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    pm['multiplicity'] = (1,1)

    def showLogin(self):
        '''When must we show the login field ?'''
        if self.isTemp(): return 'edit'
        # The manager has the possibility to change the login itself (local
        # users only).
        if self.user.hasRole('Manager') and self.source == 'zodb':
            return True
        return Show.E_

    def validateLogin(self, login):
        '''Is this p_login valid ?'''
        # 2 cases: (1) The user is being created and has no login yet, or
        #          (2) The user is being edited and has already a login, that
        #              can potentially be changed.
        if not self.login or login != self.login:
            # A new p_login is requested. Check if it is valid and free.
            # Some logins are not allowed.
            if login in self.specialUsers:
                return self.translate('login_reserved')
            # Check that no user or group already uses this login
            if self.count('User', login=login) or \
               self.count('Group', login=login):
                return self.translate('login_in_use')
        return True

    pm['layouts'] = Layouts.gd
    login = String(show=showLogin, validator=validateLogin, indexed=True, **pm)
    del pm['label']

    def getLogins(self, groupsOnly=False, compute=False, guard=None):
        '''Gets all the logins that can "match" this user: it own login
           (excepted if p_groupsOnly is True) and the logins of all the groups
           he belongs to.

           If p_compute is False, p_groupsOnly is False and p_self is the
           currently logged user, roles are retrieved from the guard, that
           caches it. Else, they are really computed.
        '''
        guard = guard or self.guard
        # Return the cached value on the guard when appropriate
        if not compute and not groupsOnly and \
           (guard and self.login == guard.userLogin):
            return guard.userLogins
        # Compute it
        r = [group.login for group in self.groups or ()]
        if not groupsOnly: r.append(self.login)
        return r

    def setLogin(self, old, new, reindex=True):
        '''Modifies p_self's login, from p_old to p_new'''
        start = time.time()
        self.login = new
        # Update the email if it corresponds to the login
        email = self.email
        if email == old:
            self.email = new
        # Update the title
        self.updateTitle()
        # Browse all objects of the database and update potential local roles
        # that referred to the old login.
        self.log(SCAN_DB)
        updated = total = 0
        for tree in self.H().dbConnection.root.iobjects.values():
            for o in tree.values():
                total += 1
                # Update local roles on this object
                rchanged = o.localRoles.replace(old, new)
                hchanged = o.history.replaceLogin(old, new)
                if rchanged or hchanged:
                    updated += 1
                    if o.class_.isIndexable():
                        o.reindex()
                # Log progression
                if (total % 10000) == 0:
                    self.log(O_WALKED % total)
        self.log(LOGIN_RN % (old, new))
        self.log(LOGIN_OP % (updated, total, time.time()-start))
        # Reindex p_self, excepted if p_reindex is False
        if reindex: self.reindex()

    def getAllowedFrom(self, roles, logins):
        '''Gets for this user, the value allowing to perform searches regarding
           index "allowed". p_roles are user roles as computed by m_getRoles and
           p_logins are user logins as computed by m_getLogins.'''
        # Get the user roles. If a copy of the list is not done, user logins
        # will be added among user roles (again and again).
        r = roles[:]
        # Get the user logins
        for login in logins:
            r.append(f'user:{login}')
        return or_(*r)

    def getAllowedValue(self):
        '''Gets, for this user, the value allowing to perform searches regarding
           index "allowed".'''
        return self.getAllowedFrom(self.getRoles(), self.getLogins())

    def showEmail(self):
        '''In most cases, email is the login. Show the field only if it is not
           the case.'''
        # Is this user local ?
        isLocal = self.source == 'zodb'
        # Show the field nevertheless if it is not empty
        if isLocal and not self.isEmpty('email'): return True
        # Hide it if the login is an email
        login = self.login
        if login and String.EMAIL.match(login): return
        # Display the email (read-only if from an external source)
        if not isLocal: return Show.E_
        return True

    pm['label'] = 'User'
    pm['layouts'] = Layouts.g
    email = String(validator=String.EMAIL, show=showEmail, **pm)

    def getMailRecipient(self, normalized=True, mailOnly=False):
        '''Returns, for this user, the "recipient string" (first name, name,
           email) as can be used for sending an email.'''
        r = self.email or self.login
        # Ensure this is really an email
        if not String.EMAIL.match(r): return
        # If p_mailOnly is True, return the email address only
        if mailOnly: return r
        # Return a formatted recipient, containing the person's first and last
        # names.
        return f'{self.getTitle(normalized=normalized)} <{r}>'

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #                          Roles and permissions
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    pm['multiplicity'] = (0, None)
    del pm['width']

    def showRoles(self):
        '''Global roles are not visible or editable under all circumstances'''
        # Local users can't be granted global roles
        if self.container != self.tool: return
        # Only appropriate users are allowed to grant global roles
        user = self.user
        if user.hasRole(self.config.model.roleSetters): return True
        # The user itself, owner of himself, can consult his roles
        if user.hasRole('Owner', self): return Show.E_

    def selectRoles(self):
        '''Returns the list of roles one may select for field "roles"'''
        # Don't let a non-manager select role "Manager"
        return self.model.getGrantableRoles(self, checkManager=True)

    roles = Select(show=showRoles, indexed=True, width=40, height=10,
      validator=Selection(selectRoles,
                          single=lambda o, role: o.translate(f'role_{role}')),
      fwidth='3em', render='checkbox', checkAll=False, **pm)

    def addRole(self, role):
        '''Adds p_role among p_self.roles'''
        r = self.roles or []
        if role not in r:
            r.append(role)
        self.values['roles'] = r

    def delRole(self, role):
        '''Deletes p_role from p_self.roles'''
        roles = self.values.get('roles')
        if roles and role in roles:
            roles.remove(role)
            self.values['roles'] = roles

    def getRoles(self, compute=False, guard=None):
        '''Returns all the global roles granted to this user'''
        # The method returns not simply self.roles, but also "ungrantable roles"
        # (like Anonymous or Authenticated) and roles inherited from group
        # membership.
        #
        # If p_compute is False and p_self is the currently logged user, roles
        # are retrieved from the guard, that caches it. Else, they are really
        # computed.
        guard = guard or self.guard
        # Return the cached value on the guard when appropriate
        if not compute and guard is not None and self.login == guard.userLogin:
            return guard.userRoles
        # Compute it
        r = list(self.roles or ())
        # Add ungrantable roles
        r.append('Anonymous' if self.isAnon() else 'Authenticated')
        # Add group global roles
        for group in self.groups:
            for role in group.roles:
                if role not in r: r.append(role)
        return r

    def hasRole(self, role, o=None, solely=False):
        '''Has p_self this p_role? If p_o is None, check if this user has p_role
           globally; else, check if he has it in the context of p_o.'''
        # p_role can also be a list/tuple of roles. In this case, the method
        # returns True if the user has at least one of the listed roles.
        #
        # If p_solely is True, the method returns True if p_self has this global
        # p_role and no other one (excepted automatic roles Authenticated or
        # Anonymous). p_solely=True can be specified only if p_role is a single
        # role and if p_o is None (no local role check must be performed).
        noo = o is None
        # Check parameters
        if solely and (not noo or not isinstance(role, str)):
            raise Exception(SOL_KO)
        # Try with the user's global roles, excepted if p_o is in "local" mode
        if noo or not o.localRoles.only:
            userRoles = self.getRoles()
            r = sutils.stringIsAmong(role, userRoles)
            # Use p_solely
            if r and solely and len(userRoles) > 2:
                r = False
            if noo or r:
                return r
        # Check now p_o(bject)'s local roles
        logins = self.getLogins()
        for login, roles in o.localRoles.items():
            if login in logins and sutils.stringIsAmong(role, roles):
                return True

    def ensureIsManager(self):
        '''Ensures p_self has role "Manager"'''
        roles = self.roles
        if 'Manager' not in roles:
            if not roles: roles = ['Manager']
            else: roles.append('Manager')
            self.roles = roles

    def hasPermission(self, permission, o):
        '''Has user p_self p_permission on p_o ?'''
        # What are the roles which are granted p_permission on p_o ?
        allowedRoles = o.getWorkflow().getRolesFor(o, permission)
        # Grant access based on global user roles (that include ungrantable
        # roles like Authenticated or Anonymous), excepted if p_o is in
        # "local" mode.
        if not o.localRoles.only:
            for role in self.getRoles():
                if role in allowedRoles: return True
        # Grant access based on local roles. Gets the logins of this user and
        # all its groups
        userLogins = self.getLogins()
        for login, roles in o.localRoles.items():
            # Ignore logins not corresponding to this user
            if login not in userLogins: continue
            for role in roles:
                if role in allowedRoles: return True

    #- -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #                               Source
    #- -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    # Where is this user stored ? By default, in the ZODB. But the user can be
    # stored in an external LDAP (source='ldap').
    source = String(show='xml', default='zodb', layouts='f', label='User')

    def isLocal(self):
        '''Returns True if p_self is a zodb user'''
        return self.source == 'zodb'

    def convertTo(self, source):
        '''Convert p_self as if, now, he would be of p_source, that is different
           from is currently defined p_self.source.'''
        # p_self.source and p_source must be different
        origSource = self.source
        if origSource == source: return
        # Update p_self's parameters
        self.source = source
        self.syncDate = DateTime()
        # This flag is not relevant for external users
        if self.source != 'zodb':
            self.changePasswordAtNextLogin = False
        # Log the operation
        self.log(USR_CONV % (self.login, origSource, source))

    #- -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #                            Editable pages
    #- -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    def showEPages(self):
        '''Show the list of editable pages to Managers and the user itself,
           provided there is at least one such page.'''
        if not self.editablePages: return
        user = self.user
        if self.login == user.login or user.hasRole('Manager'): return 'view'

    #- -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #                               Actions
    #- -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    def mayResetPassword(self):
        '''Anyone having write acces to a user may reset his password, excepted
           if this action is configured to be available to Managers only.'''
        if self.config.security.resetPasswordForManagers:
            r = self.user.hasRole('Manager')
        else:
            r = self.allows('write')
        return r

    def doResetPassword(self, secure=True):
        '''Triggered from the UI, this method defines a new, automatically
           generated password for this user and returns it in the UI.'''
        if secure and not self.mayResetPassword():
            self.raiseUnauthorized()
        password = self.getField('password').generate()
        self.password = password
        self.changePasswordAtNextLogin = True
        # If p_self corresponds to the currently logged user, update the
        # authentication cookie with its new password.
        user = self.user
        if self == user:
            self.guard.Cookie.updatePassword(self.H(), password)
        message = self.translate('new_password_text',
                                 mapping={'password': password})
        self.say(message, fleeting=False)

    def showResetPassword(self):
        '''Action "reset password" is available on local users only, to
           authorized users only.'''
        # If p_self is the connected user, he has the possibility to choose a
        # new password on his page "Password": consequently, the "reset
        # password" action is not avalable for him.
        if self.source == 'zodb' and self.user != self and \
           self.mayResetPassword() and not self.isSpecial(includeAdmin=False):
            return Show.BS

    resetPassword = Action(action=doResetPassword, show=showResetPassword,
                           confirm=True, label='User', icon='pagePassword.svg',
                           sicon='password.svg', render='icon')

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #                              Hidden fields
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    hidden = {'show': False, 'layouts': 'f', 'label': 'User'}

    # For external users (source != "zodb"), we store the date of the last time
    # the external user and the local copy were synchronized.
    syncDate = Date(format=Date.WITH_HOUR, **hidden)

    # The date of the last login for this user
    lastLoginDate = Date(format=Date.WITH_HOUR, **hidden)

    # We may force a local user (source=zodb) to change its password at next
    # login (ie, for users created by an admin).
    changePasswordAtNextLogin = Boolean(**hidden)

    def getLanguage(self):
        '''Gets the language (code) for p_self'''
        handler = self.H()
        # There may be a forced language defined for everyone
        config = handler.config.ui
        if config.forcedLanguage: return config.forcedLanguage
        # Try to get the value from a cookie. Indeed, if such a cookie is
        # present, it means that the user has explicitly chosen this language
        # via the language selector.
        r = handler.req.AppyLanguage
        if r: return r
        # Try the "Accept-Language" header, which stores language preferences as
        # defined in the user's browser. Several languages can be listed, from
        # most to less wanted.
        r = handler.headers['Accept-Language']
        if not r:
            # Return the first language supported by the app
            return config.languages[0]
        # Browse preferred languages and return the first that is among app
        # language. If no language matches, return the first one as supported by
        # the app.
        #
        # When selectable languages are defined, they will constitute the basis
        # for defining the languages being supported by the running app.
        supported = config.selectableLanguages or config.languages
        for lang in r.split(','):
            # Extract the 2-letter code
            code = None
            i = lang.find('-')
            if i != -1:
                code = lang[:i]
            else:
                i = lang.find(';')
                if i != -1:
                    code = lang[:i]
            code = (code or lang).strip()
            if code in supported:
                # Warn the user that this one has been chosen
                handler.resp.setHeader('Content-Language', code)
                return code
        # No supported language was found among user's preferred languages
        return supported[0]

    #- -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #                                  PXs
    #- -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    # Display, in the user strip, a link to the User instance of the logged user
    pxLink = Px('''
     <!-- The variant with a clickable username -->
     <div if="cfg.userLink" class="textIcon">
       <a if="showUserIcon|True" href=":user.url"><img src=":svg('user')"
          class="icon"/></a>
       <div>
        <a href=":user.url"><span>:cfg.getUserText(user)</span></a>
       </div>
     </div>

     <!-- The variant with the name not being clickable -->
     <span if="not cfg.userLink">:cfg.getUserText(user)</span>''')

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #                              Class methods
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    class System:
        '''Fake class representing the "system" user at places where its
           corresponding User object is not available yet.'''
        login = 'system'
        logins = [login]
        roles = ['Manager', 'Authenticated']
        allowedValue = or_(*roles)

        def getLogins(self, **kwargs): return self.logins
        def getRoles(self, **kwargs): return self.roles
        def getAllowedFrom(self, roles, logins): return self.allowedValue
        def getLanguage(self): return 'en'
        def getInitiator(self): return
        def hasPermission(self, permission, o): return True
        def hasRole(self, role, o=None): return True

    @classmethod
    def identify(class_, guard):
        '''To identify a user means: get its login, password and authentication
           context. There are several places to look for this information: the
           Appy authentication cookie, HTTP authentication, or credentials from
           the login form.'''

        # If no user could be identified, the "anon" user, representing an
        # anonymous user, will nevertheless be identified.
        handler = guard.handler
        req = handler.req
        login = password = ctx = place = None
        # a. Identify the user from the authentication cookie
        try:
            login, password, ctx = guard.Cookie.read(handler)
        except Exception as e:
            handler.log('app', 'error', COOKIE_KO % str(e))
        if login: place = 'cookie'
        # b. Identify the user from HTTP basic authentication
        if not login and 'Authorization' in handler.headers:
            creds = handler.headers['Authorization']
            if creds.lower().startswith('basic '):
                # Decode these credentials from HTTP basic authentication
                creds = base64.decodebytes(creds[6:].encode()).decode()
                login, password = creds.split(':', 1)
                if login: place = 'basic'
        # c. Identify the user from the authentication form. This form is
        #    identified via the presence of key "authInfo".
        if not login and 'authInfo' in req:
            login = req.login
            if login:
                login = handler.config.security.transformLogin(login.strip())
            password = req.password or ''
            ctx = req.context
            if login: place = 'form'
        # d. Identify the user from a SSO reverse proxy
        if not login or login == '_s_s_o_':
            sso = handler.config.security.sso
            if sso:
                login = sso.extractUserLogin(handler)
                if login: place = 'sso'
        # e. If all identification methods failed, identify the user as "anon"
        return login or 'anon', password, ctx, place

    @classmethod
    def authenticate(class_, guard):
        '''Authenticate the currently logged user and return its corresponding
           User instance.'''
        handler = guard.handler
        # Manage a non-HTTP request
        if handler.fake:
            # We are running in a specific context: at HTTP server startup, or
            # by a script. The "system" user, representing the running server
            # himself, must be used and returned. This user, for which a User
            # instance normally exists, may be requested before it is created
            # (on database initialization). This is why we may create here a
            # fake one.
            return handler.getSpecial('system') or User.System()
        # Identify the user
        login, password, ctx, place = User.identify(guard)
        config = guard.config.security
        authContext = config.authContext
        tool = handler.tool
        if place == 'sso':
            # We have found a user already authenticated by a SSO (Single
            # Sign-On) reverse proxy: its credentials were carried in HTTP
            # headers. Simply return its local copy, or create it if not found.
            user = config.sso.getUser(tool, login, createIfNotFound=True)
            if not user:
                # For some reason, SSO user credentials could not be accepted
                handler.log('app', 'error', SSO_USR_KO % login)
                tool.raiseMessage('sso_user_blocked', isLabel=True,
                                  mapping={'login': login})
            # If authentication contexts are in use, retrieve the potentially
            # defined default context when relevant.
            if ctx is None and authContext:
                ctx = authContext.getDefaultContext(tool, user)
                # Update the cookie with this default context
                if ctx: guard.Cookie.update(handler, ctx)
        else:
            # In any other case, authentication must be performed
            user = None
            if place == 'form':
                # A user has typed its login and password from the ui (pxLogin).
                # If a LDAP server is defined, try to find it there.
                if config.ldap:
                    user = config.ldap.getUser(tool, login, password)
            # Get the user from the local database if it was not found yet
            user = user or tool.search1('User', login=login)
            # Authentication fails (and user "anon" is returned) if the user was
            # not found or inactive, its password was invalid or the required
            # authentication context was not found.
            if user is None or user.isAnon() or \
               user.state in config.noLoginStates or \
               not user.getField('password').check(user, password) or \
               (not ctx and authContext and authContext.isMandatory(tool, True)\
                and place != 'basic'):
                # Disable the authentication cookie
                guard.Cookie.disable(handler)
                user = handler.getSpecial('anon')
            else:
                # The user is authenticated. Create an authentication cookie for
                # him. Set a default context when appropriate (v_ctx being None
                # involves searching for a default context, while p_ctx being
                # the empty string means that selecting no context at all was a
                # positive action performed by the user: no default context must
                # be searched in that case).
                if authContext and ctx is None:
                    ctx = authContext.getDefaultContext(tool, user)
                guard.Cookie.write(handler, user.login, password, ctx)
        # Set, on the guard, when present, attributes related to the
        # authentication context.
        if ctx and authContext: authContext._setOnGuard(tool, user, guard, ctx)
        return user

    @classmethod
    def getOnline(class_, tool, expr=None, context=None):
        '''Returns a XHTML table showing users being currently connected'''
        # If p_expr is given, it must be an expression that will be evaluated on
        # every connected user. The user will be part of the result only if the
        # expression evaluates to True. The user is passed to the expression as
        # variable "user".
        # ~
        # Get and count connected users
        users = list(tool.H().onlineUsers.items())
        users.sort(key=lambda u: u[1], reverse=True) # Sort by last access date
        count = len(users)
        # Prepare the expression's context when relevant
        if expr:
            if context is None: context = {}
        # Compute table rows
        rows = []
        for login, access in users:
            user = tool.search1('User', login=login)
            if not user: continue # Could have been deleted in the meanwhile
            if expr:
                # Update the p_expr's context with the current user
                context['user'] = user
                # Evaluate it
                if not eval(expr, context): continue
            rows.append(f'<tr><td><a href="{user.url}">{user.title}</a></td>' \
                        f'<td>{tool.formatDate(access)}</td></tr>')
        # Create an empty row if no user has been found
        if not rows:
            text = tool.translate('no_value')
            rows.append(f'<tr><td colspan="2" align="center">{text}</td></tr>')
            count = 0
        else:
            count = len(rows)
        # Build the entire table
        rows = '\n'.join(rows)
        last = tool.translate('last_user_access')
        return f'<table class="small"><tr><th>({count})</th><th>{last}</th>' \
               f'</tr>{rows}</table>'

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #                             Base methods
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    def onEditEarly(self, o):
        '''(re)-compute p_self's title, computed from other fields'''
        req = self.req
        if req and req.page and req.page != 'main': return
        self.updateTitle()

    def onEdit(self, created):
        '''To do when a user is p_created or updated'''
        # For a freshly created local user, generate him a password (if not
        # already set).
        isLocal = self.source == 'zodb'
        message = None
        if created and isLocal and self.isEmpty('password') and \
           self.config.security.generatePassword:
            # Generate a clear password
            password = self.getField('password').generate()
            # Store it, encrypted
            self.password = password
            recipient = self.getMailRecipient()
            _ = self.translate
            if self.config.mail and recipient:
                # Send the password by mail to the user
                subject = _('first_password')
                map = {'siteUrl': self.siteUrl, 'login': self.login,
                       'password': password}
                body = _('first_password_body', mapping=map, asText=True)
                self.tool.sendMail(recipient, subject, body)
                message = _('first_password_sent')
            else:
                # Return the clear password to the UI
                message = _('new_password_text', mapping={'password': password})
            self.resp.fleetingMessage = False
            # The user will need to change it at next login
            self.changePasswordAtNextLogin = True
        page = self.req.page or 'main'
        if page == 'main':
            login = self.login
            # Ensure correctness of some infos about this user
            if isLocal and self.id == 'admin': self.ensureIsManager()
            # p_self must be owned by itself
            self.localRoles.add(login, 'Owner')
            # If the user was created by anon|system, anon|system can't stay its
            # Owner.
            self.localRoles.delete(('anon', 'system'))
        elif page == 'password':
            # If p_self corresponds to the currently logged user, update the
            # authentication cookie with its new password.
            if self.user == self:
                self.guard.Cookie.updatePassword(self.H(), self.req.password)
            # Reset this flag
            self.changePasswordAtNextLogin = False
        return message

    def mayUpdate(self, includeAdmin=False):
        '''Conditions preventing a user from being edited or deleted'''
        # No one can touch users "system" and "anon" (and also "admin" if
        # includeAdmin is True).
        if self.isSpecial(includeAdmin=includeAdmin): return
        # Non-managers cannot edit managers
        if self.hasRole('Manager') and not self.user.hasRole('Manager'):
            return
        return True

    def mayEdit(self):
        '''Additional conditions preventing a user from being edited'''
        return self.mayUpdate()

    def mayDelete(self):
        '''The condition is similar to m_mayEdit; the only difference is that
           the "admin" user cannot be deleted but can be edited.'''
        return self.mayUpdate(includeAdmin=True)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
