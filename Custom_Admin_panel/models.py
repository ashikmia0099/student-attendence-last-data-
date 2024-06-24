
from django.db import models
from django.utils import timezone
from datetime import timedelta
from Deshboard.models import All_Category_Card_Data

from Login_Logout.models import  User, Sponsor,Profile
from Social_Media.models import Notification,ContractUs_Form

from Student_Profile.models import Student_Certificate


# Teacher Model Database


class Create_Batch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='create_teacher_batch')
    course_name = models.ForeignKey(All_Category_Card_Data, on_delete=models.CASCADE)
    batch_id = models.CharField(max_length=100)
    
    
    class Meta:
        verbose_name = 'Create Batch'
        verbose_name_plural = 'Create Batch'
        
    
    def __str__(self): 
        return self.batch_id or 'Untitled batch name'
    
       
    
class Batch_wise_Student_Select(models.Model):
    batch_number = models.ForeignKey(Create_Batch, on_delete=models.CASCADE)
    Student_User_data = models.ForeignKey(User, on_delete=models.CASCADE)
    Student_profile_data = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Student_profile_Id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='Student_id')
    


class Batch_time_set(models.Model):
    batchId = models.ForeignKey(Create_Batch, on_delete=models.CASCADE)
    start_Time = models.CharField(max_length=50, blank=True, null=True)
    end_Time = models.CharField(max_length=50, blank=True, null=True)

    
    class Meta:
         verbose_name = 'Batch Time Set'
         verbose_name_plural = 'Batch Time Set'
     
    def __str__(self): 
        return f'Batch id {self.batchId.batch_id} and {self.start_Time} and {self.end_Time}' 

# Class Link database model

class Meet_link(models.Model):
    batchId = models.ForeignKey(Create_Batch, on_delete=models.CASCADE)
    learnig_topic_name = models.CharField(max_length=500)
    meetLink = models.URLField(max_length=400)
    absent = models.CharField(max_length=10)
   
    
    class Meta:
         verbose_name = 'Meet Link'
         verbose_name_plural = 'Meet Link'
    
    
    def __str__(self): 
        return self.learnig_topic_name or 'Untitled topic name'



class Student_Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    meet_link = models.ForeignKey(Meet_link, on_delete=models.CASCADE)
    attend = models.BooleanField(default=False)
    
    
    class Meta:
         verbose_name = 'Student Attendence'
         verbose_name_plural = 'Student Attendence'
    
    def __str__(self): 
        return f'{ self.attend}' 
         
         
         

    

class batch_wise_message(models.Model):
    batchId = models.ForeignKey(Create_Batch, on_delete=models.CASCADE)
    message = models.TextField()
    
    
    class Meta:
         verbose_name = 'Batch Wise Message'
         verbose_name_plural = 'Batch Wise Message'
    
    
    def __str__(self): 
        return self.batchId.batch_id or 'Untitled batch name'
    
    


class Batch_wise_Assingment(models.Model):
    batchId = models.ForeignKey(Create_Batch, on_delete=models.CASCADE)
    Assingment_topic_name = models.CharField(max_length=150)
    Assingment_pdf = models.FileField(upload_to='Custom_Admin_panel/media/', blank=True, null=True, default=' ')
    
    class Meta:
         verbose_name = 'Batch Wise Assingment'
         verbose_name_plural = 'Batch Wise Assingment'
    
    
    def __str__(self): 
        return self.Assingment_topic_name or 'Untitled Topic name'
    

class Assingment_Submit(models.Model):
    batchId = models.ForeignKey(Create_Batch, on_delete=models.CASCADE)
    Assingment_pdf = models.FileField(upload_to='Custom_Admin_panel/media/', blank=True, null=True, default=' ')
    
    
    class Meta:
         verbose_name = 'Assingment Submit'
         verbose_name_plural = 'Assingment Submit'
         
 
class Assingment_result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result_pdf = models.FileField(upload_to='Custom_Admin_panel/media/', blank=True, null=True, default=' ')
    
    class Meta:
         verbose_name = 'Assingment Result'
         verbose_name_plural = 'Assingment Result'
    
    
    def __str__(self): 
        return self.user.email 
    