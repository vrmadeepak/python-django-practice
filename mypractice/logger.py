import os


def location(x):
    return os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), x)


LOG_ROOT = location("logs")
if not os.path.exists(LOG_ROOT):
    os.mkdir(LOG_ROOT)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(message)s",
        },
        "standard": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s@%(funcName)s:%(lineno)s] %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
        "simple": {"format": "[%(asctime)s] %(message)s"},
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console"],
    },
    "handlers": {
        "null": {
            "level": "DEBUG",
            "class": "logging.NullHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "logfile": {
            "level": "DEBUG",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": LOG_ROOT + "/logfile.log",
            "when": "midnight",
            "backupCount": 0,
            "formatter": "standard",
        },
    },
    "loggers": {
        # Django loggers
        "django": {
            "handlers": ["null"],
            "propagate": False,
            "level": "INFO",
        },
        "django.request": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.db.backends": {
            "level": "DEBUG",
            "propagate": False,
        },
        "django.security.DisallowedHost": {
            "handlers": ["null"],
            "propagate": False,
        },
        "apps.common": {
            "handlers": ["console", "logfile"],
            "level": "DEBUG",
        },
        "apps.todolist": {
            "handlers": ["console", "logfile"],
            "level": "DEBUG",
        },
        "apps.calculator": {
            "handlers": ["console", "logfile"],
            "level": "DEBUG",
        },
        "apps.contactlist": {
            "handlers": ["console", "logfile"],
            "level": "DEBUG",
        },
        "bookstore": {
            "handlers": ["console", "logfile"],
            "level": "DEBUG",
        },
    },
}
