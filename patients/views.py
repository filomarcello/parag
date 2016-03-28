from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class BaseView(TemplateView):

    @method_decorator(staff_member_required)
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


