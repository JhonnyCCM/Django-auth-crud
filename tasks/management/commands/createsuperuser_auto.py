from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a superuser if one does not exist'

    def handle(self, *args, **kwargs):
        # Verifica si ya existe un superusuario
        if not User.objects.filter(is_superuser=True).exists():
            # Crea un superusuario con las credenciales que prefieras
            User.objects.create_superuser(
                username='jhonny',  # El nombre de usuario que deseas
                email='admin@example.com',  # El correo electrónico del superusuario
                password='admin'  # La contraseña del superusuario
            )
            self.stdout.write(self.style.SUCCESS('Superuser created successfully!'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists.'))
