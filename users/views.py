from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.models import User

from users.forms import RegistrationForm, UserLoginForm


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
    form_class = UserLoginForm


class SignupView(CreateView):
    model = User
    form_class = RegistrationForm
    success_url = '/login/'
    template_name = 'register.html'
