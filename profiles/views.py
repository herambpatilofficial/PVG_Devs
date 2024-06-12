from django.shortcuts import render
from django.contrib import messages

# Create your views here.
# profiles/views.py

from django.shortcuts import render, redirect
from .forms import ProfileForm, ProjectForm
from .models import Profile, Project
from django.db.models import Count

from .utils import fetch_leetcode_data

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            
            profile.save()
            messages.success(request, 'Profile created successfully!')
            return redirect('dashboard')
    else:
        form = ProfileForm()
    return render(request, 'profiles/create_profile.html', {'form': form})

def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            leetcode_data = fetch_leetcode_data(profile.leetcode_username)
            messages.success(request, 'Profile updated successfully!')
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/edit_profile.html', {'form': form})

def dashboard(request):
    profile = Profile.objects.get(user=request.user)
    projects = Project.objects.filter(profile=profile)
    leetcode_data = fetch_leetcode_data(profile.leetcode_username) if profile.leetcode_username else None
    return render(request, 'profiles/dashboard.html', {'profile': profile, 'projects': projects, 'leetcode_data': leetcode_data})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = request.user.profile
            project.save()
            messages.success(request, 'Project added successfully!')
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'profiles/add_project.html', {'form': form})

def rankings(request):
    profiles = Profile.objects.annotate(num_projects=Count('project')).order_by('-num_projects')
    return render(request, 'profiles/rankings.html', {'profiles': profiles})

# import Q from django.db.models to perform OR query
from django.db.models import Q
from django.shortcuts import get_object_or_404
def search_profiles(request):
    query = request.GET.get('q')
    if query:
        profiles = Profile.objects.filter(
            Q(name__icontains=query) | Q(branch__icontains=query)
        )
    else:
        profiles = Profile.objects.all()
    return render(request, 'profiles/search_results.html', {'profiles': profiles, 'query': query})

def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('dashboard')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'profiles/edit_project.html', {'form': form})

def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('dashboard')
    return render(request, 'profiles/delete_project.html', {'project': project})


def home(request):
    return render(request, 'profiles/home.html')