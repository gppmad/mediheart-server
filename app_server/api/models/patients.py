from django.db import models
from api.models.bloodtype import BloodType as BloodType
from django.contrib.auth.models import User

# Create your models here.
class Patients(models.Model):
    class Meta:
        app_label = "api"
        db_table = 'api_patients'

    # Choises Values
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    # BLOODTYPE_CHOICES = (
    #     ('A+', 'A+'),
    #     ('A-', 'A-'),
    #     ('B+', 'B+'),
    #     ('B-', 'B-'),
    #     ('AB+', 'AB+'),
    #     ('AB-', 'AB-'),
    #     ('0+', '0+'),
    #     ('0-', '0-'),
    # )
    #bloodType = models.CharField(max_length=3, choices=BLOODTYPE_CHOICES)

    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    birthDate = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    bloodtype = models.ForeignKey(BloodType, on_delete=models.CASCADE)
    fk_user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    

    def __str__(self):
       return str(str(self.__dict__))