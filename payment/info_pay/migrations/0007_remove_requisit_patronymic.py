# Generated by Django 4.2.9 on 2024-01-29 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_pay', '0006_alter_application_requisit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisit',
            name='patronymic',
        ),
    ]
