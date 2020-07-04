from django.urls import path,include

from .views import TurismoAPIView


urlpatterns = [
    path('', TurismoAPIView.as_view()),
]
