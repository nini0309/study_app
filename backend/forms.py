from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Task

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class AddTask(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'details', 'date', 'status']