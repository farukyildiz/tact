from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('save', views.save, name='save'),
    path('update', views.update, name='update'),
    path('view', views.view, name='view'),
    path('set/active/<int:id>', views.set_active, name='set_active'),
]