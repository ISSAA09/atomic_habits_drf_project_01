from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='habit@habitov.ru',
            first_name='habit',
            last_name='habitov',
            is_staff=True,
            is_superuser=True,
            is_active=True,
            role='moderator'
        )

        user.set_password('Q1234567')
        user.save()
