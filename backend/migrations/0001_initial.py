# Generated by Django 4.1 on 2022-08-31 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('details', models.CharField(max_length=500, null=True)),
                ('date', models.DateField(max_length=100, null=True)),
                ('status', models.CharField(choices=[('Not started', 'Not started'), ('Completed', 'Completed'), ('On hold', 'On hold'), ('In progress', 'In progress')], max_length=50, null=True)),
            ],
        ),
    ]