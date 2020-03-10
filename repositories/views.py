from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Repository

def home(request):
    return render(request, 'home.html')

def my_repositories(request):
    repositories = Repository.objects.all()
    return render(request, 'my_repositories.html', {'repositories': repositories})

def repository_detail(request, id):
    try:
        repository = Repository.objects.get(id=id)
    except Repository.DoesNotExist:
        raise Http404('Repository not found')
    return render(request, 'repository_detail.html', {'repository': repository})

def recommendations(request):
    return render(request, 'recommendations.html')
