from django.db.models import F
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from api.models.patients import Patients
#from api.models.bloodtype import BloodType


class TestChangePwd(TestCase):

    def setUp(self):

        # Needs API_PATIENTS, AUTH USER AND AUTHTOKEN_TOKEN ENTRIES
        
        # Setting up user obj
        user1 = User.objects.create_user('rosario', 'rosario@thebeatles.com', 'rosariopassword')
        user1.save()
        
        # Setting up patients objs
        p1 = Patients.objects.create(firstname="Valery", lastname="Dolce", birthDate=None, gender="F", bloodType=None, fk_user=None )
        p2 = Patients.objects.create(firstname="Rosario", lastname="Dolce", birthDate=None, gender="M", bloodType=None, fk_user=user1)
        
        # Setting up token objs
        token, created = Token.objects.get_or_create(user=user1)
        
        # Setting up bloodtype values
        # print("Setting up bloodtype table")
        # bloodtype_list=("A+","A-","B+","B-","AB+","AB-","0+","0-")
        # for be in bloodtype_list:
        #     BloodType.objects.create(label=be)
        
        
    def test_getAll(self):
        #bloodtype_table = list(BloodType.objects.all())
        
        patients_table = list(Patients.objects.all().values("firstname","lastname","birthDate","gender", patientId=F("id"), userId=F("fk_user")  ) )
        print("here the list",patients_table)
        self.assertEqual( len(patients_table),2)
