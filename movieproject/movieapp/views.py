from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from .forms import movieform


def index(request):
    film = movie.objects.all()
    context = {
        'movie': film
    }
    return render(request, 'index.html', context)


def detail(request, movieid):
    movie1 = movie.objects.get(id=movieid)
    return render(request, 'detail.html', {'movie': movie1})


def add_movie(request):
    if request.method == "POST":
        mname = request.POST.get('mname', )
        mdesc = request.POST.get('mdesc', )
        myear = request.POST.get('myear', )
        mimg = request.FILES['mimg']
        mmovie = movie(mname=mname, mdesc=mdesc, myear=myear, mimg=mimg)
        mmovie.save()
    return render(request, 'add.html')


def update(request, id):
    film = movie.objects.get(id=id)
    form = movieform(request.POST or None, request.FILES, instance=film)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'film': film})


def delete(request, id):
    if request.method == 'POST':
        film = movie.objects.get(id=id)
        film.delete()
        return redirect('/')
    return render(request, 'delete.html')
