'''
filter.py
Created on 22nd Dec, 2020
'''
import django_filters

from .models import Teacher

__author__ = 'Tanya'

class TeacherFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(lookup_expr='istartswith')
    subjects__name = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Teacher
        fields = ['last_name', 'subjects__name']