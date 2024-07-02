from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import set_language
from .views import about, contact, custom_404


urlpatterns = [
    path('adminMy/', admin.site.urls),
    path('lang', set_language, name="set_language"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),

    path('404/', custom_404, name="custom_404"),

    # Internal Apps
    path('', include('jobs.urls', namespace="jobs")),
    path('api/', include('API.urls', namespace="API")),

]

# Error 404 url
handler404 = 'Employ.views.custom_404'

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)