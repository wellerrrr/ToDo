from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import ToDoList
from .forms import PostForm
from todo.models import ToDoList


@login_required
def todo(request):
    todo = ToDoList.objects.filter(user=request.user)  # Получаем список задач текущего пользователя
    
    if request.method == 'POST':
        form = PostForm(request.POST)  # Создаем форму из POST-данных
        if form.is_valid():
            new_task = form.save(commit=False)  # Создаем новую задачу, но не сохраняем ее в БД
            new_task.user = request.user  # Связываем задачу с текущим пользователем
            new_task.save()  # Сохраняем задачу в БД
            return redirect('todo:todo_view') 
    else:
        form = PostForm()  # Создаем пустую форму

    return render(request, 'todo/todo.html', {'form': form, 'todo': todo})


def todo_details(request, pk):
    todo_det = get_object_or_404(ToDoList, pk=pk)
    todo = ToDoList.objects.filter(pk=pk)
    return render(request, 'todo/todo_details.html', {'todo_det': todo_det, 'todo': todo})


def todo_delete(request, pk):
    todo_del = get_object_or_404(ToDoList, pk=pk)
    todo_del.delete()

    messages.success(request, 'Your todo have been deleted')
    return redirect('todo:todo_view')


def todo_edit(request, pk):
    todo = get_object_or_404(ToDoList, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'The changes was saved')
            return redirect('todo:todo_view')
    else:
        form = PostForm(instance=todo)
    return render(request, 'todo/todo_edit.html', {'form': form})

