'''
views.py
Created on 22nd Dec, 2020
'''
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect, render, reverse

__author__ = 'Tanya'

def signup(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect(reverse('teachers'))
    context = {}
    context['form'] = form
    return render(request, 'registration/signup.html', context)