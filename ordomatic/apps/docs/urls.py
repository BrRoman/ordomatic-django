""" apps/docs/urls.py """

from django.urls import path

from . import views

app_name = 'docs'
urlpatterns = [
    path('', views.index, name='index'),
    path('overview/', views.overview, name='overview'),
    path('what_is_an_ordo/', views.what_is_an_ordo, name='what_is_an_ordo'),
    path('create_an_account/', views.create_an_account, name='create_an_account'),
    path('create_a_calendar/', views.create_a_calendar, name='create_a_calendar'),
    path('populate_your_calendar/', views.populate_your_calendar,
         name='populate_your_calendar'),
    path('create_an_ordo/', views.create_an_ordo, name='create_an_ordo'),
    path('for_developers/', views.for_developers, name='for_developers'),
]
