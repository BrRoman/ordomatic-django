""" ordomatic/urls.py """

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('ordomatic/', include('apps.main.urls')),
    path('ordomatic/docs/', include('apps.docs.urls')),
    path('ordomatic/accounts/', include('apps.accounts.urls')),
    path('ordomatic/calendars/', include('apps.calendars.urls')),
    path('ordomatic/days/', include('apps.days.urls')),
    path('ordomatic/admin/', admin.site.urls),
]
