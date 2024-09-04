from django.db import models
from django.utils import timezone


class CalculationLog(models.Model):
    expression = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Calculation: {self.expression} = {self.result}"
