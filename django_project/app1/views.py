from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student

class StudentViewset(viewsets.ModelViewSet):

    serializer_class = StudentSerializer
    queryset = Student.objects.all()
