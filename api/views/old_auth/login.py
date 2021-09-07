from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from api.models.patients import Patients

class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user'] # user obj
        token, created = Token.objects.get_or_create(user=user)

        try:
            patient = Patients.objects.get(fk_user_id=user.id) # patient obj
        except:
            return Response({"msg":"application error"}, status=500)
                    
        return Response({
            'token': token.key,
            'patientId': patient.id,
            'username': user.username
    })
