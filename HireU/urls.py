from django.conf.urls.static import static
from .settings import MEDIA_ROOT, MEDIA_URL

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += static( MEDIA_URL, document_root = MEDIA_ROOT )
