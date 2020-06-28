from django.shortcuts import render
from django import views
from .models import Clubs
from django.http import HttpResponse

# Create your views here.
def GetClubs(request):
    clubs = Clubs.objects.all()
    template_clubs = 'clubs/list.html'
    context = {
        'clubs':clubs

    }
    return render(request, template_clubs, context)


def GetClub(request, id):
    club = Clubs.objects.get(pk=id)
    template_club = "clubs/detail.html"
    context = {
        'club':club
    }
    return render(request, template_club, context)
    



