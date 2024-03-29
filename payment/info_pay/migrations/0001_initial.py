# Generated by Django 5.0.1 on 2024-01-26 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_payment', models.CharField(choices=[('Card', 'Карта'), ('Payment account', 'Платежный счет')], default='Card', max_length=20)),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('patronymic', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(max_length=12)),
                ('limit', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('card_type', models.CharField(blank=True, choices=[('Debit', 'Дебетовая'), ('Credit', 'Кредитная'), ('Prepaid', 'Предоплаченная')], max_length=20, null=True)),
                ('account_type', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
