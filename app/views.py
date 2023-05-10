from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
# from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView

from app.forms import UserCreateForm, ProductForm
from app.models import Product


class ProductListView(ListView):
    template_name = 'base.html'
    queryset = Product.objects.all()
    paginate_by = 10


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'
    form_class = ProductForm
    template_name = 'create_product.html'
    success_url = '/'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'
    slug_url_kwarg = 'slug'


class Registration(CreateView):
    template_name = 'registration.html'
    form_class = UserCreateForm
    success_url = '/'


class Login(LoginView):
    template_name = 'log-in.html'
    next_page = '/'


class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'

# class ProductCreateView(CreateView):
#     form_class = ProductForm
#     template_name = 'create_product.html'
#     success_url = reverse('base')
#     model = Product
#
#
# class ProductUpdateView(UpdateView):
#     model = Product
#     form_class = ProductForm
#     success_url = reverse('base')
#     template_name = 'update_product/html'
#
