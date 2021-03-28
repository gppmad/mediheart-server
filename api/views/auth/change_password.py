import logging
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken

class ChangePassword (ObtainAuthToken):

    # permission_classes = (IsAuthenticated,) 
    def post (self,request):
        
        logging.info("test logging")
        return Response({"msg":"ok"})
