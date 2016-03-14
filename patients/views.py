from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.shortcuts import render

from parag.constants import VIP_USERS


def index(request):

    user = request.user
    context = {'user': user,
               'navbar_selected': 'home',
               'vip_users': VIP_USERS,
               }

    return render(request, 'patients/main.html', context)


def statistics(request):
    return render(request, 'patients/statistics.html')

def help(request):
    return render(request, 'patients/help.html')

def contacts(request):
    return render(request, 'patients/contacts.html')

