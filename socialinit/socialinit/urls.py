"""
URL configuration for socialinit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from apps.inicio.views import obtenerDatos
from apps.usuarios.views import CustomPasswordSetView

urlpatterns = [
    path("", TemplateView.as_view(template_name='inicio.html'), name='home'),
    path("form/", TemplateView.as_view(template_name='general.html'), name="form_general"),
    path("accounts/google/login/callback", obtenerDatos, name="datos"),
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('allauth.urls')),
    path('u/', include('apps.usuarios.urls')),
    path('a/', include('apps.conjunto.urls')),
    path('accounts/set_password/', CustomPasswordSetView.as_view(), name='account_set_password'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)