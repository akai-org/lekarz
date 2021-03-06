from django.contrib import admin
from .models import Intervention, Patient, Operation, Doctor


class InterventionAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'min_time']


class DoctorAdmin(admin.ModelAdmin):
    fieldsets = [('Dodaj nowego doktora', {'fields':['specialization', 'section', 'card_number', 'user']})]


class OperationInLine(admin.StackedInline):
    model = Operation
    extra = 1


class PatientAdmin(admin.ModelAdmin):
    fieldsets = [('Informacje o pacjencie', {'fields':['user','hospitalization_case', 'start_date', 'main_dr', 'dr_description']})]
    inlines = [OperationInLine]


admin.site.register(Intervention, InterventionAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)