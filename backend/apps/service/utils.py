from csv import DictReader
from backend.apps.service.models import Aircraft, Event, Type


def upload_csv_data(csv_file):
    file = DictReader(csv_file)
    for col in file:
        print(col['aircraft'])
        aircraft_obj, created = Aircraft.objects.get_or_create(
            name=col['aircraft']
        )
        type_obj, created = Type.objects.get_or_create(
            name=col['type']
        )
        try:
            Event.objects.create(
                aircraft=aircraft_obj,
                type=type_obj,
                priority=col['priority'],
                status=col['status'],
                info_count=col['info_count'],
                errors_count=col['errors_count'],
            )
        except Exception as e:
            print(e)
            raise Exception

