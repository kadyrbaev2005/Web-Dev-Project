from django.contrib import admin
from .models import Task, Project

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'assigned_to', 'project', 'due_date')
    list_filter = ('status', 'project')
    search_fields = ('title', 'description')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by')
    search_fields = ('title', 'description')