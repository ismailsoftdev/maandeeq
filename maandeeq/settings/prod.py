from .base import *

ALLOWED_HOSTS = ["maandeeq.onrender.com", "maandeeq.ismailsoftdev.com"]

CSRF_TRUSTED_ORIGINS = ['https://maandeeq.ismailsoftdev.com', 'https://maandeeq.onrender.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', cast=int),
    }
}


STATIC_ROOT = BASE_DIR / "staticfiles"
