from django.db.models import  Q, Count, Sum
# Create your views here.
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status

from backend.apps.service.models import Event
from .serializers import AircrafEventDataSerializer






class EventDataAPIView(APIView):
    annotate_params = {
        "pre_legend": Count("type", filter=Q(type__name="PreLegend")),
        "lower_a": Count("type", filter=Q(type__name="Lower A")),
        "lower_b": Count("type", filter=Q(type__name="Lower B")),
        "legend": Count("type", filter=Q(type__name="Legend")),
        "repeat_legend": Count("type", filter=Q(type__name="Repeat Legend")),
        "warning": Count("type", filter=Q(type__name="Warning")),
        "paired_a": Count("type", filter=Q(type__name="Paired A")),
        "paired_b": Count("type", filter=Q(type__name="Paired B")),
        "upper_a": Count("type", filter=Q(type__name="Upper A")),
        "errors_sum":Sum("errors_count"),
        "infos_sum":Sum("info_count"),
    }

    def get_sql_query(self):
        queryset = Event.objects.values("status", "aircraft", "type").annotate(
            **self.annotate_params
        )
        group_set_query = 'GROUP BY GROUPING SETS( ("service_event"."status"), ("service_event"."aircraft_id"), ("service_event"."type_id"));'
        sql_query, params = queryset.query.sql_with_params()
        query = sql_query.split("GROUP BY")[0].replace("SELECT", "SELECT 1 as id,")
        group_set_query = query + group_set_query
        return group_set_query, params

    def get(self, request, **kwargs):
        query = self.get_sql_query()
        qs = Event.objects.raw(*query)
        serializer = AircrafEventDataSerializer(qs, many=True)
        print(serializer.data)
        return Response(data=serializer.data, status=status.HTTP_200_OK)