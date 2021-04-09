""" apps/main/views.py """

from django.shortcuts import render


def home(request):
    """ Home page of Ordomatic. """
    return render(request, 'main/home.html')
