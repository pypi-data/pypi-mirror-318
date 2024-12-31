'''Module managing database locks set on object pages'''

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
from DateTime import DateTime
from persistent.mapping import PersistentMapping

from appy.px import Px

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
LOCKED_O = 'This page was locked by someone else.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Lock:
    '''A lock is a database structure remembering which user (login) has locked
      which page on which object.'''

    # Locks on a given database object are implemented as a dict object.locks of
    # the form
    #
    #              ~{s_page: (s_userLogin, DateTime_lockDate)}~
    #

    @classmethod
    def hasOn(class_, o, page=None, ignoreMine=True, lockInfo=False,
              formatted=True):
        '''Is a lock currently set on p_o ?'''
        # If a p_page is passed, the method returns True if this specific page
        # is locked. Else, it returns True if at least one lock is found on at
        # least one page on p_o.
        #
        # If p_ignoreMine is True, the locks belonging to the current user are
        # ignored. While this may seem to have sense from the UI point of view
        # (if the page is locked by myself, I don't care about the lock), this
        # is also a technical requirement, because auto-locks may pose problems
        # when transitions are triggered programmatically. Let's take an
        # example. Suppose some object is created from the UI, and, in its
        # "onEdit" method, a transition is automatically triggered. At this
        # time, the lock on the object has not been cleaned yet by the framework
        # and an error is raised.
        #
        # If p_lockInfo is True, when the method should return True, it returns,
        # instead, the locker login and date, for the first encountered relevant
        # lock, as a string if p_formatted is True, as a tuple else, of the form
        #
        #                   (s_login, DateTime_lockDate)
        #
        locks = getattr(o, 'locks', None)
        if not locks: return
        # Return True if at least one not expired lock is found
        userLogin = o.user.login
        now = DateTime()
        expires = o.config.database.lockExpires
        for aPage, info in locks.items():
            # Ignore inappropriate locks
            if page and aPage != page: continue
            # Unwrap lock info
            login, date = info
            # Ignore my own locks if requested
            if ignoreMine and login == userLogin:
                continue
            # Ignore the lock if he has expired
            if (now - date) >= expires:
                continue
            # If we are here, a relevant lock has been found
            if not lockInfo:
                r = True
            elif formatted:
                r = f'{login}::{o.tool.formatDate(date)}'
            else:
                r = (login, date)
            return r

    @classmethod
    def isSet(class_, o, page):
        '''Is this p_page locked on p_o ?'''
        # If the page is locked by the current user or if the lock has expired,
        # we don't mind and consider the page as unlocked. If the page is
        # locked, this method returns the tuple (login, lockDate).
        #
        # m_isSet is a shorthand for m_hasOn with a specific set of attributes.
        return class_.hasOn(o, page=page, lockInfo=True, formatted=False)

    @classmethod
    def set(class_, o, page=None, field=None):
        '''The current user edits a given p_page on p_o: set a lock, to prevent
           other users to edit this page at the same time.'''
        # When setting a lock from a field being inline-edited, p_page is not
        # given and p_field is given instead. In that case, the page will be
        # retrieved from the field, but the lock will not be set if the field is
        # not persistent or whose persistence is managed by a specific method.
        if field and (not field.persist or callable(field.persist)): return
        # This operation requires a database commit
        o.H().commit = True
        # If it does not exist yet, create, on p_o, the persistent mapping that
        # will store the lock.
        page = page or field.page.name
        if not hasattr(o, 'locks'):
            # ~{s_page: (s_userLogin, DateTime_lockDate)}~
            o.locks = PersistentMapping()
        else:
            # Raise an error is the page is already locked by someone else. If
            # the page is already locked by the same user, we don't mind: he
            # could have used its browser's back / forward buttons...
            info = class_.isSet(o, page)
            if info:
                login, date = info
                locker = o.search1('User', login=login)
                maP = {'user': locker.getTitle(),
                       'date': o.tool.formatDate(date)}
                o.raiseUnauthorized(o.translate('page_locked', mapping=maP))
        # Set the lock
        o.locks[page] = (o.user.login, DateTime())

    @classmethod
    def remove(class_, o, page=None, field=None, force=False):
        '''Removes the lock on p_o's p_page. This happens:
           - after the page has been saved: the lock must be released;
           - when an admin wants to force the deletion of a lock that was left
             on p_page for too long (p_force=True).
        '''
        # When removing a lock from a field being inline-edited, p_page is not
        # given and p_field is given instead.
        page = page or field.page.name
        locks = getattr(o, 'locks', None)
        if not locks or (page not in locks): return
        # If there is a custom persistence for p_field, the lock was not set
        if field and (not field.persist or callable(field.persist)): return
        # Raise an error if the user saving changes is not the one that has
        # locked the page (excepted if p_force is True).
        if not force:
            login = o.user.login
            if locks[page][0] != login:
                o.raiseUnauthorized(LOCKED_O)
        # Remove the lock
        del(locks[page])
        # This requires a database commit
        o.H().commit = True

    @classmethod
    def removeMine(class_, o, user, page):
        '''If p_user has set a lock on p_page, this method removes it. This
           method is called when the user that locked a page consults PX "view"
           for this page. In this case, we consider that the user has left the
           edit page in an unexpected way and we remove the lock.'''
        if hasattr(o, 'locks') and (page in o.locks) and \
           (user.login == o.locks[page][0]):
            del(o.locks[page])

    @classmethod
    def getLockers(class_, o, names=False, sep=None):
        '''Returns the logins (or names if p_names is True) of the users having
           locked at least on page on p_o. The p_result is a list, excepted
           if p_sep is given: in that case, it is a string, joined via p_sep.'''
        r = set()
        if hasattr(o, 'locks'):
            for login, date in o.locks.values():
                r.add(login)
        if not names: return r
        r = [o.search1('User', login=login).getTitle() for login in r]
        return sep.join(r) if sep else r

    @classmethod
    def unlockableBy(class_, o, user):
        '''May the currently logged p_user unlock p_o ?'''
        for role in o.config.database.unlockers:
            if isinstance(role, str):
                condition = user.hasRole(role)
            else:
                if role.local:
                    condition = user.hasRole(role.name, o)
                else:
                    condition = user.hasRole(role.name)
            if condition:
                return True

    @classmethod
    def unlock(class_, handler):
        '''Called when the logged user wants to remove a lock that was left for
           too long by some user.'''
        req = handler.req
        o = handler.tool.getObject(req.objectId)
        Lock.remove(o, req.page, force=True)
        handler.resp.goto(message=o.translate('action_done'))

    # Shows icons instead of the "edit" icon/button when a lock is defined
    px = Px('''
     <a if="editable and locked">
      <img class=":'help ' + lockStyle"
       var="unlock=o.Lock.unlockableBy(o, user);
            lockDate=tool.Date.format(tool, locked[1]);
            lockMap={'user':user.getTitleFromLogin(locked[0]),'date':lockDate};
            lockMsg=_('page_locked', mapping=lockMap);
            lockTxt='%s %s' % (lockMsg,_('page_unlock')) if unlock else lockMsg"
       src=":svg('locked')" title=":lockTxt"
       onclick=":'onUnlockPage(%s,%s)' % (q(o.url),q(page)) if unlock else ''"/>
     </a>''')
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
