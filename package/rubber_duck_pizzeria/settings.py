"""Django settings for the kitchen admin (dev lab)."""
import os

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "")
DEBUG = os.environ.get("DJANGO_DEBUG", "True")
ALLOWED_HOSTS = ["kitchen.example.com"]
INSTALLED_APPS = ["django.contrib.admin", "django.contrib.auth"]
ROOT_URLCONF = "kitchen.urls"
