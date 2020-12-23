'''
urls.py
Created on 22nd Dec, 2020
'''
from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import TeachersListView, TeacherDetailView, Import

__author__ = 'Tanya'

urlpatterns = [
    path('', TeachersListView.as_view(), name='teachers'),
    path('<int:pk>', TeacherDetailView.as_view(), name='teacher-detail'),
    path('import/', login_required(Import.as_view()), name='import-teachers'),
]