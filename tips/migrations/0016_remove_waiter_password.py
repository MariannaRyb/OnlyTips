# Generated by Django 4.0.4 on 2022-05-20 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0015_waiter_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waiter',
            name='password',
        ),
    ]