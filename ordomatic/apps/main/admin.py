""" apps/main/admin.py """

from django.contrib import admin
from .models import DaySancto, DayTempo

admin.site.register(DaySancto)
admin.site.register(DayTempo)
