import os
from epiphane_web_app.settings import *
import dj_database_url
import django_heroku


DEBUG = False
TEMPLATE_DEBUG = True

DEFAULT_ENV = os.environ.get("DATABASE_URL")

DATABASES = {"default": dj_database_url.config(default="postgres://localhost")}

MIDDLEWARE += [
    "whitenoise.middleware.WhiteNoiseMiddleware",
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

django_heroku.settings(locals())

ALLOWED_HOSTS = ["epiphane-app-django-abd9746eda9b.herokuapp.com", "www.epiphane-egah.fr"]
