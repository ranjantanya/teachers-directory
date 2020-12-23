'''
admin.py
Created on 22nd Dec, 2020
'''
from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import Teacher, Subject

__author__ = 'Tanya'

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

    def clean(self):
        subjects = self.cleaned_data.get('subjects')
        if subjects.count() > 5:
            raise ValidationError("A teacher cannot teach more than 5 subjects")
        return self.cleaned_data

class TeacherAdmin(admin.ModelAdmin):
    form = TeacherForm

class SubjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Subject, SubjectAdmin)
