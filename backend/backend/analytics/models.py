from django.db import models

class AnalyticsData(models.Model):
    metric_name = models.CharField(max_length=100)
    metric_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.metric_name