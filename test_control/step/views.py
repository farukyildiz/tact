from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "test_control/step/index.html")