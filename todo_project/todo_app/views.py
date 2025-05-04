from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# def todo_list(request):
#     if request.method == "POST":
#         form = TodoForm(request.POST)
#     todos = Todo.objects.all()
#     if form.is_valid():
#         form.save()
#         return redirect('todo_list')
#     # todoは保存されているオブジェクト、formは入力欄を渡している
#     return render(request, 'todo_app/todo_list.html', {'todos': todos, 'form': form})
def todo_list(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()

        todos = Todo.objects.all()
    return render(request, 'todo_app/todo_list.html', {'todos': todos, 'form': form})