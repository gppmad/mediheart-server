from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import authentication
from api.models.patients import Patients
from api.serializers.serializers import PatientsSerializer,PatientsSimpleSerializer


class PatientsListCreate(generics.ListCreateAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientsSimpleSerializer

class PatientsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientsSimpleSerializer

class GetPatientByUser(generics.ListAPIView):
    serializer_class = PatientsSerializer
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        """
        This view should return the patient
        for the currently authenticated user.
        """
        user = self.request.user
        return Patients.objects.filter(fk_user=user)