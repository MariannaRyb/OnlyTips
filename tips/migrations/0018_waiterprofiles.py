# Generated by Django 4.0.4 on 2022-05-20 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tips', '0017_remove_waiter_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaiterProfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images')),
                ('cafe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tips.cafe')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
