from django.db import models
from core.models import Country, State, Course, Department

class PendingStudent(models.Model):
    # Add all fields similar to Student, but for pending review
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    nationality = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pending/photos/')
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    # ...add all other fields as needed...
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    admission_type = models.CharField(max_length=20)
    # Add a status field
    is_approved = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

class PendingStaff(models.Model):
    # Add all fields similar to Staff, but for pending review
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    nationality = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    # ...add all other fields as needed...
    is_approved = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)