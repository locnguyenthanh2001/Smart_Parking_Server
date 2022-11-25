# Generated by Django 4.1.3 on 2022-11-18 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_lot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parkinglot',
            name='area',
        ),
        migrations.AddField(
            model_name='parkinglot',
            name='lattitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='parkinglot',
            name='longtitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='parkinglot',
            name='radius',
            field=models.FloatField(default=0),
        ),
        migrations.DeleteModel(
            name='Corner',
        ),
    ]
