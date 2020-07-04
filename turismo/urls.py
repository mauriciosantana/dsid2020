from django.urls import path

from .views import TurismoListView, hotel, voo
from . import views


urlpatterns = [
    path('', TurismoListView.as_view(), name='home'),

    path('hotel', views.hotel, name='hotel'),
    path('voo', views.voo, name='voo'),
]
