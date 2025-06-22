from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Team, Project, Member, Task
from .forms import ProjectForm, TaskForm
from django.utils.timezone import now
from datetime import date, timedelta

# Create your views here.

class TeamListView(ListView):
    model = Team
    template_name = 'management/team_list.html'

class TeamCreateView(CreateView):
    model = Team
    fields = ['name', 'description']
    template_name = 'management/team_form.html'
    success_url = reverse_lazy('team-list')

class TeamUpdateView(UpdateView):
    model = Team
    fields = ['name', 'description']
    template_name = 'management/team_form.html'
    success_url = reverse_lazy('team-list')

class TeamDeleteView(DeleteView):
    model = Team
    template_name = 'management/team_confirm_delete.html'
    success_url = reverse_lazy('team-list')


# Class views for Projects

class ProjectListView(ListView):
    model = Project
    template_name = 'management/project_list.html'
    context_object_name = 'projects'

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'management/project_form.html'
    success_url = reverse_lazy('project-list')

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'management/project_form.html'
    success_url = reverse_lazy('project-list')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'management/project_confirm_delete.html'
    success_url = reverse_lazy('project-list')

# CRUD Operationsfor Member Class
class MemberListView(ListView):
    model = Member
    template_name = 'management/member_list.html'
    context_object_name = 'members'

class MemberCreateView(CreateView):
    model = Member
    fields = ['name', 'email', 'role', 'team']
    template_name = 'management/member_form.html'
    success_url = reverse_lazy('member-list')

class MemberUpdateView(UpdateView):
    model = Member
    fields = ['name', 'email', 'role', 'team']
    template_name = 'management/member_form.html'
    success_url = reverse_lazy('member-list')

class MemberDeleteView(DeleteView):
    model = Member
    template_name = 'management/member_confirm_delete.html'
    success_url = reverse_lazy('member-list')


# CRUD Operations for Task class.
class TaskListView(ListView):
    model = Task
    template = 'management/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()
        project_id = self.request.GET.get('project')
        member_id = self.request.GET.get('member')

        if project_id:
            queryset = queryset.filter(project_id = project_id)
        if member_id:
            queryset = queryset.filter(assigned_to_id = member_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['members'] = Member.objects.all()
        return context

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'management/task_form.html'
    success_url = reverse_lazy('task-list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm    
    template_name = 'management/task_form.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'management/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

# Dashboard class view
class DashboardView(TemplateView):
    template_name = 'management/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_teams'] = Team.objects.count()
        context['total_projects'] = Project.objects.count()
        context['total_members'] = Member.objects.count()
        context['total_tasks'] = Task.objects.count()

        #Tasks by status.
        context['tasks_pending'] = Task.objects.filter(status='pending').count()
        context['tasks_in_progress'] = Task.objects.filter(status='in_progress').count()
        context['tasks_completed'] = Task.objects.filter(status='completed').count()

        today = date.today()
        next_week = today + timedelta(days=7)

        # Filter tasks due within next week
        upcoming_tasks = Task.objects.filter(due_date__range=(today, next_week))
        context['upcoming_tasks'] = upcoming_tasks

        return context




