from django.contrib import admin
from .models import ShopifyApi, XymogenApi


@admin.register(ShopifyApi)
class ShopifyApiAdmin(admin.ModelAdmin):
    list_display = ('environment', 'base_url',)


@admin.register(XymogenApi)
class ShopifyApiAdmin(admin.ModelAdmin):
    list_display = ('username', 'environment', 'base_url',)