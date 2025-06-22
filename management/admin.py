from django.contrib import admin
from .models import Team, Member, Project, Task

# Register your models here.

admin.site.register(Team)
admin.site.register(Member)
admin.site.register(Project)
admin.site.register(Task)
