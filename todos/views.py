from django.http import HttpResponse
from django.shortcuts import redirect,render,get_object_or_404

from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task'] # get HTTP POST data
    Task.objects.create(task=task) # create a new Task object
    return redirect('home-todo')

def deleteTask(request,task_id):
    task=get_object_or_404(Task,id=task_id) #
    task.delete()
    return redirect('home-todo')
