'''
urls.py
Created on 22nd Dec, 2020
'''
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

__author__ = 'Tanya'

urlpatterns = [
    path('', include("accounts.urls")),
    path('', include("directory.urls")),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('teachers/', include('directory.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
