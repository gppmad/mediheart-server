from django.db import models
from api.models.bloodtype import BloodType as BloodType

# Create your models here.
class Patient(models.Model):
    class Meta:
        app_label = "api"
        db_table = 'api.patients'

    # Choises Values
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    BLOODTYPE_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('0+', '0+'),
        ('0-', '0-'),
    )

    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    birthDate = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    #bloodType = models.CharField(max_length=3, choices=BLOODTYPE_CHOICES)
    bloodType = models.ForeignKey(BloodType, on_delete=models.CASCADE)

    def __str__(self):
       return str(str(self.__dict__))