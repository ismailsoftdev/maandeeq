from .base import *

ALLOWED_HOSTS = ["*"]

DATABASES['default'] = dj_database_url.config(
    conn_max_age=600,
    default=config('DATABASE_URL')
)