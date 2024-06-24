from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Count
from django.core.paginator import Paginator


from Deshboard.models import BannerModel,All_category_text,All_Category_model,All_Category_Card_Data,HomeOurService, Our_Service_Text,HomeInstituteBanner,HomeInstituteBannersecond,Success_history_video,HomeEvent,HomeExpertTeacher,HomeStudentOpenion,our_partner

from Home_Page_Two.models import Course_Title, All_course_data_header_name,Course_All_Data,Puropse_of_course, Project_image, Student_openion, Teacher_About, Student_Question, Learning_Topic, Module_Week,Module_Name_Number,Module_Video_And_PDF

from HomePage.models import Navbar_text, Footer_other_detail_header,Header_li , Footer_Last_section

# category Page model
from HomePage.models import CourseInfo, Seminer_Time, Seminer_Image_Text

from Login_Logout.models import  User,Profile
from Social_Media.models import Notification,Popup_banner,ContractUs_Form

from Student_Profile.models import Student_Certificate, Student_image

from .models import Create_Batch,Batch_time_set,Student_Attendance, Batch_wise_Student_Select, Meet_link,batch_wise_message,Batch_wise_Assingment,Assingment_result




# এখানে আমি একজন ইউজার login করার জন্য ভিউস এর কোড করসি

    
def Custom_admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(email = email, password = password)
            
            if user is not None:
                if user.is_staff:
                    login(request,user)
                    messages.success(request, f' welcome {user.first_name} {user.last_name} !!')
                    return redirect('admin_all_notifications')
                
                else:
                    messages.success(request,'You are not staff')
                    return redirect('Custom_admin_loginPage')
            
            else:
                messages.error(request,'Login info is  incorret')
        else:
            messages.error(request,'This Data is not valid. Please try again. ')
    else:
        form = AuthenticationForm()
        
    return render(request, 'admin_login.html', {'form':form})


 

# এখানে আমি একজন ইউজার Logout করার জন্য ভিউস এর কোড করসি

@login_required
def Admin_logout(request):
    user = request.user
    logout(request)
    messages.success(request, f'{user.first_name} {user.last_name} is successfully logged out.')
    return redirect('Custom_admin_loginPage')







@login_required
def Custom_Admin_Panel(request):
    # Form Data Show
    form_dat = ContractUs_Form.objects.all().order_by('-created_at')
    
    # Paginate form data with 3 items per page
    paginator = Paginator(form_dat, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Total Staff number
    stafcount = User.objects.filter(is_staff=True).count()
    
    # Total Department
    depatment = All_Category_model.objects.all().count()
    
    # Total Course
    totalCourse = All_Category_Card_Data.objects.all().count()
    
    # Total Student
    total_student = User.objects.all().count()
    
    return render(request, 'Admin_homepage.html', {
        'page_obj': page_obj, 
        'department': depatment,
        'stafcount': stafcount,
        'totalCourse': totalCourse,
        'total_student': total_student,
    })

 



@login_required
@csrf_exempt
def toggle_message_status(request):
    if request.method == 'POST':
        message_id = request.POST.get('id')
        message = ContractUs_Form.objects.get(id=message_id)
        if not message.message_seen:
            message.message_seen = True
            message.save()
            return JsonResponse({'status': 'completed'})
        return JsonResponse({'status': 'already_completed'})
    return JsonResponse({'status': 'error'}, status=400)



# এখানে স্টুডেন্ট এর ইমেইল  সিলেক্ট করে মেসেজ পাঠানো হলো 
@login_required
def All_type_notifications(request):
    
    return render(request, 'Admin_notification.html')
    
    

# এখানে স্টুডেন্ট এর ইমেইল  সিলেক্ট করে মেসেজ পাঠানো হলো 
@login_required
def send_message(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message_text = request.POST.get('message')

        try:
            user = User.objects.get(email=email)
            Notification.objects.create(user=user, message=message_text)
            messages.success(request, 'Message Sent Successfully')
            return redirect('admin_all_notifications')
        except User.DoesNotExist:
            messages.error(request, 'This user does not exist')
            return redirect('admin_all_notifications')

    else:
        messages.error(request, 'Invalid request method')
        return redirect('admin_all_notifications')
    





# এখানে সকল message স্টুডেন্টকে পাঠানো হলো 
@login_required
def All_Studnt_messege(request):
    
    if request.method == 'POST':
        text_message = request.POST.get('message')
        if text_message:
            users = User.objects.all()
            for user in users:
                Notification.objects.create(user = user, message = text_message)
                
            return redirect('admin_all_notifications')
    return redirect('admin_all_notifications')
    
     
     
    
    
# এখানে সকল স্টুডেন্টকে পাঠানো হলো
@login_required
def All_student_notifications(request):
    
    return render(request, 'Admin_notification.html')
    
    
    
# স্টুডেন্ট এর সার্টিফিকেট এর জন্য কোড লেখা হলো
@login_required
def Send_certificate_request(request):
    
    return render(request, 'Teacher_Site_Batch_Data/4_admin_certificate.html')



@login_required
def Send_certificate(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        certificate_file = request.FILES.get('Certificate')

        try:
            user = User.objects.get(email=email)
            student_certificate, created = Student_Certificate.objects.get_or_create(user=user)
            student_certificate.Certificate = certificate_file
            student_certificate.save()
            messages.success(request, 'Certificate Sent Successfully')
            return redirect('StudentCertificate')
        except User.DoesNotExist:
            messages.error(request, 'This user does not exist')
            return redirect('StudentCertificate')
    else:
        messages.error(request, 'Invalid request method')
        return redirect('StudentCertificate')
    


# 1. Home Page Deshboard  all views code 

# 1. নতুন খবর

@login_required
def Admin_News_forms(request):
    
    if request.method == 'POST':
        new_news = request.POST.get('Text')
        if new_news:
            
            Navbar_text.objects.create( Text = new_news)
            messages.success(request, 'Your News Has Been Successfully Created')
                
            return redirect('AdminNewsformsReturn')
    else:
        messages.error(request, 'Your News Has Been Invalid')
        return redirect('AdminNewsformsReturn')
 
 
    
@login_required
def Admin_News_forms_return(request):
    
    return render(request, 'home_page_deshboard/1_new_news.html')
    
    
@login_required
def Popup_forms(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        is_read = request.POST.get('is_read')

        # Convert the is_read value to a boolean
        is_read = is_read is not None and is_read.lower() in ['true', '1', 'yes', 'on']

        try:
            Popup_banner.objects.create(
                message=message,
                is_read=is_read,
            )
            
            messages.success(request, 'Popup news Sent Successfully')
            return redirect('AdminNewsformsReturn')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('AdminNewsformsReturn')
    else:
        messages.error(request, 'Invalid request method')
        return redirect('AdminNewsformsReturn')

    
# 2. ব্যানার
    
@login_required
def Banner_forms(request):
    
    if request.method == 'POST':
        Bannertitle = request.POST.get('Banner_title')
        Bannertext = request.POST.get('Banner_text')
        Bannervideo_image = request.FILES.get('Banner_video_image')
        Bannervideo = request.FILES.get('Banner_video')

        try:
            
            BannerModel.objects.create(
                Banner_title = Bannertitle,
                Banner_text = Bannertext,
                Banner_video_image = Bannervideo_image,
                Banner_video = Bannervideo
            )
            
            messages.success(request, ' Sent Successfully')
            return redirect('StudentCertificate')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('BannerformsReturn')
    else:
        messages.error(request, 'Invalid request method')
        return redirect('StudentCertificate')
    
    
@login_required
def Banner_forms_Return(request):
    
    return render(request, 'home_page_deshboard/2_banner.html')
    
    
# 3. কোর্স ডিপার্টমেন্ট নাম

@login_required
def All_Category_model_forms_return(request):
    
    return render(request, 'home_page_deshboard/3_course_department.html')


@login_required
def All_Category_model_forms(request):
    if request.method == 'POST':
        CategoryName = request.POST.get('Category_Name')
        slug = request.POST.get('slug')
        CategoryImage = request.FILES.get('Category_Image')
       
        try:
            
            All_Category_model.objects.create(
                Category_Name = CategoryName,
                slug = slug,
                Category_Image = CategoryImage,
                
            )
            
            messages.success(request, ' Sent Successfully')
            return redirect('AllCategorymodel_forms_return')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('AllCategorymodel_forms_return')
    else:
        messages.error(request, 'Invalid request method')
        return redirect('AllCategorymodel_forms_return')
    
    


@login_required
def Category_Page_Header_image_text_forms(request):
    
    if request.method == 'POST':
        Category = request.POST.get('Category')
        Category_summery_text = request.POST.get('Category_summery_text')
        Category_image = request.FILES.get('Category_image')
  
        try:
            catname = All_Category_model.objects.get(Category_Name=Category)
            
            CourseInfo.objects.create(
                Category=catname,
                Category_summery_text = Category_summery_text,
                Category_image = Category_image,
               
            )
            
            messages.success(request, 'Category Title Create Successfully')
            return redirect('AllCategorymodel_forms_return')
        
        except All_Category_model.DoesNotExist:
            messages.error(request, 'This Departname does not exist')
            return redirect('AllCategorymodel_forms_return')
        
    else:
        messages.error(request, 'Invalid request method')
        return redirect('AllCategorymodel_forms_return')
    
    


# 4. জনপ্রিয় কোর্সসমূহ

@login_required
def All_Category_model_data_forms(request):
    
    if request.method == 'POST':
        text = request.POST.get('Cattegory_top_text')
        if text:
            
            All_category_text.objects.create( Cattegory_top_text = text)
            messages.success(request, 'Text Added Successfully')
            return redirect('Categorymodelwise_dataforms_return')
        else:
            messages.error(request, 'Text Added Failurefully')
            return redirect('Categorymodelwise_dataforms_return')
    else:
        pass
    return redirect('Categorymodelwise_dataforms_return')



@login_required
def All_Category_model_data_forms_return(request):
    
    return render(request, 'home_page_deshboard/4_famous_course.html')


# 4.1 জনপ্রিয় কোর্সসমূহ
@login_required
def All_Category_Card_wise_data_forms(request):
    
    if request.method == 'POST':
        CategoryName = request.POST.get('Category_Name')
        Image = request.FILES.get('Image')
        Course_name = request.POST.get('Course_name')
        student_review = request.POST.get('student_review')
        Course_fees = request.POST.get('Course_fees')
        
        
        try:
            catname = All_Category_model.objects.get(Category_Name=CategoryName)
            
            All_Category_Card_Data.objects.create(
                Category_Name=catname,
                Image = Image,
                Course_name = Course_name,
                student_review = student_review,
                Course_fees = Course_fees
            )
            
            messages.success(request, 'Course Create Successfully')
            return redirect('Categorymodelwise_dataforms_return')
        
        except All_Category_model.DoesNotExist:
            messages.error(request, 'This Departname does not exist')
            return redirect('Categorymodelwise_dataforms_return')
        
    else:
        messages.error(request, 'Invalid request method')
        return redirect('Categorymodelwise_dataforms_return')
    
    
    
# 5. আমাদের বিশেষ সেবা সমূহ
@login_required
def Our_services_return(request):
    
    return render(request, 'home_page_deshboard/5_our_service.html')

@login_required
def Our_Service_Text_Image_forms(request):
    if request.method == 'POST':
        service_text = request.POST.get('service_text')
        
        Image = request.FILES.get('Image')
       
        try:
            
            Our_Service_Text.objects.create(
                service_text = service_text,
                
                Image = Image,
                
            )
            
            messages.success(request, ' Service Text And Image Sent Successfully')
            return redirect('Ourservicesreturn')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('Ourservicesreturn')
    else:
        messages.error(request, 'Invalid request method')
        return redirect('Ourservicesreturn')
    

@login_required
def Our_Service_Name_forms(request):
    
    if request.method == 'POST':
        service_name = request.POST.get('service_name')
        if service_name:
            
            HomeOurService.objects.create( service_name = service_name)
            messages.success(request, 'Your service name has been Created')
                
            return redirect('Ourservicesreturn')
    else:
        messages.error(request, 'Your requsted is invalid')
        return redirect('Ourservicesreturn')


# 6. অংশ নিন ফ্রি সেমিনারে

@login_required
def Free_seminer_Return(request):
    
    return render(request, 'home_page_deshboard/6_join_seminer.html')

@login_required
def Seminer_time_forms(request):
    
    if request.method == 'POST':
        day = request.POST.get('day')
        month_Year = request.POST.get('month_Year')
        seminer_subject = request.POST.get('seminer_subject')
        seminer_time = request.POST.get('seminer_time')
        
        try:
            Seminer_Time.objects.create(
                day = day,
                month_Year = month_Year,
                seminer_subject = seminer_subject,
                seminer_time = seminer_time
            )
            
            messages.success(request, 'Seminer Time Create Successfully')
            return redirect('ourfreeseminerreturn')
        
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('ourfreeseminerreturn')
        
    else:
        messages.error(request, 'Invalid request method')
        return redirect('ourfreeseminerreturn')
    
@login_required
def Seminer_Image_text_forms(request):
    
    if request.method == 'POST':
        seminer_text = request.POST.get('seminer_text')
        Seminer_image = request.FILES.get('Seminer_image')
        
        
        try:
            Seminer_Image_Text.objects.create(
                seminer_text = seminer_text,
                Seminer_image = Seminer_image,
                
            )
            
            messages.success(request, 'Seminer Text and Image Create Successfully')
            return redirect('ourfreeseminerreturn')
        
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('ourfreeseminerreturn')
        
    else:
        messages.error(request, 'Invalid request method')
        return redirect('ourfreeseminerreturn')
    
    
# 7. ইনস্টিটিউট ব্যানার
@login_required
def Institute_banner_return(request):
    return render(request, 'home_page_deshboard/7_institute_banner.html')
    

@login_required
def Banner_right_imge_forms(request):
    
    if request.method == 'POST':
        BannerTitle = request.POST.get('BannerTitle')
        BannerText = request.POST.get('BannerText')
        Banner_image = request.FILES.get('Banner_image')
        
        
        try:
            HomeInstituteBanner.objects.create(
                BannerTitle = BannerTitle,
                BannerText = BannerText,
                Banner_image = Banner_image,
               
            )
            
            messages.success(request, 'Banner Right Data Saved Successfully Created.')
            return redirect('Institutebannerreturn')
        
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('Institutebannerreturn')
        
    else:
        messages.error(request, 'Invalid Request Failed')
        return redirect('Institutebannerreturn')
    
    
    
@login_required
def Banner_Left_imge_forms(request):
    
    if request.method == 'POST':
        Banner_Title = request.POST.get('Banner_Title')
        Banner_Text = request.POST.get('Banner_Text')
        Banner_image = request.FILES.get('Banner_image')
        
        
        try:
            HomeInstituteBannersecond.objects.create(
                Banner_Title = Banner_Title,
                Banner_Text = Banner_Text,
                Banner_image = Banner_image,
               
            )
            
            messages.success(request, 'Banner Left Data Saved Successfully Created.')
            return redirect('Institutebannerreturn')
        
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('Institutebannerreturn')
        
    else:
        messages.error(request, 'Invalid Request Failed')
        return redirect('Institutebannerreturn')
    
    
# 8. সফলতার গল্প
@login_required
def Success_history_return(request):
    
    return render(request, 'home_page_deshboard/8_success_history.html')




@login_required
def Success_history_Video_Image_Forms(request):
    if request.method == 'POST':
        Success_history_text = request.POST.get('Success_history_text')
        Success_history_image = request.FILES.get('Success_history_image')
        Success_Video_history = request.FILES.get('Success_Video_history')
        
        try:
            Success_history_video.objects.create(
                Success_history_text=Success_history_text,
                Success_history_image=Success_history_image,
                Success_Video_history=Success_Video_history,
            )
            messages.success(request, 'Success Story Successfully Created.')
            return redirect('successstoryreturn')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('successstoryreturn')
    else:
        messages.error(request, 'Invalid Request Failed')
        return redirect('successstoryreturn')



# 9. ইভেন্ট এবং কার্যক্রম

@login_required
def Event_Image_return(request):
    
    return render(request, 'home_page_deshboard/9_event_and_acctivities.html')


@login_required
def Event_Image_forms(request):
    
    if request.method == 'POST':
        Event_image = request.FILES.get('Event_image')
        if Event_image:
            
            HomeEvent.objects.create( Event_image = Event_image)
            messages.success(request, 'Image Show Successfully Created')
                
            return redirect('EventImageRetrun')
    else:
        messages.error(request, 'This Request Has Been Invalid')
        return redirect('EventImageRetrun')
    
    
    
# 10. আমাদের শিক্ষক সমূহ
@login_required
def Teacher_return(request):
    
    return render(request, 'home_page_deshboard/10_our_teacher.html')


@login_required
def Teacher_Forms(request):
    if request.method == 'POST':
        Teacher_name = request.POST.get('Teacher_name')
        Position_name = request.POST.get('Position_name')
        institute_name = request.POST.get('institute_name')
        Teacher_image = request.FILES.get('Teacher_image')
        
        
        try:
            HomeExpertTeacher.objects.create(
                Teacher_name=Teacher_name,
                Position_name=Position_name,
                institute_name=institute_name,
                Teacher_image=Teacher_image,
            )
            messages.success(request, 'Teacher Successfully Created.')
            return redirect('Teacherreturn')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('Teacherreturn')
    else:
        messages.error(request, 'Invalid Request Failed')
        return redirect('Teacherreturn')


# 11. শিক্ষার্থীদের মতামত

@login_required
def Student_Openion_return(request):
    
    return render(request, 'home_page_deshboard/11_student_review.html')


@login_required
def Student_Forms(request):
    if request.method == 'POST':
        Student_name = request.POST.get('Student_name')
        openion_course_name = request.POST.get('openion_course_name')
        Openion_text = request.POST.get('Openion_text')
        Student_image = request.FILES.get('Student_image')
        
        
        try:
            HomeStudentOpenion.objects.create(
                Student_name=Student_name,
                openion_course_name=openion_course_name,
                Openion_text=Openion_text,
                Student_image=Student_image,
            )
            messages.success(request, 'Student Openion Successfully Created.')
            return redirect('StudentOpenioneturn')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('StudentOpenioneturn')
    else:
        messages.error(request, 'Invalid Request Failed')
        return redirect('StudentOpenioneturn')


# 12.আমাদের পার্টনার


@login_required
def Partner_Image_return(request):
    
    return render(request, 'home_page_deshboard/12_our_partner.html')


@login_required
def Partner_Image_forms(request):
    
    if request.method == 'POST':
        Prather_Logo = request.FILES.get('Prather_Logo')
        if Prather_Logo:
            
            our_partner.objects.create( Prather_Logo = Prather_Logo)
            messages.success(request, 'Prather Logo Successfully Created')
                
            return redirect('Partner_ImageReturn')
    else:
        messages.error(request, 'This Request Has Been Invalid')
        return redirect('Partner_ImageReturn')
    
    
# 13. ফুটার অনন্যা বিষয়

@login_required
def Footer_return(request):
    
    return render(request, 'home_page_deshboard/13_footer_other_detials.html')




@login_required
def Footer_forms(request):
    
    if request.method == 'POST':
        Header_Name = request.POST.get('Header_Name')
        if Header_Name:
            
            Footer_other_detail_header.objects.create( Header_Name = Header_Name)
            messages.success(request, 'Title Has Been Successfully Created')
                
            return redirect('FooterReturn')
    else:
        messages.error(request, 'Title Has Been Invalid')
        return redirect('FooterReturn')




@login_required
def Footer_Title_Wise_forms(request):
    
    if request.method == 'POST':
        HeaderChoice = request.POST.get('HeaderChoice')
        
        List_Data = request.POST.get('List_Data')
        
        
        try:
            ChoiceHeaderName = Footer_other_detail_header.objects.get(Header_Name=HeaderChoice)
            
            Header_li.objects.create(
                HeaderChoice=ChoiceHeaderName,
                List_Data = List_Data,
               
            )
            
            messages.success(request, 'Data Push Successfully')
            return redirect('FooterReturn')
        
        except Footer_other_detail_header.DoesNotExist:
            messages.error(request, 'This title does not exist')
            return redirect('FooterReturn')
        
    else:
        messages.error(request, 'Invalid request method')
        return redirect('FooterReturn')
    
    


# 14. ইনস্টিটিউট লাইসেন্স

@login_required
def Licence_return(request):

    return render(request, 'home_page_deshboard/14_institute_licence.html')



@login_required
def Licence_Forms(request):
    if request.method == 'POST':
        copyright_text = request.POST.get('copyright_text')
        licence_number = request.POST.get('licence_number')
        Institute_Logo = request.FILES.get('Institute_Logo')
        
        
        try:
            Footer_Last_section.objects.create(
                copyright_text=copyright_text,
                licence_number=licence_number,
                Institute_Logo=Institute_Logo,
                
            )
            messages.success(request, 'Copyrigh Warning Successfully Created.')
            return redirect('Licencereturn')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('Licencereturn')
    else:
        messages.error(request, 'Invalid Request Failed')
        return redirect('Licencereturn')


    
    
# 2. Card Wise Data Show Views Code

# 1. কোর্স ওভারভিউ টেক্সট

@login_required
def Course_overview_Return(request):

    return render(request, 'Card_wise_data_show/1_course_overview_text.html')


@login_required
def Course_overview_Forms(request):
    
    if request.method == 'POST':
        chooes_Course = request.POST.get('chooes_Course')
        Course_about_text = request.POST.get('Course_about_text')
        course_image = request.FILES.get('course_image')
        video = request.FILES.get('video')
        
        
        try:
            CourseName = All_Category_Card_Data.objects.get(Course_name=chooes_Course)
            
            Course_Title.objects.create(
                chooes_Course=CourseName,
                Course_about_text = Course_about_text,
                course_image = course_image,
                video = video,
               
            )
            
            messages.success(request, 'Course Title Created Successfully')
            return redirect('Course_oveReturn')
        
        except Course_Title.DoesNotExist:
            messages.error(request, 'This title does not exist')
            return redirect('Course_oveReturn')
        
    else:
        messages.error(request, 'Invalid request method')
        return redirect('Course_oveReturn')
    
    

    
# 2. কোর্সের বিস্তারিত
    
    

@login_required
def Course_Detials_Return(request):

    return render(request, 'Card_wise_data_show/2_Course_details.html')


@login_required
def Course_Detials_Forms(request):
    
    if request.method == 'POST':
        chooes_Category = request.POST.get('chooes_Category')
        Header_Name = request.POST.get('Header_Name')
       
        
        
        try:
            CourseName = All_Category_Card_Data.objects.get(Course_name=chooes_Category)
            
            All_course_data_header_name.objects.create(
                chooes_Category=CourseName,
                Header_Name = Header_Name,
                
               
            )
            
            messages.success(request, 'Course Title Created Successfully')
            return redirect('Course_DetialsReturn')
        
        except All_course_data_header_name.DoesNotExist:
            messages.error(request, 'This course name does not exist')
            return redirect('Course_DetialsReturn')
        
    else:
        messages.error(request, 'Invalid request method')
        return redirect('Course_DetialsReturn')
    
    
    
@login_required
def Course_Detials_ALL_Data_Forms(request):
    
    if request.method == 'POST':
        chooes_Category = request.POST.get('chooes_Category')
        choose_Header_Name = request.POST.get('choose_Header_Name')
        Left_text = request.POST.get('Left_text')
        Right_text = request.POST.get('Right_text')
       
        
        
        try:
            CourseName = All_Category_Card_Data.objects.get(Course_name=chooes_Category)     
            
            headerNames= All_course_data_header_name.objects.filter(Header_Name=choose_Header_Name)    
            
            for headername in headerNames:
                            
                Course_All_Data.objects.create(
                    chooes_Category=CourseName,
                    choose_Header_Name = headername,
                    Left_text=Left_text,
                    Right_text = Right_text,
                    
                    
                )
            
            messages.success(request, 'Header Wise Data Push Successfully')
            return redirect('Course_DetialsReturn')
        
        except All_Category_Card_Data.DoesNotExist:
            messages.error(request, 'This  does not exist')
            return redirect('Course_DetialsReturn')
        
    else:
        messages.error(request, 'Invalid request method')
        return redirect('Course_DetialsReturn')
    
    
    
# 3. কোর্সের উদ্দেশ্যে


@login_required
def Course_Purpose_Return(request):

    return render(request, 'Card_wise_data_show/3_Course_objectives.html')


@login_required
def Course_Purpose_Forms(request):
    
    if request.method == 'POST':
        chooes_Category = request.POST.get('chooes_Category')
        Purpose_Text = request.POST.get('Purpose_Text')
        Image = request.FILES.get('Image')
       
        
        
        try:
            CourseName = All_Category_Card_Data.objects.get(Course_name=chooes_Category)
            
            Puropse_of_course.objects.create(
                chooes_Category=CourseName,
                Purpose_Text = Purpose_Text,
                Image = Image,
                
               
            )
            
            messages.success(request, 'Purpose Created Successfully')
            return redirect('Course_DetialsReturn')
        
        except All_Category_Card_Data.DoesNotExist:
            messages.error(request, 'This course name does not exist')
            return redirect('Course_DetialsReturn')
        
    else:
        messages.error(request, 'Invalid request method')
        return redirect('Course_DetialsReturn')
    
    
# 4. কোর্সের পরিপূর্ণ কারিকুলাম
    
@login_required
def Course_full_curryculam_Return(request):

    return render(request, 'Card_wise_data_show/4_Full_curriculum.html')


@login_required
def Course_full_curryculam_Forms(request):
    
    if request.method == 'POST':
        chooes_Category = request.POST.get('chooes_Category')
        Purpose_Text = request.POST.get('Purpose_Text')
        Image = request.FILES.get('Image')
       
        
        
        try:
            CourseName = All_Category_Card_Data.objects.get(Course_name=chooes_Category)
            
            Puropse_of_course.objects.create(
                chooes_Category=CourseName,
                Purpose_Text = Purpose_Text,
                Image = Image,
                
               
            )
            
            messages.success(request, 'Purpose Created Successfully')
            return redirect('Course_DetialsReturn')
        
        except All_Category_Card_Data.DoesNotExist:
            messages.error(request, 'This course name does not exist')
            return redirect('Course_DetialsReturn')
        
    else:
        messages.error(request, 'Invalid request method')
        return redirect('Course_DetialsReturn')
    
    
    
# 5. কোর্সের প্রজেক্ট এর ছবি

@login_required
def Course_Project_image_Return(request):

    return render(request, 'Card_wise_data_show/5_course_project.html')


@login_required
def Course_Project_image_Forms(request):
    
    if request.method == 'POST':
        chooes_Category = request.POST.get('chooes_Category')
        image = request.FILES.get('image')
       
        
        
        try:
            CourseName = All_Category_Card_Data.objects.get(Course_name=chooes_Category)
            
            Project_image.objects.create(
                chooes_Category=CourseName,
                image = image,
                
               
            )
            
            messages.success(request, 'Image Send Successfully')
            return redirect('CourseProjectimage')
        
        except All_Category_Card_Data.DoesNotExist:
            messages.error(request, 'This course name does not exist')
            return redirect('CourseProjectimage')
        
    else:
        messages.error(request, 'Invalid request method')
        return redirect('CourseProjectimage')
    
    


# 6. শিক্ষার্থীদের মতামত

@login_required
def Student_Feedback_Return(request):

    return render(request, 'Card_wise_data_show/6_student_feedback.html')



@login_required
def Student_Feedback_Forms(request):
    
    if request.method == 'POST':
        chooes_Category = request.POST.get('chooes_Category')
        Student_name = request.POST.get('Student_name')
        Openion_text = request.POST.get('Openion_text')
        Student_image = request.FILES.get('Student_image')
       
        
        
        try:
            CourseName = All_Category_Card_Data.objects.get(Course_name=chooes_Category)
            
            Student_openion.objects.create(
                chooes_Category=CourseName,
                Student_name = Student_name,
                Openion_text = Openion_text,
                Student_image = Student_image,
                
               
            )
            
            messages.success(request, 'Student Feedback Created Successfully')
            return redirect('StudentFeedbackReturn')
        
        except All_Category_Card_Data.DoesNotExist:
            messages.error(request, 'This course name does not exist')
            return redirect('StudentFeedbackReturn')
        
    else:
        messages.error(request, 'Invalid request method')
        return redirect('StudentFeedbackReturn')
    
     
     
# 7. কোর্সের শিক্ষক সম্পর্কে
    
@login_required
def Course_Teacher_about_Return(request):

    return render(request, 'Card_wise_data_show/7_course_teacher.html')



@login_required
def Course_Teacher_about_Forms(request):
    
    if request.method == 'POST':
        chooes_Category = request.POST.get('chooes_Category')
        Teacher_name = request.POST.get('Teacher_name')
        Teacher_position = request.POST.get('Teacher_position')
        Teacher_About_text = request.POST.get('Teacher_About_text')
        Teacher_image = request.FILES.get('Teacher_image')
       
        
        
        try:
            CourseName = All_Category_Card_Data.objects.get(Course_name=chooes_Category)
            
            Teacher_About.objects.create(
                chooes_Category=CourseName,
                Teacher_name = Teacher_name,
                Teacher_position = Teacher_position,
                Teacher_About_text = Teacher_About_text,
                Teacher_image = Teacher_image,
                
               
            )
            
            messages.success(request, 'Teacher About Created Successfully')
            return redirect('Course_TeacheraboutReturn')
        
        except All_Category_Card_Data.DoesNotExist:
            messages.error(request, 'This course name does not exist')
            return redirect('Course_TeacheraboutReturn')
        
    else:
        messages.error(request, 'Invalid request method')
        return redirect('Course_TeacheraboutReturn')
    
     
     
# 8. কোর্স সম্বন্ধে শিক্ষার্থীদের প্রশ্ন     
     
@login_required
def Course_Student_Question_Return(request):

    return render(request, 'Card_wise_data_show/8_student_question.html')



@login_required
def Course_Student_Question_Forms(request):
    
    if request.method == 'POST':
        chooes_Category = request.POST.get('chooes_Category')
        Question_Title_Name = request.POST.get('Question_Title_Name')
        Question_Answer_Text = request.POST.get('Question_Answer_Text')
        
       
        
        
        try:
            CourseName = All_Category_Card_Data.objects.get(Course_name=chooes_Category)
            
            Student_Question.objects.create(
                chooes_Category=CourseName,
                Question_Title_Name = Question_Title_Name,
                Question_Answer_Text = Question_Answer_Text,
                
                
               
            )
            
            messages.success(request, 'Question And Answer Created Successfully')
            return redirect('Course_StudentQuestionReturn')
        
        except All_Category_Card_Data.DoesNotExist:
            messages.error(request, 'This course name does not exist')
            return redirect('Course_StudentQuestionReturn')
        
    else:
        messages.error(request, 'Invalid request method')
        return redirect('Course_StudentQuestionReturn')
    
     
# 9. এই কোর্সের ভেতরে যা যা রয়েছে


@login_required
def Which_learn_you_Return(request):

    return render(request, 'Card_wise_data_show/9_Which_learn_you_Return.html')



@login_required
def Which_learn_you_forms(request):
    
    if request.method == 'POST':
        chooes_Category = request.POST.get('chooes_Category')
        Learning_Topics = request.POST.get('Learning_Topics')
   
        try:
            CourseName = All_Category_Card_Data.objects.get(Course_name=chooes_Category)
            
            Learning_Topic.objects.create(
                chooes_Category= CourseName,
                Learning_Topics = Learning_Topics,
               
            )
            
            messages.success(request, 'Learning Topic Created Successfully')
            return redirect('Which_learnReturn')
        
        except All_Category_Card_Data.DoesNotExist:
            messages.error(request, 'This course name does not exist')
            return redirect('Which_learnReturn')
        
    else:
        messages.error(request, 'Invalid request method')
        return redirect('Which_learnReturn')
    
     


# Betch All Data

# 1. নতুন ব্যাচ তৈরি করুন

@login_required
def Create_new_batch_return (request):
    
   
    batchwise_filter = Create_Batch.objects.select_related('course_name').all()          
    courses_with = {}           
    
    for batch in batchwise_filter:
        course_name = batch.course_name.Course_name if batch.course_name else None
        if course_name:
            if course_name not in courses_with:
                courses_with[course_name] = []
            courses_with[course_name].append(batch.batch_id)

    return render(request, 'Betch_All_Data/1_create_new_batch.html', {
        'courses_with':courses_with,
    })


@login_required
def Create_new_batch_forms(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        course_name = request.POST.get('course_name')
        batch_id = request.POST.get('batch_id')
        try:
            CourseName = All_Category_Card_Data.objects.get(Course_name=course_name)
            user_email = User.objects.get(email = user)
            Create_Batch.objects.create(
                user = user_email,
                course_name=CourseName,
                batch_id=batch_id,
            )
            messages.success(request, 'New Batch Created Successfully')
            return redirect('Create_newbatchreturn')
        except All_Category_Card_Data.DoesNotExist:
            messages.error(request, 'This course name does not exist')
            return redirect('Create_newbatchreturn')
    else:
        messages.error(request, 'Invalid request method')
        return redirect('Create_newbatchreturn')




@login_required
def Batch_wise_student_select_forms(request):
    if request.method == 'POST':
        batch_number = request.POST.get('batch_number')
        Student_User_data = request.POST.get('Student_User_data')
        Student_profile_data = request.POST.get('Student_profile_data')
        Student_profile_Id = request.POST.get('Student_profile_Id')
        
        try:
            BatchNumber = Create_Batch.objects.get(batch_id=batch_number)
            Student_Email = User.objects.get(email=Student_User_data)
            Student_Phone_number = Profile.objects.get(phone=Student_profile_data)
            StudentId = Profile.objects.get(account_number=Student_profile_Id)
            
            
            Batch_wise_Student_Select.objects.create(
                batch_number=BatchNumber,
                Student_User_data=Student_Email,
                Student_profile_data=Student_Phone_number,
                Student_profile_Id=StudentId,
            )
            messages.success(request, 'Batch Wish Student Select Successfully')
            return redirect('Create_newbatchreturn')
        except Create_Batch.DoesNotExist:
            messages.error(request, 'This batch name does not exist')
            return redirect('Create_newbatchreturn')
    else:
        messages.error(request, 'Invalid request method')
        return redirect('Create_newbatchreturn')




@login_required
def Batch_wise_time_set(request):
    if request.method == 'POST':
        batchId = request.POST.get('batchId')
        start_Time = request.POST.get('start_Time')
        end_Time = request.POST.get('end_Time')
        
        
        try:
            BatchNumber = Create_Batch.objects.get(batch_id=batchId)
            
            Batch_time_set.objects.create(
                batchId=BatchNumber,
                start_Time=start_Time,
                end_Time=end_Time,
                
            )
            messages.success(request, 'Batch Wish Time Select Successfully')
            return redirect('Create_newbatchreturn')
        except Create_Batch.DoesNotExist:
            messages.error(request, 'This batch name does not exist')
            return redirect('Create_newbatchreturn')
    else:
        messages.error(request, 'Invalid request method')
        return redirect('Create_newbatchreturn')




# 2. সবগুলো কোর্স এর ব্যাচসমূহ


@login_required
def All_course_batches_return(request, batch_id=None):
    student_data = None
    if batch_id:
        student_data = Batch_wise_Student_Select.objects.filter(batch_number__batch_id=batch_id)
    
    batchwise_filter = Create_Batch.objects.select_related('course_name').all()
    courses_with_batches = {}
    
    for batch in batchwise_filter:
        course_name = batch.course_name.Course_name if batch.course_name else None
        if course_name:
            if course_name not in courses_with_batches:
                courses_with_batches[course_name] = []
            courses_with_batches[course_name].append(batch.batch_id)

    return render(request, 'Betch_All_Data/2_All_course_batches.html', {
        'courses_with_batches': courses_with_batches,
        'student_data': student_data,
    })
 


# Teacher Site Batch Data


     
# 1. ব্যাচ ভিত্তিক ক্লাস সমূহ

def batch_wise_class_return(request):
    
    
    batchwise_filter = Create_Batch.objects.select_related('course_name').all()          
    courses_with = {}           
    
    for batch in batchwise_filter:
        course_name = batch.course_name.Course_name if batch.course_name else None
        if course_name:
            if course_name not in courses_with:
                courses_with[course_name] = []
            courses_with[course_name].append(batch.batch_id)

    
    return render(request, 'Teacher_Site_Batch_Data/1_batch_wise_class_set_data.html', {'courses_with':courses_with})




@login_required
def Batch_wise_Class_Create_forms(request):
    if request.method == 'POST':
        batchId = request.POST.get('batchId')
        learnig_topic_name = request.POST.get('learnig_topic_name')
        meetLink = request.POST.get('meetLink')

        try:
            # Fetch the batch
            batch_id = Create_Batch.objects.get(batch_id= batchId)
            
            
            Meet_link.objects.create(
                batchId=batch_id,
                learnig_topic_name=learnig_topic_name,
                meetLink=meetLink,
            )
            messages.success(request, 'Today Class Created Successfully')
            return redirect('batch_wiseclassreturn')
        except Create_Batch.DoesNotExist:
            messages.error(request, 'This batch name does not exist')
            return redirect('batch_wiseclassreturn')
    else:
        messages.error(request, 'Invalid request method')
        return redirect('batch_wiseclassreturn')


# 2. ব্যাচ ভিত্তিক মেসেজ


def batch_wise_message_return(request):
    return render(request, 'Teacher_Site_Batch_Data/2_batch_wise_message.html')


def Batch_wise_message_forms(request):
    
    if request.method == 'POST':
        batchId = request.POST.get('batchId')
        message = request.POST.get('message')
        
        try:
            batch_id = Create_Batch.objects.get(batch_id= batchId)
           
            
            batch_wise_message.objects.create(
                batchId = batch_id,
                message = message,
            )
            messages.success(request, 'Message Send Successfully')
            return redirect('batch_wisemessagereturn')
        
        except Create_Batch.DoesNotExist:
            messages.error(request, 'This batch name does not exist')
            return redirect('batch_wisemessagereturn')
    
    else:
        messages.error(request, 'Invalid request method')
        return redirect('batch_wisemessagereturn')
    
    

# 3. ব্যাচ ভিত্তিক এক্সাম এবং অ্যাসাইনমেন্ট


def batch_wise_exam_assingtmet_return(request):
    return render(request, 'Teacher_Site_Batch_Data/3_exam_assingment.html')



def Exam_assingment_forms(request):
    
    if request.method == 'POST':
        batchId = request.POST.get('batchId')
        Assingment_topic_name = request.POST.get('Assingment_topic_name')
        Assingment_pdf = request.FILES.get('Assingment_pdf')
        
        
        try:
            batch_id = Create_Batch.objects.get(batch_id= batchId)
            
            Batch_wise_Assingment.objects.create(
                batchId = batch_id,
                Assingment_topic_name = Assingment_topic_name,
                Assingment_pdf = Assingment_pdf
            )
            messages.success(request, 'Assingment send successfully')
            return redirect('batch_wise_exam_return')
        
        except Create_Batch.DoesNotExist:
            messages.error(request, 'This batch Does Not exist')
            return redirect('batch_wise_exam_return')
    
    else:
        messages.error(request, 'Invalid request method')
        return redirect('batch_wisemessagereturn')
    


def Assingment_result_forms(request):
    
    if request.method == 'POST':
        users = request.POST.get('user')
        result_pdf = request.FILES.get('result_pdf')
        
        
        try:
            userid = User.objects.get(email= users)
            
            Assingment_result.objects.create(
                user = userid,
                result_pdf = result_pdf,
               
            )
            messages.success(request, 'Result send successfully')
            return redirect('batch_wise_exam_return')
        
        except User.DoesNotExist:
            messages.error(request, 'This User Does Not exist')
            return redirect('batch_wise_exam_return')
    
    else:
        messages.error(request, 'Invalid request method')
        return redirect('batch_wisemessagereturn')






# Teacher Personal Site

# 1. টিচার ভিত্তিক স্টুডেন্ট ডাটা





# def teacher_wise_student_data_return(request, batch_id=None):
#     student = None
#     attendance_records = []
#     meet_links = []

#     if batch_id:
#         try:
#             student = User.objects.get(email=batch_id)
#             attendance_records = Student_Attendance.objects.filter(student=student).select_related('meet_link')
#         except User.DoesNotExist:
#             student = None


#     user = request.user
#     batchwise_filter = Create_Batch.objects.filter(user=user).select_related('course_name')

#     courses_with_batches = {}
#     for batch in batchwise_filter:
#         course_name = batch.course_name.Course_name if batch.course_name else 'None'
#         if course_name not in courses_with_batches:
#             courses_with_batches[course_name] = []
#         courses_with_batches[course_name].append(batch.batch_id)

#     student_data = None
#     if batch_id:
#         student_data = Batch_wise_Student_Select.objects.filter(batch_number__batch_id=batch_id).select_related('Student_profile_data', 'Student_User_data')

#     meet_links = Meet_link.objects.filter(batchId__user=user).select_related('batchId')

#     return render(request, 'Teacher_Personal_Site/1_Teacher_Wise_student_data.html', {
#         'courses_with_batches': courses_with_batches,
#         'student_data': student_data,
#         'student': student,
#         'attendance_records': attendance_records,
#         'meet_links': meet_links,
#     })






def teacher_wise_student_data_return(request, batch_id=None):
    student = None
    attendance_records = []
    meet_links = []

    if batch_id:
        try:
            student = User.objects.get(email=batch_id)
            attendance_records = Student_Attendance.objects.filter(student=student).select_related('meet_link')
        except User.DoesNotExist:
            student = None


    user = request.user
    batchwise_filter = Create_Batch.objects.filter(user=user).select_related('course_name')

    courses_with_batches = {}
    for batch in batchwise_filter:
        course_name = batch.course_name.Course_name if batch.course_name else 'None'
        if course_name not in courses_with_batches:
            courses_with_batches[course_name] = []
        courses_with_batches[course_name].append(batch.batch_id)

    student_data = None
    if batch_id:
        student_data = Batch_wise_Student_Select.objects.filter(batch_number__batch_id=batch_id).select_related('Student_profile_data', 'Student_User_data')

    meet_links = Meet_link.objects.filter(batchId__user=user).select_related('batchId')

    return render(request, 'Teacher_Personal_Site/1_Teacher_Wise_student_data.html', {
        'courses_with_batches': courses_with_batches,
        'student_data': student_data,
        'student': student,
        'attendance_records': attendance_records,
        'meet_links': meet_links,
    })
    
    
    



def student_absent_forms(request):
    if request.method == 'POST':
        absent = request.POST.get('absent')
        learnig_topic_name_id = request.POST.get('learnig_topic_name')

        try:
            topic = Meet_link.objects.get(id=learnig_topic_name_id)
            topic.absent = absent
            topic.save()
            messages.success(request, 'Attendance marked successfully')
            return redirect('teacher_wise_student_datareturn')

        except Meet_link.DoesNotExist:
            messages.error(request, 'This topic does not exist')
            return redirect('teacher_wise_student_datareturn')

    else:
        messages.error(request, 'Invalid request method')
        return redirect('teacher_wise_student_datareturn')

        
        
        
        
        
        
    
    
# def teacher_wise_student_data_return(request, batch_id=None):
#     student = None
#     attendance_records = []
#     meet_links = []

#     if batch_id:
#         try:
#             student = User.objects.get(email=batch_id)
#             attendance_records = Student_Attendance.objects.filter(student=student).select_related('meet_link')
#         except User.DoesNotExist:
#             student = None


#     user = request.user
#     batchwise_filter = Create_Batch.objects.filter(user=user).select_related('course_name')

#     courses_with_batches = {}
#     for batch in batchwise_filter:
#         course_name = batch.course_name.Course_name if batch.course_name else 'None'
#         if course_name not in courses_with_batches:
#             courses_with_batches[course_name] = []
#         courses_with_batches[course_name].append(batch.batch_id)

#     student_data = None
#     if batch_id:
#         student_data = Batch_wise_Student_Select.objects.filter(batch_number__batch_id=batch_id).select_related('Student_profile_data', 'Student_User_data')

#     meet_links = Meet_link.objects.filter(batchId__user=user).select_related('batchId')

#     return render(request, 'Teacher_Personal_Site/1_Teacher_Wise_student_data.html', {
#         'courses_with_batches': courses_with_batches,
#         'student_data': student_data,
#         'student': student,
#         'attendance_records': attendance_records,
#         'meet_links': meet_links,
#     })

 


    
 


# 2. টিচার ভিত্তিক স্টুডেন্ট এসাইনমেন্ট




def teacher_wise_student_assingment_return(request):
    
    return render(request, 'Teacher_Personal_Site/2_Teacher_Wise_student_assing.html')
        




# Student Attencdenc




 

     