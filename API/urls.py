from django.urls import path, include
from rest_framework import routers
from .views import (
    JobCategoryViewSet,
     JobViewSet
)

app_name = "API"

router = routers.DefaultRouter()
router.register(r'job-categories', JobCategoryViewSet)
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Add other paths or include other app's URLs as needed
]
