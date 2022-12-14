from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget

from .models import Task, Course, Link

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        

class AddTask(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'details', 'date', 'status']
        widgets = {
                'date': SelectDateWidget(),
        }

class AddCourse(ModelForm):
    class Meta:
        model = Course
        fields = ['subject', 'important', 'done', 'left']

class AddLink(ModelForm):
    class Meta:
        model = Link
        fields = ['name', 'link']