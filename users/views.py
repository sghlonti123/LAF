from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

data = {'subject': 'hello',
        'message': 'Hi there',
        'sender': 'foo@example.com',
        'cc_myself': True}


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Create for {username}!')
            return redirect('landf-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login(request):
    pass













