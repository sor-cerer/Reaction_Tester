# Generated by Django 3.2.8 on 2021-12-21 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sem5', '0002_remove_rguser_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='datahub',
        ),
        migrations.DeleteModel(
            name='rguser',
        ),
        migrations.RemoveField(
            model_name='uscore',
            name='id',
        ),
        migrations.AddField(
            model_name='uscore',
            name='avg',
            field=models.FloatField(default='', editable='false'),
        ),
        migrations.AddField(
            model_name='uscore',
            name='best',
            field=models.FloatField(default='', editable='false'),
        ),
        migrations.AddField(
            model_name='uscore',
            name='index',
            field=models.AutoField(default='', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='uscore',
            name='lvl',
            field=models.CharField(default='warm_up', max_length=40),
        ),
        migrations.AddField(
            model_name='uscore',
            name='username',
            field=models.ForeignKey(default='warm_up', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
