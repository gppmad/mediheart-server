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

class Signup(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        #This function is used for the web service signup process.
        form = UserCreationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return Response({"data":"user created"})
        else:
            return Response({"error:":form.errors}, status=404)