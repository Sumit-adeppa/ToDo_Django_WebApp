from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo

def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        title = request.POST.get('title')
        details = request.POST.get('details')
        Todo.objects.create(title=title, details=details)
        messages.success(request, "Task added successfully!")
        return redirect('index')
    return render(request, 'todo/index.html', {'list': item_list})

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Task removed!")
    return redirect('index')