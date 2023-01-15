from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse

from authapp.forms import RegisterForm, LoginForm


def register(request):
    title = 'Регистрация'
    context = {
        'title': title
    }
    if request.method.lower() == 'post':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main'))
        context['form'] = form
        return render(request, 'authapp/register.html', context)
    form = RegisterForm()
    context['form'] = form
    return render(request, 'authapp/register.html', context)


def login(request):
    title = 'Вход'
    context = {
        "title": title
    }

    if request.method.lower() == 'post':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print('valid')
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                print('user')
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))
        else:
            print(form.errors.as_json())
    form = LoginForm()
    context['form'] = form
    return render(request, 'authapp/register.html', context)


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return HttpResponseRedirect(reverse('main'))