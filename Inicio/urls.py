from django.urls import path 
from . import views
urlpatterns = [
    path('', views.hola),
    path('about/',views.acercade),
    path('polityka-prywatnosci/',views.privacidad),
    path('menu/',views.menu),
    path('kontakt/',views.contacto),
    path('rezerwacje/',views.reserva, name='reserva'),
    path('o-klubie/',views.acercade),
    path('coming-soon/', coming_soon, name='coming_soon'),


]