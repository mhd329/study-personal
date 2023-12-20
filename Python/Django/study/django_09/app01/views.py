from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
def movies(request):
    movie = Movie.objects.all()
    context = {
        "movies": movie,
    }
    return render(request, "app01/movies.html", context)


def create(request):
    if request.method == "POST":
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            return redirect("app01:movies")
        else:
            pass
    else:
        movie_form = MovieForm()
    context = {
        "movie_form": movie_form,
    }
    return render(request, "app01/form.html", context)


def update(request, pk):
    movie = Movie.objects.get(id=pk)
    if request.method == "POST":
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie_form.save()
            context = {
                "movie": movie,
            }
            return render(request, "app01/detail.html", context)
        else:
            pass
    else:
        movie_form = MovieForm(instance=movie)
    context = {
        "movie_form": movie_form,
    }
    return render(request, "app01/form.html", context)


def detail(request, pk):
    movie = Movie.objects.get(id=pk)
    context = {
        "movie": movie,
    }
    return render(request, "app01/detail.html", context)


def delete(request, pk):
    movie = Movie.objects.get(id=pk)
    movie.delete()
    return render(request, "app01/movies.html")


def add_score(request, pk):
    score = int(request.POST.get("score"))
    movie = Movie.objects.get(id=pk)
    movie.total_score += score
    movie.vote_cnt += 1
    movie.avg_score = movie.total_score / movie.vote_cnt
    movie.save()
    context = {
        "movie": movie,
    }
    return render(request, "app01/detail.html", context)
