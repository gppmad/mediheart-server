from django.http import JsonResponse
from django.views import View
from api.models.patients import Patients as DBModel
# from api.serializers import PatientsSerializer as DBModelSerializer
#from api.serializers import RamDeleteSerializer as DBModelDeleteSerializer
import json
from datetime import date

import os

class PersonalInformationsView(View):
    
    #GET OBJECT(S) WITH ID PARAMETER
    def get(self, request, id=""):
        
        #Get with ID Parameter    
        try:
            query = DBModel.objects.values().get(pk=id)
        except DBModel.DoesNotExist:
            return JsonResponse({"error":"resource not found" }, status=404)
        return JsonResponse({"result":query})

class PersonalInformationsModifyView(View):
    pass
 