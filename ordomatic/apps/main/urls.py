""" apps/main/urls.py """

from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path(
        '',
        views.home,
        name='home',
    ),
    path(
        'ordo/<int:year>',
        views.ordo,
        name='ordo',
    ),
    path(
        'get_list_of_days_as_html/<int:year>/',
        views.get_list_of_days_as_html,
        name='get_list_of_days_as_html',
    ),
]
