# Generated by Django 5.2.1 on 2025-05-29 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_course_course_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='undergraduatecourse',
            name='course',
        ),
        migrations.DeleteModel(
            name='PostgraduateCourse',
        ),
        migrations.DeleteModel(
            name='UndergraduateCourse',
        ),
    ]
