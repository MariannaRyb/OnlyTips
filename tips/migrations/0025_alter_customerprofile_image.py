# Generated by Django 4.0.4 on 2022-05-29 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0024_alter_customerprofile_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='image',
            field=models.ImageField(default='tips/images/pic user.png', upload_to='images'),
        ),
    ]
