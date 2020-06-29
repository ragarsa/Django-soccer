from django.urls import path
from .views import GetPlayer, GetPlayers

urlpatterns = [
    path('players/', GetPlayers),
    path('<int:id>', GetPlayer)
]
