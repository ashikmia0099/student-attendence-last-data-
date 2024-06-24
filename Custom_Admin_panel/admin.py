from django.contrib import admin

from .models import Create_Batch,Assingment_result, Batch_wise_Student_Select, Meet_link,batch_wise_message,Batch_wise_Assingment,Assingment_Submit,Batch_time_set

from .models import Student_Attendance

admin.site.register(Create_Batch)
admin.site.register(Batch_wise_Student_Select)
admin.site.register(Meet_link)
admin.site.register(batch_wise_message)
admin.site.register(Batch_wise_Assingment)

admin.site.register(Assingment_Submit)
admin.site.register(Batch_time_set)
admin.site.register(Assingment_result)

admin.site.register(Student_Attendance)