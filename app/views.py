from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from app.forms import UserCreateForm
from django.views.generic import TemplateView
from app.models import Product


class ProductView(TemplateView):
    template_name = 'base.html'
    model = Product
    paginate_by = 3


class Registration(CreateView):
    template_name = 'registration.html'
    form_class = UserCreateForm
    success_url = '/'


class Login(LoginView):
    template_name = 'log-in.html'
    next_page = '/'


class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'
