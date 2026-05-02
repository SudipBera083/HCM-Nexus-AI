from django.db import models

class WorkflowRule(models.Model):
    name = models.CharField(max_length=255)
    trigger_event = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)