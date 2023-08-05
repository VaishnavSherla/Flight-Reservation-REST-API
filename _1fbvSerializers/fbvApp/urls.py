from django.urls import include, path
from .views import studentList, studentDetail

urlpatterns = [
    path('students/', studentList, name='students'),
    path('students/<int:pk>/', studentDetail, name='student'),
]
