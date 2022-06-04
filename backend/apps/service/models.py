from django.db import models

from backend.apps.service import EventType
# Create your models here.


class Aircraft(models.Model):
    name = models.CharField("Airplane", max_length=20, unique=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    STATUS_STARTED = 0
    STATUS_IN_PROGRESS = 1
    STATUS_SUSPEND = 2
    STATUS_KICKBACK = 3
    STATUS_FINISHED = 4
    EVENT_STATUSES = (
        (STATUS_STARTED, "Started"),
        (STATUS_IN_PROGRESS, "In progress"),
        (STATUS_KICKBACK, "Kickback"),
        (STATUS_SUSPEND, "Suspend"),
        (STATUS_FINISHED, "Finished")
    )
    PRIORITY_EASY = 0
    PRIORITY_USUAL = 1
    PRIORITY_HARD = 2
    PRIORITIES = (
        (PRIORITY_EASY, "Easy"),
        (PRIORITY_USUAL, "Usual"),
        (PRIORITY_HARD, "Hard"),
    )

    aircraft = models.ForeignKey(Aircraft, on_delete=models.PROTECT, related_name="aircraft", db_index=True)
    type = models.CharField(max_length=15, choices=EventType.choices, db_index=True)
    priority = models.PositiveSmallIntegerField(choices=PRIORITIES, db_index=True)
    status = models.PositiveSmallIntegerField(choices=EVENT_STATUSES, db_index=True)
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


