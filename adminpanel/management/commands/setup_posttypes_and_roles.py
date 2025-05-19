from django.core.management.base import BaseCommand
from django.apps import apps
from adminpanel.models import Role
from pages.models import PostType

class Command(BaseCommand):
    help = 'Add post types based on existing app_info entries and create default roles'

    def handle(self, *args, **kwargs):
        # Create roles
        roles = ['admin', 'user', 'editor', 'shop manager']
        for role_name in roles:
            role, created = Role.objects.get_or_create(name=role_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Role: {role_name}'))
            else:
                self.stdout.write(f'Role "{role_name}" already exists')

        # Check for 'pages' app_info
        if apps.is_installed('pages'):
            self.stdout.write('App "pages" found. Adding "pages" and "posts" PostTypes...')
            for name, url in [('pages', 'pages'), ('posts', 'posts')]:
                pt, created = PostType.objects.get_or_create(
                    name=name,
                    defaults={'url_starter': url, 'app_info': 'pages'}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created PostType: {name}'))
                else:
                    self.stdout.write(f'PostType "{name}" already exists')
        else:
            self.stdout.write('App "pages" not found. Skipping pages post types.')

        # Check for 'shopping' app_info
        if apps.is_installed('shopping'):
            self.stdout.write('App "shopping" found. Adding "products" and "orders" PostTypes...')
            for name, url in [('products', 'products'), ('orders', 'orders')]:
                pt, created = PostType.objects.get_or_create(
                    name=name,
                    defaults={'url_starter': url, 'app_info': 'shopping'}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created PostType: {name}'))
                else:
                    self.stdout.write(f'PostType "{name}" already exists')
        else:
            self.stdout.write('App "shopping" not found. Skipping shopping post types.')

        self.stdout.write(self.style.SUCCESS('Setup completed.'))
