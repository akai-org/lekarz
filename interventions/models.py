from django.db import models
from django.contrib.auth.models import User


class Intervention(models.Model):
    name = models.CharField('Nazwa', max_length=255, default="zabieg", null=False)
    description = models.TextField('Opis')
    min_time = models.FloatField('Czas trwania zabiegu')


class Operation(models.Model):
    intervention = models.ForeignKey(Intervention, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospitalization_case = models.CharField(max_length=128)
    start_date = models.DateField()
    main_dr = models.CharField(max_length=32, default="Pole na przypisanie doktora")
    dr_description = models.TextField()