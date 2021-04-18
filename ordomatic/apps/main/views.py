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


def get_list_of_days(year):
    """ Returns a list of the days of the given year. """
    days = {}  # 'date': {'tempo': object, 'sancto': object}

    # Christmas time:
    christmas_days = DayTempo.objects.filter(baseline='start').order_by('add')
    christmas = date(year - 1, 12, 25)
    christmas_weekday = christmas.weekday()
    start = christmas - timedelta(days=22 + christmas_weekday)
    for index, christmas_day in enumerate(christmas_days):
        key = start + timedelta(days=christmas_day.add)
        days[key] = {}
        days[key]['tempo'] = christmas_day
        sancto = DaySancto.objects.filter(
            month=key.month,
            day=key.day,
        )
        if sancto:
            days[key]['sancto'] = sancto[0]

    # Easter time:
    easter_days = DayTempo.objects.filter(baseline='easter').order_by('add')
    easter = calculate_easter(year)
    for index, easter_day in enumerate(easter_days):
        key = easter + timedelta(days=easter_day.add)
        days[key] = {}
        days[key]['tempo'] = easter_day
        sancto = DaySancto.objects.filter(
            month=key.month,
            day=key.day,
        )
        if sancto:
            days[key]['sancto'] = sancto[0]

    return days


def get_list_of_days_as_html(request, **kwargs):
    """ Returns a list of the days of the given year as html. """
    days = get_list_of_days(kwargs['year'])

    return render(
        request,
        'main/days_list.html',
        {
            'days': days,
        },
    )


def get_ordo_output_as_html(request, **kwargs):
    """ Returns the ordo of the given year as html. """
    days = get_list_of_days(kwargs['year'])

    return render(
        request,
        'main/ordo_output.html',
        {
            'year': kwargs['year'],
            'days': days,
        }
    )
