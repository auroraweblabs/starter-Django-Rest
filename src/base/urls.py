from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, static(settings.STATIC_ROOT))
urlpatterns += static(settings.MEDIA_URL, static(settings.MEDIA_ROOT))
