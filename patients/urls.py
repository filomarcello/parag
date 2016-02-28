""" created 27/02/2016
author: marcello
version: 0.1
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]