# Generated by Django 4.2.9 on 2024-02-01 15:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('info_pay', '0009_alter_requisit_card_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='time_create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='application',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
