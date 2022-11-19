from django.contrib import admin
from .models import XyomgenProduct, Category, Brand, UnitCount, Flavor
# Register your models here.


@admin.register(XyomgenProduct)
class XyomgenProductAdmin(admin.ModelAdmin):
    list_display = ('productName', 'brand', 'descriptionShort',
                    'wholesalePrice', 'retailPrice', 'releaseDate')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)



@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)


@admin.register(UnitCount)
class UnitCountAdmin(admin.ModelAdmin):
    list_display = ('unit_count_name',)


@admin.register(Flavor)
class FlavorAdmin(admin.ModelAdmin):
    list_display = ('flavor_name',)


