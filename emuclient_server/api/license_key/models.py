from django.db import models

class LicenseKey(models.Model):
    key = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)