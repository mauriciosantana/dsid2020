from django.urls import path

from .views import TurismoListView, busca_hotel, busca_voo
from . import views


urlpatterns = [
    path('', TurismoListView.as_view(), name='home'),

    path('hotel', views.busca_hotel, name='busca_hotel'),
    path('voo', views.busca_voo, name='busca_voo'),
]
