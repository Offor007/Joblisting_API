from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .permissions import IsOwnerOrReadOnly
from rest_framework.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.pagination import PageNumberPagination
from .models import Job, Category, Industry, JobType, Tag, Location
from .serializers import JobSerializer

def cache_job_list_view(view_func):
    return method_decorator(cache_page(60 * 15))(view_func)

class CustomPagination(PageNumberPagination):
    page_size = 10  

class JobListCreateView(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Job.objects.all()
    pagination_class = CustomPagination
    
    def perform_create(self, serializer):
        job_data = self.request.data
        category_data = job_data.get('category')
        industry_data = job_data.get('industry')
        job_type_data = job_data.get('job_type')
        tags_data = job_data.get('tags')
        locations_data = job_data.get('location')

        
        category, created_category = Category.objects.get_or_create(name=category_data['name'])
        industry, created_industry = Industry.objects.get_or_create(name=industry_data['name'])
        job_type, created_job_type = JobType.objects.get_or_create(name=job_type_data['name'])

        tags = [Tag.objects.get_or_create(name=tag_data['name'])[0] for tag_data in tags_data]
        location, created_location = Location.objects.get_or_create(name=locations_data['name'])

        # Set the fields of the Job instance
        serializer.save(
            posted_by=self.request.user,
            category=category,
            industry=industry,
            job_type=job_type,
            tags=tags,
            location=location
        )

    def create(self, request, *args, **kwargs):
        request.data["posted_by"] = self.request.user.id
        return super().create(request, *args, **kwargs)



class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        if serializer.instance.posted_by != self.request.user:
            raise PermissionDenied("You don't have permission to edit this job post.")
        serializer.save()

class JobSearchView(generics.ListAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('q', '')

        if not search_query:
            return Job.objects.none() 
        
        queryset = Job.objects.filter(title__icontains=search_query)

        return queryset