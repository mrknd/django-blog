from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

from blogs.models import Category, Blog
from assignments.models import About
from .forms import RegistrationForm


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')

    # Fetch About Us
    try:
        about = About.objects.get()
    except:
        about = None
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about
    }
    return render(request=request, template_name='home.html', context=context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.password1)
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request=request, template_name='register.html', context=context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(userrname=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home_page')

    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request=request, template_name='login.html', context=context)


def logout(request):
    auth.logout(request)
    return redirect('home_page')