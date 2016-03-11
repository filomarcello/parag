""" created 11/03/2016
author: marcello
version: 0.1
"""

from django.contrib.admin.sites import AdminSite
from django.contrib import admin

class NormalUserAdmin(AdminSite):
    pass

centersadmin = NormalUserAdmin(name='centersadmin')
centersadmin.site_header = 'Paraganglioma database'
centersadmin.site_title = centersadmin.site_header

admin.site.site_header = centersadmin.site_header
admin.site.site_title = centersadmin.site_header
