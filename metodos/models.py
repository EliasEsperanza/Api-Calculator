from django.db import models
from django.contrib.auth.models import User

class CalculationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    method = models.CharField(max_length=100)
    input_data = models.JSONField()
    result = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True) 