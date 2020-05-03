from django.http import HttpResponse
import os
import environ

def index(request):
    import environ
    env = environ.Env()
    # reading .env file
    environ.Env.read_env()
    x = env('DEBUG')
    y = env('SECRET_KEY')
    return HttpResponse(y)

    # if x:
        
    # else:
    #     return HttpResponse("Hello, world. Production Mode")
    # print("Value: "+ str(os.getenv('DEBUG')))
    # return HttpResponse("Hello, world. Developer Mode")