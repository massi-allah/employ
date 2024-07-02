from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import mainpage, job

app_name = "jobs"

urlpatterns = [
    path("", mainpage, name="main_page"),
    path("job/<id>/", job, name="job_detail"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)