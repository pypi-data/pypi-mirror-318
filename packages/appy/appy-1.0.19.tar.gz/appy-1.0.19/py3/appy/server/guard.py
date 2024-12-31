'''A guard is responsible for authenticating and authorizing app users, be they
   humans or other apps. A guard will ensure that any action is performed in the
   respect of security rules defined: policy, workflows, permissions, etc.'''

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
from pathlib import Path

from DateTime import DateTime

from appy.px import Px
from appy.utils import multicall
from appy.model.user import User
from appy.server.cookie import Cookie
from appy.utils import path as putils
from appy.model.utils import Object as O
from appy.model.fields.string import String
from appy.model.fields.password import Password

# Errors - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
KO_LOG_TFM  = 'Invalid value "%s" for attribute "loginTransform".'
KO_PERM     = '%s ⛁ %s: « %s » disallowed%s.'
AUTH_KO     = 'Authentication failed with login %s.'
AUTH_OK     = 'Logged in.'
LOGGED_OUT  = 'Logged out.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Config:
    '''Security configuration'''

    # Allowed value for field "loginTransform"
    transformValues = ('lower', 'upper', 'capitalize')

    def __init__(self):
        # Activate or not the button on home page for asking a new password
        self.activateForgotPassword = True
        # During the procedure for generating a new password, a security token
        # is generated. Indicate here, in minutes, this token's validity.
        self.forgotTokenValidity = 2
        # By default, when creating a local user, Appy generates a password for
        # him and tries to send him by email. If you want to disable this and
        # manage yourself, in your app's User.onEdit method, generation and
        # sending of passwords, set the following attribute to False.
        self.generatePassword = True
        # By default, the action for resetting a user's password is available to
        # anyone having write access to the user. If you want to restrict this
        # action to Managers only, set the following attribute to True.
        self.resetPasswordForManagers = False
        # On user log on, you may want to ask them to choose their
        # "authentication context" in a list. Such a context may have any
        # semantics, is coded as a string and will be accessible on the Handler
        # object in attribute "authContext". In order to activate authentication
        # contexts, place here an instance of a sub-class of class
        # appy.server.context.AuthenticationContext. Consult this class'
        # docstring for more information.
        self.authContext = None
        # Allow self-registering ?
        self.selfRegister = False
        # When a login is encoded by the user, a transform can be applied (one
        # among Config.transformValues).
        self.loginTransform = None
        # When the user is in one of the following states, logging in will be
        # blocked.
        self.noLoginStates = ('inactive',)
        # When using a LDAP for authenticating users, place an instance of class
        # appy.server.ldap.Config in the field below.
        self.ldap = None
        # When using, in front of an Appy server, a reverse proxy for
        # authentication for achieving single-sign-on (SSO), place an instance
        # of appy.server.sso.Config in the field below.
        self.sso = None
        # If the following attribute is not None, a warning about accepting
        # cookies will be shown until the user accepts it. His acceptance will
        # be stored in a cookie named "cookiesAccepted". Attribute
        # "cookieWarning" must contain the name of an attribute on the tool,
        # that must store the URL of a page displaying the privacy policy.
        self.cookieWarning = False
        # Who has access to the Python UI console ? In this set, place only
        # logins of users having the Manager role.
        self.consoleUsers = {'admin'}

    def getLdap(self):
        '''Returns the LDAP config if it exists'''
        # The LDAP config can be found either in attribute "ldap" or in the
        # context of a SSO system. This method returns a tuple
        #                     (ldapConfig, context)
        # "context" being None if the global LDAP config is returned, or being
        # the SSO config if the LDAP is the one embedded in the SSO config.
        if self.ldap:
            r = self.ldap, None
        else:
            sso = self.sso
            if not sso or not sso.ldap:
                r = None, None
            else:
                r = sso.ldap, sso
        return r

    def check(self, messages):
        '''Check this config'''
        # Check attribute "loginTransform"
        transform = self.loginTransform
        if transform and (transform not in self.transformValues):
            raise Exception(KO_LOG_TFM % transform)
        return True

    def transformLogin(self, login):
        '''Return p_login as potentially transformed via
           p_self.loginTransform.'''
        return getattr(login, self.loginTransform)() \
               if self.loginTransform else login

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Unauthorized(Exception):
    '''Error that is raised when a security problem is encountered'''

    def __init__(self, text, translated=None):
        # p_text contains technical details about the error
        super().__init__(text)
        # p_translated contains a potentially translated, human-targeted message
        self.translated = translated

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Guard:
    '''Implements security-related functionality'''
    Error = Unauthorized
    Cookie = Cookie
    traverse = {}

    def __init__(self, handler, user=None):
        # The handler that has instantiated this guard
        self.handler = handler
        # Info about the currently selected authentication context
        self.authContext = None
        # A human-readable name for this context
        self.authContextName = None
        # If the authentication context corresponds to a Appy object, the
        # following attribute will get this object once per request and store it
        # here.
        self.authObject = None
        # Unwrap some useful objects
        self.model = handler.server.model
        self.config = handler.server.config
        # Get the current user and store user-related attributes on p_self
        self.initUser(user=user)

    def initUser(self, user=None):
        '''Initialise guard attributes related to the current user'''
        # Authenticate the currently logged user and get its User instance
        if user is None:
            self.user = User.authenticate(self)
        else:
            # If p_user is passed, it is probably the anon user and we are
            # creating some fake guard in order to get a handler being complete.
            self.user = user
        # Remember that this user hits the server now
        handler = self.handler
        if not handler.fake:
            handler.onlineUsers[self.user.login] = DateTime()
        # Cache info about this user
        self.cache()
        # Has the user accepted the cookie warning ?
        if self.config.security.cookieWarning:
            self.cookiesAccepted = handler.req.cookiesAccepted == '1'
        else:
            # We don't care about accepting cookies
            self.cookiesAccepted = True

    def cache(self):
        '''Pre-compute, for performance, heavily requested information about the
           currently logged user.'''
        u = self.user
        self.userLogin = u.login
        self.userLogins = u.getLogins(compute=True, guard=self)
        self.userRoles = u.getRoles(compute=True, guard=self)
        self.userAllowed = u.getAllowedFrom(self.userRoles, self.userLogins)
        self.userLanguage = u.getLanguage() if not self.handler.fake else 'en'

    # In the remaining of this class, when talking about "the user", we mean
    # "the currently logged user".

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                       Security checks on classes
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def mayInstantiate(self, class_, checkInitiator=False, initiator=None,
                       raiseOnError=False):
        '''May the user create instances of p_class_ ?'''
        # This information can be defined on p_class_.python, in static
        # attribute "creators". If this attribute holds...
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # a list    | we consider it to be a list of roles, and we check that
        #           | the user has at least one of those roles;
        # a boolean | we consider that the user can create instances of this
        #           | class if the boolean is True;
        # a method  | we execute the method, and via its result, we fall again
        #           | in one of the above cases.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # If p_class_.python does not define such an attribute, a default list
        # of roles defined in the config will be used.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # An initiator object may dictate his own rules for instance creation
        if checkInitiator:
            # No need to check for an initiator in the context of a root class
            init = initiator or self.user.getInitiator()
            if init and getattr(init.field, 'creators', None):
                return self.user.hasRole(init.field.creators, init.o)
        # Get the Python class defined in the app
        class_ = class_.python
        # Get attribute "creators" on the class, or use the config
        creators = class_.creators if hasattr(class_, 'creators') \
                   else self.config.model.defaultCreators
        # If "creators" is a method, execute it
        if callable(creators): creators = creators(self.handler.tool)
        # Manage the "boolean" case
        if isinstance(creators, bool) or not creators: return creators
        # Manage the "roles" case
        for role in self.userRoles:
            if role in creators:
                return True

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                       Security checks on objects
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def stringInfo(self, info):
        '''Returns this additional p_info about an error, as a string'''
        return '' if info is None else f' ({info.asString()})'

    def allows(self, o, permission='read', raiseError=False, info=None):
        '''Has the user p_permission on p_o ?'''
        r = self.user.hasPermission(permission, o)
        if not r and raiseError:
            # Raise an Unauthorized exception
            s = self.stringInfo(info)
            raise Unauthorized(KO_PERM % (o.class_.name, o.id, permission, s))
        return r

    def mayAct(self, o):
        '''m_mayAct allows to hide the whole set of actions for an p_o(bject).
           Indeed, beyond workflow security, it can be useful to hide controls
           like "edit" icons/buttons. For example, if a user may only edit some
           Ref fields with add=True on an object, when clicking on "edit", he
           will see an empty edit form.'''
        return multicall(o, 'mayAct', True)

    def mayDelete(self, o, perm=True):
        '''May the currently logged user delete this p_o(bject) ?'''
        # Check the base p_perm(ission) if requested. It can be disabled if the
        # caller knows that this permission has already been checked.
        if perm:
            r = self.allows(o, 'delete')
            if not r: return
        # An additional, user-defined condition, may refine the base permission
        return multicall(o, 'mayDelete', True)

    def mayEdit(self, o, permission='write', permOnly='specific',
                raiseError=False, info=None):
        '''May the user edit this object ? p_permission can be a field-specific
           permission. If p_permOnly is True, the additional user-defined
           condition (custom m_mayEdit) is not evaluated. If p_permOnly is
           "specific", this condition is evaluated only if the permission is
           specific (=not "write") If p_raiseError is True, if the user may not
           edit p_o, an error is raised.'''
        # p_info, if passed, represents additional contextual information that
        # will be part of the error message in case p_o's edition can't be
        # performed and p_raiseError is True.
        r = self.allows(o, permission, raiseError=raiseError, info=info)
        if not r: return
        if permOnly == True or \
           (permOnly == 'specific' and permission != 'write'): return r
        # An additional, user-defined condition, may refine the base permission
        r = multicall(o, 'mayEdit', True)
        if not r and raiseError:
            method = f'{o.class_.name}::mayEdit'
            s = self.stringInfo(info)
            raise Unauthorized(KO_PERM % (method, o.id, permission, s))
        return r

    def mayView(self, o, permission='read', raiseError=False, info=None):
        '''May the user view this p_o(bject) ? p_permission can be a field-
           specific permission. If p_raiseError is True, if the user may not
           view p_o, an error is raised.'''
        # Check m_mayEdit hereabove to know what p_info is all about
        r = self.allows(o, permission, raiseError=raiseError, info=info)
        if not r: return
        # An additional, user-defined condition, may refine the base permission
        r = multicall(o, 'mayView', True)
        if not r and raiseError:
            method = f'{o.class_.name}::mayView'
            s = self.stringInfo(info)
            raise Unauthorized(KO_PERM % (method, o.id, permission, s))
        return r

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                              Login / logout
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    traverse['enter'] = True
    def enter(self, tool):
        '''Perform login'''
        user = self.user
        req = tool.req
        handler = tool.H()
        if user.isAnon():
            # Authentication failed
            label = 'login_ko'
            success = False
            login = req.login.strip() if req.login else ''
            msg = AUTH_KO % login
        else:
            # Authentication succeeded
            label = 'login_ok'
            success = True
            msg = AUTH_OK
        # Log the action
        tool.log(msg)
        # Redirect the user to the appropriate page
        if success:
            if user.changePasswordAtNextLogin:
                # Redirect to the page where the user can change its password
                back = f'{user.url}/edit?page=password'
                label = 'login_ok_change_password'
                tool.resp.fleetingMessage = False
            elif req.goto:
                # The user came to its home page for authenticating: he must now
                # be redirected to the page at request key "goto".
                back = req.goto
            else:
                # Redirect to the app's home page
                back = user.tool.computeHomePage()
                info = req.authInfo
                # Carry custom authentication data when appropriate
                if info: back = f'{back}?authInfo={info}'
        else:
            # Stay on the same page
            back = tool.H().headers['Referer']
        # Redirect the user to the appropriate page
        tool.resp.goto(back, message=user.translate(label))

    traverse['leave'] = True
    def leave(self, tool):
        '''Perform logout'''
        handler = tool.H()
        # Disable the authentication cookie
        Cookie.disable(handler)
        # Log the action
        handler.log('app', 'info', LOGGED_OUT)
        # Redirect the user to the app's home page
        back = self.config.server.getUrl(handler)
        handler.resp.goto(back, message=tool.translate('logout_ok'))

    def getLogoutUrl(self, tool, user):
        '''The "logout" URL may not be the standard Appy one if the app is
           behind a SSO reverse proxy.'''
        if user.source == 'sso': return self.config.security.sso.logoutUrl
        return f'{tool.url}/guard/leave'

    def getLoginUrl(self, ctx):
        '''When discreet logins are in use, compute the JS code or link allowing
           to open the login box as a popup or redirect the user to tool/home,
           depending on the config.'''
        if ctx.cfg.discreetLogin == 'home':
            # "discreet" may hold "home" or "homes". Attribue "stay" will force
            # to stay on this page. Indeed, without it, in "discreet login"
            # mode, tool/home[s] redirects to tool/public.
            r = f'{ctx.tool.url}/{ctx.cfg.home}?stay=1'
        else:
            r = 'javascript:toggleLoginBox(true)'
        return r

    def getSelfRegisterJS(self, tool):
        '''Gets the JS code allowing to create a User instance for the purpose
           of self-registering.'''
        # Compute the URL to post the form to
        return f"javascript:post('{tool.url}/new',{{'action':'Create'," \
               f"'className':'User','nav':'ref.tool.users.0.0'}})"

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                         Password reinitialisation
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    traverse['askPasswordReinit'] = True
    def askPasswordReinit(self, tool):
        '''A user (anonymous) does not remember its password. Send him a mail
           containing a link that will trigger password re-initialisation.'''
        login = (tool.req.rlogin or '').strip()
        _ = tool.translate
        # All return messages must not be fleeting
        tool.resp.fleetingMessage = False
        if not login:
            return tool.goto(message=_('missing_login'))
        user = tool.search1('User', login=login)
        message = _('reinit_mail_sent')
        if not user:
            # Return the message nevertheless. This way, malicious users can't
            # deduce information about existing users.
            return tool.goto(message=message)
        # Get the mail recipient for this user
        recipient = user.getMailRecipient()
        if not recipient:
            # Impossible to re-initialise the password
            return tool.goto(message=message)
        # Create a temporary file whose name is the user login and whose
        # content is a generated token.
        token = Password().generate()
        with (putils.getOsTempFolder(asPath=True) / login).open('w') as f:
            f.write(token)
        # Send an email
        urlI = f'{tool.url}/guard/doPasswordReinit?login={login}&token={token}'
        subject = _('reinit_password')
        map = {'url':urlI, 'siteUrl':tool.siteUrl}
        body= _('reinit_password_body', mapping=map, asText=True)
        tool.sendMail(recipient, subject, body)
        return tool.goto(message=message)

    traverse['doPasswordReinit'] = True
    def doPasswordReinit(self, tool):
        '''Performs the password re-initialisation'''
        siteUrl = tool.computeHomePage()
        _ = tool.translate
        # All return messages must not be fleeting
        tool.resp.fleetingMessage = False
        # This can only be triggered by the anonymous user
        if not self.user.isAnon():
            tool.goto(siteUrl, _('for_anon_only'))
            return
        req = tool.req
        login = req.login
        token = req.token
        # Stop if the URL was called with missing parameters
        if not login or not token:
            return tool.goto(siteUrl, _('wrong_password_reinit'))
        # Check if such token exists and is still valid
        tokenFile = putils.getOsTempFolder(asPath=True) / login
        validity = tool.config.security.forgotTokenValidity
        if tokenFile.exists() and putils.isLessThan(tokenFile, validity):
            with tokenFile.open() as f:
                storedToken = f.read()
            if storedToken == token:
                # Authenticate the user and take him to his "change
                # password" page.
                user = tool.search1('User', login=login)
                if user and user.source == 'zodb':
                    # A commit will be required
                    tool.H().commit = True
                    # Generate a new password for this user
                    newPassword = Password().generate()
                    user.password = newPassword
                    user.changePasswordAtNextLogin = True
                    # Simulate an authentication
                    req.authInfo = True
                    req.login = user.login
                    req.password = newPassword
                    user = user.authenticate(self)
                    backUrl = f'{user.url}/edit?page=password'
                    # Delete the token file
                    tokenFile.unlink()
                    return tool.goto(backUrl, _('password_redefine'))
        # If here, something went wrong
        return tool.goto(siteUrl, _('wrong_password_reinit'))

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                                    PXs
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # A custom zone, at the bottom of pxLogin, allowing an app to add custom
    # content.
    pxLoginBottom = Px('')

    def getLoginLogo(self, tool, discreetBox, url):
        '''Returns the possibly clickable logo to include in the login box'''
        # Compute the "img" tag representing the logo
        r = f'<img src="{url("loginLogo")}"/>'
        # Wrap it, when appropriate, in a link allowing to go back to the public
        # or home page.
        if discreetBox:
            r = f'<a onclick="goto(siteUrl)" class="clickable">{r}</a>'
        elif tool.defaultPage and tool.config.ui.discreetLogin == 'home':
            r = f'<a onclick="goto(siteUrl+\'/tool/public\')" ' \
                f'class="clickable">{r}</a>'
        return r

    def getLoginBoxCss(self, discreet):
        '''Get the CSS class(es) for the main login box tag'''
        return 'loginBox boxD' if discreet == True else 'loginBox'

    # The link to open the login box, if we are in "discreet login" mode
    pxLoginLink = Px('''
     <div class="textIcon" id="loginIcon" name="loginIcon"
          var2="loginUrl=guard.getLoginUrl(_ctx_)">
      <a href=":loginUrl">
       <img if="showLoginIcon" src=":svg('login')" class="icon textIcon"/>
      </a>
      <a href=":loginUrl"><span>:_('app_connect')</span></a>
     </div>''')

    # The login form
    pxLogin = Px('''
     <!-- Popup for reinitializing the password -->
     <div if="isAnon and config.security.activateForgotPassword"
          id="askPasswordReinitPopup" class="popup">
      <form id="askPasswordReinitForm" method="post"
            action=":f'{tool.url}/guard/askPasswordReinit'">
       <div align="center">
        <p>:_('app_login')</p>
        <input type="text" size="35" name="rlogin" id="rlogin" value=""
               required="required"/>
        <br/><br/>
        <input type="submit" value=":_('ask_password_reinit')"/>
        <input type="button" onclick="closePopup('askPasswordReinitPopup')"
               value=":_('object_cancel')"/>
       </div>
      </form>
     </div>

     <!-- The login box -->
     <div var="cfg=config.security;
               discreetBox=showLoginBox == 'discreet';
               display='none' if discreetBox and not req.stay else 'block'"
          class=":guard.getLoginBoxCss(discreetBox)"
          style=":f'display:{display}'">

      <!-- Allow to hide the box when relevant -->
      <img if="discreetBox" src=":svg('close')" style="float:right"
           onclick="toggleLoginBox(false)" class="clickable iconXS"/>

      <!-- A (possibly clickable) logo -->
      <div align="center">::guard.getLoginLogo(tool, discreetBox, url)</div>

      <h1>::_('app_name')</h1>
      <center class="sub">:_('please_connect')</center>
      <div class="loginSpace"></div>
      <form id="loginForm" name="loginForm" method="post" class="login"
            action=":f'{tool.url}/guard/enter'">

       <!-- Login fields  -->
       <center><input type="text" name="login" id="login" value=""
                placeholder=":_('app_login')" autofocus="autofocus"
                required="required"/></center>

       <center><input type="password" name="password" id="password"
                placeholder=":_('app_password')" required="required"/></center>

       <!-- The authentication context -->
       <x var="ctx=cfg.authContext"
          if="ctx and ctx.chooseOnLogin">:ctx.pxOnLogin</x>

       <!-- Additional authentication data to carry -->
       <input type="hidden" name="authInfo" id="authInfo"
              value=":req.authInfo or ''"/>

       <!-- Must we go to some page after login ? -->
       <input type="hidden" name="goto" value=":req.goto or ''"/>

       <!-- The "submit" button -->
       <div class="submitLogin">
         <input type="submit" name="submit" var="label=_('app_connect')"
                value=":label" alt=":label"/></div>

       <!-- Forgot password ? -->
       <div class="lostPassword" if="cfg.activateForgotPassword">
         <a class="clickable"
         onclick="openPopup('askPasswordReinitPopup')">:_('forgot_password')</a>
       </div>

       <!-- Link to self-registration -->
       <div if="cfg.selfRegister" class="autoRegister">
        <span style="padding-right: 10px">:_('want_register')</span>
          <a style="font-size: 90%" class="clickable"
             onclick=":guard.getSelfRegisterJS(tool)">:_('app_register')</a>
       </div>
      </form>

      <!-- Custom zone -->
      <x>:guard.pxLoginBottom</x>
     </div>''',

     css='''
      .loginBox {
         border:|loginBorder| |loginColorPh|; padding:|loginBoxPadding|;
         color:|loginColor|; background-color:|boxBgColor|; position:absolute;
         top:|loginTop|; left:50%; z-index:10; transform:translate(-50%,-50%);
         box-shadow:|loginShadow|; border-radius: |loginBorderRadius|
      }
      .boxD { border:|loginBorderD| |loginColorPh|; top:|loginTopD|;
              box-shadow:|loginShadowD| }
      .loginBox a, .loginBox a:visited {
        font-weight:bold; letter-spacing:1px; color:|loginColor| }
      .loginBox h1 {
         padding-bottom:0; margin:|loginTitleMargin|; text-align:center;
         font-size:|loginTitleSize|; font-weight:|loginTitleWeight|;
         text-transform:|loginTitleTransform| }
      .loginBox .sub { font-size:120% }
      #loginForm input {
        background-color:|loginBgColor|; width:|loginWidth|; border:none;
        padding:|loginPadding|; margin:|loginMargin|; color:|loginColor|;
        border-radius:|loginRadius|; font-size:|loginInputSize| }
      .submitLogin { text-align:|submitAlign| }
      #loginForm input[type=submit] {
        color:|submitColor|; width:|submitWidth|; height:|submitHeight|;
        background:|submitBgColor| |submitBgUrl| no-repeat center left;
        border-radius:|submitBgRadius|; font-weight:|submitWeight|;
        margin-top:|submitTop|; text-transform:uppercase;
        padding:|submitPadding|
      }
      .lostPassword { padding:10px 0; font-size:80%; text-align:|loginAlign| }
      .autoRegister { text-align:|loginAlign| }

      /* Placeholder color for the login form */
      .loginBox ::placeholder { color:|loginColorPh|;
        font-weight:|loginWeightPh|; text-transform:|loginTransformPh| }
      .loginSpace { height:35px }
      #rlogin { color:|popupColor| }
     ''')

    # Warning about using cookies  - - - - - - - - - - - - - - - - - - - - - - -

    pxWarnCookies = Px('''
     <div class="cookieWarn">
      <div>
       <x>:_('cookie_warn')</x>
       <a href=":getattr(tool, config.security.cookieWarning)">:_('cookie_read')
       </a>
       <input type="button" value=":_('cookie_accept')"
              onclick="setAcceptCookie(this)"/>
      </div>
     </div>''',

    css='''
      .cookieWarn { background-color:lightgrey; width:100%; position:absolute;
                    bottom:0; font-size:90%; z-index: 100 }
      .cookieWarn div { padding: 7px 15px }
      .cookieWarn a { margin: 0 10px; text-decoration: underline }
      .cookieWarn input { display:inline; background-color:#b5b5b5 }''',

    js='''
      function setAcceptCookie(button) {
        createCookie('cookiesAccepted', '1');
        button.parentNode.parentNode.style.display = 'none';
      }'''
    )
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
