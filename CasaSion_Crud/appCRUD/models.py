from django.db import models

# Create your models here.

class casasAvivamiento(models.Model):
    codCA = models.AutoField(primary_key=True)
    codNom = models.CharField(max_length=40)

    def __str__(self):
        return self.codNom

    
class UsuarioCRUD(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    rut = models.CharField(max_length=12)
    email= models.EmailField()
    direccion = models.CharField(max_length=40)
    comuna= models.CharField(max_length=40) # Poxima actualización a las comunas de santiago region metropolitana
    fecha = models.DateField()
    numero = models.IntegerField()
    codCA = models.ForeignKey(casasAvivamiento, on_delete=models.CASCADE)


