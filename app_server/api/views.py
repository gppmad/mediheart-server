from django.http import HttpResponse
import os

def index(request):
    print(os.environ)
    if(os.environ['ENVIRONMENT'] == 'dev'):
        return HttpResponse("You are in Dev")
    else:
        return HttpResponse("You are in Prod")
 