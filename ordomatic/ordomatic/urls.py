""" ordomatic/urls.py """

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('ordomatic/', include('apps.main.urls')),
    path('ordomatic/admin/', admin.site.urls),
]
