from django.test import TestCase
from django.db.models import F
from api.models.patients import Patients
#from api.serializers.serializers import PatientsSerializer as PatientsSerializer

class PatientListTest(TestCase):

    def test(self):
        
        array_data = {
            "firstname": "valeria",
            "lastname": "dolce",
            "birthDate": "1992-04-13",
            "gender": "F",
            "bloodtype": 1
        }
        print(array_data)
        patients_table = list(Patients.objects.all().values("firstname","lastname","birthDate","gender", patientId=F("id"), userId=F("fk_user")  ) )
        print(patients_table)

        #serializer = PatientsSerializer(data=array_data,many=True)
        
        # if serializer.is_valid():
        #     serializer.save()
        #     patients_table = list(Patients.objects.all().values("firstname","lastname","birthDate","gender", patientId=F("id"), userId=F("fk_user")  ) )
        #     self.assertGreaterEqual(len(patients_table),0)
        # else:
        #     self.assertTrue(1==0)   
        #self.assertGreater(len(patients_table),0)
        #self.assertEqual('foo'.upper(), 'FOOX')

