from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class JobType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Industry(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company_name = models.CharField(max_length=100)
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)
    tags = models.ManyToManyField(Tag)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
