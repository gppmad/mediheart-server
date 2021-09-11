import logging
from django.db.models import ObjectDoesNotExist
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class Logout(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        logger = logging.getLogger(__name__)

        try:
            request.user.auth_token.delete()
            logger.info("deleted %s token", request.user)
            return Response()
        except (AttributeError, ObjectDoesNotExist):
            logger.error("user %s does not exist", request.user)
            return Response({"message": "can't find user with this token"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
