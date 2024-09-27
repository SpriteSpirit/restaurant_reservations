from django.contrib.auth.views import LogoutView, PasswordResetDoneView
from django.urls import path

from users.apps import UsersConfig
from users.views import CustomLoginView, UserRegisterView, UserDetailView, ResetPasswordView, ResetPasswordCompleteView, \
    CustomPasswordResetConfirmView

app_name = UsersConfig.name

urlpatterns = [
    path("", CustomLoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("register/", UserRegisterView.as_view(), name='register'),
    path("profile/", UserDetailView.as_view(), name='profile'),

    # reset password
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<str:token>/',
         CustomPasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/', ResetPasswordCompleteView.as_view(), name='password_reset_complete'),
    path('password_reset-done/',
         PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
]
