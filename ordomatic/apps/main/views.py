""" apps/main/views.py """

from datetime import date, timedelta

from django.shortcuts import render

from .dates import calculate_easter
from .models import DaySancto, DayTempo


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
    days = {}

    # Easter days:
    easter_days = DayTempo.objects.filter(baseline='easter').order_by('add')
    easter = calculate_easter(kwargs['year'])
    for index, easter_day in enumerate(easter_days):
        date = easter + timedelta(days=easter_day.add)
        days[date] = {}
        days[date]['tempo'] = easter_day
        sancto = DaySancto.objects.filter(
            month=date.month,
            day=date.day,
        )
        if sancto:
            days[date]['sancto'] = sancto[0]

    return render(
        request,
        'main/days_list.html',
        {
            'year': kwargs['year'],
            'days': days,
        },
    )
