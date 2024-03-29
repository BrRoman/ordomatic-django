"""apps/days/views.py """

from datetime import date, timedelta

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from apps.calendars.models import Calendar
from .dates import calculate_easter
from .forms import DayTempoForm, DaySanctoForm
from .models import DaySancto, DayTempo


def fetch_days(calendar, year):
    """ Returns a list of the days of the given year. """
    calendar = Calendar.objects.get(pk=calendar)
    days = {}  # {'date': {'tempo': object, 'sancto': object}, …}.

    # Start time (Advent):
    start_days = DayTempo.objects \
        .filter(
            calendar=calendar
        ) \
        .filter(
            baseline='start'
        ) \
        .order_by(
            'add'
        )
    christmas = date(year - 1, 12, 25)
    christmas_weekday = christmas.weekday()
    start = christmas - timedelta(days=22 + christmas_weekday)
    for index, christmas_day in enumerate(start_days):
        key = start + timedelta(days=christmas_day.add)
        days[key] = {}
        days[key]['tempo'] = christmas_day
        sancto = DaySancto.objects \
            .filter(
                calendar=calendar
            ) \
            .filter(
                month=key.month,
                day=key.day,
            )
        if sancto:
            days[key]['sancto'] = sancto[0]

    # Christmas time:
    christmas_days = DayTempo.objects \
        .filter(
            calendar=calendar
        )\
        .filter(
            baseline='christmas'
        )\
        .order_by(
            'add'
        )
    for index, christmas_day in enumerate(christmas_days):
        key = christmas + timedelta(days=christmas_day.add)
        days[key] = {}
        days[key]['tempo'] = christmas_day
        sancto = DaySancto.objects \
            .filter(
                calendar=calendar
            ) \
            .filter(
                month=key.month,
                day=key.day,
            )
        if sancto:
            days[key]['sancto'] = sancto[0]

    # Easter time:
    easter_days = DayTempo.objects \
        .filter(
            calendar=calendar) \
        .filter(
            baseline='easter'
        ) \
        .order_by(
            'add'
        )
    easter = calculate_easter(year)
    for index, easter_day in enumerate(easter_days):
        key = easter + timedelta(days=easter_day.add)
        days[key] = {}
        days[key]['tempo'] = easter_day
        sancto = DaySancto.objects \
            .filter(
                calendar=calendar
            ) \
            .filter(
                month=key.month,
                day=key.day,
            )
        if sancto:
            days[key]['sancto'] = sancto[0]

    return days


@login_required
def home(request, **kwargs):
    """ Home page of the days of a given calendar. """
    calendar = Calendar.objects.get(pk=kwargs['calendar'])
    if calendar.owner != request.user:
        return HttpResponseForbidden('403 Forbidden')

    return render(
        request,
        'days/home.html',
        {
            'calendar': calendar,
        },
    )


@login_required
def days_list(request, **kwargs):
    """ List of days. """
    category = kwargs['category']
    calendar = Calendar.objects.get(pk=kwargs['calendar'])
    tempo = DayTempo.objects.filter(
        calendar=calendar).order_by('baseline', 'add')
    sancto = DaySancto.objects.filter(
        calendar=calendar).order_by('month', 'day')

    if category == 'tempo':
        url = 'days/list_tempo.html'
        days = tempo
    else:
        url = 'days/list_sancto.html'
        days = sancto

    if calendar.owner != request.user:
        return HttpResponseForbidden('403 Forbidden')

    return render(
        request,
        url,
        {
            'category': category,
            'calendar': calendar,
            'days': days,
        },
    )


@login_required
def day_create(request, **kwargs):
    """ Create a day. """
    category = kwargs['category']
    calendar = Calendar.objects.get(pk=kwargs['calendar'])

    if request.method == 'POST':
        form = DayTempoForm(request.POST) \
            if category == 'tempo' else DaySanctoForm(request.POST)
        if form.is_valid():
            day = form.save(commit=False)
            day.calendar = calendar
            day.save()
            return HttpResponseRedirect(
                reverse(
                    'days:days_list',
                    kwargs={
                        'category': category,
                        'calendar': kwargs['calendar'],
                    }
                )
            )

    else:
        form = DayTempoForm() if category == 'tempo' else DaySanctoForm()

    if calendar.owner != request.user:
        return HttpResponseForbidden('403 Forbidden')

    return render(
        request,
        'days/form.html',
        {
            'form': form,
            'category': category,
            'calendar': calendar,
        }
    )


@login_required
def day_details(request, **kwargs):
    """ Details of a day. """
    category = kwargs['category']
    calendar = Calendar.objects.get(pk=kwargs['calendar'])

    if category == 'tempo':
        day = get_object_or_404(DayTempo, pk=kwargs['pk'])
    else:
        day = get_object_or_404(DaySancto, pk=kwargs['pk'])

    if calendar.owner != request.user:
        return HttpResponseForbidden('403 Forbidden')

    return render(
        request,
        'days/details.html',
        {
            'category': category,
            'calendar': calendar,
            'day': day,
        },
    )


@login_required
def day_update(request, **kwargs):
    """ Update a day. """
    category = kwargs['category']

    if category == 'tempo':
        day = get_object_or_404(DayTempo, pk=kwargs['pk'])
    else:
        day = get_object_or_404(DaySancto, pk=kwargs['pk'])

    calendar = Calendar.objects.get(pk=kwargs['calendar'])

    if request.method == 'POST':
        form = DayTempoForm(request.POST, instance=day) \
            if category == 'tempo' else DaySanctoForm(request.POST, instance=day)
        if form.is_valid():
            day = form.save(commit=False)
            day.calendar = calendar
            day.save()
            return HttpResponseRedirect(
                reverse(
                    'days:day_details',
                    kwargs={
                        'category': category,
                        'calendar': kwargs['calendar'],
                        'pk': day.pk,
                    },
                )
            )

    else:
        form = DayTempoForm(instance=day) \
            if category == 'tempo' else DaySanctoForm(instance=day)

    if calendar.owner != request.user:
        return HttpResponseForbidden('403 Forbidden')

    return render(
        request,
        'days/form.html',
        {
            'form': form,
            'category': kwargs['category'],
            'calendar': calendar,
            'day': day,
        },
    )


@login_required
def day_delete(request, **kwargs):
    """ Delete a day. """
    category = kwargs['category']

    if category == 'tempo':
        day = get_object_or_404(DayTempo, pk=kwargs['pk'])
    else:
        day = get_object_or_404(DaySancto, pk=kwargs['pk'])

    calendar = Calendar.objects.get(pk=kwargs['calendar'])

    if calendar.owner != request.user:
        return HttpResponseForbidden('403 Forbidden')

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

    return render(
        request,
        'days/delete.html',
        {
            'category': category,
            'calendar': calendar,
            'day': day,
        },
    )
