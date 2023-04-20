from django.conf import settings
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path, reverse_lazy

from users import views as local_views

app_name = 'users'

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(
            template_name='users/login.html',
        ),
        name='login',
        ),
    path(
        'logout/',
        LogoutView.as_view(
            template_name='users/logout.html',
        ),
        name='logout',
        ),
    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='users/password_change.html',
            success_url=reverse_lazy('users:password_change_done'),
        ),
        name='password_change',
        ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html',
        ),
        name='password_change_done',
        ),
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='users/password_reset.html',
            success_url=reverse_lazy('users:password_reset_done'),
            email_template_name='users/password_reset_email.html',
            from_email=settings.ADMIN_EMAIL,
        ),
        name='password_reset',
        ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html',
        ),
        name='password_reset_done',
        ),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html',
            success_url=reverse_lazy('users:password_reset_complete'),
        ),
        name='password_reset_confirm',
        ),
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html',
        ),
        name='password_reset_complete',
        ),
    path(
        'sign_up/',
        local_views.SignUpView.as_view(),
        name='sign_up',
        ),
    path(
        'profile/',
        local_views.ProfileView.as_view(),
        name='profile',
    ),
]
