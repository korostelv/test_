import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.utils import timezone
from django.apps import apps

Application = apps.get_model('info_pay', 'Application')
Requisit = apps.get_model('info_pay', 'Requisit')


class Command(BaseCommand):
    help = 'Забить данными Application'

    def add_arguments(self, parser):
        parser.add_argument('--number', type=int, default=1, help='Количество строк данных')

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        seeder.add_entity(Application, options['number'], {
            'requisit': lambda x: random.choice(Requisit.objects.all()),
            'summ': lambda x: random.randint(0, random.choice(Requisit.objects.all()).limit),
            'time_update': timezone.now()
        })
        seeder.execute()

