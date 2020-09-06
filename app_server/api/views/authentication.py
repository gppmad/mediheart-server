from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


@api_view(('POST',))
def signup(request):
    
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


@api_view(('GET',))
@permission_classes([IsAuthenticated])
def logout(request):

    response = {}
    response["action"] = "logout"
    response["user"] = str(request.user)

    # Simply delete the token to force a login
    request.user.auth_token.delete()
    return Response({"data": response })
    

