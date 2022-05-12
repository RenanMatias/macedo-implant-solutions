# Application definition

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Debug toolbar
    'debug_toolbar',
    # Django REST framework
    'rest_framework',
    # Local apps
    'apps.home',
    'apps.login'
]
