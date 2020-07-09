from django.db import models

# Create your models here.
class BloodType(models.Model):
    class Meta:
        app_label = "api"
        db_table = 'app_server.api.bloodtype'

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

    bloodType = models.CharField(max_length=3, choices=BLOODTYPE_CHOICES)
    
    def __str__(self):
       return str(str(self.__dict__))