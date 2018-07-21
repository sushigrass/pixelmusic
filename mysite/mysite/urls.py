from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url('pixelmusic/', include('pixelmusic.urls')),
    url('admin/', admin.site.urls),
]
