from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = "Homepage"),

    path('tasks/', views.tasks, name = "Tasks"),
    path('tasks/add/', views.addtasks, name = "Add Tasks"),
    path('tasks/edit/<str:pk>/', views.edittasks, name = "Edit Tasks"),
    path('tasks/delete/<str:pk>/', views.deletetasks, name = "Delete Tasks"),

    path('calendar/', views.calendar, name = "Calendar"),

    path('courses/', views.courses, name = "Courses"),
    path('courses/add', views.addcourses, name = "Add Course"),
    path('courses/edit/<str:pk>', views.editcourses, name = "Edit Course"),
    path('courses/delete/<str:pk>', views.deletecourses, name = "Delete Course"),


    path('links/', views.links, name = "Links"),
    path('schedule/', views.schedule, name = "Schedule"),
    path('studymode/', views.study_mode, name = "Study Mode"),
    path('register/', views.register, name = "Register"),
    path('login/', views.login_page, name = "Log in"),
    path('logout/', views.logout_page, name = "Log out")
]