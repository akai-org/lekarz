from django.contrib import admin
from .models import Intervention


class InterventionAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'min_time']


admin.site.register(Intervention, InterventionAdmin)
