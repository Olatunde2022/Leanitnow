# Generated by Django 4.2.5 on 2023-11-17 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Learnit', '0005_alter_myreview_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myreview',
            old_name='user',
            new_name='student',
        ),
    ]
