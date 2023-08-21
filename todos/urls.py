from django.urls import path

from . import views 
urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('delete/<int:task_id>/', views.deleteTask, name='deleteTask'),

]