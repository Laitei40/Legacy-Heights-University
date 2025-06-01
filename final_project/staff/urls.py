
from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_index, name='staff_index'),
    path('<int:pk>/', views.staff_detail, name='staff_detail'),
]
