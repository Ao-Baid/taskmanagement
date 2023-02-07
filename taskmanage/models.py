from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
class Task(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    task_status = models.CharField(max_length=100)
    task_created_at = models.DateTimeField(auto_now_add=True)
    task_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name

class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    subtask_name = models.CharField(max_length=100)
    subtask_description = models.TextField()
    subtask_status = models.CharField(max_length=100)
    subtask_created_at = models.DateTimeField(auto_now_add=True)
    subtask_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subtask_name
