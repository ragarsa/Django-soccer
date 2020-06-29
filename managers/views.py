from django.shortcuts import render
from django import views
from .models import Managers
from django.http import HttpResponse
# Create your views here.

def GetManagers(request):
    managers = Managers.objects.all()
    template_players = 'managers/list.html'
    context = {
        'managers':managers

    }
    return render(request, template_players, context)


def GetManager(request, id):
    manager = Managers.objects.get(pk=id)
    template_manager = "managers/detail.html"
    context = {
        'manager':manager
    }
    return render(request, template_manager, context)
    