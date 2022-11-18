from django.contrib import admin
from .models import Task, Course, Link, Event, Quote
admin.site.site_header = 'Keep Up Dashboard'

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'details', 'date', 'status')
    list_filter = ['date']

class CourseAdmin(admin.ModelAdmin):
    list_display = ('subject', 'important', 'done', 'left')
    list_filter = ['subject']

class LinkAdmin(admin.ModelAdmin):
    list_display = ('link','name')
    list_filter = ['name']

class EventAdmin(admin.ModelAdmin):
    list_display = ('date','name')
    list_filter = ['date']

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('quote','author')
    list_filter = ['quote']

# Register your models here.
admin.site.register(Task, TaskAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Quote, QuoteAdmin)
