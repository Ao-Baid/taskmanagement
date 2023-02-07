from django.shortcuts import render
from .models import Task, SubTask
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='register/')
def index(request):
    #store all tasks in a variable
    tasks = Task.objects.all()
    #store all subtasks in a variable
    subtasks = SubTask.objects.all()
    #store all tasks and subtasks in a dictionary
    context = {'tasks': tasks, 'subtasks': subtasks}
    #render the index.html template with the context
    return render(request, 'index.html', context)

@login_required(login_url='register/')
def registerPage(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)