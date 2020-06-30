from django.db import models

class Kosdaq(models.Model):
    fluctuation = models.FloatField(null=True)
    time = models.TimeField(null=True)
    
class Kospi(models.Model):
    fluctuation = models.FloatField(null=True)
    time = models.TimeField(null=True)


class Kospi_by_10second(models.Model):
    class Meta:
        ordering = ["time"]
    time = models.DateTimeField(null=True)
    price = models.FloatField(null=True)


class Kosdaq_by_10second(models.Model):
    class Meta:
        ordering = ["time"]
    time = models.DateTimeField(null=True)
    price = models.FloatField(null=True)
