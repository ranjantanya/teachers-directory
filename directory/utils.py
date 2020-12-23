'''
utils.py
Created on 22nd Dec, 2020
'''
import os
import zipfile

from .exceptions import TooManySubjectsException
from .models import Teacher, Subject

__author__ = 'Tanya'

def extract_zipped_files(zip_file, dest_dir):
    '''
    Extract all contents of zip file to dest_dir and return the list
    of all contained filenames
    '''
    with zipfile.ZipFile(zip_file) as zip_fd:
        files_lst = zip_fd.namelist()
        zip_fd.extractall(path=dest_dir)
    return files_lst

def create_teacher(row, photo_filename):
    '''
    Given a csv file row with required details and a
    validated profile photo file, create a teacher and related subjects
    '''
    teacher = Teacher(first_name=row[0].strip(),
                      last_name=row[1].strip(),
                      profile_picture=os.path.join('profile_photos', photo_filename) if photo_filename else None,
                      email=row[3].strip(),
                      phone_number=row[4].strip(),
                      room_number=row[5].strip(),
                      )
    teacher.save()
    subject_names = row[6].strip().split(',')
    if len(subject_names) > 5:
        raise TooManySubjectsException
    for subject_name in subject_names:
        subject, _ = Subject.objects.get_or_create(name=subject_name.title())
        teacher.subjects.add(subject)

    return teacher