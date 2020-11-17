from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from api.models.patients import Patients

class Login(ObtainAuthToken):
    #TODO: add error if patient doesn't exist.

    def post(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user'] # user obj
        patient = Patients.objects.get(fk_user_id=user.id) # patient obj
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            #'user_id': user.id, # Only for dev
            'patientId': patient.id,
            'username': user.username,
            #'patientName': patient.firstname
    })
