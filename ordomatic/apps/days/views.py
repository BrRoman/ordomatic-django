"""apps/days/views.py """

from datetime import date, timedelta

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .dates import calculate_easter
from .forms import DayTempoForm, DaySanctoForm
from .models import DaySancto, DayTempo


def fetch_days(year):
    """ Returns a list of the days of the given year. """
    days = {}  # {'date': {'tempo': object, 'sancto': object}, …}.

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


def home(request):
    """ Home page of days. """
    return render(
        request,
        'days/home.html',
        {},
    )


def days_list(request, **kwargs):
    """ List of days. """
    category = kwargs['category']
    tempo = DayTempo.objects.all().order_by('baseline', 'add')
    sancto = DaySancto.objects.all().order_by('month', 'day')

    if category == 'tempo':
        url = 'days/list_tempo.html'
        days = tempo
    else:
        url = 'days/list_sancto.html'
        days = sancto

    return render(
        request,
        url,
        {
            'category': category,
            'days': days,
        },
    )


def day_create(request, **kwargs):
    """ Create a day. """
    category = kwargs['category']

    if request.method == 'POST':
        form = DayTempoForm(request.POST) \
            if category == 'tempo' else DaySanctoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse(
                    'days:days_list',
                    kwargs={
                        'category': category,
                    }
                )
            )

    else:
        form = DayTempoForm() if category == 'tempo' else DaySanctoForm()

    return render(
        request,
        'days/form.html',
        {
            'form': form,
            'category': category,
        }
    )


def day_details(request, **kwargs):
    """ Details of a day. """
    category = kwargs['category']

    if category == 'tempo':
        day = DayTempo.objects.get(pk=kwargs['pk'])
    else:
        day = DaySancto.objects.get(pk=kwargs['pk'])

    return render(
        request,
        'days/details.html',
        {
            'day': day,
            'category': category,
        },
    )


def day_update(request, **kwargs):
    """ Update a day. """
    category = kwargs['category']
    day = DayTempo.objects.get(pk=kwargs['pk']) \
        if category == 'tempo' else DaySancto.objects.get(pk=kwargs['pk'])

    if request.method == 'POST':
        form = DayTempoForm(request.POST, instance=day) \
            if category == 'tempo' else DaySanctoForm(request.POST, instance=day)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse(
                    'days:day_details',
                    kwargs={
                        'category': category,
                        'pk': day.pk,
                    },
                )
            )

    else:
        form = DayTempoForm(instance=day) \
            if category == 'tempo' else DaySanctoForm(instance=day)

    return render(
        request,
        'days/form.html',
        {
            'form': form,
            'day': day,
            'category': kwargs['category'],
        },
    )


def day_delete(request, **kwargs):
    """ Delete a day. """
    category = kwargs['category']
    day = DayTempo.objects.get(pk=kwargs['pk']) \
        if category == 'tempo' else DaySancto.objects.get(pk=kwargs['pk'])

    if request.method == 'POST':
        day.delete()
        return HttpResponseRedirect(
            reverse(
                'days:days_list',
                kwargs={
                    'category': category,
                },
            ),
        )

    else:
        return render(
            request,
            'days/delete.html',
            {
                'category': category,
                'day': day,
            },
        )
