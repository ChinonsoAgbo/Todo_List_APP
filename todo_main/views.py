from django.shortcuts import render

from todos.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=False) # filter tasks that are not completed
    context= {
        'tasks': tasks,
        
    }

    return render(request,'home-todo.html',context)