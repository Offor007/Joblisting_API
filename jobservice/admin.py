from django.contrib import admin
from .models import JobType, Industry, Category, Skill, Job, Tag, Location

# Register your models here.


admin.site.register(JobType)
admin.site.register(Industry)
admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(Job)
admin.site.register(Tag)
admin.site.register(Location)
