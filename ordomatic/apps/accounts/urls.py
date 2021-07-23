""" apps/accounts/urls.py """

from django.urls import path

from . import views as accounts_views

app_name = 'accounts'
urlpatterns = [
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', accounts_views.Login.as_view(), name='login'),
    path('logout/', accounts_views.Logout.as_view(), name='logout'),
    path('details/', accounts_views.details, name='details'),
    path('update/', accounts_views.update, name='update'),
    path('change_password/', accounts_views.ChangePassword.as_view(),
         name='change_password'),
    path('change_password/done/', accounts_views.change_password_done,
         name='change_password_done'),
    path('reset_password/', accounts_views.ResetPassword.as_view(),
         name='reset_password'),
    path('reset_password_done/', accounts_views.reset_password_done,
         name='reset_password_done'),
    path('reset/<uidb64>/<token>/', accounts_views.PasswordResetConfirm.as_view(),
         name='reset_password_confirm'),
    path('reset/done/', accounts_views.reset_password_complete,
         name='reset_password_complete'),
]
