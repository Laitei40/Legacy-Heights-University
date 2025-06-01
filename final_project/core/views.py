from django.shortcuts import render
from django.http import JsonResponse
from .models import State

# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'core/home.html')

def registration(request):
    return render(request, 'accounts/registration.html')

def get_states(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country_id=country_id).values('id', 'name')
    return JsonResponse({'states': list(states)})
