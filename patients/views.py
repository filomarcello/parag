from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.shortcuts import render

from parag.constants import VIP_USERS


class BaseView(TemplateView):
    pass

class MainView(BaseView):
    template_name = 'patients/main.html'

class StatisticsView(BaseView):
    template_name = 'patients/statistics.html'

class HelpView(BaseView):
    template_name = 'patients/help.html'

class ContactsView(BaseView):
    template_name = 'patients/contacts.html'


