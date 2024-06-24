from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
  
   path("All-Course-Page/", views.All_course_Page_views, name= 'All_Course_Page'),
   path("Seminer-page/",views.Seminer_Page_views, name='seminer_page'),
   path('category/<slug:category_slug>/',views.Seminer_Page_views, name = 'seminer_page_category'),
    
]
