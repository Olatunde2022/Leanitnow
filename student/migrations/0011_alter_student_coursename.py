# Generated by Django 4.2.5 on 2023-10-31 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_remove_mycourse_user_student_coursename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courseName',
            field=models.ManyToManyField(blank=True, null=True, to='student.mycourse'),
        ),
    ]
