from rest_framework import serializers
from .models import JobType, Industry, Category, Skill, Job, Tag, Location

class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = '__all__'

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    job_type = JobTypeSerializer(read_only=True)
    industry = IndustrySerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Job
        fields = '__all__'


