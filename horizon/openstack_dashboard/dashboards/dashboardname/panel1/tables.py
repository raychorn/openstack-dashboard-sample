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

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tables

from openstack_dashboard import api

LOG = logging.getLogger(__name__)

class SampleData(tables.DataTable):
    id = tables.Column("id", hidden=True)

    class Meta:
        name = "sample_data"
        verbose_name = _("Sample Data")
