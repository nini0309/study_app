# Generated by Django 4.1 on 2022-09-17 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_task_options_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='details',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Not started', 'Not started'), ('Completed', 'Completed'), ('On hold', 'On hold'), ('In progress', 'In progress')], default='In progress', max_length=50, null=True),
        ),
    ]
