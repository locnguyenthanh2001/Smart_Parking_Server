# Generated by Django 4.1.3 on 2022-11-29 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='license_plate',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
