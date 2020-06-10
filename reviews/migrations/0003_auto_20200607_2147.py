# Generated by Django 3.0.2 on 2020-06-07 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0026_auto_20200607_2147'),
        ('reviews', '0002_auto_20200518_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='appointment',
        ),
        migrations.AddField(
            model_name='review',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carts.CartItem'),
        ),
    ]