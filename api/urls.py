from rest_framework.routers import DefaultRouter
from django.urls import path,include

from . import views

route = DefaultRouter()

route.register(r'usuario', views.UsuarioDetailView,basename= 'usuario')
route.register(r'humedad', views.HumedadReservorioDetailView, basename='humedad')
route.register(r'altura', views.AlturaReservorioDetailView, basename='altura')
route.register(r'bomba', views.BombaDetailView, basename='bomba')


urlpatterns = [
        path('api/', include(route.urls))
]