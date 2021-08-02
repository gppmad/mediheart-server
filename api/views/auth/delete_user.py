from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from api.models.patients import Patients

import logging

class DeleteUser(ObtainAuthToken):
    permission_classes = (IsAuthenticated,) 

    @transaction.atomic
    def __delete_user(self, token):
        
        # Delete Patients from PatientsTable with get_userid_by_token
        # Delete Token entry from Token Table
        # Delete User from User with get_userid_by_token 
        userid_by_token = Token.objects.values().get(key=token)["user_id"]
        Patients.objects.filter(fk_user_id=userid_by_token).delete()
        Token.objects.filter(user_id=userid_by_token).delete()
        User.objects.filter(pk=userid_by_token).delete() 
        return True
        
    def get(self, request, *args, **kwargs):
        logger = logging.getLogger(__name__)

        content = {
        'action': "delete_user",
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # Token
        }

        token_request = str(request.auth)
        if self.__delete_user(token_request):
            logger.info(f"user {request.user} deleted")
            return Response(content)
        else:
            logger.info(f"can't delete user {request.user}")
            return Response(content , status=500)
        
