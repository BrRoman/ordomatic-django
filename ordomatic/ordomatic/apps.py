""" ordomatic/apps.py """

from django.contrib.admin.apps import AdminConfig


class MyAdminConfig(AdminConfig):
    """
    New app admin. Don't forget to replace
        'django.contrib.admin',
    by
        'ordomatic.apps.MyAdminConfig',
    in your settings.py
    """
    default_site = 'ordomatic.admin.MyAdminSite'
