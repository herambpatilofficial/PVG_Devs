# Create your models here.
# profiles/models.py

from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    whatsapp_number = models.CharField(max_length=15)
    domains = models.ManyToManyField('Domains')
    linkedin_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    leetcode_username = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    domains = models.ManyToManyField('Domains')

    def __str__(self):
        return self.title
    
class Domains(models.Model):
    domain_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)

    def __str__(self):
        return self.domain_name
    

