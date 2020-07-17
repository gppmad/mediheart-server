from django.urls import path
from . import views
from api.views.personalInfo import PersonalInfoView,PersonalInfoModifyView

urlpatterns = [
    #path('', views.index, name='index'),
    #path('personalInformations/<int:id>/', PersonalInformationsView.as_view()),
    path('personal-info/<int:id>/', PersonalInfoView.as_view()),
    path('personal-info/', PersonalInfoView.as_view()),
    #path('personalInformations/modify/<int:id>/', PersonalInformationsModifyView.as_view())
    path('personal-info/modify/', PersonalInfoModifyView.as_view())
]