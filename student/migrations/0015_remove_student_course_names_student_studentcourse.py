# Generated by Django 4.2.5 on 2023-10-31 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_rename_coursename_student_course_names'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course_names',
        ),
        migrations.AddField(
            model_name='student',
            name='studentcourse',
            field=models.ManyToManyField(to='student.mycourse'),
        ),
    ]
