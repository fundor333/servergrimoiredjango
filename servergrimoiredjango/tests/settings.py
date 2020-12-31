# -*- coding: utf-8 -*-
# ensure package/conf is importable

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}

INSTALLED_APPS = (
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "django.contrib.auth",
    "servergrimoiredjango",
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
)

ROOT_URLCONF = "servergrimoiredjango.tests.urls"
TEMPLATE_DEBUG = True

SECRET_KEY = "foobar"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
    }
]

STATIC_URL = "/static/"

# XMLTestRunner output
TEST_OUTPUT_DIR = ".xmlcoverage"
