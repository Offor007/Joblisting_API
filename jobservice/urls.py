from django.urls import path
from .views import JobListCreateView, JobDetailView, JobSearchView

urlpatterns = [
   
    path('jobs/', JobListCreateView.as_view(), name='job_list'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('jobs/search/', JobSearchView.as_view(), name="job-search"),
        
]