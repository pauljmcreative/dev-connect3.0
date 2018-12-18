from django import forms
from .models import StudentProfile, Project

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('tag_line', 'location', 'linkedin_link', 'github_link', 'website_link', 'image', 'skills', 'favorite_snack', 'dream_job', 'favorite_tech', 'hidden_talent')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'hosted_link', 'github_link', 'screenshot', 'description', 'tech', 'teammates')
