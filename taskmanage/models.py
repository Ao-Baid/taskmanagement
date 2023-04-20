from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse


task_status = [('To Do', 'To Do'), ('In Progress', 'In Progress'), ('Done', 'Done'), ('cancelled', 'Cancelled')]
# Create your models here.
class Task(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_staff': False})
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    task_status = models.CharField(max_length=100, choices=task_status, default="todo")
    task_created_at = models.DateTimeField(auto_now_add=True)
    task_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name
    
    class Meta:
        ordering = ['-task_created_at']
    
    def get_absolute_url(self):
        return reverse('taskmanage:index', kwargs={'pk': self.pk})
    
    def get_user_id(self):
        return self.user_id

class SubTask(models.Model):

    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    subtask_name = models.CharField(max_length=100)
    subtask_description = models.TextField()
    subtask_status = models.CharField(max_length=100, choices=task_status, default="To Do")
    subtask_created_at = models.DateTimeField(auto_now_add=True)
    subtask_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subtask_name
