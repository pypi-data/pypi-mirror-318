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
from appy import Config
from appy.model.base import Base
from appy.model.user import User
from appy.model.fields import Show
from appy.ui.layout import Layouts
from appy.model.fields.ref import Ref
from appy.model.fields.string import String
from appy.model.workflow import standard as workflows
from appy.model.fields.select import Select, Selection
from appy.model.fields.group import Group as FieldGroup

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Group(Base):
    '''Base class representing a group'''

    workflow = workflows.Owner

    m = {'group': FieldGroup('main', style='grid', hasLabel=False),
         'width': 25, 'indexed': True, 'layouts': Layouts.g, 'label': 'Group'}

    # CSS class to apply to every group title in a list of groups
    styles = {'title': 'titlet'}

    @staticmethod
    def update(class_):
        title = class_.fields['title']
        title.group = Group.m['group']
        title.layouts = Layouts.g

    def showLogin(self):
        '''When must we show the login field ?'''
        return 'edit' if self.isTemp() else Show.TR

    def showGroups(self):
        '''Only the admin can view or edit roles'''
        return self.user.hasRole('Manager')

    def validateLogin(self, login):
        '''Is this p_login valid ?'''
        return True

    login = String(multiplicity=(1,1), show=showLogin,
                   validator=validateLogin, **m)

    # Field allowing to determine which roles are granted to this group

    def selectRoles(self):
        '''Get the selectable roles'''
        return self.model.getGrantableRoles(self, checkManager=True)

    roles = Select(render='checkbox', multiplicity=(0,None),
      validator=Selection(selectRoles,
                  single=lambda o, role: o.translate(f'role_{role}')), **m)

    users = Ref(User, multiplicity=(0,None), add=False, link='popup',
      height=15, back=Ref(attribute='groups', show=User.showRoles,
                          multiplicity=(0,None), label='User',
                          group=User.baseGroup, render='links'),
      showHeaders=True, shownInfo=('title', 'login', 'state*100px|'),
      actionsDisplay='inline', label='Group', group=m['group'])

    def getMailRecipients(self):
        '''Gets the list of mail recipients for every group member'''
        r = []
        for user in self.users:
            recipient = user.getMailRecipient()
            if recipient:
                r.append(recipient)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
