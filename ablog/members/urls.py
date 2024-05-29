from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import PasswordsChangeView, UserEditView, UserRegisterView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("edit_profile/", UserEditView.as_view(), name="edit_profile"),
    # path("password/", auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path(
        "password/",
        PasswordsChangeView.as_view(template_name="registration/change_password.html"),
    ),
    path("password_success", views.password_success, name="password_success"),
]
