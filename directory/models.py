'''
directory.models
Created on 21st Dec, 2020
'''
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models
from django.shortcuts import reverse

__author__ = 'Tanya'

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_photos', null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = PhoneNumberField()
    room_number = models.CharField(max_length=5)
    subjects = models.ManyToManyField(Subject)

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('teacher-detail', args=[(self.pk)])