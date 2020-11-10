from rest_framework.views import APIView
from rest_framework.response import Response
from api.models.patient import Patient
from api.serializers.serializers import PatientSerializer as PatientSerializer

class PatientsList (APIView):
    
    # Get the list of all patients.
    def get(self, request):
        
        patients_table = Patient.objects.all()
        patient_serializer = PatientSerializer(patients_table, many=True)
        return Response(patient_serializer.data)