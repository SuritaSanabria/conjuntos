from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect

from django.core import signing
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.urls import reverse
from django.template.loader import render_to_string

from apps.usuarios.models import CustomUser
from .forms import CustomUserForm, CustomUserRegistrationForm
from .forms import TelefonoForm
from allauth.account.views import PasswordSetView


# class customSingUp(SignupView):

def crear_usuario(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirige a la página de éxito después de crear el usuario
    else:
        form = CustomUserRegistrationForm()

    return render(request, 'users/formularioRegistro.html', {'form': form})



def agregar_telefono(request, user_id):
    # Obtén el usuario existente si se proporciona un ID
    if user_id:
        user = get_object_or_404(CustomUser, pk=user_id)

    if request.method == 'POST':
        form = TelefonoForm(request.POST, instance=user)
        if form.is_valid():
            # Guarda los datos del usuario en la base de datos
            form.save()
            return redirect('verificartlf', user_id=user.id) # Reemplaza 'página_de_éxito' con la URL correcta
    else:
        form = TelefonoForm(instance=user)

    return render(request, 'users/anadirtelefono.html', {'form': form})


class CustomPasswordSetView(PasswordSetView):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.has_usable_password():
            # El usuario ya tiene una contraseña configurada, redirige al home.
            return redirect('/')  # Reemplaza 'home' con la URL de tu página de inicio.
        return super().dispatch(request, *args, **kwargs)

def verificarTelefono(request,user_id):
    if request.method == 'POST':
        # Procesar el formulario aquí
        # ...
        usuario = CustomUser.objects.get(id=user_id)
        if usuario.esVerificadoTelefono ==False:
            usuario.esVerificadoTelefono=True
            usuario.save()
        return redirect('home')  # Reemplaza 'home' con el nombre de la vista de inicio
    else:
        # Manejar la lógica cuando se carga la página (GET request)
        # ...

        return render(request, 'users/verificaTelefono.html')
    
    
def generar_y_enviar_token(email):
    token = signing.dumps(email, salt=settings.SECRET_KEY)
    token_url = reverse('verificar_exito', args=[token])

    subject = 'Verifica tu correo'
    message = f'Por favor, haz clic en el siguiente enlace para verificar tu correo: {settings.BASE_URL}{token_url}'
    from_email = 'suritayeifre@gmail.com'  
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)

    return token
def verificar_exito(request, token):
    try:
        # Desencripta el token para obtener el correo electrónico
        email = signing.loads(token, salt=settings.SECRET_KEY, max_age=settings.EMAIL_VERIFICATION_TIMEOUT)

        # Verifica si el usuario con ese correo existe
        usuario = CustomUser.objects.get(email=email)

        # Si el usuario existe y su correo no está verificado, actualiza el valor de correo_verificado a True
        if not usuario.emailVerificado:
            usuario.emailVerificado = True
            usuario.save()

        # Realiza cualquier acción de verificación adicional aquí
        # Por ejemplo, puedes cambiar el estado de verificación del usuario en la base de datos.

        # Redirige o muestra un mensaje de éxito
        return render(request, 'verificacion_exitosa.html')
    except signing.BadSignature:
        # El token es inválido o ha caducado
        return HttpResponseNotFound('Token inválido o ha caducado')

def verificarCorreo(request, user_id):
    usuario = get_object_or_404(CustomUser, pk=user_id)
    email = usuario.email
    if request.method == 'POST':
        
        token = generar_y_enviar_token(email)  # Genera el token si es necesario

    return render(request, 'users/verificarcorreo.html', {'user_id': user_id, 'correo':email})


def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(CustomUser, pk=usuario_id)

    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            # Redirige a donde quieras después de guardar los cambios
            return redirect('nombre_de_la_vista')
    else:
        form = CustomUserForm(instance=usuario)

    return render(request, 'editar_usuario.html', {'form': form})
