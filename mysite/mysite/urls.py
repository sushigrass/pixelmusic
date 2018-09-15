from django.contrib import admin
from django.conf.urls import include, url
from pages.views import FrontEndRenderView, index

urlpatterns = [
    url('pixelmusic/', FrontEndRenderView.as_view(), name='home'),
    url('admin/', admin.site.urls),
    url('index/', index),
]
