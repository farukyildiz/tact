from django.db import models


class Priority(models.Model):
    priority = models.CharField(max_length=150)
    status = models.BooleanField(default=True)
    created_by = models.IntegerField(default=0)
    updated_by = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
