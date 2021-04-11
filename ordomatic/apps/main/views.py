""" apps/main/views.py """

from django.shortcuts import render

from .dates import calculate_easter


def home(request):
    """ Home page of Ordomatic. """
    return render(
        request,
        'main/home.html',
    )


def get_easter(request, **kwargs):
    """ Returns a piece of web page containing the Easter's date of the given year. """
    easter = calculate_easter(kwargs['year'])
    return render(
        request,
        'main/easter.html',
        {
            'year': kwargs['year'],
            'easter': easter,
        },
    )
