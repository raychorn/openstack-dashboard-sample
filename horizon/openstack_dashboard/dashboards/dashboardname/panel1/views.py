# vim: tabstop=4 shiftwidth=4 softtabstop=4

#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# @author: Abishek Subramanian, Cisco Systems, Inc.
# @author: Sergey Sudakovich,   Cisco Systems, Inc.

import logging

from django.core import urlresolvers
from django.utils import datastructures
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms
from horizon import tables
from horizon import tabs
from horizon.utils import memoized

from openstack_dashboard import api

LOG = logging.getLogger(__name__)


class DefaultIndexView(tables.DataTableView):
    template_name = 'dashboard/panel1/index.html'

    def get_data(self):
        return []


class IndexTabGroup(tabs.TabGroup):
    slug = "group"
    tabs = (DefaultIndexView,)


class IndexView(tables.MultiTableView):
    template_name = 'dashboard/panel1/index.html'

