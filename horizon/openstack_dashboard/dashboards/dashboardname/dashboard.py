# vim: tabstop=4 shiftwidth=4 softtabstop=4

# @author: Ray C Horn, AT&T

from django.utils.translation import ugettext_lazy as _

import horizon

class Panels(horizon.PanelGroup):
    slug = "panels"
    name = _("Panels")
    panels = ('panel1',)

class DashboardName(horizon.Dashboard):
    name = _("DashboardName")
    slug = "DashboardName"
    panels = (Panels,)
    default_panel = 'panel1'
    permissions = ('openstack.roles.admin',)

horizon.register(DashboardName)
