from django.contrib import admin
from .models import Intervention, Patient, Operation


class InterventionAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'min_time']


class OperationInLine(admin.StackedInline):
    model = Operation
    extra = 1


class PatientAdmin(admin.ModelAdmin):
    fieldsets = [('Informacje o pacjencie', {'fields':['hospitalization_case', 'start_date', 'main_dr', 'dr_description']})]
    inlines = [OperationInLine]


admin.site.register(Intervention, InterventionAdmin)
admin.site.register(Patient, PatientAdmin)
