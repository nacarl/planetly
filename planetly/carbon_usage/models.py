from django.contrib.auth.models import User
from django.db import models


class Usage(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True, related_name='usages')
    usage_type = models.ForeignKey('UsageType', models.SET_NULL, blank=True, null=True, related_name='usage_types')
    usage_at = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = True


class UsageType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    factor = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = True
