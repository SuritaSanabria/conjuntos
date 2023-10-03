from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils import timezone
class CustomUser(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True, null=True)
    document = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    theme = models.CharField(max_length=20, blank=True, null=True)
    fecact = models.DateField(default=timezone.now())
    emailVerificado = models.BooleanField(default=False)
    esVerificadoTelefono = models.BooleanField(default=False)  
    esResidente =models.BooleanField(default=True)  
    def __str__(self) -> str:
        return str(self.document)
    # Agrega cualquier otro campo adicional que necesites aquí
