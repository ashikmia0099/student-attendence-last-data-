from django.db import models
from Deshboard.models import All_Category_Card_Data,All_Category_model

# left site model code

class Course_Title(models.Model):
    chooes_Course = models.ForeignKey(All_Category_Card_Data, models.CASCADE, blank=True, null=True)
    Course_about_text =models.TextField(blank=True, null=True)
    course_image = models.ImageField(upload_to='Home_Page_Two/media/', blank=True, null=True, default=' ')
    video = models.FileField(upload_to='Home_Page_Two/media/video', blank=True, null=True, default=' ')
    
    class Meta: 
         verbose_name = '1. Course Header About'
         verbose_name_plural = '1. Course Header About'

    
# course All Informations 

class All_course_data_header_name(models.Model):
    chooes_Category = models.ForeignKey(All_Category_Card_Data, models.CASCADE, blank=True, null=True)
    Header_Name =models.CharField(max_length=200, blank=True, null= True, default='')
    
    class Meta:
         verbose_name = '2. Create Course Detials Title'
         verbose_name_plural = '2. Create Course Detials Title'
         
    def __str__(self): 
        return self.Header_Name
    
    

class Course_All_Data(models.Model):
    chooes_Category = models.ForeignKey(All_Category_Card_Data, models.CASCADE, blank=True, null=True)
    choose_Header_Name = models.ForeignKey(All_course_data_header_name, models.CASCADE, blank=True, null=True)
    Left_text =models.CharField(max_length=300, blank=True, null= True, default=' ')
    Right_text =models.CharField(max_length=300, blank=True, null= True, default=' ')
    
    class Meta:
         verbose_name = '3. Title Wise Show Data'
         verbose_name_plural = '3. Title Wise Show Data'
    
    
    
     
# purpose of the coruse 

class Puropse_of_course(models.Model):
    chooes_Category = models.ForeignKey(All_Category_Card_Data, models.CASCADE, blank=True, null=True)
    Image = models.ImageField(upload_to='Home_Page_Two/media/', blank=True, null=True, default=' ')
    Purpose_Text = models.CharField(max_length=200, blank=True, null= True, default=' ')
    
    class Meta:
         verbose_name = '4. Puropse of course Deta Set'
         verbose_name_plural = '4. Puropse of course Deta Set'


# Full Curryculam of the course model 

# 1. week model

class Module_Week(models.Model):
    chooes_Category = models.ForeignKey(All_Category_Card_Data, models.CASCADE, blank=True, null=True)
    Week_name = models.CharField(max_length=200, blank= True, null= True, default=' ')
    
    
    class Meta:
         verbose_name = ' 5. Set Module Week'
         verbose_name_plural = ' 5. Set Module Week'
         
    def __str__(self):
        return self.Week_name
    
    

# 2. module name and number

class Module_Name_Number(models.Model):
    chooes_Category = models.ForeignKey(All_Category_Card_Data, models.CASCADE, blank=True, null=True)
    select_week = models.ForeignKey(Module_Week, models.CASCADE, blank=True, null=True) 
    Module_number_and_Title = models.CharField(max_length=200, blank= True, null= True, default=' ')
    
    
    class Meta:
         verbose_name = '6. Set Week Wise Module '
         verbose_name_plural = '6. Set Week Wise Module '
         
    def __str__(self):
        return self.Module_number_and_Title
    
# 3. module under other data

class Module_Video_And_PDF(models.Model):
    chooes_Category = models.ForeignKey(All_Category_Card_Data, models.CASCADE, blank=True, null=True)
    select_week = models.ForeignKey(Module_Week, models.CASCADE, blank=True, null=True) 
    select_Module= models.ForeignKey(Module_Name_Number, models.CASCADE, blank=True, null=True)
    video_Title = models.CharField(max_length=200, blank= True, null= True, default=' ')
    video = models.FileField(upload_to='Home_Page_Two/media/video/', blank=True, null=True, default=' ')
   
    
    
    
    class Meta:
         verbose_name = '7. Set Module Wise video '
         verbose_name_plural = '7. Set Module Wise video '
         
    def __str__(self):
        return self.video_Title

 

# project and assingment demo

class Project_image(models.Model):
    chooes_Category = models.ForeignKey(All_Category_Card_Data, models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='Home_Page_Two/media/', blank=True, null=True, default=' ')
    
    class Meta:
         verbose_name = '8. Project Image'
         verbose_name_plural = '8. Project Image'
    
    
# Student openion

class Student_openion(models.Model):
    chooes_Category = models.ForeignKey(All_Category_Card_Data, models.CASCADE, blank=True, null=True)
    Student_image = models.ImageField(upload_to='Home_Page_Two/media/', blank=True, null=True, default=' ')
    Student_name = models.CharField(max_length=200, blank=True, null= True, default=' ')
    Openion_text = models.TextField()
    
    class Meta:
         verbose_name = '9. Student openion'
         verbose_name_plural = '9. Student openion'
    
    
    
    
    def __str__(self):
        return self.Student_name
    
    
# about of teacher

class Teacher_About(models.Model):
    chooes_Category = models.ForeignKey(All_Category_Card_Data, models.CASCADE, blank=True, null=True)
    Teacher_image = models.ImageField(upload_to='Home_Page_Two/media/', blank=True, null=True, default=' ')
    Teacher_name = models.CharField(max_length=200, blank=True, null= True, default=' ')
    Teacher_position = models.CharField(max_length=300, blank=True, null= True, default=' ')
    Teacher_About_text = models.TextField()
    
    class Meta:
         verbose_name = '10. Course Teacher About'
         verbose_name_plural = '10. Course Teacher About'
    
    
    
    def __str__(self):
        return self.Teacher_name
    
    
# Asked Student_Question 

class Student_Question(models.Model):
    chooes_Category = models.ForeignKey(All_Category_Card_Data, models.CASCADE, blank=True, null=True)
    Question_Title_Name = models.CharField(max_length=200, blank=True, null= True, default=' ')
    Question_Answer_Text = models.TextField()
    
    class Meta:
         verbose_name = ' 11. Student Course Related Question And Answer'
         verbose_name_plural = ' 11. Student Course Related Question And Answer'
    
    
    
     
    
# Right site

class Learning_Topic(models.Model):
    chooes_Category = models.ForeignKey(All_Category_Card_Data, models.CASCADE, blank=True, null=True)
    Learning_Topics =models.CharField(max_length=200, blank=True, null= True, default= ' ')
    
    class Meta:
         verbose_name = '12. EveryThing in this course'
         verbose_name_plural = '12. EveryThing in this course'
    
    


         
         
