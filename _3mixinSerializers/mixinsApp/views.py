from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.http import Http404

from rest_framework import generics, mixins

# Create your views here.
class StudentList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class StudentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def patch(self, request, pk):
        return self.partial_update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)

