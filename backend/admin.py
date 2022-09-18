from django.contrib import admin
from .models import Task
admin.site.site_header = 'Keep Up Dashboard'

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'details', 'date', 'status')
    list_filter = ['date']

# Register your models here.
admin.site.register(Task, TaskAdmin)
