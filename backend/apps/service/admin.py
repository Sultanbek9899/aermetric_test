from django.contrib import admin
from django.forms import Form, FileField
# Register your models here.

from backend.apps.service.models import Aircraft, Event


class CsvForm(Form):
    file = FileField()

@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = ['name']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['aircraft', 'type', 'status', 'priority', 'errors_count', 'info_count']
