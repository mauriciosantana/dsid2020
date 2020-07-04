from django.urls import path

from .views import TurismoListView, busca
from . import views


urlpatterns = [
    path('', TurismoListView.as_view(), name='home'),

    path('busca', views.busca, name='busca'),
    #path('', views.home, name='home'),
]
