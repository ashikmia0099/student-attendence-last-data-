from django.shortcuts import render,redirect,get_object_or_404
from Login_Logout.models import User, Profile
from .models import Student_image,Student_Certificate
from django. views import View
from Login_Logout.forms import RegisterForm,User_Update_Form  
from .forms import Student_Info_Forms,attendence_forms
from django.contrib.auth.decorators import login_required
from Social_Media.models import Notification,PhoneUs_Form
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib import messages

from Custom_Admin_panel.models import Create_Batch,Batch_wise_Assingment,Batch_time_set, Batch_wise_Student_Select, Meet_link,batch_wise_message,Batch_wise_Assingment,Assingment_result


from Custom_Admin_panel.models import Student_Attendance



def Student_info(request):
    
    if request.method == 'POST':
        form = Student_Info_Forms(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            
    else:
        form = Student_Info_Forms(instance = request.user)
        
        image = Student_image.objects.filter(user=request.user).last()

    
    return render(request, 'student_info.html',{'form':form, 'user':image})


def ChangeInfo(request):
    if request.method == 'POST':
        form = User_Update_Form(request.POST, request.FILES, instance=request.user)
        
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('student_dataUpdate')
    else:
        form = User_Update_Form(instance=request.user)
        
        
    # change student image 
    
    image = Student_image.objects.filter(user=request.user).last()
    
    return render(request, 'update_info.html', {'form': form , 'user':image})




def Student_Certificate_view(request):
    user = request.user

    try:
        pdf = Student_Certificate.objects.get(user=user)
    except Student_Certificate.DoesNotExist:
        pdf = None

    return render(request, 'certificate.html', {'pdf': pdf})
    



def Announcement_view(request, ):
    
    see_all_notification = Notification.objects.filter(user=request.user)
    
    notipragitor = Paginator(see_all_notification, 10)
    page_number = request.GET.get('page')
    page_obj = notipragitor.get_page(page_number)
    
        
    
    return render(request, 'Announcement.html', {
        'see_all_notification': see_all_notification,
        'page_obj': page_obj,
        
        })
    
    

def Announcement_message(request, message_id=None ):
    
    full_message = None
    if message_id:
        
        full_message= get_object_or_404(Notification, id= message_id)
        
    return render(request, 'Announcement.html', {
       
        'full_message': full_message,
        })
    
    
    
# def my_class(request):
#     user = request.user

#     try:
#         batch_wise_student_select = Batch_wise_Student_Select.objects.get(Student_User_data=user)
#         batch_id = batch_wise_student_select.batch_number  # This is the Create_Batch instance
#     except Batch_wise_Student_Select.DoesNotExist:
#         batch_wise_student_select = None
#         batch_id = None

#     if batch_id:
#         student_class = Meet_link.objects.filter(batchId=batch_id)
#         timeset = Batch_time_set.objects.filter(batchId=batch_id)
#     else:
#         student_class = None
#         timeset = None
        
   
#     return render(request, 'myclass.html', 
#                   {'batch_wise_student_select': batch_wise_student_select,
#                    'student_class': student_class,
#                    'timeset':timeset
                   
                   
#                    })




# Custom_Admin_panel model views 

def Exam_and_Assingment(request):
    
    user = request.user

    try:
        batch_wise_student_select = Batch_wise_Student_Select.objects.get(Student_User_data=user)
        batch_id = batch_wise_student_select.batch_number
    except Batch_wise_Student_Select.DoesNotExist:
        batch_wise_student_select = None
        batch_id = None

    if batch_id:
        student_assingment = Batch_wise_Assingment.objects.filter(batchId=batch_id)
    else:
        student_assingment = None
        
    result = Assingment_result.objects.filter(user=user)
        
    
    
    return render(request, 'exam_assingment.html', {
        'student_assingment':student_assingment,
        'result': result,
    })




@login_required
def message_show(request):
    user = request.user
    print(f"User: {user}")

    try:
        batch_wise_student_select = Batch_wise_Student_Select.objects.get(Student_User_data=user)
        batch_id = batch_wise_student_select.batch_number  # This is the Create_Batch instance
        
    except Batch_wise_Student_Select.DoesNotExist:
        batch_wise_student_select = None
        batch_id = None
        

    if batch_id:
        batch_messages = batch_wise_message.objects.filter(batchId=batch_id)
         
    else:
        batch_messages = None

    return render(request, 'message_show_class.html', {'batch_messages': batch_messages})

    



# Right code for attendence 




# def update_attendance(request):
#     if request.method == 'POST':
#         meet_link_id = request.POST.get('meet_link_id')
#         meet = bool(request.POST.get('attend', False))
#         user = request.user
        
#         try:
#             meet_link = Meet_link.objects.get(id=meet_link_id)
            
#             student_attendance, created = Student_Attendance.objects.get_or_create(
#                 student=user, meet_link=meet_link
#             )
            
#             if not student_attendance.attend:
#                 student_attendance.attend = True
#                 student_attendance.save()
#                 messages.success(request, 'You have successfully marked attendance.')
#             else:
#                 messages.info(request, 'Attendance already marked.')
            
#             return redirect('myclass')
        
#         except Meet_link.DoesNotExist:
#             messages.error(request, 'This meet link does not exist.')
#             return redirect('myclass')
        
#     else:
#         messages.error(request, 'Invalid request method.')
#         return redirect('myclass')
    




# @login_required
# def my_class(request):
#     user = request.user

#     try:
#         batch_wise_student_select = Batch_wise_Student_Select.objects.get(Student_User_data=user)
#         batch_id = batch_wise_student_select.batch_number
#     except Batch_wise_Student_Select.DoesNotExist:
#         batch_wise_student_select = None
#         batch_id = None

#     if batch_id:
#         student_class = Meet_link.objects.filter(batchId=batch_id)
#         timeset = Batch_time_set.objects.filter(batchId=batch_id)
#         attendance_records = {record.meet_link.id: record.attend for record in Student_Attendance.objects.filter(student=user, meet_link__in=student_class)}
#     else:
#         student_class = None
#         timeset = None
#         attendance_records = {}

#     return render(request, 'myclass.html', 
#                   {'batch_wise_student_select': batch_wise_student_select,
#                    'student_class': student_class,
#                    'timeset': timeset,
#                    'attendance_records': attendance_records,
#                   })









# experement code for attendence 




def update_attendance(request):
    if request.method == 'POST':
        meet = bool(request.POST.get('attend', False))
        user = request.user

        try:
            # Get the meet link object (assuming you have meet link information in the request)
            meet_link_id = request.POST.get('meet_link_id')
            meet_link = get_object_or_404(Meet_link, id=meet_link_id)

            # Ensure you get the specific Student_Attendance for the user and meet_link
            student_attendance, created = Student_Attendance.objects.get_or_create(
                student=user,
                meet_link=meet_link
            )

            if not student_attendance.attend:
                student_attendance.attend = True
                student_attendance.save()
                messages.success(request, 'You have successfully marked attendance.')
            else:
                messages.info(request, 'Attendance already marked.')

            return redirect('myclass')

        except Student_Attendance.MultipleObjectsReturned:
            messages.error(request, 'Multiple attendance records found. Please contact the administrator.')
            return redirect('myclass')

    else:
        messages.error(request, 'Invalid request method.')
        return redirect('myclass')

 
@login_required
def my_class(request):
    user = request.user

    try:
        batch_wise_student_select = Batch_wise_Student_Select.objects.get(Student_User_data=user)
        batch_id = batch_wise_student_select.batch_number
    except Batch_wise_Student_Select.DoesNotExist:
        batch_wise_student_select = None
        batch_id = None

    if batch_id:
        student_class = Meet_link.objects.filter(batchId=batch_id)
        timeset = Batch_time_set.objects.filter(batchId=batch_id)
        attendance_records = {record.meet_link.id: record.attend for record in Student_Attendance.objects.filter(student=user, meet_link__in=student_class)}
    else:
        student_class = None
        timeset = None
        attendance_records = {}

    return render(request, 'myclass.html', 
                  {'batch_wise_student_select': batch_wise_student_select,
                   'student_class': student_class,
                   'timeset': timeset,
                   'attendance_records': attendance_records,
                  }) 


 