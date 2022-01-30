from decimal import Decimal

from django.core.management.base import BaseCommand

from planetly.carbon_usage.models import UsageType


class Command(BaseCommand):
    help = 'Imports the base usage types into the database'

    def handle(self, *args, **options):
        # this is not dynamic at all, but it's the easiest way to assure the data is where we need it
        types = [UsageType(id=100, name='electricity', unit='kwh', factor=Decimal('1.5')),
                 UsageType(id=101, name='water', unit='kg', factor=Decimal('26.93')),
                 UsageType(id=102, name='heating', unit='kwh', factor=Decimal('3.89')),
                 UsageType(id=103, name='heating', unit='l', factor=Decimal('8.57')),
                 UsageType(id=104, name='heating', unit='m3', factor=Decimal('19.46')),
                 ]
        for type in types:
            type.save()