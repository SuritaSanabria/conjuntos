from django import forms
from django.contrib.auth.forms import UserCreationForm  # Importa UserCreationForm
from .models import CustomUser  # Importa el modelo CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'telefono', 'document']  # Lista los campos que deseas incluir en el formulario

class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'telefono', 'document']

class TelefonoForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # Especifica el modelo al que pertenece el formulario
        fields = ['telefono']  # Lista los campos que deseas incluir en el formulario

    def __init__(self, *args, **kwargs):
        super(TelefonoForm, self).__init__(*args, **kwargs)
        self.fields['telefono'].label = 'Número de Teléfono'  # Personaliza la etiqueta del campo de teléfono

# class ContrasenaForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser  # Especifica el modelo al que pertenece el formulario
#         fields = ['password1', 'password2']  # Lista los campos que deseas incluir en el formulario

