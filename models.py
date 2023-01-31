from datetime import datetime

from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.

class Person(models.Model):
    male = 'male'
    female = 'female'
    agender = 'agender'
    polygender = 'polygender'
    Genderfluid = 'genderfluid'
    Bigender = 'bigender'
    GENDER_CHOICES = [(male, 'male'), (female, 'female'), (agender, 'agender'), (polygender, 'polygender'),
                      (Genderfluid, 'genderfluid'), (Bigender, 'bigender')]

    first_name = models.CharField(db_column="first_name", max_length=256, null=False, blank=False)
    last_name = models.CharField(db_column="last_name", max_length=256, null=False, blank=False)
    personal_email = models.CharField(db_column="personal_email", max_length=256, null=False, blank=False)
    gender = models.CharField(db_column="gender", choices=GENDER_CHOICES, max_length=32)
    birth_date = models.DateField(db_column="birth_date", null=False, blank=False,
                                  validators=[MinValueValidator(datetime(1900, 1, 1, 0, 0))])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'persons'

class Company(models.Model):

    company_name = models.CharField(db_column="company_name", max_length=256, null=False, blank=False)
    country = models.CharField(db_column="country", max_length=256, null=False, blank=False)
    city = models.CharField(db_column="city", max_length=256)
    address = models.CharField(db_column="address", max_length=256, null=False, blank=False)
    phone_num = models.CharField(db_column="phone_num", max_length=32, null=False, blank=False)
    persons = models.ManyToManyField(Person, through='Employee')

    def __str__(self):
        return self.company_name

    def __repr__(self):
        return self.company_name

    class Meta:
        db_table = 'companies'

class Employee(models.Model):

    person = models.ForeignKey('Person', on_delete=models.RESTRICT)
    company = models.ForeignKey('Company', on_delete=models.RESTRICT)
    job_title = models.CharField(db_column="job_title", max_length=256, null=False, blank=False)
    is_current_job = models.BooleanField(db_column="is_current_job", default=True, null=False, blank=False)
    company_email = models.CharField(db_column="company_email", max_length=256, null=True, blank=True)

    def __str__(self):
        return f"{self.person} working at {self.company} (is current job? {self.is_current_job})"

    class Meta:
        db_table = 'employees'