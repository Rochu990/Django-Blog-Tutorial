from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import SingUpForm


class UserRegisterView(generic.CreateView):
    form_class = SingUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")
