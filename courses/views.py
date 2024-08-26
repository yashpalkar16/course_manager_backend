from rest_framework import generics
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseInstanceListCreateView(generics.ListCreateAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        year = self.request.query_params.get('year', None)
        semester = self.request.query_params.get('semester', None)
        if year and semester:
            queryset = queryset.filter(year=year, semester=semester)
        return queryset

    def perform_create(self, serializer):
        course_id = self.request.data.get('course')
        course = Course.objects.get(id=course_id)
        year = self.request.data.get('year')
        semester = self.request.data.get('semester')

        serializer.save(course=course, year=year, semester=semester)

class CourseInstanceDetailView(generics.RetrieveDestroyAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
