""" apps/main/urls.py """

from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('get_easter/<int:year>/', views.get_easter, name='get_easter'),
]
