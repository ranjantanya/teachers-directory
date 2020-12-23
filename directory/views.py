'''
views.py
Created on 22nd Dec, 2020
'''
import csv
import io
import os
import zipfile

from django_filters.views import FilterView

from django.conf import settings
from django.contrib import messages
from django.db import transaction
from django.shortcuts import render
from django.views import generic

from .exceptions import TooManySubjectsException
from .filter import TeacherFilter
from .models import Teacher
from .utils import create_teacher

__author__ = 'Tanya'

class TeachersListView(FilterView):
    context_object_name = 'teachers'
    template_name = 'directory/teacher_list.html'
    filterset_class = TeacherFilter
    #[TODO]: Paginate


class TeacherDetailView(generic.DetailView):
    model = Teacher
    context_object_name = 'teacher'


class Import(generic.View):
    def get(self, request):
        return render(request, 'directory/upload.html', {})

    def post(self, request):
        uploaded_files = request.FILES.getlist('file')
        if not len(uploaded_files) == 2:
            messages.error(request, "You need to upload both a csv file containing teacher details and "
                                    "a zip file containing teacher profile photos.")
            return render(request, 'directory/upload.html', {})
        teacher_details_file = uploaded_files[0]
        teacher_photos_file = uploaded_files[1]

        filename, file_extension = os.path.splitext(teacher_details_file.name)
        if not file_extension == '.csv':
            messages.error(request, "Only csv file is allowed for uploading details")
            return render(request, 'directory/upload.html', {})

        if not zipfile.is_zipfile(teacher_photos_file):
            messages.error(request, "Only zip file is allowed for uploading photos")
            return render(request, 'directory/upload.html', {})

        file_data = io.StringIO(teacher_details_file.read().decode())
        csv_reader = csv.reader(file_data, delimiter=',')
        try:
            with zipfile.ZipFile(teacher_photos_file) as zip_fd:
                profile_photo_files_lst = zip_fd.namelist()
        except zipfile.BadZipFile:
            messages.error(request, "The zip file is corrupted. Please try again with a different file.")
            return render(request, 'directory/upload.html', {})
        except zipfile.LargeZipFile:
            messages.error(request, "The zip file is too large. Please try again with a different file.")
            return render(request, 'directory/upload.html', {})

        successful, failed = [], {}
        for row_count, row in enumerate(csv_reader, 1):
            if row_count == 1:
                # Skip the header
                continue
            if not row[0].strip():
                continue
            photo_filename = row[2].strip() or None

            if photo_filename:
                for name in profile_photo_files_lst:
                    if photo_filename.upper() == name.upper():
                        # case insensitive match, set filename to the corresponding file present in zip
                        profile_pic_file = name
                        break
                else:
                    print(f'photo {photo_filename} missing in zip')
                    profile_pic_file = None
            else:
                profile_pic_file = None

            if profile_pic_file:
                with zipfile.ZipFile(teacher_photos_file) as zip_fd:
                    zip_fd.extract(profile_pic_file, path=os.path.join(settings.MEDIA_ROOT, 'profile_photos'))

            try:
                with transaction.atomic():
                    teacher = create_teacher(row, profile_pic_file)
            except TooManySubjectsException:
                failed[f'{row[3].strip()} (row {row_count})'] = "More than 5 subjects are not allowed"
            except Exception as e:
                failed[f'{row[3].strip()} (row {row_count})'] = e
            else:
                successful.append(teacher.email)

        messages.info(request, "Operation Completed")
        if failed:
            for key, value in failed.items():
                messages.error(request, f"[Failed] {key}: {value}")
        return render(request, 'directory/upload.html', {})






