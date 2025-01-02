from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    pass


class CustomLogoutView(LogoutView):
    pass


class CustomPasswordChangeView(PasswordChangeView):
    pass


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    pass


class CustomPasswordResetView(PasswordResetView):
    pass


class CustomPasswordResetDoneView(PasswordResetDoneView):
    pass


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    pass


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    pass
