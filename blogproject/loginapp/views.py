from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
# from django.contrib.auth.decorators
from .utils import random_string

# from .models import *

# Create your views here.

def login(request):
    # now the context exists but it is empty by default
    context = {}

    if request.method == 'POST':
        # request.POST is a dictionary, you need a key to get the value
        user = authenticate(request, 
            username=request.POST['user'], 
            password=request.POST['password'])
        # check if user is real
        if user:
            # if user is in the system, redirect them
            dj_login(request, user)
            #context = {'user':request.POST['user']} - useless, not passing the context to the return
            return HttpResponseRedirect(reverse ('blogapp:index'))
        else:
            # send error message
            # context = {'error':'Username or password is wrong.'}
            context['error'] = "Username or password is wrong."

    # don't receive a post request, render template as default
    # request and url are required arguments, context is not require
    return render(request, 'loginapp/login.html', context)

def logout(request):
    dj_logout(request)
    # redirect user if they logout
    return HttpResponseRedirect(reverse ('loginapp:login'))



def signup(request):
    if User.is_authenticated:
        dj_logout(request)

    if request.method == 'POST':
        
        context = {}
        if not request.POST['password'] == request.POST['confirmPassword']:
            context['error'] = "Passwords do not match."
            return render(request, 'loginapp/signup.html', context)
        if len(User.objects.filter(username = request.POST['user'])) > 0:
            context['error'] = 'Username already exists'
            return render(request, 'loginapp/signup.html', context)

        # create user
        user = User.objects.create_user(request.POST['user'],password=request.POST['password'])
        user.save()
        dj_login(request, user)
        return HttpResponseRedirect(reverse ('blogapp:index'))
        


    return render(request, 'loginapp/signup.html')


def password_reset(request):
    context = {}
    if request.method == 'POST':
    
        users = User.objects.filter(username=request.POST['user'])
        if users:
            user = users[0]
            new_password = random_string()
            user.set_password(new_password)
            user.save()
            print(f'*********** User {user} change password to {new_password}')
            return HttpResponseRedirect(reverse('loginapp:login'))

        else:
            context['error'] = "No such username"

    return render(request, 'loginapp/password_reset.html', context)

