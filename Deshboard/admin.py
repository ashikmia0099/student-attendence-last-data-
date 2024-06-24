from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import BannerModel,All_category_text,All_Category_model,All_Category_Card_Data,HomeOurService, Our_Service_Text,HomeInstituteBanner,HomeInstituteBannersecond,Success_history_video,HomeEvent,HomeExpertTeacher,HomeStudentOpenion,our_partner



class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Category_Name',)}
    list_display = ['Category_Name', 'slug']

admin.site.register(BannerModel, MyModelAdmin)


admin.site.register(All_category_text)
admin.site.register(All_Category_model,categoryAdmin)
admin.site.register(All_Category_Card_Data)
admin.site.register(HomeOurService)
admin.site.register(Our_Service_Text)
admin.site.register(HomeInstituteBanner)
admin.site.register(HomeInstituteBannersecond)
admin.site.register(Success_history_video)
admin.site.register(HomeEvent)
admin.site.register(HomeExpertTeacher)
admin.site.register(HomeStudentOpenion)
admin.site.register(our_partner)

