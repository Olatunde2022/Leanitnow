# Generated by Django 4.2.5 on 2023-11-17 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0023_alter_proof_student'),
        ('Learnit', '0004_myreview_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myreview',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.student'),
        ),
    ]
