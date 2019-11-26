from django.urls import path

from interventions.models import Patient
from interventions.views import PatientDetails, PatientUpdate

app_name = 'interventions'
urlpatterns = [
    path('patients/<pk>/details', PatientDetails.as_view(model=Patient)),
    path('patients/<pk>/edit', PatientUpdate.as_view(model=Patient))
]
