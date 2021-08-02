from django.contrib.auth.forms import UserModel
from api.models.bloodtype import BloodType
from api.models.patients import Patients
from rest_framework import serializers

class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ['id','firstname','birth_date','gender','blood_type','fk_user']

class PatientsDelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ['id',]

class BloodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodType
        fields = ['bloodType']

