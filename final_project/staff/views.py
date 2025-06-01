# views.py
from django.shortcuts import render, get_object_or_404
from .models import Staff

def staff_index(request):
    staff_list = Staff.objects.all()
    return render(request, 'staff/staff.html', {'staff_list': staff_list})


def staff_list(request):
    staff_list = Staff.objects.all()
    return render(request, 'staff/staff_list.html', {'staff_list': staff_list})

def staff_detail(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    return render(request, 'staff/staff_detail.html', {'staff': staff})