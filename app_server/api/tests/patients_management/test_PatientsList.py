from django.db.models import F
from django.test import TestCase
from api.models.patients import Patients
from api.models.bloodType import BloodType

class TestPatientsList(TestCase):
    def setUp(self):

        #setting up bloodtype values
        bloodtype_list=("A+","A-","B+","B-","AB+","AB-","0+","0-")
        for be in bloodtype_list:
            BloodType.objects.create(label=be)
        
        #setting up patients values
        Patients.objects.create(firstname="Valery", lastname="Dolce", birthDate=None, gender="F", bloodType=None, fk_user=None )
        Patients.objects.create(firstname="Rosario", lastname="Dolce", birthDate=None, gender="M", bloodType=None, fk_user=None )

    def test_getAll(self):
        bloodtype_table = list(BloodType.objects.all())
        
        patients_table = list(Patients.objects.all().values("firstname","lastname","birthDate","gender", patientId=F("id"), userId=F("fk_user")  ) )
        print("here the list",patients_table)
        self.assertEqual( len(patients_table),2)
