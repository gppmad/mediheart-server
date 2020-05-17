from django.urls import path
from . import views
from api.views import PatientsView

urlpatterns = [
    #path('', views.index, name='index'),
    path('patients/', PatientsView.as_view()),
]