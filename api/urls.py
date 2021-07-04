from django.urls import path
from api.samples.sample_log import TestLog
from api.views.auth.login import Login
from api.views.auth.logout import Logout
from api.views.auth.signup import Signup
from api.views.auth.delete_user import DeleteUser
from api.views.auth.change_password import ChangePasswordView
from api.views.patients_management.patients_list import PatientsList
from api.views.patients_management.personal_info import PersonalInfoView,PersonalInfoModifyView,PersonalInfoAllUsersView
from api.views.auth.welcome_auth import WelcomeAuth
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    #path('', views.index, name='index'),
    #path('personalInformations/<int:id>/', PersonalInformationsView.as_view()),
    #path('personalInformations/modify/<int:id>/', PersonalInformationsModifyView.as_view())
    #path('login/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    
    # auth view folder 
    path('login/', Login.as_view(), name='api_token_auth'),  # <-- And here
    path('logout/', Logout.as_view(), name="logout"),
    path('signup/', Signup.as_view(), name="signup"),
    path('deleteuser/', DeleteUser.as_view(), name="delete_user"),
    path('changepass/', ChangePasswordView.as_view(), name="change_pass"),
    path('welcomeAuth/', WelcomeAuth.as_view()),


    path('personalInfo/<int:id>/', PersonalInfoView.as_view()),
    path('personalInfo/modify/<int:id>/', PersonalInfoModifyView.as_view()),
    path('personalInfo/', PersonalInfoAllUsersView.as_view()),  # for multiple operations (update all patients)

    # patients_management view folder
    path('patients/', PatientsList.as_view(), name="patients"),

    # test section
    path('log/', TestLog.as_view())
]