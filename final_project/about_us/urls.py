from django.urls import path
from . import views

urlpatterns = [
    path('', views.aboutus, name='aboutus'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
]