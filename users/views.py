from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket
from users.models import User
from common.views import CommonMixin


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm


class UserRegistrationView(CommonMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вітаємо! Ви зареєстровані'
    title = 'DESIREX Store - Реєстрація'


class UserProfileView(CommonMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'DESIREX Store -  Особистий кабінет'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))
