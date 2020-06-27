from django.shortcuts import render

# Create your views here.
def GetClubs(request):
    clubs = Clubs.objects.all()
    return render (request)