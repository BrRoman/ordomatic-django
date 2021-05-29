""" apps/main/views.py """

from datetime import date
from django.contrib.auth.models import User

from django.shortcuts import render

from apps.calendars.models import Calendar
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
    calendars = Calendar.objects \
        .filter(
            owner=User.objects.filter(username='Universal')
            .get()
        )
    # TODO: add all the public calendars of other users.
    if str(request.user) != 'AnonymousUser':
        calendars_owner = Calendar.objects.filter(
            owner=request.user).order_by('name')
        calendars = calendars_owner.union(calendars)
    return render(
        request,
        'main/ordo.html',
        {
            'calendars': calendars,
            'year': date.today().year,
        }
    )


def get_ordo_as_html(request, **kwargs):
    """ Returns the ordo of the given year as html. """
    days = fetch_days(kwargs['calendar'], kwargs['year'])

    return render(
        request,
        'main/ordo_block.html',
        {
            'calendar': kwargs['calendar'],
            'year': kwargs['year'],
            'days': days,
        }
    )
