from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import os
from django.contrib.auth.models import Group


class Command(BaseCommand):
    """Command to verify is the user admin exits, case don't create it"""

    def handle(self, *args, **options):
        user_admin = get_user_model().objects.filter(email=os.getenv('MASTER_USER'))
        if len(user_admin) == 0:
            self.stdout.write('Admin User not exits, will be creating automatically')
            payload = {
                'email': os.getenv('MASTER_USER'),
                'password': os.getenv('MASTER_PWD'),
                'name': 'Master Administrator',
                'last_name': 'AdContent',
                'is_staff': True
            }
            user_admin = get_user_model().objects.create_user(**payload)
            if user_admin is None:
                self.stdout.write(self.style.ERROR('An error ocurring at create admin user!!!!!!!'))