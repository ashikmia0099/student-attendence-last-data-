from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='homepage'),
    path('category/<slug:category_slug>/', views.HomeView, name='cattegory_wise_sort'),
    path('Category-Page/<int:id>/', views.detail_category_page, name='category_page'),
    
    
    # contract us form
    path('Contract-Us-Return/', views.Contract_us_forms_reqturn, name='contract_us_return'),
    path('Contract-Us-Forms/', views.Contract_us_forms_view, name='contraactusforms'),
    
     
    
]

