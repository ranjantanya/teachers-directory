'''
urls.py
Created on 22nd Dec, 2020
'''
from django.urls import path

from . import views

__author__ = 'Tanya'

urlpatterns = [
    path('accounts/signup/', views.signup, name="register")
]