from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied

from .models import Patient,Doctor


def patient_details(request, patient_id):
    if not request.user.is_authenticated:
        raise PermissionDenied()
    user = request.user
    patient = get_object_or_404(Patient, id=patient_id)
    if user.id == patient.user.id or user.id==patient.main_dr.user.id:
        return render(request, 'interventions/patient.html', {'patient': patient})
    else:
        raise PermissionDenied()

# Create your views here.