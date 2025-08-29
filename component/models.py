from django.db import models

# Create your models here.
class Components(models.Model):
    title = models.CharField(max_length=200)
    JSON = models.JSONField()
    date_time_created = models.DateTimeField(auto_now_add=True)