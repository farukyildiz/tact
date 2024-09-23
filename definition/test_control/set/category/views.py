from django.http import HttpResponse
from django.shortcuts import render, redirect

from definition.test_control.set.category.models import Category

CATEGORY_TEMPLATE_DIR = "definition/test_control/set/category"
INDEX_HTML = CATEGORY_TEMPLATE_DIR + "/index.html"
CREATE_HTML = CATEGORY_TEMPLATE_DIR + "/create.html"
EDIT_HTML = CATEGORY_TEMPLATE_DIR + "/edit.html"


def index(request):
    categories = Category.objects.all()
    data = {"categories": categories}
    return render(request, INDEX_HTML, data)

def create(request):
    return render(request, CREATE_HTML)

def edit(request, id):
    category = Category.objects.get(id=id)
    return render(request, EDIT_HTML, {"category": category})

def save(request):
    print("=== category save function")
    if request.method == "POST":
        print("=== request POST")
        category = Category()
        category.category = request.POST["category"]
        category.status = request.POST["status"]
        category.save()
        
        print("=== before render")
        return redirect("/definition/test_control/set/category")
    
    print("=== function end")


def update(request):
    print("=== case_type update function")
    if request.method == "POST":
        print("=== request POST")
        case_type = CaseType.objects.get(id=request.POST["id"])
        case_type.name = request.POST["name"]
        case_type.status = request.POST["status"]
        case_type.save()
        
        print("=== before render")
        return redirect("/case_type")
    
    print("=== function end")
