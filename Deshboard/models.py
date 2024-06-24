from django.db import models
from embed_video.fields import EmbedVideoField
from django.utils.text import slugify


# 2. Banner model
 
class BannerModel(models.Model):
    Banner_title = models.CharField(max_length=150, blank=True, null= True, default=' ')
    Banner_text = models.TextField(blank=True, null= True, default=' ')
    Banner_video_image = models.ImageField(upload_to='Deshboard/media/', blank=True, null=True, default=' ')
    Banner_video = models.FileField(upload_to='Deshboard/media/', blank=True, null=True, default=' ')
    
    
    class Meta:
         verbose_name = '2. Banner Model'
         verbose_name_plural = '2. Banner Model'
    
    
    def __str__(self): 
        return self.Banner_title or 'Untitled Banner'


# 4. all category models
 

class All_category_text(models.Model):
    Cattegory_top_text =models.TextField(blank=True, null=True, default=' ')
    
    class Meta:
         verbose_name = '4. All Course Heading Text'
         verbose_name_plural = '4. All Course Heading Text'
    


class All_Category_model(models.Model):
    Category_Name = models.CharField(max_length=150, blank=True, null=True, default=' ')
    slug = models.SlugField( max_length=150, unique= True, blank=True, null=True, default=' ')
    Category_Image = models.ImageField(upload_to='Deshboard/media/', blank=True, null=True, default=' ')
     
     
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Category_Name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Category_Name
    
    class Meta:
         verbose_name = '4.1 All Category Name and Image'
         verbose_name_plural = '4.1 All Category Name and Image'
     
    
    
    def __str__(self):
         return self.Category_Name if self.Category_Name else "No Category Name"

    
 
class All_Category_Card_Data(models.Model):
    Category_Name = models.ForeignKey(All_Category_model, on_delete=models.CASCADE, blank=True, null=True, default=' ', related_name='category_name')
    Image = models.ImageField(upload_to='Deshboard/media/', blank=True, null=True, default=' ')
    Course_name = models.CharField(max_length=100, blank=True, null=True, default=' ')
    student_review = models.CharField(max_length=200, blank=True, null=True, default=' ')
    Course_fees = models.CharField(max_length=100, blank=True, null=True, default=' ')
    
    class Meta:
         verbose_name = '4.2 All Category Card Data'
         verbose_name_plural = '4.2 All Category Card Data'
    

    def __str__(self):
        return self.Course_name if self.Course_name else "No Course Name"

# 5. Our Spicial service 

class HomeOurService(models.Model):
    service_name  = models.CharField(max_length=100, blank=True,null= True, default=' ')
    
    class Meta:
         verbose_name = '5.1 Our Service '
         verbose_name_plural = '5.1 Our Service '
    
    
    def __str__(self):
        return self.service_name
    
#5.1 our special service

class Our_Service_Text(models.Model):
    service_text = models.TextField( blank=True, null=True)
    Image =models.ImageField(upload_to='Deshboard/media/', blank=True, null=True, default=' ')
    
    
    class Meta:
         verbose_name = '5. Our Service Heading Text And Banner Image '
         verbose_name_plural = '5. Our Service Heading Text And Banner Image '
    


    
     
    
# 8.intitute Banner Site
 
class HomeInstituteBanner(models.Model):
    BannerTitle = models.CharField(max_length=150, blank=True, null=True)
    BannerText = models.TextField(blank=True, null=True)
    Banner_image = models.ImageField(upload_to='Deshboard/media/', blank=True, null=True)
    
    class Meta:
         verbose_name = '8. Institute Banner left Image'
         verbose_name_plural = '8. Institute Banner left Image'
    
    
    
    def __str__(self):
        return self.BannerTitle
    
class HomeInstituteBannersecond(models.Model):
    Banner_Title = models.CharField(max_length=150, blank=True, null=True)
    Banner_Text = models.TextField(blank=True, null=True)
    Banner_image = models.ImageField(upload_to='Deshboard/media/', blank=True, null=True)
    
    class Meta:
         verbose_name = '8.1 Institute Banner Right Image'
         verbose_name_plural = '8.1 Institute Banner Right Image'
    
    
    
    def __str__(self):
        return self.Banner_Title



# 9. Institute success histoy video
class Success_history_video(models.Model):
    Success_history_text = models.TextField( blank=True, null= True, default=' ')
    Success_history_image = models.ImageField(upload_to='Deshboard/media/', blank=True, null=True, default=' ')
    Success_Video_history = models.FileField(upload_to='Deshboard/media/', blank=True, null=True, default=' ')
    
     
    class Meta:
         verbose_name = '9. Success History Video Model'
         verbose_name_plural = '9. Success History Video Model'
    
    
   


    
     
# 10. Event and Accitivites
class HomeEvent(models.Model):
    Event_image = models.ImageField(upload_to='Deshboard/media/', blank=True, null=True)
    
    
    class Meta:
         verbose_name = '10. Institute Event Image'
         verbose_name_plural = '10. Institute Event Image'
    
   

# 11. Expert Teacher

class HomeExpertTeacher(models.Model):
    Teacher_image = models.ImageField(upload_to='Deshboard/media/', blank=True, null=True)
    Teacher_name = models.CharField(max_length=50, null=True, blank=True)
    Position_name = models.CharField(max_length=100, null=True, blank=True)
    institute_name = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
         verbose_name = '11. Teacher Information '
         verbose_name_plural = '11. Teacher Information '
    
    
    def __str__(self):
        return self.Teacher_name


    
# 12.Student Openion

class HomeStudentOpenion(models.Model):
    Student_image = models.ImageField(upload_to='Deshboard/media/', blank=True, null=True)
    Student_name = models.CharField(max_length=50, blank=True, null=True)
    openion_course_name = models.CharField(max_length=100, blank=True, null=True)
    Openion_text = models.CharField(max_length=1000, blank=True, null=True)
    
    class Meta:
         verbose_name = '12. Student Openion '
         verbose_name_plural = '12. Student Openion '
    
    
    def __str__(self):
        return f'{self.Student_name}'


# 14. Our Support Partner

class our_partner(models.Model):
    
    Prather_Logo = models.ImageField(upload_to='Deshboard/media/', blank=True, null=True)
    
    class Meta: 
         verbose_name = '14. Our Partner Image '
         verbose_name_plural = '14. Our Partner Image '
         
         
         
