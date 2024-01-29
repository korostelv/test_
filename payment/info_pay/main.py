from django_seed import Seed
from models import Application, Requisit
seeder = Seed.seeder(locale='ru_RU')



seeder.add_entity(Requisit, 5)
inserted_pks = seeder.execute()


# python manage.py seed info_pay --number=10 - команда


