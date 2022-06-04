from django.db import models

from backend.apps.service import EventType
# Create your models here.


class Aircraft(models.Model):
    name = models.CharField("Airplane", max_length=20, unique=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField("Type", max_length=20, unique=True)

    def __str__(self):
        return self.name


class Event(models.Model):

    aircraft = models.ForeignKey(Aircraft, on_delete=models.PROTECT, related_name="aircraft", db_index=True)
    type = models.ForeignKey(Type, on_delete=models.PROTECT, related_name="types")
    priority = models.CharField(max_length=10)
    status = models.CharField(max_length=15)
    info_count = models.IntegerField()
    errors_count = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['type']

    def __str__(self):
        return f"Event #{self.pk}-{self.status}"




