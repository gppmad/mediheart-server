from django.http import HttpResponse
import os

def index(request):
     if str(os.getenv('DEBUG')) == "True":
         return HttpResponse("Hello, world. Developer Mode")
     else:
         return HttpResponse("Hello, world. Production Mode")
    # print("Value: "+ str(os.getenv('DEBUG')))
    # return HttpResponse("Hello, world. Developer Mode")