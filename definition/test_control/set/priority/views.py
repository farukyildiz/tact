from django.http import HttpResponse
from django.shortcuts import render, redirect

from definition.test_control.set.priority.models import Priority

PRIORITY_TEMPLATE_DIR = "definition/test_control/set/priority"
INDEX_HTML = PRIORITY_TEMPLATE_DIR + "/index.html"
CREATE_HTML = PRIORITY_TEMPLATE_DIR + "/create.html"
EDIT_HTML = PRIORITY_TEMPLATE_DIR + "/edit.html"


def index(request):
    priorities = Priority.objects.all()
    data = {"priorities": priorities}
    return render(request, INDEX_HTML, data)

def create(request):
    return render(request, CREATE_HTML)

def edit(request, id):
    priority = Priority.objects.get(id=id)
    return render(request, EDIT_HTML, {"priority": priority})

def save(request):
    print("=== priority save function")
    if request.method == "POST":
        print("=== request POST")
        priority = Priority()
        priority.priority = request.POST["priority"]
        priority.status = request.POST["status"]
        priority.save()
        
        print("=== before render")
        return redirect("/definition/test_control/set/priority")
    
    print("=== function end")


def update(request):
    print("=== priority update function")
    if request.method == "POST":
        print("=== request POST")
        priority = CaseType.objects.get(id=request.POST["id"])
        priority.priority = request.POST["priority"]
        priority.status = request.POST["status"]
        priority.save()
        
        print("=== before render")
        return redirect("/definition/test_control/set/priority")
    
    print("=== function end")
