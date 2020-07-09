from django.urls import path
from . import views
from api.views.personalInformations import PersonalInformationsView,PersonalInformationsModifyView

urlpatterns = [
    #path('', views.index, name='index'),
    path('personalInformations/<int:id>/', PersonalInformationsView.as_view()),
    #path('personalInformations/modify/<int:id>/', PersonalInformationsModifyView.as_view())
    path('personalInformations/modify/', PersonalInformationsModifyView.as_view())
]