# import the logging library
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from api.models.patients import Patients

class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        logger = logging.getLogger(__name__)
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user'] # user obj
        token, created = Token.objects.get_or_create(user=user)

        try:
            patient = Patients.objects.get(fk_user_id=user.id) # patient obj
        except:
            # Get an instance of a logger
            logger.error("error catched")
            print("error catched")
            return Response({"msg":"application error"}, status=500)
            
        
        return Response({
            'token': token.key,
            'patientId': patient.id,
            'username': user.username
             #'user_id': user.id, # Only for dev
            #'patientName': patient.firstname
    })
