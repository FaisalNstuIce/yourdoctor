# Generated by Django 3.0.2 on 2020-05-22 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_delete_payment'),
        ('carts', '0007_auto_20200523_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='appointment_fee',
            field=models.DecimalField(decimal_places=2, default='00.00', max_digits=10),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='appointment_schedule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appointments.AppointmentSchedule'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='49cdf2', max_length=20, unique=True),
        ),
    ]