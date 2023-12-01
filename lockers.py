from django.core.management.base import BaseCommand
from registration.models import *

class Command(BaseCommand):
    help = 'Generate lockers with identical keys and numbers'

    def handle(self, *args, **kwargs):
        for i in range(1, 97):
            locker = Locker(number=i)
            locker.save()
            self.stdout.write(self.style.SUCCESS(f'Created locker {i}'))