from django.contrib import admin
from .models import Project

"""
Register the Project model for use in the admin panel.
The admin panel will allow direct access to the sqlite database.
"""


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'description']
    list_filter = ['title']
