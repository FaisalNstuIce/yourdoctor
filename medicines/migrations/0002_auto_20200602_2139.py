# Generated by Django 3.0.2 on 2020-06-02 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0020_auto_20200602_2139'),
        ('medicines', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='appointment',
        ),
        migrations.AddField(
            model_name='medicine',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicines', to='carts.CartItem'),
        ),
    ]
