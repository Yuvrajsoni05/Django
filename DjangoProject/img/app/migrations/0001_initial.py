# Generated by Django 4.2.7 on 2023-11-07 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imagename', models.CharField(max_length=50)),
                ('Image', models.ImageField(upload_to='img/')),
            ],
        ),
    ]