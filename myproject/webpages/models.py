# models.py
from django.db import models

class Report(models.Model):
    crime_type = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    details = models.TextField()
    more_info = models.TextField(blank=True, null=True)
    proof_files = models.FileField(upload_to='proofs/', blank=True, null=True)
    crime_datetime = models.DateTimeField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=50, default="New")  # e.g. New, In Review, Resolved

    def __str__(self):
        return f"{self.crime_type} at {self.location}"

