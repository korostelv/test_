from rest_framework import serializers
from .models import Application, Requisit


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


class RequisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisit
        fields = '__all__'

