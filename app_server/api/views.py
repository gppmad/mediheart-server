from django.http import HttpResponse
import os
#import environ

def index(request):
    #import environ
    #env = environ.Env()
    # reading .env file
    #environ.Env.read_env()
    #x = env('DEBUG')
    #y = env('SECRET_KEY')
    print(os.environ)
    #if(os.environ('DEBUG') == True):
    #    return HttpResponse("True")
    #else:
     #   return HttpResponse("False")

    if(os.environ['ENVIRONMENT'] == 'dev'):
        return HttpResponse("You are in Dev")
    else:
        return HttpResponse("You are in Prod")
    # if x:
        
    # else:
    #     return HttpResponse("Hello, world. Production Mode")
    # print("Value: "+ str(os.getenv('DEBUG')))
    # return HttpResponse("Hello, world. Developer Mode")