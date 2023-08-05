from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

# Create your views here.
class StudentPagination(PageNumberPagination):
    page_size = 2

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # I added the pagination here just to implement the class level pagination.
    # pagination_class = StudentPagination
    # Offset pagination
    pagination_class = LimitOffsetPagination
