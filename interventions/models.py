from django.db import models
from django.contrib.auth.models import User


class Intervention(models.Model):
    name = models.CharField(max_length=255, default="zabieg", null=False)
    description = models.TextField()
    min_time = models.FloatField()


class Operation(models.Model):
    intervention = models.ForeignKey(Intervention, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()


