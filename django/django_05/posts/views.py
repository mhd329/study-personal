from asyncio.windows_events import NULL
from email.policy import default
from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    post = Todo.objects.order_by("id")
    context = {
        "post": post,
    }
    return render(request, "posts/index.html", context)


# def new(request):
#     return render(request, "posts/new.html")


def create(request):
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    created_at = request.GET.get("created_at")
    deadline = request.GET.get("deadline")

    todo = Todo()
    todo.content = content
    if priority:
        todo.priority = priority
    if created_at:
        todo.created_at = created_at
    if deadline:
        todo.deadline = deadline
    todo.save()

    return redirect("posts:index")


def update(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.completed = True
    todo.save()
    return redirect("posts:index")


def delete(request, pk):
    Todo.objects.get(id=pk).delete()
    return redirect("posts:index")
