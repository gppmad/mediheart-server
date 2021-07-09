import time
from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from api.models.patients import Patients

class DeleteUser(ObtainAuthToken):
    permission_classes = (IsAuthenticated,) 

    @transaction.atomic
    def __delete_user(self, token):
        
        # Delete Patients from PatientsTable with get_userid_by_token
        # Delete Token entry from Token Table
        # Delete User from User with get_userid_by_token 
        start = time.time()
        userid_by_token = Token.objects.values().get(key=token)["user_id"]
        Patients.objects.filter(fk_user_id=userid_by_token).delete()
        Token.objects.filter(user_id=userid_by_token).delete()
        User.objects.filter(pk=userid_by_token).delete()
        elapsed = time.time() - start
        print("detroyed elapsed time: {} ".format(elapsed)) 
        return True
        
    def get(self, request, *args, **kwargs):

        content = {
        'action': "delete_user",
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # Token
        }

        token_request = str(request.auth)
        self.__delete_user(token_request)

        return Response(content)
        
