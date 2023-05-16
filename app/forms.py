# from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm

from app.models import User, Product


class UserCreateForm(UserCreationForm):
    image = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'image', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input'})
        self.fields['image'].widget.attrs.update({'class': 'form-input'})
        self.fields['password1'].widget.attrs.update({'class': 'form-input'})
        self.fields['password2'].widget.attrs.update({'class': 'form-input'})


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        def clean_price(self):
            price = self.cleaned_data.get('price')
            if price <= 0:
                raise ValidationError("price should be more than zero")
            return price

        def clean_quantity(self):
            quantity = self.cleaned_data.get('quantity')
            if quantity <= 0:
                raise ValidationError("price should be more than zero")
            return quantity
