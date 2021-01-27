from .base import *

DEBUG = False

SECRET_KEY = 'q#(5@wdrrkr20xop)tw8(l00!6e!^)h_nx=60i5%r$=$9fg%s7'
ALLOWED_HOSTS = ["localhost", "landet.jakobg.se", "*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "jakobgse_landetdb",
        "USER": "jakobgse_landet",
        "PASSWORD": "+!f}^^ywA@3@93=v.Wd?fdNs",
        "HOST": "localhost",
        "PORT": "",
    }
}

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://a649dd5d105743ccac75fda992298b50@o511791.ingest.sentry.io/5609562",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

try:
    from .local import *
except ImportError:
    pass
