from random import randint

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from userextend.forms import UserForm, ChangePasswordForm


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            new_user.last_name = new_user.last_name.title()
            new_user.email = new_user.username
            new_user.save()
            return redirect('login')
        return super().form_valid(form)


class ChangePasswordView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    model = User
    form_class = ChangePasswordForm
    success_url = reverse_lazy('home_page')
