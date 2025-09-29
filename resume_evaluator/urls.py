from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from CV_app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.upload_resume, name='upload_resume'),  # Root now shows home + upload
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


