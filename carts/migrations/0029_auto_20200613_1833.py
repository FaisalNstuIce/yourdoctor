# Generated by Django 3.0.2 on 2020-06-13 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0028_auto_20200610_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='0b3fae', max_length=20, unique=True),
        ),
    ]
