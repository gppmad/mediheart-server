from django.urls import path
from api.samples.sample_log import TestLog
from api.views.auth.login import Login
from api.views.auth.logout import Logout
from api.views.auth.signup import Signup
from api.views.patients_management.PatientsList import PatientsList
from api.views.patients_management.personalInfo import PersonalInfoView,PersonalInfoModifyView,PersonalInfoAllUsersView
from api.views.auth.test_auth import WelcomeAuth
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
    path('welcomeAuth/', WelcomeAuth.as_view()),


    path('personalInfo/<int:id>/', PersonalInfoView.as_view()),
    path('personalInfo/modify/<int:id>/', PersonalInfoModifyView.as_view()),
    path('personalInfo/', PersonalInfoAllUsersView.as_view()),  # for multiple operations (update all patients)

    # patients_management view folder
    path('patients/', PatientsList.as_view(), name="patients"),

    #TEST SECTION
    path('log/', TestLog.as_view())
]