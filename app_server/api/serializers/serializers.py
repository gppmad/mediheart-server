from rest_framework import serializers
from api.models.patient import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['firstname','lastname','birthDate','gender','bloodType']

class PatientDelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id',]