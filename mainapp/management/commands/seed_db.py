from django.core.management.base import BaseCommand
# from django.contrib.auth.models import User

from mainapp.models import ProductCategory
from authapp.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):

        CustomUser.objects.create_superuser(
            'shokurov', 'test@test.ru', '9673', age=22
        )
