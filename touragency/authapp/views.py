from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse

from authapp.forms import RegisterForm


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
