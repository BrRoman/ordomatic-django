""" apps/main/urls.py """

from django.urls import path

from . import views

app_name = 'days'
urlpatterns = [
    path('<int:calendar>/', views.home, name='home'),
    path('<int:calendar>/<str:category>/', views.days_list, name='days_list'),
    path('<int:calendar>/<str:category>/create/',
         views.day_create, name='day_create'),
    path('<int:calendar>/<str:category>/<int:pk>/',
         views.day_details, name='day_details'),
    path('<int:calendar>/<str:category>/<int:pk>/update/',
         views.day_update, name='day_update'),
    path('<int:calendar>/<str:category>/<int:pk>/delete/',
         views.day_delete, name='day_delete'),
]
