from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [

    path('doctor/service_form/', views.ServiceFormView.as_view(), name='doctor_service_form'),
    
   
]