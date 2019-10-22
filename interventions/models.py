from django.db import models


class Intervention(models.Model):
    name = models.CharField(max_length=255, default="zabieg", null=False)
    description = models.TextField()
    min_time = models.FloatField()

