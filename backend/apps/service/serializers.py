from rest_framework import serializers

from backend.apps.service.models import Aircraft, Event, Type


class AircrafEventDataSerializer(serializers.Serializer):
    aircraft = serializers.CharField(required=False, allow_null=True)
    status = serializers.CharField(required=False, allow_null=True)
    type = serializers.CharField(required=False, allow_null=True)
    warning = serializers.IntegerField()
    repeat_legend = serializers.IntegerField()
    pre_legend = serializers.IntegerField()
    legend = serializers.IntegerField()
    lower_a = serializers.IntegerField()
    lower_b = serializers.IntegerField()
    paired_a = serializers.IntegerField()
    paired_b = serializers.IntegerField()
    upper_a = serializers.IntegerField()
    errors_sum = serializers.IntegerField()
    infos_sum = serializers.IntegerField()

