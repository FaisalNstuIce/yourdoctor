# Generated by Django 3.0.2 on 2020-06-10 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0027_auto_20200609_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='4a6e23', max_length=20, unique=True),
        ),
    ]
