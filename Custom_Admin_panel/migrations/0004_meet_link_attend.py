# Generated by Django 4.2.11 on 2024-06-19 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Custom_Admin_panel', '0003_attendence_system'),
    ]

    operations = [
        migrations.AddField(
            model_name='meet_link',
            name='attend',
            field=models.BooleanField(default=False),
        ),
    ]
