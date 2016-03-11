from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):

    user = request.user
    context = {'user': user,}

    return render(request, 'patients/main.html', context)

