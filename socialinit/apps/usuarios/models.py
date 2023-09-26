from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True, null=True)
    document = models.CharField(max_length=50, blank=True, null=True)
    emailVerificado = models.BooleanField(default=False)
    esVerificadoTelefono = models.BooleanField(default=False)    
    def __str__(self) -> str:
        return str(self.document)
    # Agrega cualquier otro campo adicional que necesites aquí
