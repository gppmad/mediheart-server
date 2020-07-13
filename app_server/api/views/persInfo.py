from rest_framework.views import APIView
from rest_framework.response import Response
from api.models.patient import Patient as DBModel #LEGACY
from api.models.patient import Patient as Patient
from api.models.bloodtype import BloodType as BloodType
from api.serializers.serializers import PatientSerializer as DBModelSerializer
from api.serializers.serializers import PatientDelSerializer as DBModelDelSerializer

from datetime import date
from dateutil.relativedelta import relativedelta

import json
import os

class PersInfoView(APIView):
    
    """GET OBJECT(S) WITH ID PARAMETER"""

    def get(self, request, id=""):
        api_response = {}

        #Get with ID Parameter    
        try:

            #query = DBModel.objects.values().get(pk=id) #Dict
            #print(query_obj.bloodtype.type)
            query_obj = Patient.objects.get(pk=id)
        
            api_response["firstname"] = query_obj.firstname
            api_response["lastname"] = query_obj.lastname
            api_response["gender"] = query_obj.gender
            api_response["bloodType"] = query_obj.bloodtype.label

            #Computing Age
            age = relativedelta(date.today(), query_obj.birthDate).years
            api_response["age"] = age

        except DBModel.DoesNotExist:
            return Response({"error":"resource not found" }, status=404)
        return Response({"data":api_response})
    
class PersInfoModifyView(APIView):

    """GET OBJECT(S) WITH ID PARAMETER"""
    def get(self, request, id=""):
        api_response = {}
        form = {}
        bloodType = {}
        api_response['gender_list'] = ('M','F')
        api_response['bloodType'] = BloodType.objects.all().values()
        api_response['pers-info'] = Patient.objects.values().get(pk=1)


        return Response({"data":api_response})

class Things(APIView):

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
 