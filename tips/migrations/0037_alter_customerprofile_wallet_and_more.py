# Generated by Django 4.0.4 on 2022-06-03 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0036_remove_customerprofile_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='wallet',
            field=models.CharField(blank=True, default=0, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='waiterprofile',
            name='wallet',
            field=models.CharField(blank=True, default=0, max_length=200, unique=True),
        ),
    ]
