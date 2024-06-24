# urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('mark-notifications-as-read/',views.mark_notifications_as_read, name='mark_notifications_as_read'),
    
]
