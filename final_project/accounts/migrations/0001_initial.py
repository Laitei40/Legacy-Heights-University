# Generated by Django 5.2.1 on 2025-06-01 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0006_course_number_of_semesters_course_price_per_semester_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('nationality', models.CharField(max_length=100)),
                ('is_approved', models.BooleanField(default=False)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.country')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.department')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.state')),
            ],
        ),
        migrations.CreateModel(
            name='PendingStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('nationality', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='pending/photos/')),
                ('contact', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('admission_type', models.CharField(max_length=20)),
                ('is_approved', models.BooleanField(default=False)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.country')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.course')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.state')),
            ],
        ),
    ]
