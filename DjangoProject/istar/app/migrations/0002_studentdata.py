# Generated by Django 4.2.7 on 2024-03-06 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=100, verbose_name='Student Name')),
                ('StudentEmail', models.EmailField(max_length=299, verbose_name='Student Email')),
            ],
        ),
    ]
