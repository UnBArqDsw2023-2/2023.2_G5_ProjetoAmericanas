from .base import *  # noqa
from .base import env

# STATIC
# ------------------------------------------------------------------------------
# TODO: use S3 instead of whitenoise
STATIC_ROOT = BASE_DIR / "staticfiles"

MIDDLEWARE.append(
    'whitenoise.middleware.WhiteNoiseMiddleware',
)
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# # DATABASES
# # ------------------------------------------------------------------------------
# DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)

# # SECURITY
# # ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env("DJANGO_SECRET_KEY")

# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = [
    "https://" + env("SERVER_NAME"),
    "https://www." + env("SERVER_NAME"),
]

ALLOWED_HOSTS = [
    env("SERVER_NAME"),
    "www." + env("SERVER_NAME"),
]

EXTRA_HTPP_HOSTNAME = env("EXTRA_HTPP_HOSTNAME", default=None)
if EXTRA_HTPP_HOSTNAME is not None:
    ALLOWED_HOSTS.append(EXTRA_HTPP_HOSTNAME)
    CSRF_TRUSTED_ORIGINS.append("http://" + EXTRA_HTPP_HOSTNAME)

EXTRA_HTPPS_HOSTNAME = env("EXTRA_HTPPS_HOSTNAME", default=None)
if EXTRA_HTPPS_HOSTNAME is not None:
    ALLOWED_HOSTS.append(EXTRA_HTPPS_HOSTNAME)
    CSRF_TRUSTED_ORIGINS.append("https://" + EXTRA_HTPPS_HOSTNAME)

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL regex.
ADMIN_URL = env("DJANGO_ADMIN_URL", default="admin/")

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": True,
        },
    },
}