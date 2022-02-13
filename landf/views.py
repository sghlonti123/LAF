import django.views.defaults
from django.shortcuts import render
from django.http import HttpResponse

registered = True


def home(request):
    context = {
        'title': 'Home',
        'registered': registered
    }
    return render(request, 'landf/home.html',context)


def about(request):
    context = {
        'title': 'About',
        'registered': registered
    }
    return render(request, 'landf/about.html', context)


def profile(request):
    context = {
        'title': 'Profile',
        'registered': registered
    }
    return render(request, 'landf/profile.html', context)


def login(request):
    context = {
        'title': 'Login',
        'registered': registered
    }
    return render(request, 'landf/login.html', context)


def register(request):
    context = {
        'title': 'Register',
        'registered': registered
    }
    return render(request, 'landf/register.html', context)


def error(request):
    context = {
        'title': 'What? :('
    }
    print("This is called")
    return render(request, 'landf/error404.html', context)
