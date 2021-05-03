""" apps/main/urls.py """

from django.urls import path

from . import views

app_name = 'days'
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:class>/list/', views.days_list, name='days_list'),
    path('<str:class>/create/', views.day_create, name='day_create'),
    path('<str:class>/<int:pk>/details/',
         views.day_details, name='day_details'),
    path('<str:class>/<int:pk>/update/',
         views.day_update, name='day_update'),
    path('<str:class>/<int:pk>/delete/',
         views.day_delete, name='day_delete'),
]
