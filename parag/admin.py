""" created 11/03/2016
author: marcello
version: 0.1
"""

from django.contrib.admin.sites import AdminSite

class NormalUserAdmin(AdminSite):
    pass

centersadmin = NormalUserAdmin(name='centersadmin')