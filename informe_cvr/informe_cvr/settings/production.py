import json

from django.core.exceptions import ImproperlyConfigured

from .base import *


SECRETS_FILE = os.path.join(BASE_DIR, '..', '..', 'config.json')

with open(SECRETS_FILE) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("secret_key")


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    '.informe.work',  # Allow domain and subdomains
    '.informe.work.',  # Also allow FQDN and subdomains
]

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

STATIC_ROOT = "/var/www/informe/static/"
MEDIA_ROOT = "/var/www/informe/media/"
