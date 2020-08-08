from django.urls import path, include

from . import views as otra

from django.contrib.auth.decorators import login_required, permission_required

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'personas', otra.PersonaViewSet)

urlpatterns = [
    path('', otra.index, name='index'),
    path('viaje/<nombre>/', otra.bio, name='bio'),
    path('persona', otra.forma_viaje, name='persona'),
    path('personas', otra.PersonaLista.as_view()),
    path('login', otra.login, name='login'),
    path('logout', otra.logout, name='logout'),
    path('vista', otra.Vista.as_view(), name="vista"),
    path('api/', include(router.urls)),
    #path('api/snippets/', otra.personas_list)
    #path('api/prueba', views.jaja, name="jaja")
]
