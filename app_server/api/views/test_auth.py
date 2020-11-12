from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  
from api.models.patients import Patients as Patients
from api.models.bloodtype import BloodType as BloodType
from api.serializers.serializers import PatientsSerializer as PatientsSerializer
from api.serializers.serializers import PatientsDelSerializer as PatientsDelSerializer
from django.core.mail import send_mail

from datetime import date
from dateutil.relativedelta import relativedelta


import json
import os

class WelcomeAuth(APIView):

    #permission_classes = (IsAuthenticated,)   

    #GET OBJECT WITH ID
    def get(self, request, id=""):

        #Get with ID Parameter
        if(request.user.is_authenticated):   
            msg = "Welcome " + request.user.get_username().capitalize()
            user_id = request.user.pk
            email = request.user.email
            # send_mail('Welcome', msg, 'bobo.maddiona@gmail.com', ['giuseppe.maddiona@gmail.com'])
            return Response({"msg":msg, "email":email, "user_id":user_id})
        
        else:
            msg = "Welcome Anonymous"
            return Response({"msg":msg})
    