"""apps/ordos/views.py """

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import OrdoForm
from .models import Ordo


@login_required
def ordos_list(request):
    """ List of ordos. """
    ordos = Ordo.objects.filter(owner=request.user)
    return render(
        request,
        'ordos/list.html',
        {
            'ordos': ordos,
        }
    )


@login_required
def ordo_create(request):
    """ Create an ordo. """
    if request.method == 'POST':
        form = OrdoForm(request.POST)
        if form.is_valid():
            ordo = form.save(commit=False)
            ordo.owner = request.user
            ordo.save()
            return HttpResponseRedirect(reverse('ordos:ordos_list'))

    else:
        form = OrdoForm()

    return render(
        request,
        'ordos/form.html',
        {
            'form': form,
        }
    )


@login_required
def ordo_details(request, **kwargs):
    """ Details of an ordo. """
    ordo = get_object_or_404(Ordo, pk=kwargs['pk'])
    return render(
        request,
        'ordos/details.html',
        {
            'ordo': ordo,
        }
    )


@login_required
def ordo_update(request, **kwargs):
    """ Update an ordo. """
    ordo = get_object_or_404(Ordo, pk=kwargs['pk'])

    if request.method == 'POST':
        form = OrdoForm(request.POST, instance=ordo)
        if form.is_valid():
            ordo = form.save(commit=False)
            ordo.owner = request.user
            ordo.save()
            return HttpResponseRedirect(reverse('ordos:ordos_list'))

    else:
        form = OrdoForm(instance=ordo)

    return render(
        request,
        'ordos/form.html',
        {
            'form': form,
            'ordo': ordo,
        }
    )


@login_required
def ordo_delete(request, **kwargs):
    """ Delete an ordo. """
    ordo = get_object_or_404(Ordo, pk=kwargs['pk'])
    if request.method == 'POST':
        form = OrdoForm(request.POST, instance=ordo)
        ordo.delete()
        return HttpResponseRedirect(reverse('ordos:ordos_list'))

    form = OrdoForm(instance=ordo)

    return render(
        request,
        'ordos/delete.html',
        {
            'form': form,
            'ordo': ordo,
        },
    )
