# Generated by Django 4.1.5 on 2023-02-07 01:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('task_description', models.TextField()),
                ('task_status', models.CharField(max_length=100)),
                ('task_created_at', models.DateTimeField(auto_now_add=True)),
                ('task_updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtask_name', models.CharField(max_length=100)),
                ('subtask_description', models.TextField()),
                ('subtask_status', models.CharField(max_length=100)),
                ('subtask_created_at', models.DateTimeField(auto_now_add=True)),
                ('subtask_updated_at', models.DateTimeField(auto_now=True)),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taskmanage.task')),
            ],
        ),
    ]
