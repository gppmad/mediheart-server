from django.urls import path
from . import views
from api.views.persInfo import PersInfoView,PersInfoModifyView

urlpatterns = [
    #path('', views.index, name='index'),
    #path('personalInformations/<int:id>/', PersonalInformationsView.as_view()),
    path('personal-info/<int:id>/', PersInfoView.as_view()),
    #path('personalInformations/modify/<int:id>/', PersonalInformationsModifyView.as_view())
    path('personal-info/modify/', PersInfoModifyView.as_view())
]