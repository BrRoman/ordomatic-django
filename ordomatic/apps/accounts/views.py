""" apps/accounts/views.py """

from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy


def signup(request):
    """ Signup view. """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('main:home'))

    else:
        form = UserCreationForm()

    return render(
        request,
        'accounts/signup.html',
        {
            'form': form,
        },
    )


class Login(auth_views.LoginView):
    """ Login view. """
    template_name = 'accounts/login.html'


class Logout(auth_views.LogoutView):
    """ Logout view. """


@login_required
def details(request):
    """ Details view. """
    return render(
        request,
        'accounts/details.html',
    )


@login_required
def update(request):
    """ Update view. """
    return render(
        request,
        'accounts/update.html',
    )


class ChangePassword(PasswordChangeView):
    """ Change password view. """
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('accounts:change_password_done')


def change_password_done(request):
    """ Change password done view. """
    return render(
        request,
        'accounts/change_password_done.html',
    )


class ResetPassword(PasswordResetView):
    """ Reset password view. """
    template_name = 'accounts/reset_password.html'
    email_template_name = 'accounts/reset_password_email.html'
    success_url = reverse_lazy('accounts:reset_password_done')


def reset_password_done(request):
    """ Reset password done view."""
    return render(
        request,
        'accounts/reset_password_done.html',
    )


class PasswordResetConfirm(PasswordResetConfirmView):
    """ Reset password confirm view. """
    template_name = 'accounts/reset_password_confirm.html'
    success_url = reverse_lazy('accounts:reset_password_complete')


def reset_password_complete(request):
    """ Reset password complete view. """
    return render(
        request,
        'accounts/reset_password_complete.html',
    )
