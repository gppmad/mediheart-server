from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from django.db.models import ObjectDoesNotExist
import logging


class Logout(ObtainAuthToken):

    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        logger = logging.getLogger(__name__)

        try:
            request.user.auth_token.delete()
            logger.info("deleted %s token", request.user)
        except ObjectDoesNotExist:
            logger.error("user %s does not exist", request.user)

        return Response()
