from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import calendar
import random

from calendar import HTMLCalendar
from datetime import datetime
from datetime import timedelta 

from .models import Task, Course, Link, Quote
from .forms import AddTask, AddCourse, AddLink

# Create your views here.


@login_required(login_url='Log in')
def homepage(request):
    items = list(Quote.objects.all())
    random_item = random.choice(items)
    context = {
        'quote': random_item
    }
    return render(request, 'homepage.html', context)


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
def calendar_view(request, year, month):

    cal = HTMLCalendar().formatmonth(year, month)
    current = datetime(year, month, 1)
    next_month = current + timedelta(days = 31)
    prev_month = current - timedelta(days = 31)
    n_m = next_month.month
    n_y = next_month.year
    p_m = prev_month.month
    p_y = prev_month.year
    context = {
        'calendar' : cal,
        'next_month' : n_m,
        'next_year' : n_y,
        'prev_month' : p_m,
        'prev_year' : p_y
    }
    return render(request, 'calendar.html', context)

@login_required(login_url='Log in')
def calendar_today(request):
    now = datetime.now()
    next_month = now + timedelta(days = 30)
    prev_month = now - timedelta(days = 30)
    n_m = next_month.month
    n_y = next_month.year
    p_m = prev_month.month
    p_y = prev_month.year
    cal = HTMLCalendar().formatmonth(now.year, now.month)
    context = {
        'calendar' : cal,
        'next_month' : n_m,
        'next_year' : n_y,
        'prev_month' : p_m,
        'prev_year' : p_y
    }
    return render(request, 'calendar.html', context)


@login_required(login_url='Log in')
def courses(request):
    course_list = Course.objects.filter(user=request.user)
    context = {
        'course_list': course_list
    }
    return render(request, 'courses.html', context)

@login_required(login_url='Log in')
def addcourses(request):
    form = AddCourse()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = AddCourse(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('Courses')
    return render(request, 'courses/addcourse.html', context)

@login_required(login_url='Log in')
def editcourses(request, pk):
    course = Course.objects.get(id=pk)
    form = AddCourse(instance=course)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = AddCourse(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('Courses')
    return render(request, 'courses/addcourse.html', context)

@login_required(login_url='Log in')
def deletecourses(request, pk):
    course = Course.objects.get(id=pk)
    context = {
        'item': course
    }
    if request.method == 'POST':
        course.delete()
        return redirect('Courses')
    return render(request, 'courses/deletecourse.html', context)


@login_required(login_url='Log in')
def links(request):
    link_list = Link.objects.filter(user=request.user)
    context = {
        'link_list': link_list
    }
    return render(request, 'links.html', context)

@login_required(login_url='Log in')
def addlink(request):
    form = AddLink()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = AddLink(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('Links')
    return render(request, 'links/addlink.html', context)

@login_required(login_url='Log in')
def editlink(request, pk):
    link = Link.objects.get(id=pk)
    form = AddLink(instance=link)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = AddLink(request.POST, instance=link)
        if form.is_valid():
            form.save()
            return redirect('Links')
    return render(request, 'links/addlink.html', context)


@login_required(login_url='Log in')
def deletelink(request, pk):
    link = Link.objects.get(id=pk)
    context = {
        'item': link
    }
    if request.method == 'POST':
        link.delete()
        return redirect('Links')
    return render(request, 'links/deletelink.html', context)

# @login_required(login_url='Log in')
# def schedule(request):
#     return render(request, 'schedule.html')


# @login_required(login_url='Log in')
# def study_mode(request):
#     return render(request, 'studymode.html')


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
