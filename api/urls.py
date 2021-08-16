from django.urls import path
from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token

from api.views.auth.logout import Logout as NewLogout
from api.views.auth.signup import Signup as NewSignup
from api.views.auth.delete_user import DeleteUser as NewDeleteUser
from api.views.auth.change_password import ChangePasswordView as NewChangePassword

from api.views.old_auth.change_password import ChangePasswordView
from api.views.old_auth.delete_user import DeleteUser
from api.views.old_auth.login import Login
from api.views.old_auth.logout import Logout
from api.views.old_auth.signup import Signup
from api.views.old_auth.welcome_auth import WelcomeAuth
from api.views.patients.patients_api import PatientsDetail, PatientsListCreate
from api.views.patients_management.personal_info import (
    PersonalInfoAllUsersView, PersonalInfoModifyView, PersonalInfoView)
from api.views.generics.patient_form import PatientForm

urlpatterns = [

    # auth view folder
    path('login/', Login.as_view(), name='api_token_auth'),  # <-- And here
    path('logout/', Logout.as_view(), name="logout"),
    path('signup/', Signup.as_view(), name="signup"),
    path('deleteuser/', DeleteUser.as_view(), name="delete_user"),
    path('changepass/', ChangePasswordView.as_view(), name="change_pass"),
    path('welcomeAuth/', WelcomeAuth.as_view()),


    path('personalInfo/<int:id>/', PersonalInfoView.as_view()),
    path('personalInfo/modify/<int:id>/', PersonalInfoModifyView.as_view()),
    # for multiple operations (update all patients)
    path('personalInfo/', PersonalInfoAllUsersView.as_view()),


    # New auth management
    path('auth/api-token-auth/', views.obtain_auth_token),
    path('auth/logout/', NewLogout.as_view(), name="auth logout"),
    path('auth/signup/', NewSignup.as_view(), name="auth signup"),
    path('auth/delete-user/', NewDeleteUser.as_view(), name="auth delete-user"),
    path('auth/change-pass/', NewChangePassword.as_view(), name="auth change-pass"),

    # New patients management
    path('patients/', PatientsListCreate.as_view(), name="patients"),
    path('patients/<int:pk>/', PatientsDetail.as_view()),
    path('patients/prepare-form/', PatientForm.as_view())


]
