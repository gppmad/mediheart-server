from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


@api_view(('POST',))
def signup(request):
    #this function is used for the web service signup process.
    
    form = UserCreationForm(request.POST)
    print(form.is_valid())
    if form.is_valid():
        form.save()
        return Response({"data":"user created"})
    else:
        return Response({"error:":form.errors}, status=404)
    
    #return Response({"data":"user created"})
    # if form.is_valid():
    #     # form.save()
    #     # username = form.cleaned_data.get('username')
    #     # password = form.cleaned_data.get('password1')
    #     # user = authenticate(username=username, password=password)
    #     # login(request, user)
    #     return Response({"data":"user created"})
    # else:
    #     return Response({"error":"internal error" }, status=404)
