from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount

def obtenerDatos(request):
    # Verifica si el usuario está autenticado a través de Google
    if request.user.is_authenticated and request.user.socialaccount_set.filter(provider='google').exists():
        # Obtiene la cuenta de Google del usuario
        google_account = SocialAccount.objects.get(user=request.user, provider='google')

        # Obtiene los datos que deseas
        nombre = google_account.extra_data.get('given_name')
        apellido = google_account.extra_data.get('family_name')
        correo = google_account.extra_data.get('email')

        # Puedes realizar otras acciones con los datos aquí, como guardarlos en el modelo de usuario

        # Renderiza una plantilla con los datos o realiza otras acciones
        return render(request, 'inicio/datos.html', {'nombre': nombre, 'apellido': apellido, 'correo': correo})

    # Si el usuario no está autenticado a través de Google, redirige a otra página o realiza otras acciones
    return render(request, '/')
