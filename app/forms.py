from django.contrib.auth.forms import UserCreationForm
from django.forms import forms

from app.models import User


class UserCreateForm(UserCreationForm):
    image = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'wallet', 'image']
