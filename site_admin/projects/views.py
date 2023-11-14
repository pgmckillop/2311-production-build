from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, 'projects/index.html', {})


def about(request):
    return render(request, 'projects/about.html', {})