'''
context_processors.py
Created on 22nd Dec, 2020
'''
from django.conf import settings

__author__ = 'Tanya'


MISC_URLS = {
    'MEDIA_URL': settings.MEDIA_URL
}

def externalurls(request):
    return MISC_URLS