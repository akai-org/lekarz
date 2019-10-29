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

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=64)
    section = models.CharField(max_length=64)
    card_number = models.IntegerField('Id lekarza')
    
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospitalization_case = models.CharField(max_length=128)
    start_date = models.DateField()
    main_dr = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    dr_description = models.TextField()


    
