from django.http import JsonResponse
from django.views import View
from api.models.patients import Patients as DBModel
# from api.serializers import PatientsSerializer as DBModelSerializer
#from api.serializers import RamDeleteSerializer as DBModelDeleteSerializer
import json
from datetime import date
from dateutil.relativedelta import relativedelta

import os

class PersonalInformationsView(View):
    
    #GET OBJECT(S) WITH ID PARAMETER
    def get(self, request, id=""):
        api_response = {}

        #Get with ID Parameter    
        try:
            query = DBModel.objects.values().get(pk=id) #Dict
            print(query)
            api_response["firstname"] = query["firstname"]
            api_response["lastname"] = query["lastname"]
            api_response["gender"] = query["gender"]
            api_response["bloodType"] = query["bloodType"]
            #Computing Age
            age = relativedelta(date.today(), query["birthDate"]).years
            api_response["age"] = age

            #return JsonResponse({"result":query.birthDate})
        except DBModel.DoesNotExist:
            return JsonResponse({"error":"resource not found" }, status=404)
        return JsonResponse({"result":api_response})

class PersonalInformationsModifyView(View):
    pass
 