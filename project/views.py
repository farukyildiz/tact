import redis
from django.http import HttpResponse
from django.shortcuts import render, redirect

from project.models import Project


def index(request):
    projects = Project.objects.all()
    return render(request, "project/index.html", {"projects": projects})


def create(request):
    return render(request, "project/create.html")


def view(request):
    return render(request, "project/view.html")


def edit(request, id):
    project = Project.objects.get(id=id)
    return render(request, "project/edit.html", {"project": project})


def save(request):
    print("=== project save function")
    if request.method == "POST":
        print("=== request POST")
        project = Project()
        project.name = request.POST["name"]
        project.tag = request.POST["tag"]
        project.owner = request.POST["owner"]
        project.category = request.POST["category"]
        project.status = request.POST["status"]
        project.created_by = 0 # set current user id
        project.updated_by = 0 # set current user id
        project.save()
        
        print("=== before render")
        return redirect("/project")
    
    print("=== function end")


def update(request):
    print("=== project update function")
    if request.method == "POST":
        print("=== request POST")
        project = Project.objects.get(id=request.POST["id"])
        project.name = request.POST["name"]
        project.tag = request.POST["tag"]
        project.owner = request.POST["owner"]
        project.category = request.POST["category"]
        project.status = request.POST["status"]
        project.updated_by = 0 # set current user id
        project.save()
        
        print("=== before render")
        return redirect("/project")
    
    print("=== function end")


def set_active(request, id):
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    print(id)
    r.set("project:active", id)
    print(request.scheme)
    print(request.body)
    print(request.path)
    print(request.path_info)
    print(request.META["HTTP_REFERER"])
    return redirect(request.META["HTTP_REFERER"])