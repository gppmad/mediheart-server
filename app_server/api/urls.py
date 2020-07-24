from django.urls import path
from . import views
from api.views.personalInfo import PersonalInfoView,PersonalInfoModifyView

urlpatterns = [
    #path('', views.index, name='index'),
    #path('personalInformations/<int:id>/', PersonalInformationsView.as_view()),
    path('personalInfo/<int:id>/', PersonalInfoView.as_view()),
    path('personalInfo/', PersonalInfoView.as_view()),
    #path('personalInformations/modify/<int:id>/', PersonalInformationsModifyView.as_view())
    path('personalInfo/modify/', PersonalInfoModifyView.as_view())
]