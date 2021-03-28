import logging
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from api.models.patients import Patients
 

class DeleteUser (ObtainAuthToken):

    # def __delete_user():
    #     try:
    #     u = User.objects.get(username=username)
    #     u.delete()
    #     messages.success(request, "The user is deleted")

    #     except User.DoesNotExist:
    #         messages.error(request, "User doesnot exist")
    #         return render(request, 'front.html')

    #     except Exception as e:
    #         return render(request, 'front.html', {'err': e.message})
    
    # permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        # serializer = self.serializer_class(
        # data=request.data, context={'request': request})
        # serializer.is_valid(raise_exception=True)
        # user = serializer.validated_data['user']  # user obj

        #delete
        #token
        #patients
        #auth_user

        # patient = Patients.objects.get(fk_user_id=user.id)
        # request.user.auth_token.delete()
        # user = User.objects.get()

        logging.info("test logging")
        return Response({"msg": "ok"})
