from django.db import models
from django.contrib.auth.models import User


class ExtensionUsuario(models.Model):
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    descripcion = models.CharField(max_length = 200, null=True)
    link = models.URLField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
