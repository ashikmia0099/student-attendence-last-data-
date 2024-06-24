from django.contrib import admin
from .  import views 
from django.urls import path


 

urlpatterns = [ 
    path('Student-Information/', views.Student_info, name='student_info'),
    path('Update-student-info/', views.ChangeInfo, name='student_dataUpdate'),
    path('Student-Certificate/', views.Student_Certificate_view, name='certificate'),
    path('Announcement/', views.Announcement_view, name='announcementpath'),
    path('Announcement/<int:message_id>', views.Announcement_message, name='announcementid'),
    path('My-Class/', views.my_class, name='myclass'),
    path('Exam-Assingment/', views.Exam_and_Assingment, name='Exam_andAssingment'),
    path('message-show/', views.message_show, name='messageshow'),
    path('update_attendance/', views.update_attendance, name='update_attendance'),




]