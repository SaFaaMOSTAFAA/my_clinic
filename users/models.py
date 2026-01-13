from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    class Roles(models.TextChoices):
        DOCTOR = 'doctor', 'Doctor'
        PATIENT = 'patient', 'Patient'

    role = models.CharField(
        max_length=20,
        choices=Roles.choices
    )

    phone = models.CharField(max_length=20, blank=True, null=False)
    address = models.TextField(blank=True, null=False)
    gender = models.CharField(max_length=10, blank=True, null=False)



class Doctor(User):
    specialization = models.CharField(max_length=255)
    experience_years = models.PositiveIntegerField()


class Patient(User):
    age = models.PositiveIntegerField()
    medical_history = models.TextField(blank=True, null=True)



