"""apps/ordos/views.py """

from django.shortcuts import render


def ordos_list(request):
    """ List of ordos. """
    return render(
        request,
        'ordos/list.html',
    )


def ordo_create(request):
    """ Create an ordo. """
    return render(
        request,
        'ordos/form.html',
        {
            'action': 'create',
        },
    )


def ordo_details(request):
    """ Details of an ordo. """
    return render(
        request,
        'ordos/details.html',
    )


def ordo_update(request):
    """ Update an ordo. """
    return render(
        request,
        'ordos/form.html',
        {
            'action': 'update',
        },
    )


def ordo_delete(request):
    """ Delete an ordo. """
    return render(
        request,
        'ordos/delete.html',
    )
