# Generated by Django 5.1.3 on 2025-01-19 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_otp_user_otp_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='email',
            field=models.EmailField(default='shyam102@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
