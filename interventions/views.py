from django.shortcuts import render, get_object_or_404

from .models import Patient


def patient_details(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    return render(request, 'interventions/patient.html', {'patient': patient})
# Create your views here.
