
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('save', views.save, name='save'),
    path('view/<int:id>', views.view, name='view'),
]