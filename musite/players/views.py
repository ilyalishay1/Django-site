from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponseNotFound


def home(request):
    posts = PlayersModel.objects.all()
    context = {'posts': posts}
    return render(request, 'players/home.html', context=context)


def add_post(request):
    posts = PlayersModel.objects.all()
    form = AddPostForm()
    context = {'posts': posts, 'form': form}
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'players/add_post.html', context=context)


def players_now(request):
    posts = PlayersModel.objects.filter(cat=1)
    context = {'posts': posts}
    return render(request, 'players/players_now.html', context=context)


def all_time_players(request):
    posts = PlayersModel.objects.filter(cat=2)
    context = {'posts': posts}
    return render(request, 'players/all_time_players.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h2>Страница не найдена</h2>')
