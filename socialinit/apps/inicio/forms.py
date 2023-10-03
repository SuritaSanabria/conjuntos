from allauth.account.forms import SignupForm
from django import forms
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from apps.usuarios.models import CustomUser

import datetime

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    telefono = forms.CharField(max_length=15, required=False, label='Telefono')
    document = forms.CharField(max_length=50, required=False, label='Documento')
    direccion = forms.CharField(max_length=30, label='Direccion', required=True)
    esResidente = forms.BooleanField()
    
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        # Excluir el campo 'username' del formulario
        del self.fields['username']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        

        # Verificar si el correo ya está en uso
        if CustomUser.objects.filter(email=email).exists():
            social_account = SocialAccount.objects.filter(extra_data__contains={'email': email})
            if social_account.exists():
                social_account = social_account.first()
                extra_data = social_account.extra_data

            # Verificar si el documento ya está en uso en las cuentas de Google
            document = self.cleaned_data.get('document')
            if document and extra_data.get('email') == document:
                raise forms.ValidationError('Este documento ya está registrado con una cuenta de Google.')

            raise forms.ValidationError('Este correo electrónico ya está registrado con una cuenta de Google. Inicia Sesión con Google o Ingresa con tu correo y contraseña')

        # Obtener la cuenta de Google asociada a este formulario
        social_account = SocialAccount.objects.filter(extra_data__contains={'email': email})
        if social_account.exists():
            social_account = social_account.first()
            extra_data = social_account.extra_data

            # Verificar si el documento ya está en uso en las cuentas de Google
            document = self.cleaned_data.get('document')
            if document and extra_data.get('email') == document:
                raise forms.ValidationError('Este documento ya está registrado con una cuenta de Google.')

        return email

    def clean(self ):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        document = cleaned_data.get('document')

        # Verificar si el correo ya está en uso
        social_account = SocialAccount.objects.filter(extra_data__contains={'email': email})
        if social_account.exists():
            social_account = social_account.first()
            extra_data = social_account.extra_data

            # Verificar si el documento ya está en uso en las cuentas de Google
            if document and extra_data.get('email') == document:
                raise forms.ValidationError('Este documento ya está registrado con una cuenta de Google.')

        return cleaned_data                     

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.telefono = self.cleaned_data.get('telefono')
        user.document = self.cleaned_data.get('document')
        user.direccion = self.cleaned_data.get('direccion')
        user.esResidente = self.cleaned_data.get('esResidente')
        user.fecact = datetime.datetime.now()
        user.save()
        return user
