# Generated by Django 4.2.5 on 2023-11-05 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0021_proof_uploaddatetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proof',
            name='receipt',
            field=models.ImageField(default=2, upload_to=''),
            preserve_default=False,
        ),
    ]
