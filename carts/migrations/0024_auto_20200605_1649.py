# Generated by Django 3.0.2 on 2020-06-05 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0023_auto_20200605_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='81a6f0', max_length=20, unique=True),
        ),
    ]
