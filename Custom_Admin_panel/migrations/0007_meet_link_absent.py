# Generated by Django 4.2.11 on 2024-06-23 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Custom_Admin_panel', '0006_remove_attendence_system_batchid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='meet_link',
            name='absent',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
