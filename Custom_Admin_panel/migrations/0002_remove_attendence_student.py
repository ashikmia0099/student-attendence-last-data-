# Generated by Django 4.2.11 on 2024-06-19 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Custom_Admin_panel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendence',
            name='student',
        ),
    ]
