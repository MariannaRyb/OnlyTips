# Generated by Django 4.0.4 on 2022-05-31 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0027_alter_customerprofile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('cafe', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='image',
            field=models.ImageField(blank=True, default=0, upload_to='images'),
        ),
    ]
