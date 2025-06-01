from django.shortcuts import render

def aboutus(request):
    return render(request, 'about_us/aboutus.html')

def terms(request):
    return render(request, 'about_us/terms.html')

def privacy(request):
    return render(request, 'about_us/privacy.html')