# Generated by Django 4.2.9 on 2024-01-29 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_pay', '0007_remove_requisit_patronymic'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisit',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
