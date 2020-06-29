from django.shortcuts import render
from django import views
from .models import Players
from django.http import HttpResponse
# Create your views here.

def GetPlayers(request):
    players = Players.objects.all()
    template_players = 'players/list.html'
    context = {
        'players':players

    }
    return render(request, template_players, context)


def GetPlayer(request, id):
    player = Players.objects.get(pk=id)
    template_player = "players/detail.html"
    context = {
        'player':player
    }
    return render(request, template_player, context)
    