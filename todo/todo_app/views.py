from django.shortcuts import render,redirect
from .models import *
# Create your views here.
from .forms import TaskForm

def index(request):
    tasks = Tasks.objects.all().order_by('-created_on')

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid:
            form.save()
        return redirect('/todo_app/')

    context = {
        'tasks': tasks,
        'form' : form
    }
    return render(request, 'index.html', context)

def delete(request, pk):
    item = Tasks.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('/todo_app/')
    context = {
        'item' : item
    }
    return render(request, 'delete.html', context)


def update(request, pk):
    task = Tasks.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)# if instance=task then it wud create a new task
        if form.is_valid:
            form.save()
        return redirect('/todo_app/')

    context = {
        'form': form
    }
    return render(request, 'update.html', context)