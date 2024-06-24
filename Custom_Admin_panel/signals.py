from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import batch_wise_message, Batch_wise_Student_Select

# Signal handler
@receiver(post_save, sender=batch_wise_message)
def display_user_data(sender, instance, created, **kwargs):
    if created:
        # Assuming you have a way to get the related User, for example through batchId
        related_batch = instance.batchId
        # Assuming Batch_wise_Student_Select links User with Create_Batch
        batch_student = Batch_wise_Student_Select.objects.filter(batch_number=related_batch).first()
        if batch_student:
            user = batch_student.Student_User_data
            