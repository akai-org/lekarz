from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ManyToOne')
    receiver = models.ManyToManyField(User, related_name='ManyToMany')
    title = models.CharField(max_length=32)
    content = models.TimeField()
    time = models.TimeField()
    date = models.DateField()
