
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='core_index'),
    path('ajax/get_states/', views.get_states, name='get_states'),
]
