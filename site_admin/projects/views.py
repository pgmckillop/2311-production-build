from django.shortcuts import render, get_object_or_404
from .models import Project

def index(request):
    return render(request, 'projects/index.html', {})


def about(request):
    return render(request, 'projects/about.html', {})


def album(request):
    projects = Project.objects
    return render(request, "projects/album.html", {'projects': projects})


def detail(request, project_id):
    project_detail = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'project': project_detail})