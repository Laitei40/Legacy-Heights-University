# models.py
from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='staff_photos/', blank=True)

    def __str__(self):
        return self.name