from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

class ChangePassword(APIView):
    permission_classes = (IsAuthenticated,) 
    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            try:
                form.save()
                update_session_auth_hash(request, form.user)
                return Response({"messages":"Password has been changed"})
            except:
                return Response({"error:":"Password cannot be changed"}, status=500)
        else:
            return Response({"error:":form.errors}, status=404)