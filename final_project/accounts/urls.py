from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='accounts_index'),
    path('registration/', views.registration, name='registration'),
    path('signup/', views.signup, name='signup'),
    path('staff_signup/', views.staff_signup, name='staff_signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('ajax/get_states/', views.get_states, name='get_states'),
]