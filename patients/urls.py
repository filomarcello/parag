""" created 27/02/2016
author: marcello
version: 0.1
"""

from django.conf.urls import url
from patients.views import MainView, StatisticsView, HelpView, ContactsView

urlpatterns = [
    url(r'^main/', MainView.as_view(), name='main'),
    url(r'^statistics/', StatisticsView.as_view(), name='statistics'),
    url(r'^help/', HelpView.as_view(), name='help'),
    url(r'^contacts/', ContactsView.as_view(), name='contacts'),
]