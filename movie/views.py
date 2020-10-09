from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import *
from .forms import *
from django.contrib import messages


def home(request):
    if len(User.objects.all()) >= 1:
        return redirect('/login')
    else:
        return redirect('/register')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'detail/form.html', {'form': form})


def dashboard(request):
    data = dict()
    data['text'] = 'Movie Showing Now'
    if request.user.is_authenticated:
        data['movies'] = movieData.objects.all()
        print(data['movies'])
        return render(request, template_name='detail/dashboard.html', context=data)
    else:
        return redirect('Login')


def search(request):
    data = dict()
    data['text'] = 'Search via Movie Name'
    data['form'] = searchForm()
    if request.method == 'POST':
        form = searchForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            # messages.success(request, 'Search Results')
            data['movies'] = movieData.objects.filter(movieName__contains=text)
            print(data['movies'])
    if request.user.is_authenticated:
        return render(request, template_name='detail/dashboard.html', context=data)
    else:
        return redirect('Login')


def addMovie(request):
    data = dict()
    if request.method == 'POST':
        form = addMovieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movie Added Successfully')
    form = addMovieForm()
    data['text'] = 'ADD Movie'
    data['form'] = form
    return render(request, template_name='detail/dashboardForm.html', context=data)


def addShows(request):
    data = dict()
    if request.method == 'POST':
        form = addShowForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Show Added Successfully')
        else:
            messages.error(request, 'Show Already Exists,Try Different Slot')
    form = addShowForm()
    data['text'] = 'ADD Show'
    data['form'] = form
    return render(request, template_name='detail/dashboardForm.html', context=data)


def buyTickets(request):
    data = dict()
    if request.method == 'POST':
        form = buyTicketsForm(request.POST)
        if form.is_valid():
            # showObj = shows.objects.get(form.cleaned_data.get('movieShow'))
            # print(form.cleaned_data.get('movieShow'))
            form.save()
            messages.success(request, 'Tickets')
        else:
            messages.error(request, form.errors[0])
    data['text'] = 'Buy Tickets'
    data['form'] = buyTicketsForm()
    return render(request, template_name='detail/dashboardForm.html', context=data)
