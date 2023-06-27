from django.db import models

# Create your models here.

class Usuario(models.Model):
    correo = models.EmailField(max_length=254)
    nombre_usuario = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_usuario

class HumedadReservorio(models.Model):
    valor_h = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Humedad: {self.valor}%"

class AlturaReservorio(models.Model):
    valor_a = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Altura: {self.valor} metros"
    
class Bomba(models.Model):
    tiempo_inicio = models.DateTimeField()
    tiempo_final = models.DateTimeField()

    def __str__(self):
        return f"Bomba - Inicio: {self.tiempo_inicio} / Fin: {self.tiempo_final}"