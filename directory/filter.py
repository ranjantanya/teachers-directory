'''
filter.py
Created on 22nd Dec, 2020
'''
import django_filters

from .models import Teacher

__author__ = 'Tanya'

class TeacherFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(lookup_expr='istartswith')
    subjects__name = django_filters.CharFilter(method='my_custom_filter', label='Subject names', help_text="To search on multiple subjects, enter subject names separated by commas. "
                                              "e.g. to search a teacher who teaches both physics and biology, enter physics, biology in the box.")

    class Meta:
        model = Teacher
        fields = ['last_name', 'subjects__name']

    def my_custom_filter(self, queryset, name, value):
        subject_list = value.split(',')
        for subject_name in subject_list:
            queryset = queryset.filter(subjects__name__icontains=subject_name)
        return queryset
