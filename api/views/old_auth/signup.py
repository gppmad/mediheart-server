from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from api.models.patients import Patients
from api.serializers.serializers import PatientsSerializer as PatientsSerializer

class Signup(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        #This function is used for the web service signup process.
        form = UserCreationForm(request.POST)
        #print(form.is_valid())
        if form.is_valid():

            # Create User into auth_user
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            # Create Patient into api_patients
            try:
                new_patient = Patients.objects.create(fk_user_id=user.id) #Patient created with foreign key setted with
            except:
                user.delete()
                return Response({"error:":"can't create patient with this user ID"}, status=500)
            
            token = Token.objects.create(user=user) #TODO Manage Exception

            return Response({
                'token': token.key,
                'patientId': new_patient.id,
                'username': user.username
            })
            

        else:
            return Response({"error:":form.errors}, status=404)