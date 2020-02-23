from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from vacancy.views import create_back_call

urlpatterns = [
    path('top_secret/', admin.site.urls),
    path('', create_back_call, name='create_back_call'),
    path('', include('vacancy.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +\
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
