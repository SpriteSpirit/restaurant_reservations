from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import CustomLoginView, UserRegisterView, UserDetailView

app_name = UsersConfig.name

urlpatterns = [
    path("", CustomLoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("register/", UserRegisterView.as_view(), name='register'),
    path("profile/", UserDetailView.as_view(), name='profile'),
]
