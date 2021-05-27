""" apps/calendars/urls.py """

from django.urls import path

from . import views

app_name = 'calendars'
urlpatterns = [
    path('', views.calendars_list, name='calendars_list'),
    path('create/', views.calendar_create, name='calendar_create'),
    path('<int:pk>/', views.calendar_details, name='calendar_details'),
    path('<int:pk>/update/', views.calendar_update, name='calendar_update'),
    path('<int:pk>/delete/', views.calendar_delete, name='calendar_delete'),
]
