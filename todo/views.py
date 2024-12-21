from django.shortcuts import render, redirect
from .models import Todo

def todo_list(request):
    todos = Todo.objects.order_by('-timestamp')  # Sort by creation timestamp
    return render(request, 'todo/index.html', {'todos': todos})

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date') if request.POST.get('due_date') else None
        tags = request.POST.get('tags')  # Comma-separated tags
        Todo.objects.create(title=title, description=description, due_date=due_date, tags=tags)
    return redirect('todo_list')

def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')
