from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_product_list/', views.get_product_list, name='get_product_list'),
]
