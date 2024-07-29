from .base import *

ALLOWED_HOSTS = ["maandeeq.onrender.com", "maandeeq.ismailsoftdev.com"]

CSRF_TRUSTED_ORIGINS = ['https://maandeeq.ismailsoftdev.com', 'https://maandeeq.onrender.com']

DATABASES['default'] = dj_database_url.config(
    conn_max_age=600,
    default=config('DATABASE_URL')
)


STATIC_ROOT = BASE_DIR / "staticfiles"
