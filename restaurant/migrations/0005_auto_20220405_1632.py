# Generated by Django 3.2 on 2022-04-05 16:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_alter_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+9999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
