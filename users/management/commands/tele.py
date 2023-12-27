from django.core.management import BaseCommand

from habits.services import habit_bot


class Command(BaseCommand):
    def handle(self, *args, **options):
        habit_bot()
