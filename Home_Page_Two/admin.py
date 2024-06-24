from django.contrib import admin

from. models import Course_Title, All_course_data_header_name,Course_All_Data,Puropse_of_course, Project_image, Student_openion, Teacher_About, Student_Question, Learning_Topic
from. models import Module_Week,Module_Name_Number,Module_Video_And_PDF


# class studentImageAdmin(admin.ModelAdmin):
#     list_display = ('user', 'Image', )
#     search_fields = ('user__email', 'Image')
#     list_filter = ('user__email',)



admin.site.register(Course_Title)
admin.site.register(All_course_data_header_name)
admin.site.register(Course_All_Data)
admin.site.register(Puropse_of_course)
admin.site.register(Project_image)
admin.site.register(Student_openion)
admin.site.register(Teacher_About)
admin.site.register(Student_Question)
admin.site.register(Learning_Topic)
admin.site.register(Module_Week)
admin.site.register(Module_Name_Number)
admin.site.register(Module_Video_And_PDF)


