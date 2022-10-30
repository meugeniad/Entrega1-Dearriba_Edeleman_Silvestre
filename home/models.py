from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField

class Destino(models.Model):
    pais = models.CharField(max_length = 50)
    ciudad = models.CharField(max_length = 50)
    informacion = RichTextField(blank=True, null= True)
    sugerido_para = models.CharField(max_length = 200)
    fecha_creacion = models.DateField(auto_now_add=True)
    autor = models.CharField(max_length = 50)
    foto_destino = models.ImageField(upload_to = 'destinos',null=True, blank=True)
    fecha_modificacion =models.DateField(null=True)
    
    def __str__(self):
        return f'País: {self.pais} - Ciudad: {self.ciudad} - Autor: {self.autor} - Fecha creación: {self.fecha_creacion} - Fecha modificación: {self.fecha_modificacion}'
    
    
    
    