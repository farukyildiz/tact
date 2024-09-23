from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=150)
    tag = models.CharField(max_length=150, default="")
    category = models.IntegerField(default=0)
    owner = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_by = models.IntegerField(default=0)
    updated_by = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
