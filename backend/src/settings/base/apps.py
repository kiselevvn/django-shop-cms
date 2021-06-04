DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "constance",
    "constance.backends.database",
    "rest_framework",
    "ckeditor",
    "ckeditor_uploader",
]

PROJECT_APPS = [
    "apps.services",
    "apps.users",
    "apps.products",
    "apps.orders",
    "apps.cart",
    "apps.warehouse",
    "apps.interface",
]

DEVELOPER_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
    "debug_toolbar",
]

PRODUCTION_APPS = [*DEFAULT_APPS, *PROJECT_APPS]
