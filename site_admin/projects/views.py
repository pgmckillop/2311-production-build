from django.shortcuts import render, get_object_or_404
from .models import Project

def index(request):
    return render(request, 'projects/index.html', {})


def about(request):
    return render(request, 'projects/about.html', {})


def album(request):
    projects = Project.objects
    return render(request, "projects/album.html", {'projects': projects})