from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  
from api.models.patients import Patients as Patients
from api.models.bloodType import BloodType as BloodType
from api.serializers.serializers import PatientsSerializer as PatientsSerializer
from api.serializers.serializers import PatientsDelSerializer as PatientsDelSerializer
# from api.serializers.serializers import PatientSerializer as DBModelSerializer #LEGACY
# from api.serializers.serializers import PatientDelSerializer as DBModelDelSerializer #LEGACY
# from api.models.patient import Patient as DBModel #LEGACY

from datetime import date
from dateutil.relativedelta import relativedelta

import json
import os

class PersonalInfoView(APIView):
    #permission_classes = (IsAuthenticated,)   

    #GET OBJECT WITH ID
    def get(self, request, id=""):
        api_response = {}

        #Get with ID Parameter    
        try:

            #query = DBModel.objects.values().get(pk=id) #Dict
            #print(query_obj.bloodType.type)
            query_obj = Patients.objects.get(pk=id)
        
            api_response["firstname"] = query_obj.firstname
            api_response["lastname"] = query_obj.lastname
            api_response["gender"] = query_obj.get_gender_display()
            try:
                api_response["bloodType"] = query_obj.bloodType.label
            except:
                 api_response["bloodType"] = None

            #Computed Age
            age = relativedelta(date.today(), query_obj.birthDate).years
            api_response["age"] = age

        except:
            return Response({"error":"resource not found" }, status=404)
        return Response({"data":api_response})
    
    #POST OBJECT(S)
    def post(self, request):
        api_response = {}
        api_response["message"] = "Record(s) has been inserted successfully"
        array_data = {}

        try:
            array_data = json.loads(request.body)
            serializer = PatientsSerializer(data=array_data,many=True)
        except Exception as e:
                #print(str(e))
                return Response({"server_error":str(e) }, status=500) 

        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                #print(str(e))
                return Response({"server_error":str(e) }, status=500) 
            return Response({"data":api_response})
        else:
            return Response({"client_error":serializer.errors }, status=400)

    #UPDATE ONE OBJECT
    def put(self, request, id=""):
        api_response = {}
        api_response["message"] = "Record has been updated successfully"

        try:
            request_data = json.loads(request.body)
        except Exception as e:
            return JsonResponse({"client_error":str(e) }, status=400)

        try:
            obj = Patients.objects.get(pk=id)
            serializer = PatientsSerializer(obj,data=request_data)
            if(serializer.is_valid()):
                try:
                    serializer.save()
                except Exception as e:
                    return Response({"server_error":str(e) }, status=500)                 
            else:
                return Response({"client_error":serializer.errors }, status=400)
        except:
            return Response({"error":"resource not found" }, status=404)
        
        return Response({"data":api_response})
   
    #DELETE OBJECT(S)
    def delete(self,request):
        #Ex: [{"id":10}, {"id": 11}]

        api_response = {}
        api_response["message"] = "Record(s) has been deleted successfully"

        array_data = json.loads(request.data)
        print(array_data)
        for el in array_data:
            print(el)
            serializer = PatientsDelSerializer(data=el)

            if serializer.is_valid():
                try:
                    Patients.objects.filter(pk=el.get("id","")).delete()
                except Exception as e:
                    return Response({"server_error":str(e) }, status=500)   
            else:
                return Response({"client_error":serializer.errors }, status=400)  
        return Response({"data":api_response}) 


class PersonalInfoModifyView(APIView):

    """GET OBJECT(S) WITH ID PARAMETER"""
    def get(self, request, id=""):
        api_response = {}
        
        #Get with ID Parameter
        try:
            bloodType_obj = BloodType.objects.all()
            patient_obj = Patients.objects.values("firstname","lastname","birthDate","gender", "bloodType" ).get(pk=id)
            print(patient_obj)
            api_response['genderList'] = [{"id":'M', "label":'Male'},{"id":'F', "label":'Female'}]
            api_response['bloodTypeList'] = bloodType_obj.values()
            api_response['personalInfo'] = patient_obj
        except:
            return Response({"error":"resource not found" }, status=404)

        return Response({"data":api_response})


    
class PersonalInfoAllUsersView(APIView):
     #UPDATE MULTPLE OBJECT(S)
    def put(self, request):
        api_response = {}
        api_response["message"] = "Record(s) has been updated successfully"

        try:
            array_data = json.loads(request.body)
        except Exception as e:
            return JsonResponse({"client_error":str(e) }, status=400)

        for el in array_data:
            obj = Patients.objects.get(pk=el.get("id",""))
            serializer = PatientsSerializer(obj,data=el,partial=True)
            if(serializer.is_valid()):
                try:
                    serializer.save()
                except Exception as e:
                    return Response({"server_error":str(e) }, status=500)                 
            else:
                return Response({"client_error":serializer.errors }, status=400)
        
        return Response({"data":api_response})