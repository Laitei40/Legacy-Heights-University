from django.db import models
from core.models import Country, State, Course

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, related_name='cities', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.state.name}"

class Student(models.Model):
    CATEGORY_CHOICES = [
        ('domestic', 'Domestic'),
        ('international', 'International'),
    ]
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    ADMISSION_TYPE_CHOICES = [
        ('Regular', 'Regular'),
        ('Distance', 'Distance'),
        ('International', 'International'),
    ]

    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='students')
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, related_name='students')
    nationality = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    photo = models.ImageField(upload_to='students/photos/')
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    local_address = models.CharField(max_length=255, blank=True, null=True)
    gov_id = models.FileField(upload_to='students/gov_ids/')
    passport_visa = models.FileField(upload_to='students/passport_visa/', blank=True, null=True)
    birth_certificate = models.FileField(upload_to='students/birth_certificates/', blank=True, null=True)
    nationality_proof = models.FileField(upload_to='students/nationality_proof/', blank=True, null=True)
    marksheet_10 = models.FileField(upload_to='students/marksheets/', verbose_name="Class 10 Mark Sheet")
    marksheet_12 = models.FileField(upload_to='students/marksheets/', verbose_name="Class 12 Mark Sheet")
    grad_marksheet = models.FileField(upload_to='students/marksheets/', blank=True, null=True)
    tc = models.FileField(upload_to='students/tc/', blank=True, null=True)
    migration = models.FileField(upload_to='students/migration/', blank=True, null=True)
    abc_id = models.CharField(max_length=50, blank=True, null=True)
    language_proof = models.FileField(upload_to='students/language_proof/', blank=True, null=True)
    caste_certificate = models.FileField(upload_to='students/caste_certificate/', blank=True, null=True)
    domicile = models.FileField(upload_to='students/domicile/', blank=True, null=True)
    income_certificate = models.FileField(upload_to='students/income_certificate/', blank=True, null=True)
    disability_certificate = models.FileField(upload_to='students/disability_certificate/', blank=True, null=True)
    entrance_score = models.CharField(max_length=50, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='students')
    admission_type = models.CharField(max_length=20, choices=ADMISSION_TYPE_CHOICES)
    portal_login = models.CharField(max_length=100, blank=True, null=True)
    fee_receipt = models.FileField(upload_to='students/fee_receipt/', blank=True, null=True)
    medical_fitness = models.FileField(upload_to='students/medical_fitness/', blank=True, null=True)
    vaccination = models.FileField(upload_to='students/vaccination/', blank=True, null=True)
    parent_details = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=128)
    temp_password = models.CharField(max_length=128, blank=True, null=True, help_text="Temporary password to be changed by the student")
    batch_from = models.PositiveIntegerField(verbose_name="Batch Year (From)")
    batch_to = models.PositiveIntegerField(verbose_name="Batch Year (To)")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name