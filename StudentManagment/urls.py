"""
URL configuration for StudentManagment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .  import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Admin-Panel/', include('Custom_Admin_panel.urls')),
    path('', include('Deshboard.urls')),
    path('Home-Page/', include('HomePage.urls')),
    path('Second-Page/', include('Home_Page_Two.urls')),
    path('Login-Logout/', include('Login_Logout.urls')),
    path('Student-Profile/', include('Student_Profile.urls')),
    path('Student-Social-Media/', include('Social_Media.urls')),
    
    # project under views
    # path('Notification', views.notiview, name='notifications_view'),
    # path('message/', views.message_show, name='messageShow'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)