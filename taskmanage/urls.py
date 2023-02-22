from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('addtask/', views.addtask, name='addtask'),
    path('subtask_delete/<int:id>/', views.subtask_delete, name='subtask_delete'),
    path('subtask_update/<int:id>/', views.subtask_update, name='subtask_update'),
]

