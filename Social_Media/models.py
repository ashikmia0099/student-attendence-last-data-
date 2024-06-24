from django.db import models
from Login_Logout.models import User
from django.utils import timezone

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications', null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message
   
    class Meta: 
        ordering = ['-created_at']
         
 
class Popup_banner(models.Model):
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    
     
# contract With us Signup form 

class ContractUs_Form(models.Model):
    
    people_name = models.CharField(max_length=100 )
    people_email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    message_seen = models.BooleanField(default= False)
    
    def __str__(self):
        return self.people_name



class PhoneUs_Form(models.Model):
    
    user_name = models.CharField(max_length=100 )
    phone = models.CharField(max_length=15)
    course_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    message_seen = models.BooleanField(default= False)
    
    
    def __str__(self):
        return self.user_name
    
    
  
