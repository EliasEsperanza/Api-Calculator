from rest_framework import serializers
from .models import CalculationHistory

class CalculationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculationHistory
        fields = '__all__'