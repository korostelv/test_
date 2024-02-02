from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

class Requisit(models.Model):
    Choices_pay = [
        ('Карта', "Карта"),
        ('Платежный счет', "Платежный счет")
    ]
    Choices_card = [
        ('Дебетовая', 'Дебетовая'),
        ('Кредитная', 'Кредитная'),
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
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=12)
    limit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    card_type = models.CharField(choices=Choices_card, max_length=20, blank=True, null=True)
    account_type = models.CharField(choices=Choices_account, max_length=20, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.type_payment == 'Карта':
            self.account_type = None
        elif self.type_payment == 'Платежный счет':
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
    requisit = models.ForeignKey('Requisit', on_delete=models.CASCADE)
    time_create = models.DateTimeField(default=timezone.now)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.summ}'


@receiver(pre_save, sender=Application)
def sum(sender, instance, **kwargs):
    if instance.summ > instance.requisit.limit:
        raise ValidationError('Сумма не может превышать лимит реквизита')




