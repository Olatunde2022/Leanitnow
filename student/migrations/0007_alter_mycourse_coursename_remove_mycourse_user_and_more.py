# Generated by Django 4.2.5 on 2023-10-28 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_mycourse_remove_question_course_remove_result_exam_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycourse',
            name='courseName',
            field=models.CharField(max_length=500),
        ),
        migrations.RemoveField(
            model_name='mycourse',
            name='user',
        ),
        migrations.AddField(
            model_name='mycourse',
            name='user',
            field=models.ManyToManyField(to='student.student'),
        ),
    ]