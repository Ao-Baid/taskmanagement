from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    #reverse for password reset done
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #reverse for password reset confirm
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #reverse for password reset complete
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('addtask/', views.addtask, name='addtask'),
    path('subtask_delete/<int:id>/', views.subtask_delete, name='subtask_delete'),
    path('subtask_update/<int:id>/', views.subtask_update, name='subtask_update'),
    path('task_delete/<int:id>/', views.task_delete, name='task_delete'),
]

