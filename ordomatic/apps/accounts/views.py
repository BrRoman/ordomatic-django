""" apps/accounts/views.py """

from django.contrib.auth import views as auth_views
from django.shortcuts import render


def signup(request):
    """ Signup view. """
    return render(
        request,
        'accounts/signup.html',
    )


class Login(auth_views.LoginView):
    """ Login view. """
    template_name = 'accounts/login.html'


class Logout(auth_views.LogoutView):
    """ Logout view. """
    pass


def details(request):
    """ Details view. """
    return render(
        request,
        'accounts/details.html',
    )


def update(request):
    """ Update view. """
    return render(
        request,
        'accounts/update.html',
    )


def change_password(request):
    """ Change password view. """
    return render(
        request,
        'accounts/change_password.html',
    )


def change_password_done(request):
    """ Change password done view. """
    return render(
        request,
        'accounts/change_password_done.html',
    )


def reset_password(request):
    """ Reset password view. """
    return render(
        request,
        'accounts/reset_password.html',
    )


def reset_password_confirm(request):
    """ Reset password confirm view. """
    return render(
        request,
        'accounts/reset_password_confirm.html',
    )


def reset_password_complete(request):
    """ Reset password complete view. """
    return render(
        request,
        'accounts/reset_password_complete.html',
    )
