from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('Course-Detail-Page/<int:id>/',views.CourseDetailsPage, name='CourseDetailsPage'),
    path('Contract-Phone-Number-return/', views.contract_phone_return, name = 'contract_phonereturn'),
    path('Contract-Phone-Number-forms/', views.contract_phone_forms, name = 'contract_phoneforms')
   
]
 