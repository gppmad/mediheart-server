from django.urls import path
from . import views
from api.views.personalInformations import PersonalInformationsView,PersonalInformationsModifyView

urlpatterns = [
    #path('', views.index, name='index'),
    #path('v1/patients/', PatientsView.as_view()),
    path('personalInformations/<int:id>/', PersonalInformationsView.as_view()),
    path('personalInformations/modify/<int:id>/', PersonalInformationsModifyView.as_view())
]