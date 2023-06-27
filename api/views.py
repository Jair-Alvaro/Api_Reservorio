from rest_framework.views import APIView
from rest_framework import viewsets

from .models import * 
from .serializers import * 

class UsuarioDetailView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class HumedadReservorioDetailView(viewsets.ModelViewSet):
    queryset = HumedadReservorio.objects.all()
    serializer_class = HumedadReservorioSerializer

class AlturaReservorioDetailView(viewsets.ModelViewSet):
    queryset = AlturaReservorio.objects.all()
    serializer_class = AlturaReservorioSerializer

class BombaDetailView(viewsets.ModelViewSet):
    queryset = Bomba.objects.all()
    serializer_class = BombaSerializer