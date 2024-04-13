from django.contrib import admin

from .models import Employer, JobSeeker, Skill, Job, Application

# Register your models here.
admin.site.register(Employer)
admin.site.register(JobSeeker)
admin.site.register(Skill)
admin.site.register(Job)
admin.site.register(Application)