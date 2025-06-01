from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from core.models import Country, State, Course
from django.http import JsonResponse
from .models import PendingStudent

def index(request):
    return render(request, 'accounts/account.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        country_id = request.POST.get('country')
        state_id = request.POST.get('state')
        course_id = request.POST.get('course')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('registration')

        # Save to PendingStudent for review
        PendingStudent.objects.create(
            name=name,
            contact=contact,
            country_id=country_id,
            state_id=state_id,
            course_id=course_id,
            password=password,  # Store hashed if possible!
        )
        messages.success(request, "Registration submitted for review. You will be notified after approval.")
        return redirect('registration')
    return redirect('registration')

def login_view(request):
    if request.method == 'POST':
        uid = request.POST.get('login_uid')
        password = request.POST.get('login_password')
        user = authenticate(request, username=uid, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('accounts_index')
        else:
            messages.error(request, "Invalid UID or password.")
    # For GET requests, render the login page
    return render(request, 'accounts/sign.html')

def registration(request):
    from core.models import Country, Course
    countries = Country.objects.all()
    courses = Course.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        uid = request.POST.get('uid')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('registration')

        if User.objects.filter(username=uid).exists():
            messages.error(request, "UID already exists.")
            return redirect('registration')

        user = User.objects.create_user(username=uid, password=password, first_name=name, email=contact)
        user.save()
        messages.success(request, "Registration successful. You can now log in.")
        return redirect('registration')

    return render(request, 'accounts/registration.html', {
        'countries': countries,
        'courses': courses,
    })

def staff_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        staff_id = request.POST.get('staff_id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Basic validation
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('registration')

        if User.objects.filter(username=staff_id).exists():
            messages.error(request, "Staff ID already exists.")
            return redirect('registration')

        # Create user (you may want to use a custom Staff model for more fields)
        user = User.objects.create_user(username=staff_id, password=password, first_name=name, email=email)
        user.save()
        messages.success(request, "Staff registration successful. You can now log in.")
        return redirect('registration')
    return redirect('registration')

def custom_logout(request):
    logout(request)
    # Clear all messages
    list(messages.get_messages(request))
    # Set a new logout message
    messages.success(request, "You have been logged out.")
    return redirect('login')

def get_states(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country_id=country_id).values('id', 'name')
    return JsonResponse({'states': list(states)})