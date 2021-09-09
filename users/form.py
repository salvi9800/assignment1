from users.models import CustomUser
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['image', 'first_name', 'last_name', 'age', 'unique_id', 'email', 'password1', 'password2']