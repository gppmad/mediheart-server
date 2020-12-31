from rest_framework import serializers
from api.models.patients import Patients
from api.models.bloodType import BloodType

class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ['id','firstname','lastname','birthDate','gender','bloodType','fk_user']

class PatientsDelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ['id',]

class BloodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodType
        fields = ['bloodType']

