# Generated by Django 4.0.4 on 2022-05-31 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0028_join_alter_customerprofile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=200)),
                ('reciever', models.CharField(max_length=200)),
                ('tID', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]
