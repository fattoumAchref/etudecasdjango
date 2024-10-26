from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import ParticipantRegistrationForm, ParticipantLoginForm

def register_view(request):
    if request.method == 'POST':
        form = ParticipantRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = ParticipantRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = ParticipantLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = ParticipantLoginForm()
    return render(request, 'login.html', {'form': form})
