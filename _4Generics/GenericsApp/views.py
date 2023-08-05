from .models import Student
from .serializers import StudentSerializer

from rest_framework import generics

# Create your views here.
class StudentList(generics.ListCreateAPIView, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def patch(self, request, pk):
        return self.partial_update(request, pk)