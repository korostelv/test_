from django_seed import Seed
from models import Application, Requisit
seeder = Seed.seeder(locale='ru_RU')



seeder.add_entity(Requisit, 5)
inserted_pks = seeder.execute()


# python manage.py seed info_pay --number=10 - команда



# Ваш seed_requisit.py
from django.core.management.base import BaseCommand
from django_seed import Seed
from .models import Requisit

class Command(BaseCommand):
    help = 'Seed the Requisit model with sample data'

    def add_arguments(self, parser):
        parser.add_argument('--number', type=int, default=1, help='Indicates the number of records to seed')

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder(locale='ru_RU')

        seeder.add_entity(Requisit, kwargs['number'], {
            'type_payment': lambda x: seeder.random_element(Requisit.Choices_pay),
            'last_name': lambda x: seeder.last_name(),
            'first_name': lambda x: seeder.first_name(),
            'middle_name': lambda x: seeder.first_name() if seeder.boolean() else None,
            'phone': lambda x: seeder.phone_number(),
            'limit': lambda x: seeder.random_number(digits=5) / 100,
            'card_type': lambda x: seeder.random_element(Requisit.Choices_card) if seeder.boolean() else None,
            'account_type': lambda x: seeder.random_element(Requisit.Choices_account) if seeder.boolean() else None,
        })

        inserted_pks = seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {inserted_pks} records for Requisit.'))


