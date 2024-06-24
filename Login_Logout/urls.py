from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
  
  path('refferal/', views.ReffaralLinkView, name = 'refferal_link'),
  path('Register/', views.Register, name='Registerpage'),
  path('Login/', views.LoginView, name='loginpage'),
  path('Logout/', views.LogoutView, name='logoutpage'),
  path('Student-Profile/', views.view_Student_Profile, name='student_profile'),
  path('<str:ref_code>/',views.Refferal_code_generate, name = 'mainview'),
 
]
