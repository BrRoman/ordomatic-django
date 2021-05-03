""" apps/main/views.py """

from datetime import date

from django.shortcuts import render

from apps.days.views import fetch_days


def home(request):
    """ Home page of Ordomatic. """
    return render(
        request,
        'main/home.html',
        {},
    )


def ordo(request):
    """ Ordo page of Ordomatic. """
    return render(
        request,
        'main/ordo.html',
        {
            'year': date.today().year,
        }
    )


def get_ordo_as_html(request, **kwargs):
    """ Returns the ordo of the given year as html. """
    days = fetch_days(kwargs['year'])

    return render(
        request,
        'main/ordo_block.html',
        {
            'year': kwargs['year'],
            'days': days,
        }
    )
