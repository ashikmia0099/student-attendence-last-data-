from django.contrib import admin
from .models import Student_Certificate, Student_image
# Register your models here.
 


class CertificatAdmin(admin.ModelAdmin):
    list_display = ('user', 'Certificate', )
    search_fields = ('user__email', 'Certificate')
    list_filter = ('user__email',)



class studentImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'Image', )
    search_fields = ('user__email', 'Image')
    list_filter = ('user__email',)



admin.site.register(Student_Certificate, CertificatAdmin)
admin.site.register(Student_image, studentImageAdmin)