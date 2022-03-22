# Generated by Django 3.2 on 2022-03-22 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('location', models.CharField(choices=[('OUTSIDE', 'OUTSIDE'), ('WINDOW', 'WINDOW'), ('HALL', 'HALL')], max_length=10)),
                ('capacity', models.IntegerField()),
                ('status', models.IntegerField(choices=[(0, 'Available'), (1, 'Unavailable')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_size', models.PositiveIntegerField()),
                ('date', models.DateField(blank=True)),
                ('start_time', models.TimeField(blank=True)),
                ('end_time', models.TimeField(blank=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.table')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
