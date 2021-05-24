""" apps/ordos/urls.py """

from django.urls import path

from . import views

app_name = 'ordos'
urlpatterns = [
    path('', views.ordos_list, name='ordos_list'),
    path('create/', views.ordo_create, name='ordo_create'),
    path('<int:pk>/', views.ordo_details, name='ordo_details'),
    path('<int:pk>/update/', views.ordo_update, name='ordo_update'),
    path('<int:pk>/delete/', views.ordo_delete, name='ordo_delete'),
]
