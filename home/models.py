from django.db import models

# Create your models here.
class Destino(models.Model):
    pais = models.CharField(max_length = 50)
    ciudad = models.CharField(max_length = 50)
    informacion =  models.TextField()
    sugerido_para = models.CharField(max_length = 200)
    fecha_creacion = models.DateField()
    autor = models.CharField(max_length = 50)