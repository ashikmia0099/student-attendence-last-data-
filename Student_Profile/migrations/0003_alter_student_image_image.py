# Generated by Django 4.2.11 on 2024-06-15 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_Profile', '0002_alter_student_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_image',
            name='Image',
            field=models.ImageField(blank=True, default='Student_Profile/media/pro.png', null=True, upload_to='Student_Profile/media/'),
        ),
    ]
