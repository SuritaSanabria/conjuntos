from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'telefono', 'is_active', 'is_staff','document')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'document')

# Personaliza los campos que deseas mostrar en la lista y en la búsqueda.
admin.site.register(CustomUser, CustomUserAdmin)
