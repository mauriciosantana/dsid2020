from django.urls import path,include

from .views import TurismoAPIView, HotelAPIView, VooAPIView


urlpatterns = [
    path('', TurismoAPIView.as_view()),
    path('hotel', HotelAPIView.as_view()),
    path('voo', VooAPIView.as_view()),
]
