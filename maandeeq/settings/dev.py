from .base import *

DATABASES['default'] = dj_database_url.config(
    conn_max_age=600,
    default=config('DATABASE_URL')
)