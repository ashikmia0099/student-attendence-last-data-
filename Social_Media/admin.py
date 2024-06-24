from django.contrib import admin
from .models import Notification,Popup_banner,ContractUs_Form,PhoneUs_Form


    


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at','is_read')
    search_fields = ('user__email', 'message', 'created_at', 'is_read')
    list_filter = ('user__email',)
    
    
class Contract_Sign_up(admin.ModelAdmin):
    list_display = ('people_name', 'people_email','message','created_at')
    search_fields = ('people_name', 'people_email','message','created_at')
    list_filter = ('people_email',)
    


    
class Phone_us_form(admin.ModelAdmin):
    list_display = ('user_name', 'phone','course_name','created_at')
    search_fields = ('user_name', 'phone','course_name','created_at')
    list_filter = ('phone',)



admin.site.register(Notification, NotificationAdmin)
admin.site.register(Popup_banner)
admin.site.register(ContractUs_Form,Contract_Sign_up)
admin.site.register(PhoneUs_Form,Phone_us_form)
