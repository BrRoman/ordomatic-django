""" apps/calendars/admin.py """

from django.contrib import admin
from .models import Calendar

admin.site.register(Calendar)
