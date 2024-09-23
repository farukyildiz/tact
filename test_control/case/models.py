from django.db import models

from test_control.set.models import Set
from definition.test_control.case.type.models import Type


class Case(models.Model):
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    priority = models.IntegerField()
    summary = models.CharField(max_length=250)
    description = models.TextField()
    created_by = models.IntegerField(default=0)
    updated_by = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class PreCondition(models.Model):
    case = models.IntegerField()
    description = models.CharField(max_length=250)
    created_by = models.IntegerField(default=0)
    updated_by = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Requirement(models.Model):
    case = models.IntegerField()
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    created_by = models.IntegerField(default=0)
    updated_by = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class ExpectedResult(models.Model):
    case = models.IntegerField()
    description = models.CharField(max_length=250)
    created_by = models.IntegerField(default=0)
    updated_by = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Executed(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    status = models.IntegerField()
    note = models.TextField()
    executed_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    