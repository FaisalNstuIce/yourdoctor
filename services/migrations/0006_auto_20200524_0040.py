# Generated by Django 3.0.2 on 2020-05-23 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20200523_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicefee',
            name='service',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.Service'),
        ),
    ]