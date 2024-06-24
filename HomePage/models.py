from django.db import models
from Deshboard.models import All_Category_Card_Data,All_Category_model


class Navbar_text(models.Model): 
    Text = models.TextField(blank=True, null= True)
    class Meta:
         verbose_name = 'Latest Navbar News Text'
         verbose_name_plural = 'Latest Navbar News Text'
 



class Footer_other_detail_header(models.Model):
    Header_Name =models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
         verbose_name = '1. Footer Other Detail Title'
         verbose_name_plural = '1. Footer Other Detail Title'
     
    def __str__(self):
        return self.Header_Name 
    
    
class Header_li(models.Model):
    HeaderChoice=models.ForeignKey(Footer_other_detail_header, on_delete=models.CASCADE)
    List_Data = models.TextField(max_length=300, blank=True, null= True)
    
    class Meta:
         verbose_name = '2. Footer Other Detail Title Data'
         verbose_name_plural = '2. Footer Other Detail Title Data'
    
     

    

    
class Footer_Last_section(models.Model):
    Institute_Logo =models.ImageField(upload_to='HomePage/media/', blank=True, null=True)
    copyright_text = models.CharField(max_length=500, blank=True, null= True)
    licence_number = models.CharField(max_length=500, blank=True, null= True) 
    
    class Meta:
         verbose_name = '3.Footer warning site'
         verbose_name_plural = '3.Footer warning site'
    
    
     
# All Course heml Page model site
# Seminer html page model 

class Seminer_Time(models.Model):
    day = models.CharField( max_length=10, blank=True, null=True, default= ' ')
    month_Year = models.CharField(max_length=20, blank=True,null=True, default=' ')
    seminer_subject = models.CharField(max_length=150, blank=True, null=True, default=' ')
    seminer_time =models.CharField(max_length=100, blank=True, null=True, default=' ')
    
    class Meta:
         verbose_name = 'Set Online Seminer Time'
         verbose_name_plural = 'Set Online Seminer Time'
         
         
class Seminer_Image_Text(models.Model):
    Seminer_image =models.ImageField(upload_to='HomePage/media/', blank=True, null=True, default= ' ')
    seminer_text  = models.TextField(blank=True, null=True, default=' ')
     
     
    class Meta:
         verbose_name = 'Set Home Page Seminer Image'
         verbose_name_plural = 'Set Home Page Seminer Image'

# category Page  model database
 
# Heading Detials
 
 
        
class CourseInfo(models.Model):
    Category = models.ForeignKey(All_Category_model, on_delete=models.CASCADE, related_name='Category')
    Category_summery_text = models.TextField(blank=True, null= True, default=" ")
    Category_image = models.ImageField(upload_to='Home_Page_Two/media/', blank=True, null=True, default=' ')

    class Meta:
        verbose_name = 'Category Page Top Data'
        verbose_name_plural = 'Category Page Top Data'
        

