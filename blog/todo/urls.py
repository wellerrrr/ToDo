from django.urls import path
from .views import todo, todo_details, todo_delete, todo_edit


app_name = 'todo'
urlpatterns = [
    path('todo/', todo, name='todo_view'),
    path('todo/details/<int:pk>/', todo_details, name='todo_details'),
    path('todo/details/delete/<int:pk>/', todo_delete, name='todo_delete'),
    path('todo/details/edit/<int:pk>/', todo_edit, name='todo_edit'),
]