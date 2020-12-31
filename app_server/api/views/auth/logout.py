from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class Logout(ObtainAuthToken):
    
    permission_classes = (IsAuthenticated,) 
    def get(self, request, *args, **kwargs):
        response = {}
        response["action"] = "logout"
        response["user"] = str(request.user)

        # Simply delete the token to force a login
        request.user.auth_token.delete()
        return Response({"data": response })