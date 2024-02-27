from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    dict={"name":"chandu","age":22}
    return render(request,"templates/firsttemplate.html",dict)