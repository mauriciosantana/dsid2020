from django.urls import path

from .views import busca_hotel, busca_voo
from . import views


urlpatterns = [
    path('', views.base, name='base'),

    path('hotel/', views.busca_hotel, name='busca_hotel'),
    path('voo/', views.busca_voo, name='busca_voo'),
]
