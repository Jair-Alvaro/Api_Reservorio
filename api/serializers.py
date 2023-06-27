from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class HumedadReservorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumedadReservorio
        fields = '__all__'        

class AlturaReservorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlturaReservorio
        fields = '__all__' 

class BombaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bomba
        fields = '__all__' 