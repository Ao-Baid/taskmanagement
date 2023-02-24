from django import forms
from .models import Task, SubTask
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404



#create a login form using crispy forms and form helper
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Invalid username or password')
            if not user.is_active:
                raise forms.ValidationError('User is not active')
        return super(LoginForm, self).clean()



#create a register form using crispy forms and form helper
class RegisterForm(forms.Form):

    #get the user model and allow for the save method to be used
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
    

    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
    
    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if username and email and password and password2:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError('Username already exists')
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Email already exists')
            if password != password2:
                raise forms.ValidationError('Passwords do not match')
            #save the user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
        return super(RegisterForm, self).clean()

#create a task form using crispy forms and form helper
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task_name', 'task_description')
        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-control'}),
            'task_description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
    
    #save the task to the database
    def save(self, user_id):
        task_name = self.cleaned_data.get('task_name')
        task_description = self.cleaned_data.get('task_description')
        task = Task(task_name=task_name, task_description=task_description, user_id=user_id)
        task.save()


class SubTaskForm(forms.ModelForm):


    subtask_name = forms.CharField(label='Subtask Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    subtask_description = forms.CharField(label='Subtask Description', max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
    

    class Meta:
        model = SubTask
        fields = ('subtask_name', 'subtask_description')
        widgets = {
            'subtask_name': forms.TextInput(attrs={'class': 'form-control'}),
            'subtask_description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(SubTaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
    
    #the task name is in the url after task/ therefore, the task name is passed to the form to allow the subtask to be saved to the correct task
    def save(self, commit=True, task_id=None):
        subtask = super().save(commit=False)
        if task_id is not None:
            task = Task.objects.get(pk=task_id)
            subtask.task = task
        if commit:
            subtask.save()
        return subtask
    

#create a updatesubtaskform that allows the user to update the subtasks name, description and status
class UpdateSubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ('subtask_name', 'subtask_description', 'subtask_status')
        widgets = {
            'subtask_name': forms.TextInput(attrs={'class': 'form-control'}),
            'subtask_description': forms.Textarea(attrs={'class': 'form-control'}),
            'subtask_status': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UpdateSubTaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Update Subtask',
                'subtask_name',
                'subtask_description',
                'subtask_status',
            ),
            Submit('submit', 'Submit', css_class='btn-success d-block mx-auto mt-3')
        )

    # save the updated subtask to the database
    def save(self, commit=True, **kwargs):
        subtask = super().save(commit=False)
        if commit:
            subtask.save()
        return subtask
