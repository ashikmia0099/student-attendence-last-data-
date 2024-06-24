# Generated by Django 4.2.11 on 2024-06-15 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='All_Category_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(blank=True, default=' ', max_length=150, null=True)),
                ('slug', models.SlugField(blank=True, default=' ', max_length=150, null=True, unique=True)),
                ('Category_Image', models.ImageField(blank=True, default=' ', null=True, upload_to='Deshboard/media/')),
            ],
            options={
                'verbose_name': '4.1 All Category Name and Image',
                'verbose_name_plural': '4.1 All Category Name and Image',
            },
        ),
        migrations.CreateModel(
            name='All_category_text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cattegory_top_text', models.TextField(blank=True, default=' ', null=True)),
            ],
            options={
                'verbose_name': '4. All Course Heading Text',
                'verbose_name_plural': '4. All Course Heading Text',
            },
        ),
        migrations.CreateModel(
            name='BannerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Banner_title', models.CharField(blank=True, default=' ', max_length=150, null=True)),
                ('Banner_text', models.TextField(blank=True, default=' ', null=True)),
                ('Banner_video_image', models.ImageField(blank=True, default=' ', null=True, upload_to='Deshboard/media/')),
                ('Banner_video', models.FileField(blank=True, default=' ', null=True, upload_to='Deshboard/media/')),
            ],
            options={
                'verbose_name': '2. Banner Model',
                'verbose_name_plural': '2. Banner Model',
            },
        ),
        migrations.CreateModel(
            name='HomeEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_image', models.ImageField(blank=True, null=True, upload_to='Deshboard/media/')),
            ],
            options={
                'verbose_name': '10. Institute Event Image',
                'verbose_name_plural': '10. Institute Event Image',
            },
        ),
        migrations.CreateModel(
            name='HomeExpertTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teacher_image', models.ImageField(blank=True, null=True, upload_to='Deshboard/media/')),
                ('Teacher_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Position_name', models.CharField(blank=True, max_length=100, null=True)),
                ('institute_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': '11. Teacher Information ',
                'verbose_name_plural': '11. Teacher Information ',
            },
        ),
        migrations.CreateModel(
            name='HomeInstituteBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BannerTitle', models.CharField(blank=True, max_length=150, null=True)),
                ('BannerText', models.TextField(blank=True, null=True)),
                ('Banner_image', models.ImageField(blank=True, null=True, upload_to='Deshboard/media/')),
            ],
            options={
                'verbose_name': '8. Institute Banner left Image',
                'verbose_name_plural': '8. Institute Banner left Image',
            },
        ),
        migrations.CreateModel(
            name='HomeInstituteBannersecond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Banner_Title', models.CharField(blank=True, max_length=150, null=True)),
                ('Banner_Text', models.TextField(blank=True, null=True)),
                ('Banner_image', models.ImageField(blank=True, null=True, upload_to='Deshboard/media/')),
            ],
            options={
                'verbose_name': '8.1 Institute Banner Right Image',
                'verbose_name_plural': '8.1 Institute Banner Right Image',
            },
        ),
        migrations.CreateModel(
            name='HomeOurService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(blank=True, default=' ', max_length=100, null=True)),
            ],
            options={
                'verbose_name': '5.1 Our Service ',
                'verbose_name_plural': '5.1 Our Service ',
            },
        ),
        migrations.CreateModel(
            name='HomeStudentOpenion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_image', models.ImageField(blank=True, null=True, upload_to='Deshboard/media/')),
                ('Student_name', models.CharField(blank=True, max_length=50, null=True)),
                ('openion_course_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Openion_text', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name': '12. Student Openion ',
                'verbose_name_plural': '12. Student Openion ',
            },
        ),
        migrations.CreateModel(
            name='our_partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prather_Logo', models.ImageField(blank=True, null=True, upload_to='Deshboard/media/')),
            ],
            options={
                'verbose_name': '14. Our Partner Image ',
                'verbose_name_plural': '14. Our Partner Image ',
            },
        ),
        migrations.CreateModel(
            name='Our_Service_Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_text', models.TextField(blank=True, null=True)),
                ('Image', models.ImageField(blank=True, default=' ', null=True, upload_to='Deshboard/media/')),
            ],
            options={
                'verbose_name': '5. Our Service Heading Text And Banner Image ',
                'verbose_name_plural': '5. Our Service Heading Text And Banner Image ',
            },
        ),
        migrations.CreateModel(
            name='Success_history_video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Success_history_text', models.TextField(blank=True, default=' ', null=True)),
                ('Success_history_image', models.ImageField(blank=True, default=' ', null=True, upload_to='Deshboard/media/')),
                ('Success_Video_history', models.FileField(blank=True, default=' ', null=True, upload_to='Deshboard/media/')),
            ],
            options={
                'verbose_name': '9. Success History Video Model',
                'verbose_name_plural': '9. Success History Video Model',
            },
        ),
        migrations.CreateModel(
            name='All_Category_Card_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, default=' ', null=True, upload_to='Deshboard/media/')),
                ('Course_name', models.CharField(blank=True, default=' ', max_length=100, null=True)),
                ('student_review', models.CharField(blank=True, default=' ', max_length=200, null=True)),
                ('Course_fees', models.CharField(blank=True, default=' ', max_length=100, null=True)),
                ('Category_Name', models.ForeignKey(blank=True, default=' ', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_name', to='Deshboard.all_category_model')),
            ],
            options={
                'verbose_name': '4.2 All Category Card Data',
                'verbose_name_plural': '4.2 All Category Card Data',
            },
        ),
    ]