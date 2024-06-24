# urls.py

from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.Custom_admin_login, name='Custom_admin_loginPage'),
    path('Custom-Admin-Logout/', views.Admin_logout, name='Custom_admin_logout'),
    path('Admin-home-page/', views.Custom_Admin_Panel, name='custom_admin_panel'),
    path('toggle_message_status/', views.toggle_message_status, name='toggle_message_status'),
    path('Admin-Notifications/', views.All_type_notifications, name='admin_all_notifications'),
    path('Send-Message/', views.send_message, name='send_message'),
    path('Admin-ALL-Student-Send-Message/', views.All_Studnt_messege, name='AllStudent_messege'),
    path('Admin-ALL-Student-Send-Notifications/', views.All_student_notifications, name='Allstudent_notifications'),
    path('Admin-ALL-Student-Certificate/', views.Send_certificate_request, name='StudentCertificate'),
    path('Admin-ALL-Student-Certificate-Request/', views.Send_certificate, name='Send_certrequest'),
    
    # 1. Home Page Deshboard  all views code 
    # 1. নতুন খবর
    
    path('Admin-ALL-Student-News-Return/', views.Admin_News_forms_return, name='AdminNewsformsReturn'),
    path('Admin-ALL-Student-News-Request/', views.Admin_News_forms, name='AdminNewsforms'),
    path('Admin-ALL-Student-Popup-News-Request/', views.Popup_forms, name='popupforms'),
    
    # 2. ব্যানার
    path('Admin-ALL-Student-Banner-Return/', views.Banner_forms_Return, name='BannerformsReturn'),
    path('Admin-ALL-Student-Banner-Request/', views.Banner_forms, name='Bannerforms'),
    
    # 3. কোর্স ডিপার্টমেন্ট নাম
    path('Admin-ALL-Student-Categoy-Name-Return/', views.All_Category_model_forms_return, name='AllCategorymodel_forms_return'),
    path('Admin-ALL-Student-Category-Name-Request/', views.All_Category_model_forms, name='AllCategorymodelforms'),
    path('Admin-ALL-Student-Category-Image-Title-Request/', views.Category_Page_Header_image_text_forms, name='Category_image_text_forms'),
    
    # 4. জনপ্রিয় কোর্সসমূহ
    path('Categoy-Name-Wise-Card-Return/', views.All_Category_model_data_forms_return, name='Categorymodelwise_dataforms_return'),
    path('All-Course-Summery/', views.All_Category_model_data_forms, name='NameWiseCardReturn'),
    path('Categoy-Name-Wise-Card-Forms/', views.All_Category_Card_wise_data_forms, name='Card_wise_data_forms'),
    
    
    # 5. আমাদের বিশেষ সেবা সমূহ
    
    path('Our-Service-Return/', views.Our_services_return, name='Ourservicesreturn'),
    path('Our-Service-Forms/', views.Our_Service_Text_Image_forms, name='Our_Serviceforms'),
    path('Our-Service-Name-Forms/', views.Our_Service_Name_forms, name='Our_ServiceNameforms'),
    
    # 6. অংশ নিন ফ্রি সেমিনারে
    path('Free-Seminer-Return/', views.Free_seminer_Return, name='ourfreeseminerreturn'),
    path('Free-Seminer-Forms/', views.Seminer_time_forms, name='Seminertimeforms'),
    path('Our-Seminer-Name-Image-Forms/', views.Seminer_Image_text_forms, name='SeminerImageorms'),
 
    # 7. ইনস্টিটিউট ব্যানার
    path('Institute-Banner-Return/', views.Institute_banner_return, name='Institutebannerreturn'),
    path('Institute-Banner-Image-Forms/', views.Banner_right_imge_forms, name='Bannerright_imge_forms'),
    path('Institute-Banner-Image-Left-Forms/', views.Banner_Left_imge_forms, name='BannerLeft_imge_forms'),
 
    # 8. সফলতার গল্প
    path('Success-Story-Return/', views.Success_history_return, name='successstoryreturn'),
    path('Success-Story-Image-Video-forms/', views.Success_history_Video_Image_Forms, name='SuccessVideoImage_Forms'),
 
    #  9. ইভেন্ট এবং কার্যক্রম
    path('Event-Image-Return/', views.Event_Image_return, name='EventImageRetrun'),
    path('Event-Image-forms/', views.Event_Image_forms, name='EventImageForms'),
 
    # 10. আমাদের শিক্ষক সমূহ
    path('Teacher-Image-Return/', views.Teacher_return, name='Teacherreturn'),
    path('Teacher-Image-forms/', views.Teacher_Forms, name='TeacherForms'),
    
    # 11. শিক্ষার্থীদের মতামত
    path('Student-Return/', views.Student_Openion_return, name='StudentOpenioneturn'),
    path('Student-forms/', views.Student_Forms, name='StudentForms'),
     
    # 12.আমাদের পার্টনার
    path('Partner-Logo-Return/', views.Partner_Image_return, name='Partner_ImageReturn'),
    path('Partner-forms/', views.Partner_Image_forms, name='PartnerForms'),
    
    
    # 13. ফুটার অনন্যা বিষয়
    path('Footer-Return/', views.Footer_return, name='FooterReturn'),
    path('Footer-Form/', views.Footer_forms, name='Footerforms'),
    path('Footer-Title-Form/', views.Footer_Title_Wise_forms, name='FooterTitleWise_forms'),
    
    
    
    
    # 14. ইনস্টিটিউট লাইসেন্স
    path('Licence-Return/', views.Licence_return, name='Licencereturn'),
    path('Licence-Forms/', views.Licence_Forms, name='LicenceForms'),
    
    
    
    # 2.Card Wise Data Show 
    # 1. কোর্স ওভারভিউ টেক্সট
    
    path('Course-overview-Return/', views.Course_overview_Return, name='Course_oveReturn'),
    path('Course-overview-Forms/', views.Course_overview_Forms, name='Courseoverviewforms'),
    
    
    
    # 2. কোর্সের বিস্তারিত
    path('Course-Detials-Return/', views.Course_Detials_Return, name='Course_DetialsReturn'),
    path('Course-Detials-Forms/', views.Course_Detials_Forms, name='CourseDetialsForms'),
    path('Course-Detials-Title-Wise-Forms/', views.Course_Detials_ALL_Data_Forms, name='Course_DetialsForms'),
    
    
    # 3. কোর্সের উদ্দেশ্যে

    path('Course-Purpose-Return/', views.Course_Purpose_Return, name='CoursePurposeReturn'),
    path('Course-Purpose-Forms/', views.Course_Purpose_Forms, name='CoursePurposeForms'),
    
    
    # 4. কোর্সের পরিপূর্ণ কারিকুলাম
    path('Course-Full-Curryculam-Return/', views.Course_full_curryculam_Return, name='Course_fullcuryReturn'),
    path('Course-Purpose-Forms/', views.Course_Purpose_Forms, name='CoursePurposeForms'),
    
    
    # 5. কোর্সের প্রজেক্ট এর ছবি
    path('Course-Project-Image-Return/', views.Course_Project_image_Return, name='CourseProjectimage'),
    path('Course-Project-Image-Forms/', views.Course_Project_image_Forms, name='Course_ProjectimageForms'),
    
    
    
    
    
    # 6. শিক্ষার্থীদের মতামত
    path('Student-Feedback-Return/', views.Student_Feedback_Return, name='StudentFeedbackReturn'),
    path('Student-Feedback-Forms/', views.Student_Feedback_Forms, name='StudentFeedbackforms'),
    
    
    # 7. কোর্সের শিক্ষক সম্পর্কে
    path('Teacher-About-Return/', views.Course_Teacher_about_Return, name='Course_TeacheraboutReturn'),
    path('Teacher-About-Forms/', views.Course_Teacher_about_Forms, name='TeacherAbout_forms'),
    

      
    # 8. কোর্স সম্বন্ধে শিক্ষার্থীদের প্রশ্ন     
    path('Student-Question-Return/', views.Course_Student_Question_Return, name='Course_StudentQuestionReturn'),
    path('Student-Question-Forms/', views.Course_Student_Question_Forms, name='Course_Student_QuestionForms'),
    
    
    
    # 9. এই কোর্সের ভেতরে যা যা রয়েছে
    path('Which-Learn-Return/', views.Which_learn_you_Return, name='Which_learnReturn'),
    path('Which-Learn-Forms/', views.Which_learn_you_forms, name='Which_learn_forms'),
    



    
# Betch All Data

    # 1. নতুন ব্যাচ তৈরি করুন

    path('Create-new-batch-return/', views.Create_new_batch_return, name='Create_newbatchreturn'),
    path('Create-new-batch-Forms/', views.Create_new_batch_forms, name='Createbatchforms'),
    path('Select-batch-wise-student-Forms/', views.Batch_wise_student_select_forms, name='Batch_wise_stu_select_forms'),
    path('Batch-wise-time-set-Forms/', views.Batch_wise_time_set, name='Batch_wise_timeset'),
    
    


    # 2. সবগুলো কোর্স এর ব্যাচসমূহ
    path('All-course-batchs-data-return/', views.All_course_batches_return, name='All_coursebatchesreturn'),
    path('All-course-batchs-data-return/<str:batch_id>/', views.All_course_batches_return, name='All_coursebatchesreturn_with_id'),
    
    
    

    # Teacher Site Batch Data
    
    # 1. ব্যাচ ভিত্তিক ক্লাস সমূহ
    path('Batch-wise-class-time-return/', views.batch_wise_class_return, name='batch_wiseclassreturn'),
    path('Batch-wise-class-time-forms', views.Batch_wise_Class_Create_forms, name='Batch_wise_ClassCreateforms'),
    
    
    # 2. ব্যাচ ভিত্তিক মেসেজ
    path('Batch-wise-message-return/', views.batch_wise_message_return, name='batch_wisemessagereturn'),
    path('Batch-wise-message-forms', views.Batch_wise_message_forms, name='Batch_wise_messageforms'),
    
    
    
# 3. ব্যাচ ভিত্তিক এক্সাম এবং অ্যাসাইনমেন্ট

    path('Batch-wise-exam-assingmet-return/', views.batch_wise_exam_assingtmet_return, name='batch_wise_exam_return'),
    path('Exam-Assingment-forms', views.Exam_assingment_forms, name='Exam_assingmentforms'),
    path('Exam-Result-forms', views.Assingment_result_forms, name='Assingmentresultforms'),
    
    
    
    


    # Teacher Personal Site

    # 1. টিচার ভিত্তিক স্টুডেন্ট ডাটা

    path('teacher-wise-student-data-return', views.teacher_wise_student_data_return, name='teacher_wise_student_datareturn'),
    path('teacher-wise-student-data-show-return/<str:batch_id>/', views.teacher_wise_student_data_return, name='teacher_wise_student_datareturn'),
    path('teacher-wise-student-attendence-show-return/', views.student_absent_forms, name='student_absentforms'),
    
    # 2. টিচার ভিত্তিক স্টুডেন্ট এসাইনমেন্ট
    
    path('teacher-wise-student-assingment-return', views.teacher_wise_student_assingment_return, name='teacher_wisestudentassingment'),
    



    
 ]
