from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registerPage, name='register'),
    #('task/<int:task_id>/', views.task, name='task'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('addtask/', views.addtask, name='addtask'),
]

