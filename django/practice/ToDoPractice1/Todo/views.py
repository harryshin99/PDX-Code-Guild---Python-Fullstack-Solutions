from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import ToDoItem, Priority

# Create your views here.
def index(request):
    todos = ToDoItem.objects.filter(completed_date__isnull=True)
    completed_todos = ToDoItem.objects.filter(completed_date__isnull=False)
    priorities = Priority.objects.all()
    context = {
        'todos': todos,
        'completed_todos': completed_todos,
        'priorities': priorities
    }

    return render(request, 'todos/index.html', context)

def save_todos(request):
    form = request.POST
    description = form['description']
    priority_text = form['priority']
    priority = Priority.objects.get(name=priority_text)
    todo = ToDoItem()
    todo.description = description
    todo.priority = priority
    todo.save()
    return HttpResponseRedirect(reverse('index'))


def complete(request, todo_id):
    todo = ToDoItem.objects.get(id=todo_id)
    todo.completed_date = timezone.now()
    todo.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, todo_id):
    todo = ToDoItem.objects.get(id=todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))