from django.contrib.auth.forms import UserModel
from api.models import bloodtype
from api.models.bloodtype import BloodType
from api.models.patients import Patients
from rest_framework import serializers
from datetime import date
from dateutil.relativedelta import relativedelta

class BloodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodType
        fields = ['id','label']

class PatientsSerializer(serializers.ModelSerializer):
    blood_type = BloodTypeSerializer()
    age = serializers.SerializerMethodField()

    class Meta:
        model = Patients
        fields = ['id','firstname','birth_date','gender','blood_type','fk_user','age']
    
    def get_age(self, obj):
        return relativedelta (date.today(), obj.birth_date).years 

class PatientsSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ['id','firstname','birth_date','gender','blood_type','fk_user']

class PatientsDelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ['id',]



