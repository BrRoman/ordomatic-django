""" apps/main/views.py """

from datetime import date, timedelta

from django.shortcuts import render

from .dates import calculate_easter


def home(request):
    """ Home page of Ordomatic. """
    return render(
        request,
        'main/home.html',
        {
            'current_year': date.today().year,
        },
    )


def ordo(request, **kwargs):
    """ Ordo page of Ordomatic. """
    return render(
        request,
        'main/ordo.html',
        {
            'year': kwargs['year'],
        }
    )


def get_list_of_days_as_html(request, **kwargs):
    """ Returns a list of the days of the given year as html. """
    easter = calculate_easter(kwargs['year'])
    days = []
    for i in range(50):
        days.append(easter + timedelta(i))
    return render(
        request,
        'main/days_list.html',
        {
            'year': kwargs['year'],
            'days': days,
        },
    )
