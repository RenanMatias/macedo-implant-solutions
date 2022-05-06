from .installed_apps import INSTALLED_APPS
from .middlewares import MIDDLEWARE

INSTALLED_APPS += [
    'tailwind',
    'theme',
    'django_browser_reload',
]

MIDDLEWARE += [
    'django_browser_reload.middleware.BrowserReloadMiddleware',
]

TAILWIND_APP_NAME = 'theme'

NPM_BIN_PATH = '/home/renanm/.nvm/versions/node/v16.14.2/bin/npm'
