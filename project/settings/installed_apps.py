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
    # Easy Mask - https://github.com/dhelbegor/easy-mask
    'easy_mask',
    # Local apps
    'apps.home',
    'apps.login',
    'apps.core',
    'apps.users',
]
