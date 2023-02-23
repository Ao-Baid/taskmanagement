from django.contrib import admin
from .models import Task, SubTask
#import the django admin log
from django.contrib.admin.models import LogEntry

# Register your models here.


#in the log entry table, allow the rows to show multiple fields
class TaskAdmin(admin.ModelAdmin):
    list_display = ('get_user_id','task_name', 'task_description', 'task_status', 'task_created_at', 'task_updated_at')

    @admin.display(description='User ID')
    def get_user_id(self, obj):
        return obj.user_id

admin.site.register(Task, TaskAdmin)

class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('get_task', 'subtask_name', 'subtask_description', 'subtask_status', 'subtask_created_at', 'subtask_updated_at', 'get_task')

    @admin.display(description='Task')
    def get_task(self, obj):
        return obj.task

    @admin.display(description='Task')
    def get_task(self, obj):
        return obj.task


admin.site.register(SubTask, SubTaskAdmin)

#in the log entry table, allow the rows to show multiple fields
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('action_time', 'user', 'content_type', 'object_repr', 'action_flag', 'change_message')

