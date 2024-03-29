# Generated by Django 5.0.1 on 2024-01-26 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_pay', '0004_alter_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Ожидает оплаты', 'Ожидает оплаты'), ('Оплачена', 'Оплачена'), ('Отменена', 'Отменена')], max_length=20),
        ),
        migrations.AlterField(
            model_name='requisit',
            name='account_type',
            field=models.CharField(blank=True, choices=[('Текущий', 'Текущий'), ('Сберегательный', 'Сберегательный'), ('Бизнес-счет', 'Бизнес-счет')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='requisit',
            name='card_type',
            field=models.CharField(blank=True, choices=[('Дебетовая', 'Дебетовая'), ('Дебетовая', 'Кредитная'), ('Предоплаченная', 'Предоплаченная')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='requisit',
            name='type_payment',
            field=models.CharField(choices=[('Карта', 'Карта'), ('Платежный счет', 'Платежный счет')], default='Card', max_length=20),
        ),
    ]
