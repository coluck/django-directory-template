from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Generates a secret key and stores it in config/settings/.env file"

    def handle(self, *args, **options):
        from django.core.management.utils import get_random_secret_key
        SECRET_KEY = get_random_secret_key()
        with open("./config/settings/.env", 'w+') as f:
            f.write("SECRET_KEY=" + SECRET_KEY)

        self.stdout.write(self.style.SUCCESS("Succesfully generated secret key"))
