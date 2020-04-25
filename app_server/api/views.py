from django.http import HttpResponse
import os

def index(request):
    print(os.getenv('DEBUG',True))
    if bool(os.getenv('DEBUG')) == True:
        return HttpResponse("Hello, world. Developer Mode")
    else:
        return HttpResponse("Hello, world. Production Mode")