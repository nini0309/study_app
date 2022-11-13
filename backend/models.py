from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    STATUS = (
    ('Not started', 'Not started'),
    ('Completed', 'Completed'),
    ('On hold', 'On hold'),
    ('In progress', 'In progress')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    details = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS, null=True, default='In progress')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name}-{self.date}'
    
    class Meta:
        ordering = ['date']

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=100, null=True)
    important = models.CharField(max_length=500, null=True, blank=True)
    done = models.CharField(max_length=500, null=True, blank=True)
    left = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.subject}'
    
    class Meta:
        ordering = ['subject']

class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100,null=True)
    link = models.CharField(max_length=500,null=True)
