from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models.patients import Patients
from api.serializers.serializers import PatientsSerializer as PatientsSerializer


class PatientsList (APIView):

    # Get the list of all patients.
    def get(self, request):

        patients_table = list(Patients.objects
                              .all()
                              .values("firstname", "lastname", "birthDate", "gender", patientId=F("id"), userId=F("fk_user")))
        return Response({'data': patients_table})
