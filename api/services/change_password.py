from django.contrib.auth.models import User
from django.db.models.expressions import F
from api.models.patients import Patients as Patients
from rest_framework import serializers


def change_pass(new_pass):
    u = User.objects.get(username='test')
    u.set_password(new_pass)
    u.save()
    
    return True
