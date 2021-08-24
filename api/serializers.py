from django.db.models import fields
from rest_framework import serializers
from .models import *

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'