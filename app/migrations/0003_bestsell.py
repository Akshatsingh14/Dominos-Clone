# Generated by Django 5.1.3 on 2025-01-13 18:26

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_slide_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bestsell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\Lenovo\\Desktop\\Django\\Projects\\Dominos_Clone\\media'), upload_to='bestseller/')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('order', models.IntegerField(default=0)),
            ],
        ),
    ]
