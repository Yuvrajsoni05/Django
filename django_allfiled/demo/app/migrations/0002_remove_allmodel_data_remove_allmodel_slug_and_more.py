# Generated by Django 5.1.2 on 2024-10-17 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allmodel',
            name='data',
        ),
        migrations.RemoveField(
            model_name='allmodel',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='allmodel',
            name='uuid',
        ),
    ]