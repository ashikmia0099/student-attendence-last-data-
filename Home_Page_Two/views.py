

from django.shortcuts import render,redirect,get_object_or_404
from. models import Course_Title, All_course_data_header_name ,Course_All_Data, Puropse_of_course, Project_image, Student_openion, Teacher_About, Student_Question, Learning_Topic
from django.views.generic import DetailView

from .models import Module_Week,Module_Name_Number,Module_Video_And_PDF

from Deshboard.models import All_Category_Card_Data
from django.contrib import messages
from Social_Media.models import PhoneUs_Form



def CourseDetailsPage(request,id):
    
    card = get_object_or_404(All_Category_Card_Data, pk= id)
    
     # course titel model code
    chooes_Category = card  
    CourseTitle = Course_Title.objects.filter(chooes_Course=chooes_Category).last()
    
    
    
    
    # Course all data Header Name
    HeaderName = All_course_data_header_name.objects.filter(chooes_Category=chooes_Category)
     
     
    
    # course All Data
    header_names = All_course_data_header_name.objects.filter(chooes_Category=card)
    
    # Create a dictionary to store data grouped by header name
    grouped_data = {}

    for header in header_names:
        # Fetch Course_All_Data objects for each header
        course_data = Course_All_Data.objects.filter(chooes_Category=card, choose_Header_Name=header)
        grouped_data[header] = course_data
    
    
    
    # purpos of course model code
    
    purposeCourse = Puropse_of_course.objects.filter(chooes_Category=chooes_Category)
    
    
    # full curryculam of the course
    
    # 1. select module week
    
    modules = Module_Video_And_PDF.objects.filter(chooes_Category=card)

    # Organize modules by week and module number
    module_data = {}
    for module in modules:
        week = module.select_week
        if week not in module_data:
            module_data[week] = {}
        
        module_number = module.select_Module
        if module_number not in module_data[week]:
            module_data[week][module_number] = []
        
        module_data[week][module_number].append(module)
    # 2. Module name and number

    
    
    
    # Project image
    
    Image = Project_image.objects.filter(chooes_Category=chooes_Category)
    
    # Teacher About 
    
    TeacherAbout = Teacher_About.objects.filter(chooes_Category=chooes_Category)
    
    # student openion
    
    StudentOpenion = Student_openion.objects.filter(chooes_Category=chooes_Category)
    
    # Studeint Question 
    studentQuestion = Student_Question.objects.filter(chooes_Category=chooes_Category)
    
    
    # Right site
    # learning topic 
    
    learningTopic = Learning_Topic.objects.filter(chooes_Category=chooes_Category)




    return render(request,'course_detailpage.html', 
                  {'Home_Page_Two':card,
                   'CourseTitle': CourseTitle, 
                   'grouped_data':grouped_data,
                   'HeaderName':HeaderName,
                   'purposeCourse':purposeCourse, 
                   'Image':Image, 
                   'StudentOpenion':StudentOpenion,
                   'studentQuestion':studentQuestion, 
                   'learningTopic':learningTopic, 
                   'TeacherAbout':TeacherAbout,  
                   'module_data': module_data})    
    
    


def contract_phone_return(request):
    
    
    return render(request, 'course_detailpage.html')




def contract_phone_forms(request):
    
    if request.method == 'POST':
        
        user_name = request.POST.get('user_name')
        phone = request.POST.get('phone')
        course_name = request.POST.get('course_name')
        
        
        try:
            PhoneUs_Form.objects.create(
                
                user_name = user_name,
                phone = phone,
                course_name = course_name,
                    
                                    
            )
            
            messages.success(request, 'Your post successfully send')
            return redirect('contract_phonereturn')
        
        except  PhoneUs_Form.DoesNotExist:
            messages.error(request, 'Invalid request method')
            return redirect('contract_phonereturn')
            
    else:
        messages.error(request, 'Invalid request method')
        return redirect('contract_phonereturn')
            
    



