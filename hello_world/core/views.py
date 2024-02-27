from django.shortcuts import render

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def renderTemplate(request):
    dict={"name":"chandu","age":22}
    return render(request,"index.html",dict)

def renderEmp(request):
    context={'name':'sai','age':22,'salary':40000}
    return render(request,"index.html",context)