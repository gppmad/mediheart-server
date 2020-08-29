from django.urls import path
from . import views
from api.views.personalInfo import PersonalInfoView,PersonalInfoModifyView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #path('', views.index, name='index'),
    #path('personalInformations/<int:id>/', PersonalInformationsView.as_view()),
    #path('personalInformations/modify/<int:id>/', PersonalInformationsModifyView.as_view())
    path('token/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    path('personalInfo/<int:id>/', PersonalInfoView.as_view()),
    path('personalInfo/', PersonalInfoView.as_view()),
    path('personalInfo/modify/', PersonalInfoModifyView.as_view())
]