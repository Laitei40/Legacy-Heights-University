from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, related_name='states', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Course(models.Model):
    UNDERGRADUATE = 'UG'
    POSTGRADUATE = 'PG'
    COURSE_TYPE_CHOICES = [
        (UNDERGRADUATE, 'Undergraduate'),
        (POSTGRADUATE, 'Postgraduate'),
    ]

    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, related_name='courses', on_delete=models.CASCADE, null=True, blank=True)
    course_type = models.CharField(max_length=2, choices=COURSE_TYPE_CHOICES, default=UNDERGRADUATE)
    price_per_semester = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_semesters = models.PositiveIntegerField()
    years_to_complete = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        return self.price_per_semester * self.number_of_semesters