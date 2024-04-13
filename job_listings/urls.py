from django.urls import path
from .views import (
    EmployerListCreateView, EmployerDetailView,
    JobSeekerListCreateView, JobSeekerDetailView,
    SkillListCreateView, SkillDetailView,
    JobListCreateView, JobDetailView,
    ApplicationListCreateView, ApplicationDetailView
)

urlpatterns = [
    path('employers/', EmployerListCreateView.as_view(), name='employer-list-create'),
    path('employers/<int:pk>/', EmployerDetailView.as_view(), name='employer-detail'),
    path('jobseekers/', JobSeekerListCreateView.as_view(), name='jobseeker-list-create'),
    path('jobseekers/<int:pk>/', JobSeekerDetailView.as_view(), name='jobseeker-detail'),
    path('skills/', SkillListCreateView.as_view(), name='skill-list-create'),
    path('skills/<int:pk>/', SkillDetailView.as_view(), name='skill-detail'),
    path('jobs/', JobListCreateView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('applications/', ApplicationListCreateView.as_view(), name='application-list-create'),
    path('applications/<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),
]