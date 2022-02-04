from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib import admin


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """ automatically create a token for newly created user instances """
    if created:
        Token.objects.create(user=instance)


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

    def __str__(self):
        return self.name if self.name is not None else str(self.id)

    class Meta:
        managed = True


# registering usages to the django admin to easily create some for testing purposes
class UsageAdmin(admin.ModelAdmin):
    list_display = ('usage_type', 'usage_at', 'user')


class UsageTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit', 'factor')


admin.site.register(Usage, UsageAdmin)
admin.site.register(UsageType, UsageTypeAdmin)
