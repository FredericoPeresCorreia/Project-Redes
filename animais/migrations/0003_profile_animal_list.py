# Generated by Django 2.1.7 on 2019-05-14 11:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0002_auto_20190512_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='animal_list',
            field=models.CharField(default=0, max_length=100, validators=[django.core.validators.int_list_validator]),
        ),
    ]
