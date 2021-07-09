from django.urls import path
from api.views.old_auth.login import Login
from api.views.old_auth.logout import Logout
from api.views.old_auth.signup import Signup
from api.views.old_auth.delete_user import DeleteUser
from api.views.old_auth.change_password import ChangePasswordView
from api.views.patients_management.personal_info import PersonalInfoView,PersonalInfoModifyView,PersonalInfoAllUsersView
from api.views.patients.patients_api import PatientsList
from api.views.patients.patients_api import PatientsDetail
from api.views.old_auth.welcome_auth import WelcomeAuth
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken import views
from api.views.auth.logout import Logout as NewLogout


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
    path('personalInfo/', PersonalInfoAllUsersView.as_view()),  # for multiple operations (update all patients)


    # New auth management
    path('auth/api-token-auth/', views.obtain_auth_token),
    path('auth/logout/', NewLogout.as_view(), name="auth logout"),

    # New patients management 
    path('patients/', PatientsList.as_view(), name="patients"),
    path('patients/<int:pk>/', PatientsDetail.as_view()),  

]