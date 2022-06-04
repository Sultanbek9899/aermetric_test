from django.contrib import admin
from django.forms import Form, FileField
from django.shortcuts import redirect, render
from django.urls import path
# Register your models here.

import csv


from backend.apps.service.models import Aircraft, Event
from backend.apps.service.utils import upload_csv_data

class CsvForm(Form):
    file = FileField()

@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = ['name']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    change_list_template = "events_change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["file"]
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            upload_csv_data(decoded_file)
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )

    list_display = ['aircraft', 'type', 'status', 'priority', 'errors_count', 'info_count']
