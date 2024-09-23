import redis
from django.http import HttpResponse
from django.shortcuts import render, redirect

from definition.test_control.case.type.models import Type
from test_control.set.models import Set
from test_control.case.models import Case
from project.models import Project


def index(request):
    cases = Case.objects.select_related("set", "type")
    data = {"cases": cases}
    return render(request, "test_control/case/index.html", data)

def create(request):
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    data = {
        "types": Type.objects.filter(status=True).values(),
        "sets": Set.objects.filter(status=True).filter(project=r.get("project:active")).values(),
        "projects": Project.objects.filter(status=True).values(),
        "active_project": int(r.get("project:active")),
    }
    return render(request, "test_control/case/create.html", data)


def view(request, id):
    return render(request, "test_control/case/view.html")


def save(request):
    print("=== case save function")
    if request.method == "POST":
        print("=== request POST")
        print(request.POST)
        print(request.POST["mylist[]"])
        print(request.POST.getlist('mylist'))
        case = Case()
        case.summary = request.POST["summary"]
        case.set_id = request.POST["set"]
        case.priority = request.POST["priority"]
        case.type_id = request.POST["type"]
        case.description = request.POST["description"]
        case.created_by = 0 # set current user id
        case.updated_by = 0 # set current user id
        case.save()
        
        print("=== before render")
        return redirect("/test/case")
    
    print("=== function end")