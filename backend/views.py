from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import AddTask

# Create your views here.


@login_required(login_url='Log in')
def homepage(request):
    return render(request, 'homepage.html')


@login_required(login_url='Log in')
def tasks(request):
    task_list = Task.objects.filter(user=request.user)
    context = {
        'task_list': task_list
    }
    return render(request, 'tasks.html', context)


@login_required(login_url='Log in')
def addtasks(request):
    form = AddTask()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = AddTask(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('Tasks')
    return render(request, 'tasks/addtasks.html', context)


@login_required(login_url='Log in')
def edittasks(request, pk):
    task = Task.objects.get(id=pk)
    form = AddTask(instance=task)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = AddTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('Tasks')
    return render(request, 'tasks/addtasks.html', context)

@login_required(login_url='Log in')
def deletetasks(request, pk):
    task = Task.objects.get(id=pk)
    context = {
        'item': task
    }
    if request.method == 'POST':
        task.delete()
        return redirect('Tasks')
    return render(request, 'tasks/deletetask.html', context)


@login_required(login_url='Log in')
def calendar(request):
    return render(request, 'calendar.html')


@login_required(login_url='Log in')
def courses(request):
    return render(request, 'courses.html')


@login_required(login_url='Log in')
def links(request):
    return render(request, 'links.html')


@login_required(login_url='Log in')
def schedule(request):
    return render(request, 'schedule.html')


@login_required(login_url='Log in')
def study_mode(request):
    return render(request, 'studymode.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('Homepage')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created')
                return redirect('Log in')
        else:
            form = CreateUserForm()
        context = {
            'form': form
        }
    return render(request, 'user/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('Homepage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('Homepage')
            else:
                messages.info(request, 'Username or Password Incorrect')
    return render(request, 'user/login.html')


def logout_page(request):
    logout(request)
    return redirect('Log in')
