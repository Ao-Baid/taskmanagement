# Generated by Django 4.1.5 on 2023-02-09 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskmanage', '0004_alter_task_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='subtask_status',
            field=models.CharField(choices=[('todo', 'To Do'), ('inprogress', 'In Progress'), ('done', 'Done'), ('cancelled', 'Cancelled')], default='todo', max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(choices=[('todo', 'To Do'), ('inprogress', 'In Progress'), ('done', 'Done'), ('cancelled', 'Cancelled')], default='todo', max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='user_id',
            field=models.ForeignKey(limit_choices_to={'is_staff': False}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
