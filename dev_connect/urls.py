from django.urls import path
from . import views

urlpatterns = [
    path('<username>/', views.student_profile, name='student_profile'),
    path('<username>/projects/<title>', views.project_details, name='project_details'),
    path('', views.all_profiles, name='all_profiles'),
    path('projects/add', views.add_project, name='add_project'),
    path('projects/<title>/edit', views.edit_project, name='edit_project'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
]
