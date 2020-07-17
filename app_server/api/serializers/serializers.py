from rest_framework import serializers
from api.models.patient import Patient
from api.models.bloodtype import BloodType

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['firstname','lastname','birthDate','gender','bloodtype']

class PatientDelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id',]

class BloodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodType
        fields = ['bloodType']

