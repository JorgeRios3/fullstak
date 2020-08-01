from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('viaje/<nombre>/', views.bio, name='bio'),
    path('persona/', views.forma_viaje, name='bio'),
    path('personas/', views.PersonaLista.as_view())
]
