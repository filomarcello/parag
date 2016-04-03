from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth import logout


class BaseView(LoginRequiredMixin, TemplateView):

    login_url = '/login/'

    def dispatch(self, *args, **kwargs):
        return super(BaseView, self).dispatch(*args, **kwargs)

class MainView(BaseView):
    template_name = 'patients/main.html'

class StatisticsView(BaseView):
    template_name = 'patients/statistics.html'

class HelpView(BaseView):
    template_name = 'patients/help.html'

class ContactsView(BaseView):
    template_name = 'patients/contacts.html'

class LogoutView(BaseView):
    pass


