""" created 27/02/2016
author: marcello
version: 0.1
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main/', views.index, name='main'),
    url(r'^statistics/', views.statistics, name='statistics'),
    url(r'^help/', views.help, name='help'),
    url(r'^contacts/', views.contacts, name='contacts'),
]