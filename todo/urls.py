from django.urls import path
from .views import *
urlpatterns = [
    path('task/', task, name='task'),
    path('task/add-task/', addTask, name='addTask'),
    path('task/view/<str:pk>/', viewTask, name='viewTask'),
    path('task/edit/<str:pk>/', editTask, name='editTask'),
    path('task/delete/<str:pk>/', deleteTask, name='deleteTask'),

]
