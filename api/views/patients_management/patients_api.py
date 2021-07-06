from rest_framework import generics
from api.models.patients import Patients
from api.serializers.serializers import PatientsSerializer 

class PatientsList(generics.ListCreateAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer

class PatientsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer