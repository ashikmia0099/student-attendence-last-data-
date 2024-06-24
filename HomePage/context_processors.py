from .models import *
from Login_Logout.models import Profile,User
from Student_Profile.models import Student_image
from Social_Media.models import Notification
from django.contrib.auth.decorators import login_required

from Custom_Admin_panel.models import Create_Batch,Batch_wise_Assingment,Batch_time_set, Batch_wise_Student_Select, Meet_link,batch_wise_message,Batch_wise_Assingment,Assingment_result




def getBaseData(request):
    
    # nabbar Text
    
    navbarText = Navbar_text.objects.all().last()
    
    # footer header text
    Footer_other_header_name = Footer_other_detail_header.objects.all()
    
    # footer li text
    
    CattegoryHeader = Footer_other_detail_header.objects.all()
    CattegoryHeaderData = {}
    
    for header in CattegoryHeader:
        CattegoryHeaderData[header] = Header_li.objects.filter(HeaderChoice = header )
        
        
    # payment merchent image
    
    
    
    

    # fOOTER LAST PART
    
    footer_last = [Footer_Last_section.objects.last()]  # Wrap the object in a list
    
    
    return {'navbarText': navbarText, 
            'Footer_other_header_name':Footer_other_header_name, 
            'CattegoryHeaderData':CattegoryHeaderData,
            'footer_last':footer_last,
            
            }
    
   
def Account_id(request):
    account_number = None  # Default value if user is not authenticated or no profile exists

    if request.user.is_authenticated:
        try:
            account = User.objects.get(pk=request.user.id)
            profile = Profile.objects.filter(user=account).first()
            
            
            if profile:
                account_number = profile.account_number

        except User.DoesNotExist:
            pass  # Handle the case where the user does not exist, if necessary

    return {'account_number': account_number}



def Student_name(request):
    studentName = None  # Default value if user is not authenticated or no profile exists

    if request.user.is_authenticated:
        try:
            account = User.objects.get(pk=request.user.id)
            if account:
                studentName = account.first_name

        except User.DoesNotExist:
            pass  # Handle the case where the user does not exist, if necessary

    return {'studentName': studentName}




def Id_Student_image(request):
    studenImage = None  # Default value if user is not authenticated or no profile exists

    if request.user.is_authenticated:
        try:
            account = User.objects.get(pk=request.user.id)
            imageStudent = Student_image.objects.filter(user=account).last()
            
            if imageStudent and imageStudent.Image:
                studenImage = imageStudent.Image.url  # Ensure URL is passed if image exists
        except User.DoesNotExist:
            pass  # Handle the case where the user does not exist, if necessary

    return {'studenImage': studenImage}


# this is right code
 

def Notification_view(request):
    unread_count = 0
    notifications = []

    if request.user.is_authenticated:
        unread_count = request.user.notifications.filter(is_read=False).count()
        notifications = Notification.objects.filter(user=request.user) | Notification.objects.filter(user__isnull=True)

    return {'unread_count': unread_count, 'notifications': notifications}



# def Notification_view(request):
#     if request.user.is_authenticated:
#         unread_count = request.user.notifications.filter(is_read=False).count()
#     else:
#         unread_count = 0

#     notifications = Notification.objects.filter(user=request.user) | Notification.objects.filter(user__isnull=True)
#     notifications.update(is_read=True)

#     try:
#         batch_wise_student_select = Batch_wise_Student_Select.objects.get(Student_User_data=request.user)
#         batch_id = batch_wise_student_select.batch_number
#     except Batch_wise_Student_Select.DoesNotExist:
#         batch_wise_student_select = None
#         batch_id = None

#     if batch_id:
#         batch_messages = batch_wise_message.objects.filter(batchId=batch_id)
#     else:
#         batch_messages = []

#     # Debugging output
#     print("Notifications:", list(notifications))  # Convert to list for debugging
#     print("Batch Messages:", list(batch_messages))  # Convert to list for debugging

#     return {
#         'unread_count': unread_count,
#         'notifications': notifications,
#         'batch_messages': batch_messages
#     }


