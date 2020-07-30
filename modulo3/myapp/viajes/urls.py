from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<nombre>/', views.bio, name='bio'),
    path('/prueba', views.index, name='index'),
    path('/otra', views.index, name='index'),
]
