# Generated by Django 4.2.5 on 2023-09-21 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(default=8, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default=8, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='myInstitution-django/media/profile_pic'),
        ),
    ]
