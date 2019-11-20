from django.shortcuts import render, get_object_or_404

from .models import Patient, Doctor


def patient_details(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    return render(request, 'interventions/patient.html', {'patient': patient})


# Create your views here.


def doctor_details(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    context = {'doctor': doctor}
    return render(request, 'interventions/doctor.html', context, content_type='application/xhtml+xml')

