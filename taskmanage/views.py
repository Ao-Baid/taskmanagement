from django.shortcuts import render
from .models import Task, SubTask
from .forms import LoginForm, RegisterForm, TaskForm, SubTaskForm, UpdateSubTaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404

@login_required(login_url='login')
def index(request):
    tasks = Task.objects.filter(user_id=request.user)
    context = {'tasks': tasks}
    return render(request, 'index.html', context)

def registerPage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            return redirect('login')
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)

#task_view takes a string argument task_name from the url and uses it to filter the subtasks
def task_view(request, task_id):
    tasks = Task.objects.filter(user_id=request.user)
    task_name = Task.objects.filter(id=task_id).values_list('task_name', flat=True).get()
    task = get_object_or_404(Task, pk=task_id)
    subtasks = SubTask.objects.filter(task=task)
    form = SubTaskForm()
    if request.method == 'POST':
        form = SubTaskForm(request.POST)
        if form.is_valid():
            form.save(commit=True, task_id=task.id)
            return redirect('task', task_id=task_id)
    


    #allow for pagination of subtasks
    paginator = Paginator(subtasks, 10)
    page = request.GET.get('page')
    pages = paginator.get_page(page)
    try:
        subtasks = paginator.page(page)
    except PageNotAnInteger:
        subtasks = paginator.page(1)
    except EmptyPage:
        subtasks = paginator.page(paginator.num_pages)

    context = {'subtasks': subtasks, 'tasks': tasks, 'task': task, 'form': form, 'page': page, 'pages': pages, 'task_name': task_name}
    return render(request, 'task.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def addtask(request):
    form = TaskForm()
    tasks = Task.objects.filter(user_id=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save(user_id=request.user)
            return redirect('index')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'addtask.html', context)

def subtask_delete(request, id):
    subtask = SubTask.objects.get(id=id)
    task_id = get_object_or_404(Task, pk=subtask.task.id)
    subtask.delete()
    return redirect('task', task_id=task_id.id)

def subtask_update(request, id):
    tasks = Task.objects.filter(user_id=request.user)
    subtask = SubTask.objects.get(id=id)
    task_id = get_object_or_404(Task, pk=subtask.task.id)
    task_name = subtask.task.task_name
    form = UpdateSubTaskForm(instance=subtask)
    #handle the status update and post
    if request.method == 'POST':
        form = UpdateSubTaskForm(request.POST, instance=subtask)
        if form.is_valid():
            form.save(commit=True)
            return redirect('task', task_id=task_id.id)
    context = {'form': form, 'task_name': task_name, 'tasks': tasks}
    return render(request, 'subtask_update.html', context)