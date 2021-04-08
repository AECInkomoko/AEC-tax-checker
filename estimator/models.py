from django.db import models

# Create your models here.

class TaxBracket(models.Model):
  taxType = models.CharField(max_length=10)
  state = models.CharField(max_length=30, blank=True)
  filerType = models.CharField(max_length=30)
  rangeMax = models.DecimalField(max_digits=10, decimal_places=2)
  rangeRate = models.DecimalField(max_digits=10, decimal_places=2)
