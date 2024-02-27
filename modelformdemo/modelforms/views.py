from django.shortcuts import render
from modelforms.forms import ProjectForm
from modelforms.models import Project

def index(request):
    return render(request,'index.html')

def listProjects(request):
    projectlist=Project.objects.all()
    return render(request,'listprojects.html',{'projects':projectlist})

def addproject(request):
    form=ProjectForm()
    if request.method=='POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request,'addproject.html',{'form':form})