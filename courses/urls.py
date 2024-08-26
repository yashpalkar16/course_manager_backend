from django.urls import path
from .views import CourseListCreateView, CourseInstanceListCreateView, CourseDetailView, CourseInstanceDetailView

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('instances/', CourseInstanceListCreateView.as_view(), name='course-instance-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('instances/<int:pk>/', CourseInstanceDetailView.as_view(), name='course-instance-detail'),
]
