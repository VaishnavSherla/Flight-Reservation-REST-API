from django.urls import include, path
from .views import StudentViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
