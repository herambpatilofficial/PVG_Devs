# profiles/forms.py

from django import forms
from .models import Profile, Project, Domains

class ProfileForm(forms.ModelForm):
    domain = forms.ModelChoiceField(
        queryset=Domains.objects.all(),
        empty_label="Select Domain",
        widget=forms.Select,
        required=True)
    class Meta:
        model = Profile
        fields = ['name', 'branch', 'whatsapp_number', 'github_link', 'leetcode_username', 'linkedin_link', 'domain']

class ProjectForm(forms.ModelForm):
    domain = forms.ModelChoiceField(
        queryset=Domains.objects.all(),
        empty_label="Select Domain",
        widget=forms.Select,
        required=True)
    class Meta:
        model = Project
        fields = ['title', 'description', 'link', 'domain']