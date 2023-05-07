from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth import login
# Create your views here.


def home_view(request):
    return render(request, 'djmessenger/homepage.html')


def sing_up_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    form = CustomUserCreationForm
    return render(request, 'registration/signup.html', context={"register_form": form})



