from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from api.models.patients import Patients
from api.serializers.serializers import PatientsSerializer, PatientsSerializer


class PatientsListCreate(generics.ListCreateAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer

class PatientsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer

