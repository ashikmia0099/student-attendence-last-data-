from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import CustomManager
from django.utils.translation import gettext_lazy as _
from .utils import generate_ref_code
from django.urls import reverse
from Deshboard.models import All_Category_Card_Data,All_Category_model
 
class User(AbstractUser): 
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length= 200)
    objects = CustomManager()
  
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'User'
    

    def __str__(self):
        return self.email
 
  
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15 , )
    course = models.ForeignKey(All_Category_Card_Data, on_delete=models.CASCADE, related_name='course')
    account_number = models.IntegerField(unique=True, null=True, blank=True, default=" ")
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'
     
    def __str__(self):
        return f"  Email: {self.user.email} ----->  Student Name:  {self.user.first_name } {self.user.last_name}  ----> Course:name {self.course}  ----->   Account Number: {self.account_number}"



class Sponsor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    code = models.CharField(max_length=12, blank= True, null= True)
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='ref_by')
    
    
    
    class Meta:
         
        verbose_name = 'Refferal Link'
        verbose_name_plural = 'Refferal Link'
    
    
    def __str__(self):
        return f"{self.user.first_name} - gennerated code :  {self.code}"
    
  
    def get_recommended_profiles(self):
        recommended_profiles = Sponsor.objects.filter(recommended_by=self.user)
        recommended_profiles_info = []
        for profile in recommended_profiles:
            recommended_profiles_info.append({
                'first_name': profile.user.first_name,
                'recommended_by': profile.recommended_by.first_name if profile.recommended_by else None
            })
        return recommended_profiles_info

    def save(self, *args, **kwargs):
        if not self.code:  # Only generate code if it doesn't already exist
            self.code = generate_ref_code()
            print(self.code)
        super().save(*args, **kwargs)

    def register_link(self):
        return reverse('Registerpage') + f'?ref_code={self.code}'
    
    
    
    