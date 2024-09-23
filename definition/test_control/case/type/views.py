from django.http import HttpResponse
from django.shortcuts import render, redirect

from definition.test_control.case.type.models import Type

CASE_TYPE_TEMPLATE_DIR = "definition/test_control/case/type"
INDEX_HTML = CASE_TYPE_TEMPLATE_DIR + "/index.html"
CREATE_HTML = CASE_TYPE_TEMPLATE_DIR + "/create.html"
EDIT_HTML = CASE_TYPE_TEMPLATE_DIR + "/edit.html"


def index(request):
    types = Type.objects.all()
    data = {"types": types}
    return render(request, INDEX_HTML, data)

def create(request):
    return render(request, CREATE_HTML)

def edit(request, id):
    type = Type.objects.get(id=id)
    return render(request, EDIT_HTML, {"type": type})

def save(request):
    print("=== case_type save function")
    if request.method == "POST":
        print("=== request POST")
        type = Type()
        type.type = request.POST["type"]
        type.status = request.POST["status"]
        type.save()
        
        print("=== before render")
        return redirect("/definition/test_control/case/type")
    
    print("=== function end")


def update(request):
    print("=== case_type update function")
    if request.method == "POST":
        print("=== request POST")
        type = Type.objects.get(id=request.POST["id"])
        type.name = request.POST["type"]
        type.status = request.POST["status"]
        type.save()
        
        print("=== before render")
        return redirect("/definition/test_control/case/type")
    
    print("=== function end")
