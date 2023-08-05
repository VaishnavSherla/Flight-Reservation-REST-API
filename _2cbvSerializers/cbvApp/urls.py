from django.urls import include, path
from .views import StudentList, StudentDetail

urlpatterns = [
    path('students/', StudentList.as_view(), name='students'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student'),
]
