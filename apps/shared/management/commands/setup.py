from django.core.management.base import BaseCommand
from apps.banquets.models import State, City


class Command(BaseCommand):
    """
    Create initial data for database
    """
    help = 'Create initial data for database'

    def handle(self, *args, **options):
        # create superuser
        self.stdout.write('Creating superuser...')
        from django.contrib.auth import get_user_model
        User = get_user_model()
        try:
            User.objects.create_superuser(
                email='santiago.corrales@alternova.com',
                password='123456',
            )
        except:
            pass
        self.stdout.write('Superuser created successfully!')

        # create states and cities
        self.stdout.write('Creating states and cities...')
        with open('states.csv', 'r',  encoding="utf8") as file:
            for line in file:
                line = line.split(';')
                state = State.objects.get_or_create(name=line[0])[0]
                for city in line[1:]:
                    try:
                        City.objects.create(name=city, state=state)
                    except:
                        pass
        self.stdout.write('States and cities created successfully!')

