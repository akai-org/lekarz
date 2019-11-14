from oauth2_provider.views.generic import ProtectedResourceView  # podkresla na czerwono ale dziala
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from oauth2_provider.contrib.rest_framework import TokenHasScope, OAuth2Authentication
from interventions.models import Patient
from message.models import Message
from .serializers import PatientSerializer, MessageSerializer


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')


class PatientDetails(generics.RetrieveAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read']
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class MessageDetails(generics.RetrieveAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read']
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
