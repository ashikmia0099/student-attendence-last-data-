# Generated by Django 4.2.11 on 2024-06-23 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Custom_Admin_panel', '0008_alter_meet_link_absent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meet_link',
            name='absent',
            field=models.CharField(max_length=10),
        ),
    ]
