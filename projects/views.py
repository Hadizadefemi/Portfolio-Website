from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def home(request):
    return render(request, 'index.html', {})
    
def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/project_index.html', context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {
        'project': project
    }
    
    return render(request, 'projects/project_detail.html', context)

def custom_404(request, exception):
    return render(request, "404.html", status=404)