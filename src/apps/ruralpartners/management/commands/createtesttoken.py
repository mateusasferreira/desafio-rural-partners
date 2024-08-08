from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates a teste user and token"

    def handle(self, *args, **options):
        user_model = get_user_model()

        user, _ = user_model.objects.get_or_create(
            username="testuser", password="testuser123"
        )

        token, _ = Token.objects.get_or_create(user=user)

        self.stdout.write(self.style.SUCCESS(f"Token de autenticação: {token.key}"))
