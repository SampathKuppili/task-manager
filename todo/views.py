from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

# Task listing


def task(request):
    lists = Task.objects.all()
    context = {'lists': lists}
    template = 'todo/todo_list.html'
    return render(request, template, context)

# Add task


def addTask(request):
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your task added successfully')
            return redirect('task')
        else:
            context = {'form': form}
            template = 'todo/add_task.html'
            return render(request, template, context)
    else:
        form = taskForm()
        context = {'form': form}
        template = 'todo/add_task.html'
        return render(request, template, context)


def viewTask(request, pk):
    views = Task.objects.get(task_id=pk)
    context = {'views': views}
    template = 'todo/view_task.html'
    return render(request, template, context)


def editTask(request, pk):
    data = Task.objects.get(task_id=pk)
    if request.method == 'POST':
        form = taskForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('task')
        else:
            context = {'form': form}
            template = 'todo/add_task.html'
            return render(request, template, context)
    else:
        form = taskForm(instance=data)
        context = {'form': form}
        template = 'todo/add_task.html'
        return render(request, template, context)


def deleteTask(request, pk):
    task = Task.objects.get(task_id=pk)
    task.delete()
    messages.success(request, 'your task deleted successfully')
    return redirect('task')
