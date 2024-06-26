# from django.conf.urls import url
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.display_video, name='main'),
    path('download/',
         views.download_cheatsheet, name='download_cheatsheet'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)