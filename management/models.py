from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete = models.CASCADE, related_name = 'members')

    def __str__ (self):
        return f"{self.name} ({self.role})"

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null = True, blank=True)
    team = models.ForeignKey(Team, on_delete = models.CASCADE, related_name = 'projects')

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    status_choices = [
        ('pending','Pending'),
        ('in_progress', 'In_progress'),
        ('completed', 'Completed')
    ]
    status = models.CharField(max_length=20, choices = status_choices, default='pending')
    assigned_to = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    due_date = models.DateField(null = True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.status}"