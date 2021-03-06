# Generated by Django 3.0.2 on 2020-05-31 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0015_auto_20200530_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentschedule',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='appointment_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='fba819', max_length=20, unique=True),
        ),
    ]
