from django.db.models import ObjectDoesNotExist
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from api.models.patients import Patients
import uuid
import time
from django.db import transaction

class UserManagement():
    
    def create_user(self):
        start = time.time()

        user_str = str(uuid.uuid4())
         # Create User, Token and Patient for testing
        new_user = User.objects.create_user(username=user_str,
                                            password=user_str)
        new_token = Token.objects.create(user=new_user)
        new_patient = Patients.objects.create(firstname=user_str,lastname=user_str,fk_user_id=new_user.id)
        elapsed = time.time() - start
        print("created lapsed time: {} ".format(elapsed)) 
        return new_token

    @transaction.atomic
    def delete_user(self, token):
        
        # Delete Patients from PatientsTable with get_userid_by_token
        # Delete Token entry from Token Table
        # Delete User from User with get_userid_by_token 
        start = time.time()
        userid_by_token = Token.objects.values().get(key=token)["user_id"]
        Patients.objects.filter(fk_user_id=userid_by_token).delete()
        Token.objects.filter(user_id=userid_by_token).delete()
        User.objects.filter(pk=userid_by_token).delete()
        elapsed = time.time() - start
        print("detroyed elapsed time: {} ".format(elapsed)) 
        return True


user_management = UserManagement()
token = user_management.create_user()
print("user created")
user_management.delete_user(token)
print("user destroyed")
