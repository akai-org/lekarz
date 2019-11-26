from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView

from .models import Patient, Doctor


def doctor_check(user):
    if Doctor.objects.filter(user=user.id).first() is not None:
        return True
    else:
        return False


class PatientDetails(UserPassesTestMixin, DetailView):

    def test_func(self):
        return doctor_check(self.request.user)

    model = get_object_or_404(Patient)
    success_url = reverse_lazy('home')
    fields = ['user', 'hospitalization_case', 'start_date', 'main_dr', 'dr_description']
    template_name = 'interventions/patient_details.html'


class PatientUpdate(UserPassesTestMixin, UpdateView):

    def test_func(self):
        return doctor_check(self.request.user)

    model = get_object_or_404(Patient)
    success_url = reverse_lazy('home')
    fields = ['user', 'hospitalization_case', 'start_date', 'main_dr', 'dr_description']
    template_name = 'interventions/patient_edit.html'

