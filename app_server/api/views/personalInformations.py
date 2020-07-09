#from django.http import JsonResponse
#from django.views import View
# from api.serializers import PatientsSerializer as DBModelSerializer
#from api.serializers import RamDeleteSerializer as DBModelDeleteSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from api.models.patient import Patient as DBModel
from api.serializers.serializers import PatientSerializer as DBModelSerializer
from api.serializers.serializers import PatientDelSerializer as DBModelDelSerializer

from datetime import date
from dateutil.relativedelta import relativedelta

import json
import os

class PersonalInformationsView(APIView):
    
    """GET OBJECT(S) WITH ID PARAMETER"""

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
            return Response({"error":"resource not found" }, status=404)
        return Response({"result":api_response})
    
    

class PersonalInformationsModifyView(APIView):

    #POST OBJECT(S)
    def post(self, request):
        #[{"value":6,"um":"GB"}, {"value":10,"um":"GB"} ]
        #array_data = [{"value":600,"um":"GB"}, {"value":10,"um":"GB"} ]
        array_data = json.loads(request.body)
        
        serializer = DBModelSerializer(data=array_data,many=True)
        
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                print(str(e))
                return Response({"server_error":str(e) }, status=500) 
            return Response({"result":"ok"})
        else:
            return Response({"client_error":serializer.errors }, status=400)  

    #DELETE OBJECT(S)
    def delete(self,request):
        # array_data = [{"id":10}, {"id": 11}]

        array_data = json.loads(request.body)
        for el in array_data:
            print(el)
            serializer = DBModelDelSerializer(data=el)

            if serializer.is_valid():
                try:
                    DBModel.objects.filter(pk=el.get("id","")).delete()
                except Exception as e:
                    return Response({"server_error":str(e) }, status=500)

                return Response({"result":"ok"})    
            else:
                return Response({"client_error":serializer.errors }, status=400)
 