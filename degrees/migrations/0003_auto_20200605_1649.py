# Generated by Django 3.0.2 on 2020-06-05 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('degrees', '0002_degree_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='degree',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='degree',
            name='approved_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='degreeapproves', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='degree',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
