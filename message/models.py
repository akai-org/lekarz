from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='MessagesSent')
    receiver = models.ManyToManyField(User, related_name='MessageRecived')
    title = models.CharField(max_length=32)
    content = models.TimeField()
    time = models.TimeField()
    date = models.DateField()
    def __str__(self):
        return self.title


class Notification(models.Model):
    receiver = models.ManyToManyField(User, related_name='NotificationsRecived')
    title = models.CharField(max_length=32)
    content = models.TimeField()
    time = models.TimeField()
    date = models.DateField()
    def __str__(self):
        return self.title

