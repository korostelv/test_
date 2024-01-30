from django.apps import apps
from django.core.management.base import BaseCommand
from django_seed import Seed
import random
from faker import Faker
fake = Faker('ru_RU')

Requisit = apps.get_model('info_pay', 'Requisit')



class Command(BaseCommand):
    help = 'Забить данными Requisit'

    def add_arguments(self, parser):
        parser.add_argument('--number', type=int, default=1, help='Количество строк данных')

    def handle(self, *args, **options):
        seeder = Seed.seeder(locale='ru_RU')


        seeder.add_entity(Requisit, options['number'], {
            'type_payment': lambda x: random.choice([choice[0] for choice in Requisit.Choices_pay]),
            'first_name': lambda x: fake.first_name(),
            'last_name': lambda x: fake.last_name(),
            'middle_name': lambda x: fake.middle_name(),
            'phone': lambda x: fake.phone_number(),
            'limit': lambda x: random.randint(50000, 1000000),

        })
        inserted_pks = seeder.execute()

