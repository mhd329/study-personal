from django.shortcuts import render, redirect
from datetime import date
from .models import Todo

# Create your views here.
def index(request):
    post = Todo.objects.order_by("id")
    context = {
        "post": post,
    }
    return render(request, "posts/index.html", context)

def create(request):
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")

    p = int(priority)
    todo = Todo()
    todo.content = content
    if p:
        if p > 5 or p < 1:
            todo.priority = 3
        else:
            todo.priority = priority
    if deadline:
        todo.deadline = deadline
    todo.save()

    return redirect("posts:index")


def update(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.completed = True
    todo.completed_at = date.today()
    todo.save()
    return redirect("posts:index")


def delete(request, pk):
    Todo.objects.get(id=pk).delete()
    return redirect("posts:index")
