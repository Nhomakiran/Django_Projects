from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name = 'dashboard'),
    path('teams/', views.TeamListView.as_view(), name = 'team-list'),
    path('teams/create/', views.TeamCreateView.as_view(), name = 'team-create'),
    path('teams/<int:pk>/update/', views.TeamUpdateView.as_view(), name = 'team-update'),
    path('teams/<int:pk>/delete/', views.TeamDeleteView.as_view(), name = 'team-delete'),
    path('projects/', views.ProjectListView.as_view(), name = 'project-list'),
    path('projects/create/', views.ProjectCreateView.as_view(), name = 'project-create'),
    path('projects/<int:pk>/update/', views.ProjectUpdateView.as_view(), name = 'project-update'),
    path('projects/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name = 'project-delete'),
    path('members/', views.MemberListView.as_view(), name = 'member-list'),
    path('members/create/', views.MemberCreateView.as_view(), name = 'member-create'),
    path('members/<int:pk>/update/', views.MemberUpdateView.as_view(), name = 'member-update'),
    path('members/<int:pk>/delete/', views.MemberDeleteView.as_view(), name = 'member-delete'),
    path('tasks/', views.TaskListView.as_view(), name = 'task-list'),
    path('tasks/create/', views.TaskCreateView.as_view(), name = 'task-create'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name = 'task-update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name = 'task-delete'),
]