from django.db import models


class Requisit(models.Model):
    Choices_pay = [
        ('Карта', "Карта"),
        ('Платежный счет', "Платежный счет")
    ]
    Choices_card = [
        ('Дебетовая', 'Дебетовая'),
        ('Дебетовая', 'Кредитная'),
        ('Предоплаченная', 'Предоплаченная')
    ]
    Choices_account = [
        ('Текущий', 'Текущий'),
        ('Сберегательный', 'Сберегательный'),
        ('Бизнес-счет', 'Бизнес-счет')
    ]
    type_payment = models.CharField(max_length=20, choices=Choices_pay, default='Card')
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=12)
    limit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    card_type = models.CharField(choices=Choices_card, max_length=20, blank=True, null=True)
    account_type = models.CharField(choices=Choices_account, max_length=20, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.type_payment == 'Card':
            self.account_type = None
        elif self.type_payment == 'Payment account':
            self.card_type = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

class Application(models.Model):
    Choices_status = [
        ('Ожидает оплаты', 'Ожидает оплаты'),
        ('Оплачена', 'Оплачена'),
        ('Отменена', 'Отменена')
    ]
    summ = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    status = models.CharField(choices=Choices_status, max_length=20)
    requisit = models.ForeignKey('Requisit',blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.summ}'


