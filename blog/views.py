from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.




def acceuil(request):
    return render(request, "blog/acceuil.html")


def theses(request):
    return render(request, "blog/theses.html")


def thesis_detail(request, slug):
    return render(request,"blog/thesis_details.html")



def projects(request):
    return render(request, "blog/projects.html")


def project_detail(request, slug):
    return render(request,"blog/project_details.html")