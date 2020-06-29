from django.urls import path
from .views import GetManagers, GetManager

urlpatterns = [
    path('managers/', GetManagers),
    path('<int:id>', GetManager)
]
