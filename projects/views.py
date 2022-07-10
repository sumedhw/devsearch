from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import Project, Review, Tag
from .forms import ProjectForm


from django.contrib.auth.decorators import login_required

# Create your views here.

def projects(request):
    projects = Project.objects.all()
    context = { 'projects' : projects }
    return render(request,'projects/projects.html', context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()

    context = { 'project' :projectObj, 'tags' : tags }
    return render(request,'projects/single-project.html', context )


@login_required(login_url="login")
def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url="login")
def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url="login")
def deleteProject(request,pk):
    project = Project.objects.get(id=pk)
    context = {'object':project}

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    return render(request, 'projects/delete_template.html',context)