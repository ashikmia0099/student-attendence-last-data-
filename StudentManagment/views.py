from django.shortcuts import render,redirect
from Login_Logout.models import User, Profile
from Student_Profile.models import Student_image
from Social_Media.models import Notification
from django.contrib.auth.decorators import login_required



from Custom_Admin_panel.models import Create_Batch,Batch_wise_Assingment,Batch_time_set, Batch_wise_Student_Select, Meet_link,batch_wise_message,Batch_wise_Assingment,Assingment_result








@login_required
def message_show(request):
    user = request.user
    

    try:
        batch_wise_student_select = Batch_wise_Student_Select.objects.get(Student_User_data=user)
        batch_id = batch_wise_student_select.batch_number  
        
    except Batch_wise_Student_Select.DoesNotExist:
        batch_wise_student_select = None
        batch_id = None
       

    if batch_id:
        batch_messages = batch_wise_message.objects.filter(batchId=batch_id)
       
    else:
        batch_messages = None
        

    return render(request, 'base.html', {'batch_messages': batch_messages})


