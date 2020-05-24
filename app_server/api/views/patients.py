from django.http import JsonResponse
from django.views import View
from api.models import Patients as DBModel
from api.serializers import PatientsSerializer as DBModelSerializer
#from api.serializers import RamDeleteSerializer as DBModelDeleteSerializer
import json
from datetime import date

import os

# def index(request):
#     print(os.environ)
#     if(os.environ['ENVIRONMENT'] == 'dev'):
#         return HttpResponse("You are in Dev")
#     else:
#         return HttpResponse("You are in Prod")

class PatientsView(View):
    #GET OBJECT(S)
    def get(self, request, id=""):
        
        #return JsonResponse({"result":date.today()})

        # Get without Parameter
        if(id == ""):
            query = list(DBModel.objects.values())
            return JsonResponse({"result":query})
        else:
        #Get with ID Parameter    
            try:
                query = DBModel.objects.values().get(pk=id)
            except DBModel.DoesNotExist:
                return JsonResponse({"error":"resource not found" }, status=404)
            return JsonResponse({"result":query})
 