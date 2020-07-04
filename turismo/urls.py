from django.urls import path

from .views import TurismoListView


urlpatterns = [
    path('', TurismoListView.as_view(), name='home')

    #path('', views.home, name='home'),
]
