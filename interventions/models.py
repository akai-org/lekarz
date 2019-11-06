from django.db import models
from django.contrib.auth.models import User


def get_full_name(self):
    return self.get_full_name()


User.add_to_class("__str__", get_full_name)


class Intervention(models.Model):
    name = models.CharField('Nazwa', max_length=255, default="zabieg", null=False)
    description = models.TextField('Opis')
    min_time = models.FloatField('Czas trwania zabiegu')

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=64)
    section = models.CharField(max_length=64)
    card_number = models.IntegerField('Id lekarza')

    def supername(self):
        return "Dr. " + str(self.user)

    def __str__(self):
        return self.supername()


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospitalization_case = models.CharField('Powód hospitalizacji', max_length=128)
    start_date = models.DateField('Data przyjęcia')
    main_dr = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, verbose_name = "Lekarz prowadzący")
    dr_description = models.TextField('Opis')

    def __str__(self):
        return str(self.user)

      
class Operation(models.Model):
    intervention = models.ForeignKey(Intervention, on_delete=models.CASCADE, verbose_name = "Zabieg")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name = "Lekarz")
    date = models.DateField("Data operacji")
    time = models.TimeField("Godzina operacji")
    
    def __str__(self):
        return str(self.intervention)
