"""apps/calendars/views.py """

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import CalendarForm
from .models import Calendar


@login_required
def calendars_list(request):
    """ List of calendars. """
    calendars = Calendar.objects.filter(owner=request.user)
    return render(
        request,
        'calendars/list.html',
        {
            'calendars': calendars,
        }
    )


@login_required
def calendar_create(request):
    """ Create a calendar. """
    if request.method == 'POST':
        form = CalendarForm(request.POST)
        if form.is_valid():
            calendar = form.save(commit=False)
            calendar.owner = request.user
            calendar.save()
            return HttpResponseRedirect(reverse('calendars:calendars_list'))

    else:
        form = CalendarForm()

    return render(
        request,
        'calendars/form.html',
        {
            'form': form,
        }
    )


@login_required
def calendar_details(request, **kwargs):
    """ Details of a calendar. """
    calendar = get_object_or_404(Calendar, pk=kwargs['pk'])
    return render(
        request,
        'calendars/details.html',
        {
            'calendar': calendar,
        }
    )


@login_required
def calendar_update(request, **kwargs):
    """ Update a calendar. """
    calendar = get_object_or_404(Calendar, pk=kwargs['pk'])

    if request.method == 'POST':
        form = CalendarForm(request.POST, instance=calendar)
        if form.is_valid():
            calendar = form.save(commit=False)
            calendar.owner = request.user
            calendar.save()
            return HttpResponseRedirect(reverse('calendars:calendars_list'))

    else:
        form = CalendarForm(instance=calendar)

    return render(
        request,
        'calendars/form.html',
        {
            'form': form,
            'calendar': calendar,
        }
    )


@login_required
def calendar_delete(request, **kwargs):
    """ Delete a calendar. """
    calendar = get_object_or_404(Calendar, pk=kwargs['pk'])
    if request.method == 'POST':
        form = CalendarForm(request.POST, instance=calendar)
        calendar.delete()
        return HttpResponseRedirect(reverse('calendars:calendars_list'))

    form = CalendarForm(instance=calendar)

    return render(
        request,
        'calendars/delete.html',
        {
            'form': form,
            'calendar': calendar,
        },
    )
