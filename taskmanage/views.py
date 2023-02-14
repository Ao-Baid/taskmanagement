from django.shortcuts import render
from .models import Task, SubTask
from .forms import LoginForm, RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect

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
def task_view(request, task_name):
    tasks = Task.objects.filter(user_id=request.user)
    subtasks = SubTask.objects.filter(task__task_name=task_name)
    context = {'subtasks': subtasks , 'tasks': tasks, 'task_name': task_name} 
    return render(request, 'task.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def addtask(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        task = Task.objects.create(title=title, description=description, user_id=request.user)
        task.save()
        return redirect('task')
    return render(request, 'addtask.html')