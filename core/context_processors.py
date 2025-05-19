from django.apps import apps
from pages.models import PostType

def installed_apps_status(request):
    return {
        'pages_installed': apps.is_installed('pages'),
        'shopping_installed': apps.is_installed('shopping'),
    }


def pages_posttypes(request):
    if apps.is_installed('pages'):
        post_types = PostType.objects.filter(app_info='pages')
    else:
        post_types = PostType.objects.none()
    return {
        'pages_post_types': post_types
    }


def shops_posttypes(request):
    if apps.is_installed('shopping'):
        post_types = PostType.objects.filter(app_info='shopping')
    else:
        post_types = PostType.objects.none()
    return {
        'shopping_post_types': post_types
    }