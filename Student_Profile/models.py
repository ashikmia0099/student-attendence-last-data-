from django.db import models
from Login_Logout.models import User, Profile,Sponsor


 
class Student_image(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='studentImage')
    Image = models.ImageField(upload_to='Student_Profile/media/', blank=True, null=True, default='Student_Profile/media/pro.png')


    class Meta:
         
        verbose_name = 'Student image' 
        verbose_name_plural = 'Student image'

 

class Student_Certificate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='certificate')
    Certificate = models.FileField(upload_to='Student_Profile/media/', blank=True, null=True, default=' ')

    class Meta:
         
        verbose_name = 'Student Certificate'
        verbose_name_plural = 'Student Certificate'
