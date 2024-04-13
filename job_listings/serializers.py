from rest_framework import serializers
from .models import Employer, JobSeeker, Skill, Job, Application

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ('id', 'user', 'company_name', 'company_description', 'company_website', 'company_logo')

class JobSeekerSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)

    class Meta:
        model = JobSeeker
        fields = ('id', 'user', 'resume', 'skills')

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name', 'description')

class JobSerializer(serializers.ModelSerializer):
    employer = EmployerSerializer(read_only=True)
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = ('id', 'employer', 'title', 'description', 'location', 'job_type', 'salary_range', 'skills', 'created_at', 'is_active')

class ApplicationSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    job_seeker = JobSeekerSerializer(read_only=True)

    class Meta:
        model = Application
        fields = ('id', 'job_seeker', 'job', 'cover_letter', 'submitted_at')