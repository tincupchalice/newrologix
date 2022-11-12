from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_product_list, name='get_product_list'),
]