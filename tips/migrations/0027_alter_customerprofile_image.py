# Generated by Django 4.0.4 on 2022-05-29 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0026_alter_customerprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='image',
            field=models.ImageField(default=0, upload_to='images'),
        ),
    ]
