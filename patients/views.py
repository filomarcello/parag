from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from patients.models import Patient

class BaseView(LoginRequiredMixin, TemplateView):

    login_url = '/login/'

    def dispatch(self, *args, **kwargs):
        return super(BaseView, self).dispatch(*args, **kwargs)

class MainView(BaseView):
    template_name = 'patients/main.html'

class StatisticsView(BaseView):
    template_name = 'patients/statistics.html'

    def get_context_data(self, **kwargs):
        context = super(StatisticsView, self).get_context_data(**kwargs)
        # TODO: get values for charts
        queryset = Patient.objects.all()

        context['n_mal'] = len(queryset.filter(sesso='M'))
        context['n_fem'] = len(queryset.filter(sesso='F'))


        return context

class HelpView(BaseView):
    template_name = 'patients/help.html'

class ContactsView(BaseView):
    template_name = 'patients/contacts.html'

class LogoutView(BaseView):
    pass


