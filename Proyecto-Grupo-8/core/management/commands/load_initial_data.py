from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Carga datos iniciales desde fixtures en un orden específico'

    def handle(self, *args, **kwargs):
        fixtures = [
            'authentication/fixtures/profiletype.json',
            'authentication/fixtures/users.json',

            'core/fixtures/organismos_sectoriales.json',
            'core/fixtures/tipo_medidas.json',
            'core/fixtures/medidas.json',
            'core/fixtures/planes_descontaminacion.json',

        ]

        for fixture in fixtures:
            try:
                self.stdout.write(f"Cargando {fixture}...")
                call_command('loaddata', fixture)
                self.stdout.write(self.style.SUCCESS(f"✔ {fixture} cargado exitosamente"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error al cargar {fixture}: {e}"))