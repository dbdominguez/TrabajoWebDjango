from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registrase_wiki/', views.registrase_wiki, name='registrase_wiki'),
    path('recuperarcontra/', views.recuperarcontra, name='recuperarcontra'),
    path('micuentatf/', views.micuentatf, name='micuentatf'),
    path('menuprincipal_wiki/', views.menuprincipal_wiki, name='menuprincipal_wiki'),
    path('Lugarestf/', views.Lugarestf, name='Lugarestf'),
    path('Logros/', views.Logros, name='Logros'),
    path('inicio_sesion_wiki/', views.inicio_sesion_wiki, name='inicio_sesion_wiki'),
    path('historia/', views.historia, name='historia'),
    path('forowiki/', views.forowiki, name='forowiki'),
    path('Flora/', views.Flora, name='Flora'),
    path('Enemigos/', views.Enemigos, name='Enemigos'),
    path('Consumibles/', views.Consumibles, name='Consumibles'),
    path('Construcciones/', views.Construcciones, name='Construcciones'),
    path('Armas/', views.Armas, name='Armas'),
    path('Animales/', views.Animales, name='Animales'),
]