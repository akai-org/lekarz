from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Patient, Doctor


def patient_details(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    return render(request, 'interventions/patient.html', {'patient': patient})

def out_patient(request, patient_id): 
        patient = get_object_or_404(Patient,id=patient_id)
        if request.user.Doctor:
            if request.user.Doctor.id == patient.main_dr.id:
                patient.objects.filter(id=id).delete()
            else:
                raise Http403("Przejscia nie ma")
        else:
            raise Http403("Przejscia nie ma")
        return render(request, 'interventions/out_patient.html', {'patient': patient})     
        
                
        
# Create your views here.
