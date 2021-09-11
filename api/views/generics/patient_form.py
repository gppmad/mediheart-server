from api.models.bloodtype import BloodType
from rest_framework.views import APIView
from rest_framework.response import Response

class PatientForm(APIView):

    # Get common fields to work with patient informations (e.g Blood Type and Gender List)  
    def get(self, request):
        api_response = {}
        
        #Get with ID Parameter
        try:
            bloodType_obj = BloodType.objects.all()
            api_response['blood_type_list'] = bloodType_obj.values()
            api_response['gender_list'] = [{"id":'M', "label":'Male'},{"id":'F', "label":'Female'}]
            
        except:
            return Response({"error":"resource not found" }, status=404)

        return Response({"data":api_response})