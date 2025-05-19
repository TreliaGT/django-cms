from django.apps import apps

def installed_apps_status(request):
    return {
        'pages_installed': apps.is_installed('pages'),
        'shopping_installed': apps.is_installed('shopping'),
    }
