# Generated by Django 4.2.5 on 2023-10-27 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_student_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='myCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(choices=[('Web Development', 'Web Development'), ('Mobile Development', 'Mobile Development'), ('Python Development', 'Python Development'), ('Data Analysis', 'Data Analysis'), ('Devopn Tools', 'Devopn Tools'), ('UI/UX Design', 'UI/UX Design'), ('UI/UX Design', 'UI/UX Design')], max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='course',
        ),
        migrations.RemoveField(
            model_name='result',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='result',
            name='student',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]
