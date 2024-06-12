# URLS.PY
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_project/', views.add_project, name='add_project'),
    path('edit_project/<int:project_id>/', views.edit_project, name='edit_project'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('rankings/', views.rankings, name='rankings'),
    path('search/', views.search_profiles, name='search_profiles'),
]