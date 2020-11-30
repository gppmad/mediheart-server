from django.urls import path
from . import views
from api.views.auth.login import Login
from api.views.auth.logout import Logout
from api.views.auth.signup import Signup
from api.views.auth.changePassword import ChangePassword
from api.views.patients_management.PatientsList import PatientsList
from api.views.personalInfo import PersonalInfoView,PersonalInfoModifyView,PersonalInfoAllUsersView
from api.views.test_auth import WelcomeAuth
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
    path('changePassword/', ChangePassword.as_view(), name="changePassword"),
    path('welcomeAuth/', WelcomeAuth.as_view()),


    path('personalInfo/<int:id>', PersonalInfoView.as_view()),
    path('personalInfo/modify/<int:id>/', PersonalInfoModifyView.as_view()),
    path('personalInfo/', PersonalInfoAllUsersView.as_view()),  # for multiple operations (update all patients)

    # patients_management view folder
    path('patients/', PatientsList.as_view(), name="patients"),
]