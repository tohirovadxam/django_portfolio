from django.contrib import admin
from .models import Projects

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title',)

