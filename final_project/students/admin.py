from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'country', 'state', 'course', 'batch_from', 'batch_to')
    search_fields = ('name', 'contact', 'abc_id')
    list_filter = ('gender', 'country', 'state', 'course', 'batch_from')