from django.http import HttpResponse
from django.shortcuts import redirect,render,get_object_or_404

from .models import Task

# Add a new task
def addTask(request):
    task = request.POST['task'] # get HTTP POST data
    if task: # if task is not empty
        Task.objects.create(task=task) # create a new Task object
    return redirect('home-todo')

def deleteTask(request,task_id):
    task=get_object_or_404(Task,id=task_id) #
    task.delete()
    return redirect('home-todo')
# Mark a task as complete 
def completeTask(request,task_id):
    task=get_object_or_404(Task,id=task_id) #
    task.is_completed=True
    task.save()
    return redirect('home-todo')
# Mark a task as incomplete
def clearCompleted(request):
    Task.objects.filter(is_completed=True).delete()
    return redirect('home-todo')
