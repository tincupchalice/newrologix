from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sample_analytics/', views.sample_analytics, name='sample_analytics'),
]
