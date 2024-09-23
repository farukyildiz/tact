from django.db import models


class Set(models.Model):
    summary = models.CharField(max_length=250)
    description = models.TextField()
    project = models.IntegerField()
    category = models.IntegerField()
    priority = models.IntegerField()
    status = models.BooleanField(default=True)
    created_by = models.IntegerField(default=0)
    updated_by = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Executed(models.Model):
    status = models.IntegerField()
    note = models.TextField()
    executed_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    