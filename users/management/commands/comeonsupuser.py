import os
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@mail.ru',
            first_name='admin',
            last_name='admin',
            is_staff=True,
            is_active=True,
            is_superuser=True
        )
        admin_password = os.getenv('ADMIN_PASSWORD')
        user.set_password(admin_password)
        user.save()
