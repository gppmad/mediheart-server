from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from api.serializers.signup_serializer import SignupSerializer
import logging


class Signup(APIView):

    def post(self, request, *args, **kwargs):
        logger = logging.getLogger(__name__)

        signup_form = UserCreationForm(request.data)

        if signup_form.is_valid():
            signup_form.save()
            username = signup_form.cleaned_data.get('username')
            password = signup_form.cleaned_data.get('password1')
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                try:
                    token = Token.objects.create(user=new_user)
                    logger.info(f"user \'{new_user} \' created")
                    return Response({
                        'token': token.key,
                        'username': new_user.username
                    })
                except Exception as e:
                    logger.info(f"can't create token for {new_user} -> {e}")
                    new_user.delete()
                    return Response({"data": "user not created because token already exist"}, status=500)

        else:
            logger.info(
                f"errors during creation of username: {request.data['username']} -> {signup_form.errors.as_data}")
            return Response({"error:": signup_form.errors}, status=404)
