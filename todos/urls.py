from django.urls import path

from . import views 
urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('delete/<int:task_id>/', views.deleteTask, name='deleteTask'),
    path('completeTask/<int:task_id>/', views.completeTask, name='completeTask'), # button to complete a task


    path('clearCompleted/', views.clearCompleted, name='clearCompleted'),# button to clear completed tasks


]