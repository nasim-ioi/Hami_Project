# Generated by Django 2.2 on 2020-04-09 17:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='blog_owner',
        ),
        migrations.AlterField(
            model_name='blog',
            name='email',
            field=models.CharField(max_length=150, validators=[django.core.validators.EmailValidator]),
        ),
        migrations.AlterField(
            model_name='blog',
            name='phone_number',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format '09128158817' and have only 11 digits allowed.", regex='^(09)?\\d{11}$')]),
        ),
        migrations.AlterField(
            model_name='blog',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
