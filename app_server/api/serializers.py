from rest_framework import serializers
from api.models import Patients

class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ['firstname','lastname','birth_date','gender','blood_type']