


from django.contrib import messages
from django import forms
from Login_Logout.models import User, Profile
from Deshboard.models import All_Category_Card_Data

from Custom_Admin_panel.models import  Meet_link,batch_wise_message,Batch_wise_Assingment,Assingment_result




 
class Student_Info_Forms(forms.ModelForm):
    phone = forms.CharField(required= True)
    course = forms.ModelChoiceField(queryset=All_Category_Card_Data.objects.all(), empty_label=None, required=True)
    account_number = forms.IntegerField(required= True)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
            
        if self.instance:
            
            try:
                user_profile = self.instance.profile
            except Profile.DoesNotExist:
                user_profile = None
                
            if user_profile:
                self.fields['phone'].initial = user_profile.phone
                self.fields['course'].initial = user_profile.course
                self.fields['account_number'].initial = user_profile.account_number
    
   
class attendence_forms(forms.ModelForm):
    
    class Meta:
        model = Meet_link
        fields = []
        