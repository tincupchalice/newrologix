from django.contrib import admin
from .models import Client
# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_company', 'client_city', 'client_state',
                    'client_doctor', 'client_contact1', 'client_phone')
