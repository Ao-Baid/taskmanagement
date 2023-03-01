from django.contrib import admin
from .models import Task, SubTask
#import the django admin log
from django.contrib.admin.models import LogEntry

# Register your models here.


#in the log entry table, allow the rows to show multiple fields




#in the log entry table, allow the rows to show multiple fields
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('action_time', 'user', 'content_type', 'object_repr', 'action_flag', 'change_message')

admin.site.register(LogEntry, LogEntryAdmin)