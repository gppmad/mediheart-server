from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status

from api.models.patients import Patients

class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user'] # user obj
        token, created = Token.objects.get_or_create(user=user)
        is_first_login = Patients.objects.filter(fk_user_id=user.id).count() == 0
        
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username,
            'is_first_login': is_first_login
    })
