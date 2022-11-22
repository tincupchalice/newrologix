from django.contrib import admin
from .models import XymogenProduct, Category, Brand, UnitCount, Flavor, XProductDefaultDosingMap, XProductCategoryMap
# Register your models here.


@admin.register(XymogenProduct)
class XymogenProductAdmin(admin.ModelAdmin):
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


@admin.register(XProductDefaultDosingMap)
class XProductDefaultDosingMapAdmin(admin.ModelAdmin):
    list_display = ('product', 'time', 'qty',)


@admin.register(XProductCategoryMap)
class XProductCategoryMapAdmin(admin.ModelAdmin):
    list_display = ('product', 'category')