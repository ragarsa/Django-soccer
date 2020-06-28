from django.urls import path 
from .views import GetClubs, GetClub


urlpatterns = [
    path('', GetClubs),
    path('<int:id>', GetClub)


]