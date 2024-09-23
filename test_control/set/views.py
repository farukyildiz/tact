import redis
from django.http import HttpResponse
from django.shortcuts import render, redirect

from test_control.set.models import Set
from project.models import Project
from definition.test_control.set.category.models import Category
from definition.test_control.set.priority.models import Priority


def index(request):
    data = {
        "sets": Set.objects.all(),
        "projects": Project.objects.all()
    }
    return render(request, "test_control/set/index.html", data)


def create(request):
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    data = {
        "projects": Project.objects.filter(status=True).values(),
        "categories": Category.objects.filter(status=True).values(),
        "priorities": Priority.objects.filter(status=True).values(),
        "active_project": int(r.get("project:active")),
    }
    return render(request, "test_control/set/create.html", data)


def edit(request, id):
    set = Set.objects.get(id=id)
    return render(request, "test_control/set/edit.html", {"set": set})


def view(request):
    # set = Set.objects.get(id=id)
    return render(request, "test_control/set/view.html")


def save(request):
    print("=== set save function")
    if request.method == "POST":
        print("=== request POST")
        set = Set()
        set.summary = request.POST["summary"]
        set.project = request.POST["project"]
        set.priority = request.POST["priority"]
        set.category = request.POST["category"]
        set.status = request.POST["status"]
        set.description = request.POST["description"]
        set.created_by = 0 # set current user id
        set.updated_by = 0 # set current user id
        set.save()
        
        print("=== before render")
        return redirect("/test/set")
    
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
        project.updated_by = 0 # set current user id
        project.save()
        
        print("=== before render")
        return redirect("/project")
    
    print("=== function end")
