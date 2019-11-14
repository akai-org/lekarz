from rest_framework import serializers
from interventions.models import Patient
from message.models import Message
from django.contrib.auth.models import User


class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    main_dr = serializers.StringRelatedField()

    class Meta:
        model = Patient
        fields = ('user', 'hospitalization_case', 'start_date', 'main_dr', 'dr_description')


class MessageSerializer(serializers.ModelSerializer):

    sender = serializers.StringRelatedField()
    receiver = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = ('sender', 'receiver', 'title', 'content', 'time', 'date')

