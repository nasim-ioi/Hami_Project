# Generated by Django 2.2 on 2020-04-09 19:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0006_auto_20200409_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='purchase_id',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0, message='purchase_id should be positive integer')]),
        ),
        migrations.AlterField(
            model_name='blog',
            name='user_id',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0, message='user_id should be positive integer')]),
        ),
    ]