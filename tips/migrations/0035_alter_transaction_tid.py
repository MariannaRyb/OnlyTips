# Generated by Django 4.0.4 on 2022-06-02 20:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0034_alter_transaction_receiver_alter_transaction_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='tID',
            field=models.CharField(default=uuid.uuid4, max_length=200, unique=True),
        ),
    ]
