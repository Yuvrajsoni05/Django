from django.urls import path
from .import views


urlpatterns = [
    path('', views.example_view, name='example_form'),
    path('success/', views.success_view, name='success'),
]